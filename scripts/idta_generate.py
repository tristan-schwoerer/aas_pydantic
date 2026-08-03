#!/usr/bin/env python3
"""Generate aas_pydantic models from IDTA submodel template JSON."""

import json, sys, os

from _generator_utils import (
    safe_name, snake, format_py,
    extract_semantic_id, extract_qualifiers, extract_description,
    extract_supplemental,
)

# modelType → Python type name (second element always unused, kept for back-compat)
ELEMENT_MAP = {
    "Property": ("Property", None),
    "MultiLanguageProperty": ("MultiLanguageProperty", None),
    "Range": ("Range", None),
    "ReferenceElement": ("ReferenceElement", None),
    "RelationshipElement": ("RelationshipElement", None),
    "File": ("File", None),
    "Blob": ("Blob", None),
    "Capability": ("Capability", None),
    "SubmodelElementCollection": (None, None),
    "SubmodelElementList": (None, None),
}

def _get_cardinality(el: dict) -> str:
    """Extract cardinality value from an element's qualifiers (e.g. 'ZeroToMany')."""
    quals = el.get("qualifiers", el.get("qualifier", []))
    if not isinstance(quals, list):
        return ""
    for q in quals:
        if q.get("type", "") == "Cardinality":
            return q.get("value", "")
    return ""


def gen_template(template_path: str, output_dir: str):
    with open(template_path) as f:
        data = json.load(f)
    submodels = data.get("submodels", [])
    if not submodels:
        print(f"No submodels in {template_path}"); return
    sm = submodels[0]
    sm_name = sm["idShort"]

    lines = []
    lines.append(f'"""{sm_name} — generated from IDTA template."""')
    lines.append('')
    lines.append('from __future__ import annotations')
    lines.append('')
    lines.append('from typing import ClassVar, Dict, List, Optional')
    lines.append('from aas_pydantic import (')
    lines.append(')')  # placeholder — will be replaced
    lines.append('')

    # Types always used in generated output
    _used_leaf_types: set = {"Submodel", "SubmodelElement", "SubmodelElementCollection", "SubmodelElementList", "Qualifier"}

    # all_classes: name → (class_meta, [(fname, ftype, fdefault, is_smc, field_meta, cardinality)])
    all_classes = {}

    def class_meta_from(el: dict):
        return {
            "semantic_id": extract_semantic_id(el),
            "description": extract_description(el),
            "qualifiers": _filter_cardinality(extract_qualifiers(el)),
            "supplemental_semantic_ids": extract_supplemental(el),
            "entity_type": el.get("entityType", ""),
        }

    def _filter_cardinality(quals: list) -> list:
        """Remove Cardinality qualifiers — they drive type generation, not runtime data."""
        return [q for q in quals if "Cardinality" not in q]

    def field_meta_from(el: dict):
        return {
            "semantic_id": extract_semantic_id(el),
            "description": extract_description(el),
            "qualifiers": _filter_cardinality(extract_qualifiers(el)),
        }

    def _make_sml(name: str, meta: dict, py_type: str):
        """Register an SML class with the given value type."""
        meta["_is_sml"] = True
        all_classes[name] = (meta, [("value", f"List[{py_type}]", "[]", False, {}, "")])

    def _sml_value_type(el: dict) -> str:
        """Determine the value type for an SML from typeValueListElement."""
        tvle = el.get("typeValueListElement", "")
        if tvle == "SubmodelElement":
            return "SubmodelElement"
        if tvle in ELEMENT_MAP:
            py_type = ELEMENT_MAP[tvle][0]
            _used_leaf_types.add(py_type)
            return py_type
        return "str"

    def build(name: str, value: list, parent_sml_name: str = ""):
        fields = []
        if not value:
            return {}, []
        for el in value:
            if not isinstance(el, dict):
                continue
            mt = el.get("modelType", "Property")
            ids = el.get("idShort", "").strip()
            if not ids:
                ids = f"{parent_sml_name}Item" if parent_sml_name else f"{name}Item"
            fname = snake(ids)
            if fname == snake(name):
                fname = f"{fname}_"

            fm = field_meta_from(el)

            if mt in ("SubmodelElementCollection", "Entity"):
                child_key = "statements" if mt == "Entity" else "value"
                child_meta, child_fields = build(ids, el.get(child_key, []))
                meta = class_meta_from(el)
                if meta.get("entity_type"):
                    _used_leaf_types.add("Entity")
                all_classes[ids] = (meta, child_fields)
                fields.append((fname, f"Optional[{ids}]", "None", True, fm, _get_cardinality(el)))

            elif mt == "SubmodelElementList":
                items = el.get("value", [])
                sml_name = ids
                sml_meta = class_meta_from(el)
                if items and isinstance(items[0], dict):
                    item_ids = items[0].get("idShort", "").strip() or f"{sml_name}Item"
                    child_value = items[0].get("value", []) or items[0].get("statements", [])
                    build(item_ids, child_value, parent_sml_name=sml_name)
                    if item_ids in all_classes:
                        fields.append((fname, f"List[{item_ids}]", "[]", True, fm, ""))
                    else:
                        py_type = _sml_value_type(el)
                        _make_sml(sml_name, sml_meta, py_type)
                        fields.append((fname, sml_name, f'{sml_name}(id_short="{sml_name}")', True, {}, ""))
                else:
                    _make_sml(sml_name, sml_meta, _sml_value_type(el))
                    fields.append((fname, sml_name, f'{sml_name}(id_short="{sml_name}")', True, {}, ""))

            else:
                py_type, _ = ELEMENT_MAP.get(mt, ("str", None))
                if py_type and mt in ELEMENT_MAP:
                    _used_leaf_types.add(py_type)
                fields.append((fname, py_type or "str", None, False, fm, ""))

        return [], fields

    _, top_fields = build(sm_name, sm.get("submodelElements", []))
    all_classes[sm_name] = (class_meta_from(sm), top_fields)

    # ── Track renamed fields for write_class comments ──
    _renamed_fields: dict = {}  # (class_name, field_name) → original_name

    def _apply_cardinality_and_fix_collisions(classes: dict):
        """Upgrade Optional[X] → Dict[str, X] per cardinality; rename colliding fields.

        Pydantic v2.13.4 has a bug: if class ``A`` has ``Dict[str, B]`` and ANY
        class has a field whose *name* equals ``A`` (e.g. ``properties:
        Optional['properties']``), schema generation crashes with ``KeyError: 'type'``
        in ``schema_gather.py``.  We work around this by appending ``_ref`` to the
        colliding field name and mapping it back during AAS deserialization.
        """
        # Pass 1: upgrade cardinality
        for cls_name, (meta, field_list) in classes.items():
            for i, (fname, ftype, fdefault, is_smc, fm, cardinality) in enumerate(field_list):
                if not is_smc:
                    continue
                target = ftype
                if target.startswith("Optional["):
                    target = target[9:-1]

                if cardinality == "One":
                    # Required, non-Optional field (no default)
                    field_list[i] = (fname, target, None, True, fm, cardinality)

                elif cardinality in ("ZeroToMany", "OneToMany"):
                    if target not in classes:
                        continue
                    # If field name matches target class name, rename to avoid
                    # Pydantic v2.13.4 KeyError: 'type' in schema_gather.py
                    # (triggered by: Range field + Optional back-ref + Dict[fname, fname])
                    new_fname = fname
                    if fname == target:
                        new_fname = f"{fname}_ref"
                        _renamed_fields[(cls_name, new_fname)] = fname
                    if cardinality == "ZeroToMany":
                        # Optional dict — None means zero items
                        field_list[i] = (new_fname, f"Optional[Dict[str, {target}]]", "None", True, fm, cardinality)
                    else:
                        # OneToMany — required dict, at least one item
                        field_list[i] = (new_fname, f"Dict[str, {target}]", "{}", True, fm, cardinality)

        # Pass 2: rename any field whose name collides with a class name
        for cls_name, (meta, field_list) in classes.items():
            for j, (tfname, tftype, tfdefault, tis_smc, tfm, tcard) in enumerate(field_list):
                if not tis_smc:
                    continue
                if tfname in classes and tfname in tftype:
                    new_name = f"{tfname}_ref"
                    field_list[j] = (new_name, tftype, tfdefault, tis_smc, tfm, tcard)
                    _renamed_fields[(cls_name, new_name)] = tfname

    # ── Run post-processing ──
    _apply_cardinality_and_fix_collisions(all_classes)

    written = set()

    def write_class(name, meta, field_list, _visiting=None):
        if _visiting is None:
            _visiting = set()
        if name in written or name in _visiting:
            return
        _visiting.add(name)
        for _, ftype, _, _, _, _ in field_list:
            for cls_name in all_classes:
                if cls_name in ftype and cls_name not in written:
                    write_class(cls_name, *all_classes[cls_name], _visiting)
        written.add(name)

        if name == sm_name:
            lines.append(f'class {name}(Submodel):')
        elif meta.get("_is_sml"):
            lines.append(f'class {name}(SubmodelElementList):')
        elif meta.get("entity_type"):
            lines.append(f'class {name}(Entity):')
        else:
            lines.append(f'class {name}(SubmodelElementCollection):')

        # Class-level metadata
        for key in ("semantic_id", "description"):
            val = meta.get(key, "")
            if val:
                lines.append(f'    {key}: str = {format_py(val)}')
        for key in ("qualifiers",):
            val = meta.get(key, [])
            if val:
                lines.append(f'    {key}: List[Qualifier] = [')
                for q in val:
                    lines.append(f'        {q},')
                lines.append(f'    ]')
        for key in ("supplemental_semantic_ids",):
            val = meta.get(key, [])
            if val:
                lines.append(f'    {key}: List[str] = {format_py(val)}')

        entity_type_val = meta.get("entity_type", "")
        if entity_type_val:
            lines.append(f'    entity_type: str = {format_py(entity_type_val)}')

        if name == sm_name:
            admin = sm.get("administration", {})
            lines.append(f'    VERSION: ClassVar[str] = "{admin.get("version", "1")}"')
            lines.append(f'    REVISION: ClassVar[str] = "{admin.get("revision", "0")}"')
        lines.append('')

        if not field_list:
            lines.append('    pass')
        else:
            for fname, ftype, fdefault, is_smc, fm, cardinality in field_list:
                # Emit comment for _ref-renamed fields (Pydantic circular Dict bug workaround)
                rename_key = (name, fname)
                if rename_key in _renamed_fields:
                    original = _renamed_fields[rename_key]
                    lines.append(f'    # _ref suffix: field renamed from "{original}" (Pydantic name-collision workaround)')
                if is_smc:
                    # SMC field — metadata is on the referenced class, no json_schema_extra needed
                    if fdefault is None:
                        # Cardinality "One" — required, no default
                        lines.append(f'    {fname}: {ftype}')
                    elif fdefault == "None":
                        lines.append(f'    {fname}: {ftype} = None')
                    elif fdefault == "[]":
                        lines.append(f'    {fname}: {ftype} = []')
                    elif fdefault == "{}":
                        lines.append(f'    {fname}: {ftype} = {{}}')
                    else:
                        lines.append(f'    {fname}: {ftype} = {fdefault}')
                else:
                    # Leaf AAS element — generate model instance with pre-filled metadata.
                    # List[X] fields with AAS metadata are handled as SML classes
                    # in the parser; plain List[X] (e.g. SML.value) pass through.
                    sid = fm.get("semantic_id")
                    desc = fm.get("description")
                    quals = fm.get("qualifiers")
                    has_meta = sid or desc or quals
                    if ftype.startswith("List["):
                        lines.append(f'    {fname}: {ftype} = {fdefault}')
                    elif has_meta:
                        lines.append(f'    {fname}: {ftype} = {ftype}(')
                        if sid:
                            lines.append(f'        semantic_id={json.dumps(sid)},')
                        if desc:
                            lines.append(f'        description={json.dumps(desc)},')
                        if quals:
                            lines.append(f'        qualifiers=[')
                            for q in quals:
                                lines.append(f'            {q},')
                            lines.append(f'        ],')
                        lines.append(f'    )')
                    else:
                        lines.append(f'    {fname}: {ftype} = {ftype}()')
        lines.append('')

    for cls_name in all_classes:
        if cls_name != sm_name:
            write_class(cls_name, *all_classes[cls_name])
    write_class(sm_name, *all_classes[sm_name])

    # ── Resolve forward references for all generated classes ──
    lines.append('')
    lines.append('# ── Resolve forward references (Pydantic circular refs) ──')
    for cls_name in all_classes:
        lines.append(f'{cls_name}.model_rebuild()')

    # Replace placeholder import (line 5) with actual used types
    all_imports = sorted(t for t in _used_leaf_types if t)
    lines[5] = (
        'from aas_pydantic import (\n'
        '    ' + ', '.join(all_imports) + ',\n'
        ')'
    )
    del lines[6]

    os.makedirs(output_dir, exist_ok=True)
    out_path = os.path.join(output_dir, f"{snake(sm_name)}.py")
    with open(out_path, "w") as f:
        f.write("\n".join(lines))
    print(f"✅ {out_path}")
    print(f"   {sm_name}(Submodel) + {len(written)-1} SMC classes")


if __name__ == "__main__":
    if len(sys.argv) >= 2:
        gen_template(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else ".")
    else:
        # Hardcoded list of IDTA submodel templates
        TEMPLATES = [
            ("submodel-templates/published/Capability Description/1/0/IDTA 02020_Template_Capability_Description.json", "aas_pydantic/submodel_templates/"),
            ("submodel-templates/published/Control Component Instance/2/0/1/IDTA 02016-2-0-1 _Template_ControlComponentInstance_forAASMetamodelV3.1.json", "aas_pydantic/submodel_templates/"),
            ("submodel-templates/published/Control Component Type/2/0/1/IDTA 02015-2-0-1 _Template_ControlComponentType_forAASMetamodelV3.1.json", "aas_pydantic/submodel_templates/"),
            ("submodel-templates/published/Hierarchical Structures enabling Bills of Material/1/1/1/IDTA 02011-1-1-1_Template_HSEBoM_forAASMetamodelV3.1.json", "aas_pydantic/submodel_templates/"),
            ("submodel-templates/published/Digital nameplate/3/0/1/IDTA 02006-3-0-1_Template_Digital Nameplate.json", "aas_pydantic/submodel_templates/"),
            ("submodel-templates/published/Asset Interfaces Mapping Configuration/2/0/IDTA 02027_Template_AIMC.json", "aas_pydantic/submodel_templates/"),
            ("submodel-templates/published/Asset Interfaces Description/1/1/IDTA 02017-1-1_Template_Asset Interfaces Description.json", "aas_pydantic/submodel_templates/"),
        ]
        for tmpl_path, out_dir in TEMPLATES:
            if not os.path.exists(tmpl_path):
                print(f"⚠️  Skipping missing template: {tmpl_path}")
                continue
            gen_template(tmpl_path, out_dir)
        print(f"\n✅ Generated {len(TEMPLATES)} templates")
