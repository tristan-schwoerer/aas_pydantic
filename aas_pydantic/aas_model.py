from __future__ import annotations

from types import NoneType
from typing import Annotated, Any, List, Optional, TypeVar, Union, Literal
import typing

from basyx.aas.model import AssetAdministrationShell, DictObjectStore, Submodel
from pydantic import (
    AfterValidator,
    BaseModel,
    Field,
    ValidationError,
    model_validator,
)


BasyxModels = AssetAdministrationShell | Submodel | DictObjectStore


def string_does_start_with_a_character(v: str):
    assert v, "value must not be an empty string"
    assert v[0].isalpha(), "value must start with a character"
    return v


AasIdString = Annotated[str, AfterValidator(string_does_start_with_a_character)]
Reference = TypeVar(
    "Reference",
    bound=Annotated[str, AfterValidator(string_does_start_with_a_character)],
)


class Referable(BaseModel):
    id_short: AasIdString
    description: str = ""


class Identifiable(Referable):
    id: AasIdString

    @model_validator(mode="before")
    @classmethod
    def check_id_and_id_short(cls, data: Any) -> Any:
        if isinstance(data, BaseModel):
            data = data.model_dump()
        elif not isinstance(data, dict):
            data = {
                "id": getattr(data, "id", ""),
                "id_short": getattr(data, "id_short", ""),
            }
        assert "id" in data or "id_short" in data, "Either id or id_short must be set"
        if "id_short" not in data:
            data["id_short"] = data["id"]
        if "id" not in data:
            data["id"] = data["id_short"]
        return data


class Qualifier(BaseModel):
    """AAS Qualifier — named constraint with optional semantic reference."""
    model_config = {"populate_by_name": True}
    type_: str = Field(alias="type")
    value: str
    value_type: str = "xs:string"
    semantic_id: str = ""
    kind: str = "TemplateQualifier"

class Cardinality(Qualifier):
    type_: str = "SMT/Cardinality"
    value: Literal["ZeroToOne", "ZeroToMany", "One", "OneToMany"] = "One"
    semantic_id: str = "https://admin-shell.io/SubmodelTemplates/Cardinality/1/0"


class HasSemantics(BaseModel):
    semantic_id: str = ""
    supplemental_semantic_ids: List[str] = []
    qualifiers: List[Qualifier] = []


class AAS(Identifiable):
    # AAS-level metadata (not submodels — excluded from check_submodels)
    asset_type: str = ""
    derived_from: str = ""
    specific_asset_ids: dict[str, str] = {}

    @model_validator(mode="before")
    @classmethod
    def set_optional_fields_to_None(cls, data):
        if isinstance(data, BaseModel):
            data = data.model_dump()
        for field_name, field_info in cls.model_fields.items():
            if field_name in data:
                continue
            if typing.get_origin(field_info.annotation) == Union and type(
                None
            ) in typing.get_args(field_info.annotation):
                data[field_name] = None
        return data

    @model_validator(mode="after")
    def check_submodels(self) -> Any:
        _meta = {"id", "id_short", "description", "asset_type", "derived_from", "specific_asset_ids"}
        for field_name, field_info in self.model_fields.items():
            if field_name in _meta:
                continue
            elif (
                typing.get_origin(field_info.annotation) == Union
                and type(None) in typing.get_args(field_info.annotation)
                and getattr(self, field_name) is None
            ):
                continue
            try:
                Submodel.model_validate(getattr(self, field_name))
            except ValidationError:
                assert False, f"Field '{field_name}' must be of type Submodel"
        return self


def is_valid_submodel_element(submodel_element: Any) -> bool:
    if isinstance(submodel_element, NoneType):
        return True
    if isinstance(submodel_element, SubmodelElement):
        return True
    elif isinstance(submodel_element, (list, tuple, set)):
        return all(is_valid_submodel_element(e) for e in submodel_element)
    elif isinstance(submodel_element, dict):
        return all(is_valid_submodel_element(v) for v in submodel_element.values())
    try:
        SubmodelElement.model_validate(submodel_element)
        return True
    except Exception:
        return False


class SubmodelElement(HasSemantics, Referable):
    """Abstract base for all AAS SubmodelElements.

    Every SubmodelElement carries an id_short (from Referable) and
    optional semantic_id / qualifiers (from HasSemantics).  Concrete
    types — Property, Range, SMC, SML, Entity, etc. — inherit from here.
    """
    pass


class SubmodelElementCollection(SubmodelElement):
    @model_validator(mode="after")
    def check_submodel_elements(self) -> Any:
        for field_name in self.model_fields:
            if field_name in ["id_short", "description",
                              "semantic_id", "qualifiers",
                              "supplemental_semantic_ids"]:
                continue
            assert is_valid_submodel_element(getattr(self, field_name)), \
                f"Field {field_name} is not a valid SubmodelElement"
        return self


class SubmodelElementList(SubmodelElement):
    """Pydantic model for an AAS SubmodelElementList.

    Wraps an ordered list of submodel elements with list-level AAS metadata
    (semantic_id, description, qualifiers).  The ``value`` field holds the
    actual list items.
    """
    value: List[Any] = []

    @model_validator(mode="after")
    def check_submodel_elements(self) -> Any:
        for field_name in self.model_fields:
            if field_name in ["id_short", "description",
                              "semantic_id", "qualifiers",
                              "supplemental_semantic_ids"]:
                continue
            assert is_valid_submodel_element(getattr(self, field_name)), \
                f"Field {field_name} is not a valid SubmodelElement"
        return self


class Entity(SubmodelElement):
    """Pydantic model for an AAS Entity.

    An Entity is a SubmodelElement that represents a structured collection
    of statements.  It carries an ``entity_type`` (SelfManagedEntity or
    CoManagedEntity) and its child elements as model fields (like an SMC).
    """
    entity_type: str = ""

    @model_validator(mode="after")
    def check_submodel_elements(self) -> Any:
        for field_name in self.model_fields:
            if field_name in ["id_short", "description",
                              "semantic_id", "qualifiers",
                              "supplemental_semantic_ids", "entity_type"]:
                continue
            assert is_valid_submodel_element(getattr(self, field_name)), \
                f"Field {field_name} is not a valid SubmodelElement"
        return self


class Operation(SubmodelElement):
    id_short: AasIdString = "Operation"
    input_variables: List[SubmodelElement] = []
    output_variables: List[SubmodelElement] = []
    inoutput_variables: List[SubmodelElement] = []


class Capability(SubmodelElement):
    id_short: AasIdString = "Capability"


class Property(SubmodelElement):
    id_short: AasIdString = "Property"
    value: str = ""
    value_type: str = "xs:string"


class MultiLanguageProperty(SubmodelElement):
    id_short: AasIdString = "MultiLanguageProperty"
    language: str = "en"
    value: str = ""


class Range(SubmodelElement):
    id_short: AasIdString = "Range"
    min_: str | int | float = ""
    max_: str | int | float = ""
    value_type: str = "xs:string"


class ReferenceElement(SubmodelElement):
    id_short: AasIdString = "ReferenceElement"
    value: str = ""


class RelationshipElement(SubmodelElement):
    id_short: AasIdString = "RelationshipElement"
    first: str = ""
    second: str = ""


class File(SubmodelElement):
    id_short: AasIdString = "File"
    media_type: str = ""
    path: str = ""


class Blob(SubmodelElement):
    id_short: AasIdString = "Blob"
    media_type: str = ""
    content: Optional[bytes] = None


PrimitiveSubmodelElement = int | float | str | bool | bytes


class Submodel(HasSemantics, Identifiable):
    @model_validator(mode="after")
    def check_submodel_elements(self) -> Any:
        for field_name in self.model_fields:
            if field_name in ["id", "id_short", "description",
                              "semantic_id", "qualifiers",
                              "supplemental_semantic_ids"]:
                continue
            assert is_valid_submodel_element(getattr(self, field_name)), \
                f"Field {field_name} is not a valid SubmodelElement"
        return self
