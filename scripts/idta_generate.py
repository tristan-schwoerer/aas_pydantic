#!/usr/bin/env python3
"""Generate aas_pydantic models from IDTA submodel template JSON.

Emits the basyx/IDTA-aligned container structure:

    Submodel:  submodel_element: Dict[str, SubmodelElement] = { child: Elem(...) }
    SMC:       value:            Dict[str, SubmodelElement] = { child: Elem(...) }
    SML:       value:            List[Any]                   = [ Item(...) ]

Child elements are pre-populated from the template's example element(s) as
typed instances, with all semantic_id / description / value_type metadata.
The dict key IS the child's id_short: every instance carries
``id_short=<key>`` so key == Python variable name == model id_short ==
basyx id_short (one canonical name per element).

There is no cardinality analysis, no field renames, no Pydantic name-collision
workarounds: the container structure makes the generator template-agnostic.
Subclasses may narrow the container element type, e.g.
``value: Dict[str, Parameter]`` (see the handwritten Variables/Parameters
submodels).
"""

import json
import keyword
import os
import re
import sys

# modelType → Python type name
ELEMENT_MAP = {
    "Property": "Property",
    "MultiLanguageProperty": "MultiLanguageProperty",
    "Range": "Range",
    "ReferenceElement": "ReferenceElement",
    "RelationshipElement": "RelationshipElement",
    "File": "File",
    "Blob": "Blob",
    "Capability": "Capability",
    "Operation": "Operation",
}


def safe_name(name: str) -> str:
    # IDTA placeholders like ``Mode__00__`` mean "a repeatable instance whose
    # id_short the user picks" — strip the ``__NN__`` suffix so class and field
    # names are the clean base name (``Mode`` → field ``mode``).
    name = re.sub(r"__\d+__$", "", name or "")
    return re.sub(r"[^0-9a-zA-Z_]", "_", name)


def snake(name: str) -> str:
    s = re.sub(r"(?<!^)(?=[A-Z])", "_", name)
    return s.replace("-", "_").lower()


def field_name(name: str) -> str:
    """snake_case field name that is a valid Python identifier (reserved words
    get a trailing underscore, e.g. W3C ``in`` → ``in_``).  IDTA ``__NN__``
    placeholder suffixes (``Mode__00__``) are stripped first (→ ``mode``)."""
    name = re.sub(r"__\d+__$", "", name or "")
    s = snake(name)
    if keyword.iskeyword(s):
        s += "_"
    return s


_CLASH_RE = re.compile(r"^    (\w+): (\w+) = (\w+)\(")
_DICT_CLASH_RE = re.compile(r"^    (\w+): Dict\[str, (\w+)\] = \{\}")


def _rewrite_clash_fields(body: list, aliases_emitted: set):
    """Rewrite values-class field lines where the field name equals its type
    annotation (pydantic rejects ``security: security = security()`` and
    crashes on the multi-cardinality ``property_name: Dict[str,
    property_name] = {}`` form — the field name == element class name makes
    pydantic's schema gather fail with ``KeyError: 'type'``).

    The type is aliased as a ``TypeAlias`` (``security_t: TypeAlias =
    security``) emitted once, before the first values class that needs it —
    the aliased class is always already defined at that point (child
    containers precede the parent values class in definition order)."""
    new_body = []
    alias_lines = []
    for line in body:
        m = _CLASH_RE.match(line)
        if m and m.group(1) == m.group(2) == m.group(3):
            t = m.group(1)
            alias = f"{t}_t"
            if alias not in aliases_emitted:
                aliases_emitted.add(alias)
                alias_lines.append(f"{alias}: TypeAlias = {t}")
            new_body.append(line.replace(f"{t}: {t} = {t}(", f"{t}: {alias} = {alias}("))
            continue
        m = _DICT_CLASH_RE.match(line)
        if m and m.group(1) == m.group(2):
            t = m.group(1)
            alias = f"{t}_t"
            if alias not in aliases_emitted:
                aliases_emitted.add(alias)
                alias_lines.append(f"{alias}: TypeAlias = {t}")
            new_body.append(line.replace(
                f"{t}: Dict[str, {t}] = {{}}",
                f"{t}: Dict[str, {alias}] = {{}}",
            ))
            continue
        new_body.append(line)
    return new_body, alias_lines


def extract_semantic_id(el: dict) -> str:
    sem = el.get("semanticId") or {}
    for k in sem.get("keys", []) or []:
        if k.get("value"):
            return k.get("value", "")
    return ""


def extract_supplemental_semantic_ids(el: dict) -> list:
    """Supplemental semanticIds (list of IRIs) from ``supplementalSemanticIds``.
    These disambiguate elements that share a main semanticId — e.g. the AID
    ``InterfaceTemplateFor*`` all use ``.../Interface`` but each protocol has a
    unique supplemental IRI (per the IDTA PDF; the published JSON had OPC UA /
    BACnet copy-pasted from MQTT and is patched in the vendored copy)."""
    out = []
    for s in (el.get("supplementalSemanticIds") or []):
        for k in (s.get("keys") or []):
            if k.get("value"):
                out.append(k["value"])
    return out


def extract_description(el: dict) -> str:
    d = el.get("description")
    if isinstance(d, list):  # AAS JSON: [{"language": "en", "text": "..."}]
        return d[0].get("text", "") if d else ""
    if isinstance(d, dict):
        texts = d.get("texts") or []
        return texts[0].get("text", "") if texts else ""
    return ""


def extract_value_type(el: dict) -> str:
    return el.get("valueType", "")


def extract_cardinality(el: dict) -> str:
    """Cardinality qualifier value (e.g. ``ZeroToMany``, ``ZeroToOne``, ``One``)
    — how many instances of this element a container may hold.

    Templates encode it under three different qualifier ``type`` spellings:
    ``SMT/Cardinality``, ``Cardinality`` (AID, ConceptQualifier) and
    ``SMT/SMT/Cardinality`` (CCT) — all end in ``Cardinality``.  Values also
    carry typos in the wild (``ZerotoMany``, ``ZerotToOne``, ``ZeroToOne ``),
    so the value is normalized before returning."""
    for q in (el.get("qualifiers") or []):
        if "Cardinality" in q.get("type", ""):
            return normalize_cardinality(q.get("value", ""))
    return ""


def normalize_cardinality(value: str) -> str:
    """Normalize template cardinality values (strip whitespace + common typos)."""
    v = (value or "").strip()
    # templates contain typos: 'ZerotoMany', 'ZerotToOne', 'ZeroToOne '
    return v.replace("Zeroto", "ZeroTo").replace("Zerot", "ZeroT")


# Cardinalities that allow more than one instance of an element → the
# values model field becomes a dynamic ``Dict[str, Element]`` (name-keyed),
# so MANY instances are possible — exactly like the pre-values-model dicts.
_MULTI_CARDINALITY = {
    "ZeroToMany", "OneToMany",  # standard SMT encodings
    "TwoToMany", "Three",       # other >1 encodings in the wild
    "Recursive",                # recursive structures allow unbounded nesting
}


def emit_reference(ref: dict, indent: str) -> list:
    """Source lines constructing a pydantic Reference from an AAS JSON
    reference dict (``{"type": ..., "keys": [...]}``)."""
    cls = "ModelReference" if ref.get("type") == "ModelReference" else "ExternalReference"
    key_src = [
        f'{indent}        Key(type_={json.dumps(k.get("type", ""))}, '
        f'value={json.dumps(k.get("value", ""))}),'
        for k in (ref.get("keys") or [])
    ]
    lines = [f"{indent}{cls}("]
    if key_src:
        lines.append(f"{indent}    key=(")
        lines.extend(key_src)
        lines.append(f"{indent}    ),")
    lines.append(f"{indent})")
    return lines


def emit_leaf_instance(el: dict, indent: str) -> list:
    """Source lines constructing a leaf element instance.

    No ``id_short`` is emitted — the dict key is the single source of truth
    for the id_short (stamped at the container boundary on construction).
    """
    mt = el.get("modelType", "Property")
    cls = ELEMENT_MAP.get(mt, "Property")
    lines = [f"{indent}{cls}("]
    args = []
    sid = extract_semantic_id(el)
    desc = extract_description(el)
    vt = extract_value_type(el)
    if sid:
        args.append(f'semantic_id={json.dumps(sid)}')
    if desc:
        args.append(f'description={json.dumps(desc)}')
    if vt and cls in ("Property", "Range"):
        args.append(f'value_type={json.dumps(vt)}')
    for i, a in enumerate(args):
        lines.append(f"{indent}    {a}{',' if i < len(args) - 1 else ','}")
    if cls == "RelationshipElement":
        # Endpoints are References in basyx — emit the template's reference.
        for key_name in ("first", "second"):
            ref = el.get(key_name)
            if isinstance(ref, dict):
                ref_src = emit_reference(ref, indent + "    ")
                lines.append(f"{indent}    {key_name}=" + ref_src[0].lstrip())
                lines.extend(ref_src[1:])
                lines[-1] = lines[-1] + ","
    lines.append(f"{indent})")
    return lines


def children_of(el: dict) -> list:
    return [
        c
        for c in (el.get("submodelElements") or el.get("value")
                  or el.get("statements") or [])
        if isinstance(c, dict)
    ]


def gen_template(template_path: str, output_dir: str):
    with open(template_path) as f:
        data = json.load(f)
    submodels = data.get("submodels", [])
    if not submodels:
        print(f"No submodels in {template_path}")
        return
    sm = submodels[0]
    sm_name = safe_name(sm["idShort"])

    # name → (meta_lines, body_lines); order of definition
    classes = {}
    order = []
    values_classes = set()
    entity_classes = set()
    sml_classes = set()
    leaf_bases = {}  # dedicated leaf element class name → base (leaf) class name
    _used_leaf_types = {
        "Submodel", "SubmodelElement", "SubmodelElementCollection",
        "SubmodelElementList", "ContainerValue",
    }

    def register(name, meta, body, is_values=False, is_entity=False, is_sml=False):
        if name not in classes:
            classes[name] = (meta, body)
            order.append(name)
            if is_values:
                values_classes.add(name)
            if is_entity:
                entity_classes.add(name)
            if is_sml:
                sml_classes.add(name)

    def dedicated_leaf_cls(c: dict, leaf_cls: str) -> str:
        """Register (once) a dedicated subclass of *leaf_cls* carrying the
        element's concept semanticId — e.g. ``class SameAs(RelationshipElement)``
        with ``semantic_id="https://.../SameAs/1/0"`` — and return its name.
        This is the proper home for the concept semanticId (the old
        ``_multi_cardinality`` ClassVar); back-conversion groups Dict-map
        children by the resolved element class instead of a sid lookup.

        Falls back to the generic *leaf_cls* when there is no concept
        semanticId, the element has no idShort, or the name would shadow the
        base class or collide with an already-registered class."""
        sid = extract_semantic_id(c)
        elem_name = safe_name(c.get("idShort", ""))
        if not sid or not elem_name or elem_name == leaf_cls:
            return leaf_cls
        if elem_name in leaf_bases:
            return elem_name  # already registered as a dedicated leaf
        if elem_name in classes:
            return leaf_cls  # name taken by a container/other class — fall back
        meta = [f'    semantic_id: str = {json.dumps(sid)}']
        desc = extract_description(c)
        if desc:
            meta.append(f'    description: str = {json.dumps(desc)}')
        supp = extract_supplemental_semantic_ids(c)
        if supp:
            meta.append(f'    supplemental_semantic_ids: List[str] = {json.dumps(supp)}')
        register(elem_name, meta, [])
        leaf_bases[elem_name] = leaf_cls
        return elem_name

    def walk(el: dict, container_key: str, stack: tuple = (), name: str = None) -> list:
        """Register the ``{Name}Values`` class and the ``{Name}`` container
        class for *el*; returns the values-class body lines (one typed field
        per child, field name == id_short).

        Children whose template cardinality allows more than one
        (``SMT/Cardinality`` ZeroToMany/OneToMany) become dynamic
        ``Dict[str, Element]`` maps — MANY instances keyed by name are then
        possible, exactly like the pre-values-model dicts.

        ``name`` overrides the class name (used for SML items whose template
        idShort is missing — falls back to ``{ListName}Item``).  ``stack``
        holds the class names currently being defined (for detecting
        recursive children like HSEM ``Node`` containing a ``Node`` — those
        become empty ``Dict[str, Node]`` maps, so nothing recurses).
        """
        cname = name or safe_name(el.get("idShort", ""))
        vname = f"{cname}Values"
        mt_el = el.get("modelType", "")
        kids = children_of(el)
        lines = []
        for c in kids:
            child_name = safe_name(c.get("idShort", ""))
            skey = field_name(c.get("idShort", child_name))  # field = id_short
            mt = c.get("modelType", "")
            multi = extract_cardinality(c) in _MULTI_CARDINALITY
            if multi:
                # multi-cardinality → dynamic name-keyed map of this element.
                # Generic-leaf elements get a dedicated subclass carrying the
                # concept semanticId (e.g. ``class SameAs(RelationshipElement)``
                # with ``semantic_id``) — back-conversion groups by the
                # resolved element class, so no ``_multi_cardinality`` ClassVar
                # is needed.
                if mt in ("SubmodelElementCollection", "Entity"):
                    if child_name in stack:
                        # recursive child (e.g. HSEM Node in Node) — an empty
                        # Dict[str, <container>] map; no instantiation, so the
                        # default cannot recurse.
                        lines.append(f"    {skey}: Dict[str, {cname}] = {{}}")
                        continue
                    child_container = "statements" if mt == "Entity" else "value"
                    walk(c, child_container, stack + (child_name,))
                    lines.append(f"    {skey}: Dict[str, {child_name}] = {{}}")
                elif mt == "SubmodelElementList":
                    _walk_sml(c, stack)
                    lines.append(f"    {skey}: Dict[str, {child_name}] = {{}}")
                else:
                    leaf_cls = ELEMENT_MAP.get(mt, "Property")
                    _used_leaf_types.add(leaf_cls)
                    elem_cls = dedicated_leaf_cls(c, leaf_cls)
                    lines.append(f"    {skey}: Dict[str, {elem_cls}] = {{}}")
                continue
            if mt in ("SubmodelElementCollection", "Entity"):
                if child_name in stack:
                    # Recursive single-cardinality child — skip entirely so the
                    # ancestor's full definition wins and the default doesn't
                    # recurse forever.
                    continue
                child_container = "statements" if mt == "Entity" else "value"
                walk(c, child_container, stack + (child_name,))
                lines.append(f"    {skey}: {child_name} = {child_name}()")
            elif mt == "SubmodelElementList":
                _walk_sml(c, stack)
                lines.append(f"    {skey}: {child_name} = {child_name}()")
            else:
                leaf_cls = ELEMENT_MAP.get(mt, "Property")
                _used_leaf_types.add(leaf_cls)
                leaf_src = emit_leaf_instance(c, "    ")
                lines.append(f"    {skey}: {leaf_cls} = " + leaf_src[0].lstrip())
                lines.extend(leaf_src[1:])
        if not lines:
            lines.append("    pass")
        # values class: one typed field per child (strict — catches typos)
        register(
            vname,
            ["    model_config = {'extra': 'forbid'}"],
            lines,
            is_values=True,
        )
        # container class: attributes (semantic_id, ...) + typed value
        meta = [f'    semantic_id: str = {json.dumps(extract_semantic_id(el))}']
        desc = extract_description(el)
        if desc:
            meta.append(f'    description: str = {json.dumps(desc)}')
        supp = extract_supplemental_semantic_ids(el)
        if supp:
            meta.append(f'    supplemental_semantic_ids: List[str] = {json.dumps(supp)}')
        is_entity = mt_el == "Entity"
        if is_entity:
            _used_leaf_types.add("Entity")
            meta.append(
                f'    entity_type: str = {json.dumps(el.get("entityType", "CoManagedEntity"))}'
            )
            gid = el.get("globalAssetId")
            if gid:
                meta.append(f'    global_asset_id: str = {json.dumps(gid)}')
        if any(f": {cname}" in l or f": Dict[str, {cname}]" in l for l in lines):
            # The values class references the container itself (recursive
            # child) — the default must be built lazily, else the eager
            # ``= {vname}()`` forces schema construction before the container
            # class exists (pydantic circular-ref guard).
            body = [f"    {container_key}: {vname} = Field(default_factory={vname})"]
        else:
            body = [f"    {container_key}: {vname} = {vname}()"]
        register(cname, meta, body, is_entity=is_entity)
        return lines

    def _walk_sml(c: dict, stack: tuple):
        """Register an SML class with a typed ``value: List[Item]`` (AASd-108:
        homogeneous lists only — heterogeneous ones start empty)."""
        cname = safe_name(c.get("idShort", ""))
        item_kids = children_of(c)
        sub_meta = [f'    semantic_id: str = {json.dumps(extract_semantic_id(c))}']
        desc = extract_description(c)
        if desc:
            sub_meta.append(f'    description: str = {json.dumps(desc)}')
        supp = extract_supplemental_semantic_ids(c)
        if supp:
            sub_meta.append(f'    supplemental_semantic_ids: List[str] = {json.dumps(supp)}')
        item_src = []
        item_classes = set()  # for AASd-108 homogeneity check
        for item in item_kids:
            imt = item.get("modelType", "")
            if imt in ("SubmodelElementCollection", "Entity"):
                item_name = safe_name(item.get("idShort", f"{cname}Item"))
                if item_name in stack:
                    # Recursive item — skip entirely.
                    continue
                item_container = "statements" if imt == "Entity" else "value"
                walk(item, item_container, stack + (item_name,), name=item_name)
                item_src.append(
                    f'{item_name}(id_short={json.dumps(item.get("idShort", item_name))})'
                )
                item_classes.add(item_name)
            else:
                leaf = emit_leaf_instance(item, "        ")
                leaf_cls = ELEMENT_MAP.get(imt, "Property")
                _used_leaf_types.add(leaf_cls)
                item_src.append("\n".join(leaf))
                item_classes.add(leaf_cls)
        if item_src and len(item_classes) == 1:
            # Homogeneous list — safe to pre-populate (AASd-108).
            # item_type lets back-conversion restore item types even though
            # AASd-114 strips item semanticIds in basyx.
            item_cls = next(iter(item_classes))
            sub_meta.append(f"    item_type: ClassVar = {item_cls}")
            sml_body = [f"    value: List[{item_cls}] = ["]
            for s in item_src:
                sml_body.append(f"        {s},")
            sml_body.append("    ]")
        else:
            # Heterogeneous or empty (e.g. CapabilityPropertyType lists
            # Range/Property/MLP exemplars) — basyx cannot represent a
            # mixed-type SML (AASd-108), so start empty; users populate it
            # with a homogeneous list.
            sml_body = ["    value: List[Any] = []"]
        register(cname, sub_meta, sml_body, is_sml=True)

    sm_meta = [f'    semantic_id: str = {json.dumps(extract_semantic_id(sm))}']
    desc = extract_description(sm)
    if desc:
        sm_meta.append(f'    description: str = {json.dumps(desc)}')
    walk(sm, "submodel_element")
    admin = sm.get("administration", {})
    sm_meta.append(f'    VERSION: ClassVar[str] = "{admin.get("version", "1")}"')
    sm_meta.append(f'    REVISION: ClassVar[str] = "{admin.get("revision", "0")}"')
    # prepend the Submodel-level meta (walk registered semantic_id/description)
    existing = classes[sm_name][0]
    classes[sm_name] = (sm_meta, classes[sm_name][1])

    # ── Assemble file ──
    # Build the body first (clash aliases are emitted during assembly), then
    # derive the imports from the assembled text so nothing is missed.
    body = []
    aliases_emitted = set()
    for name in order:
        meta, cbody = classes[name]
        if name in values_classes:
            base = "ContainerValue"
        elif name == sm_name:
            base = "Submodel"
        elif name in entity_classes:
            base = "Entity"
        elif name in sml_classes:
            base = "SubmodelElementList"
        elif name in leaf_bases:
            base = leaf_bases[name]
        else:
            base = "SubmodelElementCollection"
        if name in values_classes:
            # pydantic rejects a field whose name equals its type annotation
            # (e.g. ``items: items = items()``) — alias the type as a
            # TypeAlias, emitted once, before the first values class needing
            # it.  The aliased class is always already defined at that point
            # (child containers precede the parent values class in order).
            cbody, alias_lines = _rewrite_clash_fields(cbody, aliases_emitted)
            for a in alias_lines:
                body.append(f"# alias so field ``{a.split(':')[0]}`` can name a class of the same id_short")
                body.append(f"{a}")
        body.append(f"class {name}({base}):")
        body.extend(meta)
        body.extend(cbody)
        body.append('')

    body.append('# ── Resolve forward references (Pydantic circular refs) ──')
    for name in order:
        body.append(f'{name}.model_rebuild()')
    body.append('')

    all_src = "\n".join(body)
    lines = []
    lines.append(f'"""{sm_name} — generated from IDTA template."""')
    lines.append('')
    lines.append('from __future__ import annotations')
    lines.append('')
    typing_names = ["Any", "ClassVar", "List"]
    if "Dict[" in all_src:
        typing_names.append("Dict")
    if ": TypeAlias" in all_src:
        typing_names.append("TypeAlias")
    lines.append(f"from typing import {', '.join(typing_names)}")
    lines.append('from aas_pydantic import (')
    aas_types = {"Submodel", "SubmodelElement", "SubmodelElementCollection",
                 "SubmodelElementList", "Entity", "Qualifier", "ContainerValue",
                 "ExternalReference", "ModelReference", "Key"}
    aas_types |= set(ELEMENT_MAP.values())
    imports = sorted(t for t in _used_leaf_types if t in aas_types)
    # Reference endpoints (first/second) use ExternalReference/ModelReference/Key.
    if "ExternalReference(" in all_src:
        imports = sorted(set(imports) | {"ExternalReference", "Key"})
    if "ModelReference(" in all_src:
        imports = sorted(set(imports) | {"ModelReference", "Key"})
    lines.append('    ' + ', '.join(imports) + ',')
    lines.append(')')
    if "Field(default_factory" in all_src:
        lines.append('from pydantic import Field')
    lines.append('')

    lines.extend(body)

    os.makedirs(output_dir, exist_ok=True)
    out_path = os.path.join(output_dir, f"{snake(sm_name)}.py")
    with open(out_path, "w") as f:
        f.write("\n".join(lines))
    print(f"✅ {out_path}")
    print(f"   {sm_name}(Submodel) + {len(order) - 1} classes")


if __name__ == "__main__":
    if len(sys.argv) >= 2:
        gen_template(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else ".")
    else:
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
