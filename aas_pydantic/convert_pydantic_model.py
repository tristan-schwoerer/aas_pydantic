from __future__ import annotations

from collections import OrderedDict
from urllib import parse
from enum import Enum
import uuid


from basyx.aas import model

from typing import Optional, Union
from aas_pydantic import convert_util, aas_model

from aas_pydantic.convert_util import (
    AAS_META_KEY,
    convert_primitive_type_to_xsdtype,
    get_aas_meta,
    get_attribute_infos,
    get_id_short,
    get_semantic_id,
    get_value_type_of_attribute,
)

import logging

logger = logging.getLogger(__name__)


def convert_model_to_aas(
    model_aas: aas_model.AAS,
) -> model.DictObjectStore[model.Identifiable]:
    """
    Convert a model aas to an Basyx AssetAdministrationShell and return it as a DictObjectStore with all Submodels

    Args:
        model_aas (aas_model.AAS): model aas to convert

    Returns:
        model.DictObjectStore[model.Identifiable]: DictObjectStore with all Submodels
    """
    aas_attribute_infos = get_attribute_infos(model_aas)
    aas_submodels = {}
    aas_submodel_data_specifications = []
    for attribute_info in aas_attribute_infos:
        submodel = convert_model_to_submodel(model_submodel=attribute_info.value)
        attribute_data_specification = (
            convert_util.get_data_specification_for_attribute(attribute_info, submodel)
        )
        aas_submodel_data_specifications.append(attribute_data_specification)
        if submodel and not submodel.id_short in aas_submodels:
            aas_submodels.update({submodel.id_short: submodel})

    asset_information = model.AssetInformation(
        global_asset_id=model.Identifier(model_aas.id),
        asset_kind=model.AssetKind.INSTANCE,
        asset_type=model.Identifier("Instance"),
    )

    basyx_aas = model.AssetAdministrationShell(
        asset_information=asset_information,
        id_short=get_id_short(model_aas),
        id_=model.Identifier(model_aas.id),
        description=convert_util.get_basyx_description_from_model(model_aas),
        submodel={
            model.ModelReference.from_referable(submodel)
            for submodel in aas_submodels.values()
        },
        embedded_data_specifications=convert_util.get_data_specification_for_model(
            model_aas
        )
        + aas_submodel_data_specifications,
    )
    obj_store: model.DictObjectStore[model.Identifiable] = model.DictObjectStore()
    obj_store.add(basyx_aas)
    for sm in aas_submodels.values():
        obj_store.add(sm)
    return obj_store


def convert_model_to_submodel(
    model_submodel: aas_model.Submodel,
    administration: Optional[model.AdministrativeInformation] = None,
) -> Optional[model.Submodel]:
    if not model_submodel:
        return
    submodel_attributes = get_attribute_infos(model_submodel)
    submodel_elements = []
    submodel_element_data_specifications = []

    for attribute_info in submodel_attributes:
        # Skip metadata fields (not actual submodel elements)
        if attribute_info.name in ("qualifiers", "supplemental_semantic_ids"):
            continue
        # Pass field_info so create_submodel_element can read AAS metadata
        submodel_element = create_submodel_element(
            attribute_info.name, attribute_info.value,
            field_info=attribute_info.field_info,
        )
        attribute_data_specification = (
            convert_util.get_data_specification_for_attribute(
                attribute_info, submodel_element
            )
        )
        submodel_element_data_specifications.append(attribute_data_specification)
        immutable_attribute_data_specification = (
            convert_util.get_immutable_data_specification_for_attribute(attribute_info)
        )
        if immutable_attribute_data_specification:
            submodel_element_data_specifications.append(
                immutable_attribute_data_specification
            )
        if not attribute_info.field_info.is_required():
            default_data_specification = (
                convert_util.get_default_data_specification_for_attribute(
                    attribute_info, submodel_element
                )
            )
            if default_data_specification:
                submodel_element_data_specifications.append(default_data_specification)
        if submodel_element:
            submodel_elements.append(submodel_element)

    basyx_submodel = model.Submodel(
        id_short=get_id_short(model_submodel),
        id_=model.Identifier(model_submodel.id),
        description=convert_util.get_basyx_description_from_model(model_submodel),
        embedded_data_specifications=convert_util.get_data_specification_for_model(
            model_submodel
        )
        + submodel_element_data_specifications,
        semantic_id=get_semantic_id(model_submodel),
        submodel_element=submodel_elements,
        administration=administration,
    )
    return basyx_submodel


def create_submodel_element(
    attribute_name: str,
    attribute_value: Union[
        aas_model.SubmodelElementCollection, str, float, int, bool, tuple, list, set
    ],
    field_info=None,
) -> Optional[model.SubmodelElement]:
    """Create a basyx SubmodelElement — type-based dispatch."""
    if not attribute_value and not (isinstance(attribute_value, bool) or attribute_value == 0):
        return None

    # Metadata: for model types read from the instance; for primitives from field_info
    aas_meta = get_aas_meta(field_info) if field_info else {}
    sid = (_make_external_reference(aas_meta["semantic_id"])
           if aas_meta.get("semantic_id") else None)
    quals_meta = aas_meta.get("qualifiers", [])
    suppl_meta = aas_meta.get("supplemental_semantic_ids", [])
    desc_text = aas_meta.get("description")

    def _model_metadata(inst):
        """Read qualifiers/supplemental from a model instance (HasSemantics fields)."""
        q = _make_qualifiers(getattr(inst, 'qualifiers', None) or quals_meta)
        s = ([_make_external_reference(x) for x in (getattr(inst, 'supplemental_semantic_ids', None) or suppl_meta)]
             if (getattr(inst, 'supplemental_semantic_ids', None) or suppl_meta) else [])
        d = (model.MultiLanguageTextType({"en": desc_text}) if desc_text
             else (convert_util.get_basyx_description_from_model(inst) if inst.description else None))
        return q, s, d

    quals = _make_qualifiers(quals_meta) if quals_meta else []
    suppl = [_make_external_reference(s) for s in suppl_meta] if suppl_meta else []
    desc = model.MultiLanguageTextType({"en": desc_text}) if desc_text else None

    if isinstance(attribute_value, aas_model.SubmodelElementCollection):
        smc = create_submodel_element_collection(attribute_value)
        q, s, d = _model_metadata(attribute_value)
        if q: smc.qualifier = q
        if s: smc.supplemental_semantic_id = s
        if d: smc.description = d
        return smc

    if isinstance(attribute_value, (list, tuple, set)):
        sml = create_submodel_element_list(attribute_name, attribute_value, field_info)
        if sid: sml.semantic_id = sid
        if quals: sml.qualifier = quals
        if suppl: sml.supplemental_semantic_id = suppl
        if desc: sml.description = desc
        return sml

    if isinstance(attribute_value, str) and (
        (parse.urlparse(attribute_value).scheme and parse.urlparse(attribute_value).netloc)
        or attribute_value.split("_")[-1] in ["id", "ids"]
    ):
        ref = model.ModelReference(key=(model.Key(type_=model.KeyTypes.ASSET_ADMINISTRATION_SHELL, value=attribute_value),), type_="")
        return model.ReferenceElement(id_short=attribute_name, value=ref, semantic_id=sid, qualifier=quals, supplemental_semantic_id=suppl, description=desc)

    if isinstance(attribute_value, aas_model.Capability):
        q, s, d = _model_metadata(attribute_value)
        return model.Capability(id_short=attribute_name, semantic_id=sid or get_semantic_id(attribute_value), qualifier=q, supplemental_semantic_id=s, description=d)

    if isinstance(attribute_value, aas_model.Operation):
        q, s, d = _model_metadata(attribute_value)
        return create_operation(attribute_name, attribute_value, sid, q, s, d)

    if isinstance(attribute_value, aas_model.File):
        return create_file(attribute_value)
    if isinstance(attribute_value, aas_model.Blob):
        return create_blob(attribute_value)

    prop = create_property(attribute_name, attribute_value)
    if sid: prop.semantic_id = sid
    if quals: prop.qualifier = quals
    if suppl: prop.supplemental_semantic_id = suppl
    if desc: prop.description = desc
    return prop


def create_property(
    attribute_name: str,
    attribute_value: Union[str, int, float, bool],
) -> model.Property:
    if isinstance(attribute_value, Enum):
        attribute_value = attribute_value.value
        attribute_type = str
    else:
        attribute_type = type(attribute_value)

    property = model.Property(
        id_short=attribute_name,
        value_type=convert_primitive_type_to_xsdtype(attribute_type),
        value=attribute_value,
    )
    return property


def create_submodel_element_collection(
    model_sec: aas_model.SubmodelElementCollection,
) -> model.SubmodelElementCollection:
    value = []
    smc_attributes = get_attribute_infos(model_sec)
    submodel_element_data_specifications = []

    for attribute_info in smc_attributes:
        # Skip metadata fields (not actual submodel elements)
        if attribute_info.name in ("qualifiers", "supplemental_semantic_ids"):
            continue
        sme = create_submodel_element(
            attribute_info.name, attribute_info.value,
            field_info=attribute_info.field_info,
        )
        attribute_data_specification = (
            convert_util.get_data_specification_for_attribute(attribute_info, sme)
        )
        submodel_element_data_specifications.append(attribute_data_specification)
        immutable_attribute_data_specification = (
            convert_util.get_immutable_data_specification_for_attribute(attribute_info)
        )
        if immutable_attribute_data_specification:
            submodel_element_data_specifications.append(
                immutable_attribute_data_specification
            )
        if (
            not attribute_info.field_info.is_required()
            and attribute_info.field_info.default
        ):
            default_data_specification = (
                convert_util.get_default_data_specification_for_attribute(
                    attribute_info, sme
                )
            )
            if default_data_specification:
                submodel_element_data_specifications.append(default_data_specification)
        if sme:
            value.append(sme)

    id_short = get_id_short(model_sec)

    smc = model.SubmodelElementCollection(
        id_short=id_short,
        value=value,
        description=convert_util.get_basyx_description_from_model(model_sec),
        embedded_data_specifications=convert_util.get_data_specification_for_model(
            model_sec
        )
        + submodel_element_data_specifications,
        semantic_id=get_semantic_id(model_sec),
    )
    return smc


def patch_id_short_with_temp_attribute(
    submodel_element_collection: model.SubmodelElementCollection,
) -> None:
    """
    Patch the id_short of a SubmodelElementCollection as an attribute in the value of the SubmodelElementCollection, to make it accesible after retrieving from the value list.

    Args:
        submodel_element_collection (model.SubmodelElementCollection): SubmodelElementCollection to patch
    """
    temp_id_short_property = model.Property(
        id_short="temp_id_short_attribute_" + uuid.uuid4().hex,
        value_type=get_value_type_of_attribute(str),
        value=submodel_element_collection.id_short,
    )
    submodel_element_collection.value.add(temp_id_short_property)


def create_submodel_element_list(
    attribute_name: str, value: list | tuple | set,
    field_info=None,  # Optional[FieldInfo] — for list-level AAS metadata
) -> model.SubmodelElementList:
    submodel_elements = []
    submodel_element_ids = OrderedDict()
    for el in value:
        submodel_element = create_submodel_element(attribute_name, el, field_info=field_info)
        if isinstance(submodel_element, model.SubmodelElementCollection):
            if submodel_element.id_short in submodel_element_ids:
                raise ValueError(
                    f"Submodel element collection with id {submodel_element.id_short} already exists in list"
                )
            submodel_element_ids.update({submodel_element.id_short: None})
            patch_id_short_with_temp_attribute(submodel_element)
        submodel_element.id_short = None
        # Clear individual semantic_ids (AASd-114: all SML items share the list's semantic_id)
        if hasattr(submodel_element, 'semantic_id') and submodel_element.semantic_id:
            if hasattr(submodel_element, 'supplemental_semantic_id'):
                submodel_element.supplemental_semantic_id = []
            submodel_element.semantic_id = None
        submodel_elements.append(submodel_element)

    if submodel_elements and isinstance(submodel_elements[0], model.Property):
        value_type_list_element = type(value.__iter__().__next__())
        type_value_list_element = type(submodel_elements[0])
    elif submodel_elements and isinstance(
        submodel_elements[0], model.Reference | model.SubmodelElementCollection
    ):
        value_type_list_element = None
        type_value_list_element = type(submodel_elements[0])
    else:
        value_type_list_element = convert_primitive_type_to_xsdtype(str)
        type_value_list_element = model.Property
    if isinstance(value, set):
        ordered = False
        iterable_type = "set"
    elif isinstance(value, tuple):
        ordered = True
        iterable_type = "tuple"
    elif isinstance(value, list):
        ordered = True
        iterable_type = "list"
    else:
        raise ValueError(
            f"Value must be a list, tuple or set, provided type {type(value)}"
        )

    sml = model.SubmodelElementList(
        id_short=f"{iterable_type}_{uuid.uuid4().hex}",
        type_value_list_element=type_value_list_element,
        value_type_list_element=value_type_list_element,
        value=submodel_elements,
        order_relevant=ordered,
    )
    return sml


def create_file(attribute_value: aas_model.File) -> model.File:
    """
    Function generates a basyx file objects from a pydantic File.

    Args:
        attribute_value (aas_model.File): pydantic File instance.

    Returns:
        model.File: Basyx file.
    """
    return model.File(
        id_short=attribute_value.id_short,
        description=attribute_value.description,
        semantic_id=attribute_value.semantic_id,
        content_type=attribute_value.media_type,
        value=attribute_value.path,
    )


def create_blob(attribute_value: aas_model.Blob) -> model.Blob:
    """
    Function generates a basyx file objects from a pydantic File.

    Args:
        attribute_value (aas_model.File): pydantic File instance.

    Returns:
        model.File: Basyx file.
    """
    return model.Blob(
        id_short=attribute_value.id_short,
        description=attribute_value.description,
        semantic_id=attribute_value.semantic_id,
        content_type=attribute_value.media_type,
        value=attribute_value.content,
    )


# ── Helpers ─────────────────────────────────────────────────────────────

def _make_external_reference(uri: str) -> model.ExternalReference:
    return model.ExternalReference(
        key=(model.Key(type_=model.KeyTypes.GLOBAL_REFERENCE, value=uri),)
    )


def _make_qualifiers(qds: list) -> list:
    result = []
    for qd in qds:
        # Handle both Qualifier model instances and raw dicts (from json_schema_extra)
        if hasattr(qd, 'type_'):
            # Qualifier model instance
            kwargs = {
                "type_": qd.type_,
                "value_type": model.datatypes.String,
                "value": qd.value,
                "kind": model.QualifierKind.TEMPLATE_QUALIFIER,
            }
            if qd.semantic_id:
                kwargs["semantic_id"] = _make_external_reference(qd.semantic_id)
        else:
            # Raw dict from json_schema_extra
            kwargs = {
                "type_": qd["type"],
                "value_type": model.datatypes.String,
                "value": qd["value"],
                "kind": model.QualifierKind.TEMPLATE_QUALIFIER,
            }
            if "semantic_id" in qd and qd["semantic_id"]:
                kwargs["semantic_id"] = _make_external_reference(qd["semantic_id"])
        result.append(model.Qualifier(**kwargs))
    return result


def create_operation(
    attribute_name: str,
    op: aas_model.Operation,
    sid=None, quals=None, suppl=None, desc=None,
) -> model.Operation:
    """Create a basyx Operation from an aas_pydantic Operation model."""
    input_vars = [
        create_submodel_element(f"input_{i}", v)
        for i, v in enumerate(op.input_variables)
    ]
    output_vars = [
        create_submodel_element(f"output_{i}", v)
        for i, v in enumerate(op.output_variables)
    ]
    inoutput_vars = [
        create_submodel_element(f"inoutput_{i}", v)
        for i, v in enumerate(op.inoutput_variables)
    ]
    return model.Operation(
        id_short=attribute_name,
        input_variable=input_vars,
        output_variable=output_vars,
        inoutput_variable=inoutput_vars,
        semantic_id=sid or get_semantic_id(op),
        qualifier=quals or [],
        supplemental_semantic_id=suppl or [],
        description=desc,
    )
