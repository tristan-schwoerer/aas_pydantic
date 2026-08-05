import copy
from typing import Any, Dict, Optional

from aas_pydantic.aas_model import (
    AAS,
    Submodel,
)
from aas_pydantic import (
    convert_aas_instance,
    convert_aas_template,
    convert_pydantic_model,
    convert_pydantic_type,
)
from aas_pydantic.util import compare_schemas


def _normalize_sml_items(d: Any) -> Any:
    """Normalize SubmodelElementList item id_shorts.

    AASd-120 forbids items of a SubmodelElementList from carrying an id_short,
    so basyx generates throwaway placeholders that never round-trip.  For the
    round-trip comparison we collapse every element under a ``value`` list to
    a stable marker, comparing by value instead of id_short.
    """
    if isinstance(d, dict):
        out = {}
        for k, v in d.items():
            if k == "value" and isinstance(v, list) and v and isinstance(v[0], dict):
                out[k] = [
                    {**item, "id_short": "<sml_item>"}
                    if isinstance(item, dict)
                    else item
                    for item in v
                ]
            else:
                out[k] = _normalize_sml_items(v)
        return out
    if isinstance(d, list):
        return [_normalize_sml_items(v) for v in d]
    return d


def test_convert_simple_submodel(example_submodel: Submodel):
    basyx_aas_submodel = convert_pydantic_model.convert_model_to_submodel(
        example_submodel
    )
    pydantic_model = convert_aas_instance.convert_submodel_to_model_instance(
        basyx_aas_submodel, model_type=type(example_submodel)
    )
    assert _normalize_sml_items(pydantic_model.model_dump()) == _normalize_sml_items(
        example_submodel.model_dump()
    )


def test_convert_simple_submodel_template():
    basyx_aas_submodel_template = (
        convert_pydantic_type.convert_model_to_submodel_template(Submodel)
    )
    submodel_infered_type = (
        convert_aas_template.convert_submodel_template_to_pydatic_type(
            basyx_aas_submodel_template
        )
    )
    assert compare_schemas(
        Submodel.model_json_schema(), submodel_infered_type.model_json_schema()
    )


def test_convert_simple_submodel_with_template_extraction(example_submodel: Submodel):
    basyx_aas_submodel = convert_pydantic_model.convert_model_to_submodel(
        example_submodel
    )
    basyx_aas_submodel_template = (
        convert_pydantic_type.convert_model_instance_to_submodel_template(
            example_submodel
        )
    )

    submodel_infered_type = (
        convert_aas_template.convert_submodel_template_to_pydatic_type(
            basyx_aas_submodel_template
        )
    )

    pydantic_model = convert_aas_instance.convert_submodel_to_model_instance(
        basyx_aas_submodel, model_type=submodel_infered_type
    )
    # The dynamically inferred type must round-trip the same element values.
    assert _normalize_sml_items(pydantic_model.model_dump()) == _normalize_sml_items(
        example_submodel.model_dump()
    )


def test_convert_simple_aas(example_aas: AAS):
    object_store = convert_pydantic_type.convert_model_to_aas_template(
        type(example_aas)
    )
    pydantic_type = convert_aas_template.convert_object_store_to_pydantic_types(
        object_store
    )
    assert len(pydantic_type) == 1
    assert compare_schemas(
        example_aas.model_json_schema(), pydantic_type[0].model_json_schema()
    )

    object_store_instance = convert_pydantic_model.convert_model_to_aas(example_aas)
    pydantic_instance = convert_aas_instance.convert_object_store_to_pydantic_models(
        object_store_instance, types=pydantic_type
    )
    assert len(pydantic_instance) == 1
    assert _normalize_sml_items(pydantic_instance[0].model_dump()) == _normalize_sml_items(
        example_aas.model_dump()
    )


def test_display_name_round_trip(example_submodel: Submodel):
    """display_name (basyx Referable) must survive pydantic→basyx→pydantic.

    Critical for SubmodelElementList items, which carry no id_short (AASd-120)
    and are identified visually via display_name.
    """
    basyx_submodel = convert_pydantic_model.convert_model_to_submodel(
        example_submodel
    )
    pydantic_model = convert_aas_instance.convert_submodel_to_model_instance(
        basyx_submodel, model_type=type(example_submodel)
    )

    # SML itself keeps its display_name
    assert pydantic_model.list_attribute.display_name == {"en": "The list"}

    # SML items keep their display_name (coerced into typed element instances)
    items = pydantic_model.list_attribute.value
    first = items[0]
    first_dn = first["display_name"] if isinstance(first, dict) else first.display_name
    assert first_dn == {"en": "First item"}
    second = items[1]
    second_dn = second["display_name"] if isinstance(second, dict) else second.display_name
    assert second_dn == {"en": "Second item"}

