"""Rich-style test fixtures.

Every field on an SMC/Submodel/AAS is a typed AAS element (Property, Range,
ReferenceElement, ...) — no bare primitives, matching the basyx model and the
"rich-only" design of this fork.  Each element default carries an explicit
id_short equal to its field name so round-trips are exact.
"""

from __future__ import annotations
from enum import Enum
from typing import Type

import pytest

from aas_pydantic.aas_model import (
    AAS,
    Blob,
    Capability,
    ExternalReference,
    File,
    Key,
    ModelReference,
    MultiLanguageProperty,
    Property,
    Range,
    ReferenceElement,
    RelationshipElement,
    Submodel,
    SubmodelElementCollection,
    SubmodelElementList,
)


class ExampleEnum(str, Enum):
    value1 = "value1"
    value2 = "value2"


class SimpleExampleSEC(SubmodelElementCollection):
    integer_attribute: Property = Property(
        id_short="integer_attribute", value="1", value_type="xs:int"
    )
    string_attribute: Property = Property(
        id_short="string_attribute", value="string"
    )
    literal_attribute: Property = Property(
        id_short="literal_attribute", value="value1"
    )


class ExampleSEC(SubmodelElementCollection):
    integer_attribute: Property = Property(
        id_short="integer_attribute", value="1", value_type="xs:int"
    )
    string_attribute: Property = Property(
        id_short="string_attribute", value="string"
    )
    nested_collection: SimpleExampleSEC = SimpleExampleSEC(id_short="nested_collection")
    reference_attribute: ReferenceElement = ReferenceElement(
        id_short="reference_attribute",
        value=ModelReference(
            key=(Key(type_="AssetAdministrationShell", value="aas_1"),)
        ),
    )


class ExampleSubmodel(Submodel):
    property_attribute: Property = Property(
        id_short="property_attribute", value="value"
    )
    multi_language_attribute: MultiLanguageProperty = MultiLanguageProperty(
        id_short="multi_language_attribute", value={"en": "hello"}
    )
    range_attribute: Range = Range(
        id_short="range_attribute", min=1, max=10, value_type="xs:int"
    )
    reference_attribute: ReferenceElement = ReferenceElement(
        id_short="reference_attribute",
        value=ExternalReference(
            key=(Key(type_="GlobalReference", value="https://example.com/x"),)
        ),
    )
    relationship_attribute: RelationshipElement = RelationshipElement(
        id_short="relationship_attribute",
        first=ExternalReference(
            key=(Key(type_="GlobalReference", value="https://example.com/a"),)
        ),
        second=ExternalReference(
            key=(Key(type_="GlobalReference", value="https://example.com/b"),)
        ),
    )
    capability_attribute: Capability = Capability(id_short="capability_attribute")
    file_attribute: File = File(
        id_short="file_attribute", content_type="text/plain", value="x.txt"
    )
    blob_attribute: Blob = Blob(
        id_short="blob_attribute",
        content_type="application/octet-stream",
        value=b"123",
    )
    submodel_element_collection_attribute: ExampleSEC = ExampleSEC(
        id_short="submodel_element_collection_attribute"
    )
    list_attribute: SubmodelElementList = SubmodelElementList(
        id_short="list_attribute",
        type_value_list_element="Property",
        display_name={"en": "The list"},
        value=[
            Property(id_short="i1", value="a", display_name={"en": "First item"}),
            Property(id_short="i2", value="b", display_name={"en": "Second item"}),
        ],
    )


class ExampleSubmodel2(Submodel):
    property_attribute: Property = Property(
        id_short="property_attribute", value="value2"
    )
    string_attribute: Property = Property(
        id_short="string_attribute", value="other"
    )


class ValidAAS(AAS):
    example_submodel: ExampleSubmodel
    example_submodel_2: ExampleSubmodel2


class FaultyAas(AAS):
    example_string_value: str


@pytest.fixture(scope="function")
def faulty_aas() -> Type[FaultyAas]:
    return FaultyAas


@pytest.fixture(scope="function")
def simple_submodel_element_collection() -> SimpleExampleSEC:
    return SimpleExampleSEC(id_short="simple_submodel_element_collection_id")


@pytest.fixture(scope="function")
def example_submodel_element_collection() -> ExampleSEC:
    return ExampleSEC(id_short="example_submodel_element_collection_id")


@pytest.fixture(scope="function")
def example_submodel() -> ExampleSubmodel:
    return ExampleSubmodel(
        id_short="example_submodel_id",
        description="Example Submodel",
    )


@pytest.fixture(scope="function")
def example_submodel_2() -> ExampleSubmodel2:
    return ExampleSubmodel2(id_short="example_submodel_2_id")


@pytest.fixture(scope="function")
def example_aas() -> ValidAAS:
    return ValidAAS(
        id_short="example_aas_id",
        example_submodel=ExampleSubmodel(
            id_short="example_submodel_id", description="Example Submodel"
        ),
        example_submodel_2=ExampleSubmodel2(id_short="example_submodel_2_id"),
    )


@pytest.fixture(scope="function")
def example_basemodel_with_identifier_attribute() -> (
    BaseModelWithIdentifierAttribute
):
    return BaseModelWithIdentifierAttribute(
        other_name_id_attribute="example_basemodel_with_identifier_attribute_id",
        id="id_named_attribute",
    )


@pytest.fixture(scope="function")
def example_object_with_identifier_attribute() -> ObjectWithIdentifierAttribute:
    return ObjectWithIdentifierAttribute(
        other_name_id_attribute="example_object_with_identifier_attribute_id",
        id="id_named_attribute",
    )
