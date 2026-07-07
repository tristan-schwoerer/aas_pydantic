from __future__ import annotations

from types import NoneType
from typing import Annotated, Any, List, Optional, TypeVar, Union
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


class HasSemantics(BaseModel):
    semantic_id: str = ""
    supplemental_semantic_ids: List[str] = []
    qualifiers: List[Qualifier] = []


class AAS(Identifiable):
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
        for field_name, field_info in self.model_fields.items():
            if field_name in ["id", "id_short", "description"]:
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
                assert False, f"All attributes of an AAS must be of type Submodel"
        return self


def is_valid_submodel_element(submodel_element: Any) -> bool:
    if isinstance(submodel_element, NoneType):
        return True
    if isinstance(submodel_element, PrimitiveSubmodelElement):
        return True
    elif isinstance(submodel_element, SubmodelElementCollection):
        return True
    elif isinstance(submodel_element, (list, tuple, set)):
        return all(is_valid_submodel_element(e) for e in submodel_element)
    elif isinstance(submodel_element, (Operation, Capability, Property,
            MultiLanguageProperty, Range, ReferenceElement,
            RelationshipElement, File, Blob)):
        return True
    try:
        SubmodelElementCollection.model_validate(submodel_element)
        return True
    except Exception:
        return False


class SubmodelElementCollection(HasSemantics, Referable):
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


class Operation(HasSemantics, Referable):
    id_short: AasIdString = "Operation"
    input_variables: List[SubmodelElement] = []
    output_variables: List[SubmodelElement] = []
    inoutput_variables: List[SubmodelElement] = []


class Capability(HasSemantics, Referable):
    id_short: AasIdString = "Capability"


class Property(HasSemantics, Referable):
    id_short: AasIdString = "Property"
    value: str = ""
    value_type: str = "xs:string"

    @model_validator(mode="before")
    @classmethod
    def _coerce_str(cls, data):
        if isinstance(data, str):
            return {"value": data}
        return data


class MultiLanguageProperty(HasSemantics, Referable):
    id_short: AasIdString = "MultiLanguageProperty"
    value: str = ""

    @model_validator(mode="before")
    @classmethod
    def _coerce_str(cls, data):
        if isinstance(data, str):
            return {"value": data}
        return data


class Range(HasSemantics, Referable):
    id_short: AasIdString = "Range"
    min_: str = ""
    max_: str = ""
    value_type: str = "xs:string"


class ReferenceElement(HasSemantics, Referable):
    id_short: AasIdString = "ReferenceElement"
    value: str = ""

    @model_validator(mode="before")
    @classmethod
    def _coerce_str(cls, data):
        if isinstance(data, str):
            return {"value": data}
        return data


class RelationshipElement(HasSemantics, Referable):
    id_short: AasIdString = "RelationshipElement"
    first: str = ""
    second: str = ""


class File(HasSemantics, Referable):
    id_short: AasIdString = "File"
    media_type: str = ""
    path: str = ""


class Blob(HasSemantics, Referable):
    id_short: AasIdString = "Blob"
    media_type: str = ""
    content: Optional[bytes] = None


PrimitiveSubmodelElement = int | float | str | bool | bytes
SubmodelElement = (
    PrimitiveSubmodelElement
    | SubmodelElementCollection
    | List["SubmodelElement"]
    | Operation | Capability
    | Property | MultiLanguageProperty | Range
    | ReferenceElement | RelationshipElement
    | Blob | File
)


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
