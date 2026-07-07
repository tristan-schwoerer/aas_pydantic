#!/usr/bin/env python3
"""Generate aas_pydantic models from IDTA submodel template JSON."""

import json, sys, os, re

ELEMENT_MAP = {
    "Property": ("str", '""'),
    "MultiLanguageProperty": ("str", '""'),
    "Range": ("str", '""'),
    "ReferenceElement": ("str", '""'),
    "RelationshipElement": ("str", '""'),
    "File": ("str", '""'),
    "Blob": ("str", '""'),
    "Capability": ("Capability", "Capability()"),
    "SubmodelElementCollection": (None, None),
    "SubmodelElementList": (None, None),
}


def snake(name: str) -> str:
    return re.sub(r'(?<!^)(?=[A-Z])', '_', name).lower()


def extract_semantic_id(el: dict) -> str:
    sid = el.get("semanticId", {})
    keys = sid.get("keys", [])
    return keys[0]["value"] if keys else ""


def extract_qualifiers(el: dict) -> list:
    """Return list of Qualifier constructor calls as strings (for class-level use)."""
    quals = el.get("qualifiers", el.get("qualifier", []))
    if not isinstance(quals, list):
        return []
    result = []
    for q in quals:
        qtype = q.get("type", "")
        qval = q.get("value", "")
        qsid = extract_semantic_id(q)
        if qsid:
            result.append(f'Qualifier(type_={json.dumps(qtype)}, value={json.dumps(qval)}, semantic_id={json.dumps(qsid)})')
        else:
            result.append(f'Qualifier(type_={json.dumps(qtype)}, value={json.dumps(qval)})')
    return result


def extract_qualifiers_dict(el: dict) -> list:
    """Return list of raw qualifier dicts (for json_schema_extra use)."""
    quals = el.get("qualifiers", el.get("qualifier", []))
    if not isinstance(quals, list):
        return []
    result = []
    for q in quals:
        d = {"type": q.get("type", ""), "value": q.get("value", "")}
        qsid = extract_semantic_id(q)
        if qsid:
            d["semantic_id"] = qsid
        result.append(d)
    return result


def extract_description(el: dict) -> str:
    desc = el.get("description", "")
    if isinstance(desc, list):
        for d in desc:
            if d.get("language") == "en":
                return d.get("text", "")
    return desc if isinstance(desc, str) else ""


def extract_supplemental(el: dict) -> list:
    suppl = el.get("supplementalSemanticId", [])
    if isinstance(suppl, list):
        return [s.get("keys", [{}])[0].get("value", "") for s in suppl if s.get("keys")]
    return []


def format_py(val):
    if isinstance(val, str):
        return json.dumps(val)
    if isinstance(val, list):
        return json.dumps(val)
    return repr(val)


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
    lines.append('from typing import ClassVar, List, Optional')
    lines.append('from pydantic import Field')
    lines.append('from aas_pydantic import Submodel, SubmodelElementCollection, Capability, Qualifier')
    lines.append('')

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
            "qualifiers": extract_qualifiers_dict(el),
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
                        py_type, _ = ELEMENT_MAP.get(item_mt, ("str", '""'))
                        fields.append((fname, f"List[{py_type}]", "[]", False, fm))
                else:
                    fields.append((fname, "List[str]", "[]", False, fm))

            else:
                py_type, default = ELEMENT_MAP.get(mt, ("str", '""'))
                fields.append((fname, py_type, default, False, fm))

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
                    # Primitive field — needs json_schema_extra for metadata
                    aas = {}
                    if fm.get("semantic_id"):
                        aas["semantic_id"] = fm["semantic_id"]
                    if fm.get("description"):
                        aas["description"] = fm["description"]
                    if fm.get("qualifiers"):
                        aas["qualifiers"] = fm["qualifiers"]
                    if aas:
                        aas_str = json.dumps(aas)
                        lines.append(f'    {fname}: {ftype} = Field({fdefault}, json_schema_extra={{"aas": {aas_str}}})')
                    else:
                        lines.append(f'    {fname}: {ftype} = {fdefault}')
        lines.append('')

    for cls_name in all_classes:
        if cls_name != sm_name:
            write_class(cls_name, *all_classes[cls_name])
    write_class(sm_name, *all_classes[sm_name])

    os.makedirs(output_dir, exist_ok=True)
    out_path = os.path.join(output_dir, f"{snake(sm_name)}.py")
    with open(out_path, "w") as f:
        f.write("\n".join(lines))
    print(f"✅ {out_path}")
    print(f"   {sm_name}(Submodel) + {len(written)-1} SMC classes")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python idta_generate.py <template.json> [output_dir]")
        sys.exit(1)
    gen_template(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else ".")
