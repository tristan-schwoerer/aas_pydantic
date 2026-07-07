#!/usr/bin/env python3
"""Generate aas_pydantic models from IDTA submodel template JSON."""

import json, sys, os

from _generator_utils import (
    _RESERVED, safe_name, snake, format_py,
    extract_semantic_id, extract_qualifiers, extract_description,
    extract_supplemental,
)

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

# Track which leaf model types are actually used (for imports)
_used_leaf_types: set = set()


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
    lines.append('from typing import ClassVar, List, Optional')
    lines.append('from pydantic import Field')
    lines.append('from aas_pydantic import Submodel, SubmodelElementCollection, Capability, Qualifier')
    # Leaf type imports will be appended after we know which are used
    _leaf_import_marker = len(lines)
    lines.append('')  # placeholder

    # all_classes: name → (class_meta, [(fname, ftype, fdefault, is_smc, field_meta)])
    all_classes = {}

    def class_meta_from(el: dict):
        return {
            "semantic_id": extract_semantic_id(el),
            "description": extract_description(el),
            "qualifiers": extract_qualifiers(el),
            "supplemental_semantic_ids": extract_supplemental(el),
        }

    def field_meta_from(el: dict):
        return {
            "semantic_id": extract_semantic_id(el),
            "description": extract_description(el),
            "qualifiers": extract_qualifiers(el),
        }

    def build(name: str, value: list, parent_sml_name: str = ""):
        fields = []
        if not value:
            return {}, fields
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

            if mt == "SubmodelElementCollection":
                child_value = el.get("value", [])
                child_meta, child_fields = build(ids, child_value)
                all_classes[ids] = (class_meta_from(el) or child_meta, child_fields)
                fields.append((fname, f"Optional[{ids}]", "None", True, fm))

            elif mt == "Entity":
                # Entity uses "statements" instead of "value" for children
                child_value = el.get("statements", [])
                child_meta, child_fields = build(ids, child_value)
                all_classes[ids] = (class_meta_from(el) or child_meta, child_fields)
                fields.append((fname, f"Optional[{ids}]", "None", True, fm))

            elif mt == "SubmodelElementList":
                items = el.get("value", [])
                sml_name = ids
                if items and isinstance(items[0], dict):
                    item_mt = items[0].get("modelType", "Property")
                    if item_mt == "SubmodelElementCollection":
                        item_ids = items[0].get("idShort", "").strip()
                        if not item_ids:
                            item_ids = f"{sml_name}Item"
                        child_meta, child_fields = build(item_ids, items[0].get("value", []), parent_sml_name=sml_name)
                        all_classes[item_ids] = (class_meta_from(items[0]) or child_meta, child_fields)
                        fields.append((fname, f"List[{item_ids}]", "[]", True, fm))
                    else:
                        py_type, _ = ELEMENT_MAP.get(item_mt, ("str", None))
                        _used_leaf_types.add(py_type)
                        fields.append((fname, f"List[{py_type}]", "[]", False, fm))
                else:
                    fields.append((fname, "List[str]", "[]", False, fm))

            else:
                py_type, _ = ELEMENT_MAP.get(mt, ("str", None))
                _used_leaf_types.add(py_type)
                fields.append((fname, py_type, None, False, fm))

        return {}, fields

    _, top_fields = build(sm_name, sm.get("submodelElements", []))
    all_classes[sm_name] = (class_meta_from(sm), top_fields)

    written = set()

    def write_class(name, meta, field_list, _visiting=None):
        if _visiting is None:
            _visiting = set()
        if name in written or name in _visiting:
            return
        _visiting.add(name)
        for _, ftype, _, _, _ in field_list:
            for cls_name in all_classes:
                if cls_name in ftype and cls_name not in written:
                    write_class(cls_name, *all_classes[cls_name], _visiting)
        written.add(name)

        if name == sm_name:
            lines.append(f'class {name}(Submodel):')
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

        if name == sm_name:
            admin = sm.get("administration", {})
            lines.append(f'    VERSION: ClassVar[str] = "{admin.get("version", "1")}"')
            lines.append(f'    REVISION: ClassVar[str] = "{admin.get("revision", "0")}"')
        lines.append('')

        if not field_list:
            lines.append('    pass')
        else:
            for fname, ftype, fdefault, is_smc, fm in field_list:
                if is_smc:
                    # SMC field — metadata is on the referenced class, no json_schema_extra needed
                    if fdefault == "None":
                        lines.append(f'    {fname}: {ftype} = None')
                    elif fdefault == "[]":
                        lines.append(f'    {fname}: {ftype} = []')
                    else:
                        lines.append(f'    {fname}: {ftype} = {fdefault}')
                else:
                    # Leaf AAS element — generate model instance with pre-filled metadata
                    sid = fm.get("semantic_id")
                    desc = fm.get("description")
                    quals = fm.get("qualifiers")
                    has_meta = sid or desc or quals
                    if ftype.startswith("List["):
                        # SML with leaf items — use json_schema_extra (List is not a model)
                        aas_parts = []
                        if sid:
                            aas_parts.append(f'"semantic_id": {json.dumps(sid)}')
                        if desc:
                            aas_parts.append(f'"description": {json.dumps(desc)}')
                        if quals:
                            qual_strs = ",\n".join(f"                {q}" for q in quals)
                            aas_parts.append(f'"qualifiers": [\n{qual_strs}\n            ]')
                        if aas_parts:
                            inner = ",\n            ".join(aas_parts)
                            lines.append(f'    {fname}: {ftype} = Field({fdefault}, json_schema_extra={{"aas": {{\n            {inner}\n        }}}})')
                        else:
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

    # Update the import line with leaf types actually used
    leaf_types = sorted(_used_leaf_types - {"str", "Capability"})
    if leaf_types:
        lines[_leaf_import_marker - 1] = (
            'from aas_pydantic import (\n'
            '    Submodel, SubmodelElementCollection, Capability, Qualifier,\n'
            '    ' + ', '.join(leaf_types) + ',\n'
            ')'
        )

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
