from __future__ import annotations

import copy
import itertools
import re
from types import UnionType as _UnionType
from typing import Annotated, Any, Dict, List, Optional, TypeVar, Union, Literal
import typing

from basyx.aas.model import (
    AssetAdministrationShell,
    DictIdentifiableStore,
    Submodel,
)
from pydantic import (
    AfterValidator,
    BaseModel,
    Field,
    ValidationError,
    field_serializer,
    model_validator,
)


BasyxModels = AssetAdministrationShell | Submodel | DictIdentifiableStore


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
    # Strict basyx alignment: unknown fields (e.g. the old alias names) are
    # rejected instead of silently ignored.
    model_config = {"extra": "forbid"}

    id_short: AasIdString
    description: str = ""
    # basyx Referable.display_name — lang→text map (e.g. for SML items that
    # carry no id_short, so they can still be identified visually).
    display_name: Optional[Dict[str, str]] = None


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
    """AAS Qualifier — named constraint with optional semantic reference.

    Field names follow basyx strictly: ``type_``, ``value``, ``value_type``,
    ``value_id``, ``kind``, ``semantic_id``.  Unknown fields (e.g. the old
    ``type`` alias) are rejected.
    """
    model_config = {"extra": "forbid"}

    type_: str = ""
    value: str = ""
    value_type: str = "xs:string"
    value_id: str = ""
    semantic_id: str = ""
    kind: str = "TemplateQualifier"

class Cardinality(Qualifier):
    type_: str = "SMT/Cardinality"
    value: Literal["ZeroToOne", "ZeroToMany", "One", "OneToMany"] = "ZeroToMany"
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
        _meta = {"id", "id_short", "description", "display_name", "asset_type", "derived_from", "specific_asset_ids"}
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
    """Rich-only element check.

    Accepts only ``SubmodelElement`` instances, lists/containers of them, or
    dicts that either (a) are ``Dict[str, SubmodelElement]`` containers, or
    (b) serialize to one of the concrete element classes.  Bare primitives are
    rejected.  Validation runs against the concrete element classes (not the
    abstract ``SubmodelElement`` base) because every element type declares
    extra fields that the base model forbids.
    """
    if submodel_element is None:
        return True
    if isinstance(submodel_element, SubmodelElement):
        return True
    elif isinstance(submodel_element, (list, tuple, set)):
        return all(is_valid_submodel_element(e) for e in submodel_element)
    elif isinstance(submodel_element, dict):
        if "id_short" not in submodel_element:
            # Dict[str, SubmodelElement] container
            return all(
                is_valid_submodel_element(v) for v in submodel_element.values()
            )
        # Serialized element — validate against the concrete element classes.
        for cls in _CONCRETE_ELEMENT_TYPES:
            try:
                cls.model_validate(submodel_element)
                return True
            except Exception:
                continue
        # Fallback: an SMC-shaped dict whose concrete subclass is not known
        # here — every non-meta value must itself be a valid element.
        return all(
            is_valid_submodel_element(v)
            for k, v in submodel_element.items()
            if k not in _ELEMENT_META_KEYS
        )
    return False


def _stamp_container_id_shorts(model: Any) -> None:
    """Enforce ``key == id_short`` for every dict-container child.

    The dict key is the single source of truth for a child's id_short, so
    source never repeats ``id_short=<key>`` on the instances.  This stamps
    each child's id_short from its key on every constructed model
    (defaults included).  Children are copied, never mutated."""
    for container_key in ("value", "submodel_element", "statements"):
        container = getattr(model, container_key, None)
        if not isinstance(container, dict):
            continue
        for k, v in list(container.items()):
            if isinstance(v, SubmodelElement) and v.id_short != k:
                container[k] = v.model_copy(update={"id_short": k})


# Every concrete element class registers itself here (via
# ``SubmodelElement.__init_subclass__``) so dumps can carry a ``modelType``
# discriminator and revalidation resolves the concrete type directly instead
# of relying on fragile key inference.
_ELEMENT_CLASS_REGISTRY: dict = {}

# semanticId value → list of concrete element classes carrying it.  Populated
# alongside the class registry.  Resolution only uses a semanticId when it is
# UNIQUE — shared semanticIds (e.g. handwritten MQTT deltas vs their generated
# bases, or an SML vs its items) are ambiguous and fall back to generic types.
_SEMANTIC_ID_REGISTRY: dict = {}


def _resolve_semantic_id_cls(sid: str):
    """Concrete class uniquely identified by *sid*, or ``None`` when the
    semanticId is shared by several classes (ambiguous → generic fallback)."""
    classes = _SEMANTIC_ID_REGISTRY.get(sid)
    if classes and len(classes) == 1:
        return classes[0]
    return None


def _dump_container(container: Any, concept_sid: str = "") -> Any:
    """Serialize a container losslessly — each child is dumped with its own
    concrete model and tagged with ``modelType`` (its class name).

    Handles values models (``ContainerValue``: each field is a child),
    ``Dict[str, SubmodelElement]`` containers, and lists (SML/Operation).
    pydantic's ``Dict[str, SubmodelElement]`` serializer uses the abstract
    ``SubmodelElement`` schema and drops subclass fields, hence the explicit
    per-child dump here."""
    if isinstance(container, BaseModel):
        # values model — field name → tagged child (nested Dict/List fields,
        # e.g. multi-cardinality ``Dict[str, X]`` children, recurse losslessly)
        out = {}
        for f in container.model_fields:
            v = getattr(container, f)
            if isinstance(v, BaseModel):
                out[f] = _tag_dump(v)
            elif isinstance(v, dict):
                # Dict-map child: stamp the field's concept semanticId on any
                # entry lacking one (e.g. a bare ``Property`` in ``Dict[str,
                # Mode]``) so back-conversion can regroup it by sid.
                out[f] = _dump_container(v, concept_sid=_field_concept_sid(container, f))
            elif isinstance(v, (list, tuple)):
                out[f] = _dump_container(v)
            else:
                out[f] = v
        extra = getattr(container, "__pydantic_extra__", None) or {}
        for k, v in extra.items():
            if isinstance(v, BaseModel):
                out[k] = _tag_dump(v)
            elif isinstance(v, (dict, list, tuple)):
                out[k] = _dump_container(v)
            else:
                out[k] = v
        return out
    if isinstance(container, dict):
        return {
            k: _tag_dump(v, concept_sid) if isinstance(v, BaseModel) else v
            for k, v in container.items()
        }
    if isinstance(container, (list, tuple)):
        return [_tag_dump(v) if isinstance(v, BaseModel) else v for v in container]
    return container


def _field_concept_sid(container: BaseModel, field_name: str) -> str:
    """semanticId of the element class of a ``Dict[str, E]`` field (the concept
    semanticId of the multi-cardinality map), or ``""``."""
    try:
        ann = typing.get_type_hints(type(container), include_extras=True).get(field_name)
    except Exception:
        ann = None
    args = typing.get_args(ann) if ann is not None else ()
    if len(args) == 2 and args[0] is str:
        inner = args[1]
        if isinstance(inner, type) and issubclass(inner, SubmodelElement):
            return _element_cls_semantic_id(inner)
    return ""


def _element_cls_semantic_id(cls) -> str:
    """semanticId carried by an element class (``semantic_id`` is a pydantic
    field, so read its default — the class attribute is a raising descriptor
    in pydantic v2.11+)."""
    try:
        f = cls.model_fields.get("semantic_id")
        if f is not None and isinstance(f.default, str):
            return f.default
    except Exception:
        pass
    return ""


def _tag_dump(model: BaseModel, concept_sid: str = "") -> dict:
    """Dump *model* with a ``modelType`` discriminator so revalidation can
    resolve its concrete class.  A *concept_sid* (the containing Dict-map
    field's concept semanticId) is stamped on the dump when the element has
    none — so bare user entries (e.g. ``Property`` in ``Dict[str, Mode]``)
    round-trip back into the right map field."""
    d = {**model.model_dump(), "modelType": type(model).__name__}
    if concept_sid and not d.get("semantic_id"):
        d["semantic_id"] = concept_sid
    return d


class ContainerValue(BaseModel):
    """Base for per-container values models: every field is a child
    SubmodelElement, and the FIELD NAME IS the child's id_short (stamped on
    validation).  This is what makes inheritance clean — subclass the values
    class to add/override children instead of merging string-keyed dicts.

    Raw dicts (config / AAS JSON / pydantic dumps) are coerced to concrete
    element types by ``coerce_submodel_element`` (registry-driven), with the
    field's declared type enforced for typed fields.

    The base is open (``extra="allow"``) so generic/dynamic containers can
    hold arbitrary children; typed values classes may set
    ``model_config = {"extra": "forbid"}`` to catch typos.
    """
    model_config = {"extra": "allow"}

    @model_validator(mode="before")
    @classmethod
    def coerce_values(cls, data):
        if isinstance(data, BaseModel):
            return data
        if not isinstance(data, dict):
            return data
        out = {}
        for k, v in data.items():
            field = cls.model_fields.get(k)
            target = _resolve_annotation(field.annotation) if field else None
            if isinstance(v, dict) and "modelType" in v:
                # dump child carries its own type discriminator — the registry
                # resolves the concrete class (e.g. ExtendedSkills overriding a
                # generated Skills field); never force the declared type.
                target = None
            origin = typing.get_origin(target)
            if origin is dict and isinstance(v, dict):
                # nested Dict[str, X] container field (e.g. Term.terms) —
                # coerce each child, targeted at X.
                args = typing.get_args(target)
                item_tp = args[1] if len(args) == 2 else None
                out[k] = {
                    ik: coerce_submodel_element(iv, id_short=ik, target_type=item_tp)
                    for ik, iv in v.items()
                }
            elif origin in (list, tuple, set) and isinstance(v, (list, tuple, set, dict)):
                args = typing.get_args(target)
                item_tp = args[0] if args else None
                # back-conversion may pass a name-keyed dict for a list field
                # (flattened in basyx) — use its values as the list items.
                seq = v.values() if isinstance(v, dict) else v
                out[k] = [
                    coerce_submodel_element(iv, target_type=item_tp) for iv in seq
                ]
            else:
                out[k] = coerce_submodel_element(v, id_short=k, target_type=target)
        return out

    @model_validator(mode="after")
    def check_value_elements(self) -> Any:
        names = list(self.model_fields)
        names += list((getattr(self, "__pydantic_extra__", None) or {}).keys())
        for field_name in names:
            el = getattr(self, field_name, None)
            if el is None:
                continue
            assert is_valid_submodel_element(el), \
                f"Field {field_name} is not a valid SubmodelElement"
            if isinstance(el, SubmodelElement) and el.id_short != field_name:
                # field name == id_short (single canonical name per element)
                setattr(self, field_name, el.model_copy(update={"id_short": field_name}))
        return self


class SubmodelElement(HasSemantics, Referable):
    """Abstract base for all AAS SubmodelElements.

    Every SubmodelElement carries an id_short (from Referable) and
    optional semantic_id / qualifiers (from HasSemantics).  Concrete
    types — Property, Range, SMC, SML, Entity, etc. — inherit from here.
    """

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        _ELEMENT_CLASS_REGISTRY[cls.__name__] = cls
        # semanticId is read robustly: a value defined in this class's own
        # body wins (``__dict__`` — still a plain attribute at this point);
        # otherwise the inherited field default from ``model_fields`` is used.
        # (``getattr`` alone fails here: pydantic v2.11+ replaces plain class
        # attributes with raising descriptors once the parent is finalized, so
        # inherited semanticIds would silently never register.)
        _sid = cls.__dict__.get("semantic_id")
        if not isinstance(_sid, str):
            _sid = ""
        if not _sid:
            _field = cls.model_fields.get("semantic_id")
            if _field is not None and isinstance(_field.default, str):
                _sid = _field.default
        if _sid:
            _SEMANTIC_ID_REGISTRY.setdefault(_sid, []).append(cls)


class SubmodelElementCollection(SubmodelElement):
    """An SMC holding named child elements in ``value``.

    Mirrors basyx ``SubmodelElementCollection.value`` (a NamespaceSet keyed by
    id_short) and the IDTA JSON ``value`` container.  Subclasses specialise the
    value as a values model::

        class MySMCValues(ContainerValue):
            x: Property = Property(...)

        class MySMC(SubmodelElementCollection):
            value: MySMCValues = MySMCValues()

    Dynamic name-keyed maps may instead keep ``value: Dict[str, X]``.
    """
    value: ContainerValue = ContainerValue()
    id_short: AasIdString = "SubmodelElementCollection"

    @field_serializer("value")
    def _ser_value_lossless(self, v, _info):
        return _dump_container(v)

    @model_validator(mode="before")
    @classmethod
    def coerce_containers(cls, data):
        return _coerce_container_data(cls, data)

    @model_validator(mode="after")
    def check_submodel_elements(self) -> Any:
        _stamp_container_id_shorts(self)
        for field_name in self.model_fields:
            if field_name in ["id_short", "description", "display_name",
                              "semantic_id", "qualifiers",
                              "supplemental_semantic_ids"]:
                continue
            if field_name == "value":
                assert isinstance(getattr(self, field_name), (ContainerValue, dict)), \
                    f"Field {field_name} must be a ContainerValue or Dict"
                continue
            assert is_valid_submodel_element(getattr(self, field_name)), \
                f"Field {field_name} is not a valid SubmodelElement"
        return self


class SubmodelElementList(SubmodelElement):
    """Pydantic model for an AAS SubmodelElementList.

    Wraps an ordered list of submodel elements with list-level AAS metadata
    (semantic_id, description, qualifiers).  The ``value`` field holds the
    actual list items.  ``type_value_list_element``/``value_type_list_element``/
    ``semantic_id_list_element``/``order_relevant`` mirror the basyx
    SubmodelElementList attributes.
    """
    value: List[Any] = []
    id_short: AasIdString = "SubmodelElementList"
    type_value_list_element: Optional[str] = None
    value_type_list_element: Optional[str] = None
    semantic_id_list_element: str = ""
    order_relevant: bool = True

    @field_serializer("value")
    def _ser_value_lossless(self, v, _info):
        return _dump_container(v)

    @model_validator(mode="before")
    @classmethod
    def coerce_containers(cls, data):
        return _coerce_container_data(cls, data)

    @model_validator(mode="after")
    def check_submodel_elements(self) -> Any:
        for field_name in self.model_fields:
            if field_name in ["id_short", "description", "display_name",
                              "semantic_id", "qualifiers",
                              "supplemental_semantic_ids",
                              "type_value_list_element",
                              "value_type_list_element",
                              "semantic_id_list_element",
                              "order_relevant"]:
                continue
            assert is_valid_submodel_element(getattr(self, field_name)), \
                f"Field {field_name} is not a valid SubmodelElement"
        return self


class Entity(SubmodelElement):
    """Pydantic model for an AAS Entity.

    Mirrors basyx ``Entity``: an ``entity_type`` (SelfManagedEntity or
    CoManagedEntity), an optional ``global_asset_id`` (required for
    self-managed entities per AASd-014), and child elements in the
    ``statements`` container (a values model, like SMC ``value``).
    """
    entity_type: str = "CoManagedEntity"
    id_short: AasIdString = "Entity"
    global_asset_id: str = ""
    statements: ContainerValue = ContainerValue()

    @field_serializer("statements")
    def _ser_statements_lossless(self, v, _info):
        return _dump_container(v)

    @model_validator(mode="before")
    @classmethod
    def coerce_containers(cls, data):
        return _coerce_container_data(cls, data)

    @model_validator(mode="after")
    def check_submodel_elements(self) -> Any:
        _stamp_container_id_shorts(self)
        for field_name in self.model_fields:
            if field_name in ["id_short", "description", "display_name",
                              "semantic_id", "qualifiers",
                              "supplemental_semantic_ids", "entity_type",
                              "global_asset_id"]:
                continue
            if field_name == "statements":
                assert isinstance(getattr(self, field_name), (ContainerValue, dict)), \
                    f"Field {field_name} must be a ContainerValue or Dict"
                continue
            assert is_valid_submodel_element(getattr(self, field_name)), \
                f"Field {field_name} is not a valid SubmodelElement"
        return self


class Operation(SubmodelElement):
    id_short: AasIdString = "Operation"
    input_variable: List[SubmodelElement] = []
    output_variable: List[SubmodelElement] = []
    in_output_variable: List[SubmodelElement] = []

    @field_serializer("input_variable", "output_variable", "in_output_variable")
    def _ser_variables_lossless(self, v, _info):
        return _dump_container(v)


class Capability(SubmodelElement):
    id_short: AasIdString = "Capability"


class Property(SubmodelElement):
    id_short: AasIdString = "Property"
    value: str = ""
    value_type: str = "xs:string"
    value_id: str = ""


class MultiLanguageProperty(SubmodelElement):
    """A MultiLanguageProperty; ``value`` is a lang→text map (basyx LangStringSet)."""
    id_short: AasIdString = "MultiLanguageProperty"
    value: Optional[Dict[str, str]] = None
    value_id: str = ""


class Range(SubmodelElement):
    """A Range element matching basyx (``min``/``max``)."""
    id_short: AasIdString = "Range"
    min: str | int | float = ""
    max: str | int | float = ""
    value_type: str = "xs:string"


def _aas_json_reference_normalize(data: Any) -> Any:
    """Normalize AAS JSON reference field names (``type``/``keys``) onto the
    strict pydantic names (``type_``/``key``).  Used by ``Key`` and
    ``Reference`` so raw AAS JSON (e.g. RelationshipElement endpoints, AAS
    JSON dumps) coerces cleanly without adding backwards-compat aliases."""
    if isinstance(data, BaseModel):
        return data.model_dump()
    if isinstance(data, dict):
        data = dict(data)
        if "type" in data and "type_" not in data:
            data["type_"] = data.pop("type")
        if "keys" in data and "key" not in data:
            data["key"] = tuple(data.pop("keys"))
    return data


class Key(BaseModel):
    """A key of a Reference, referencing an element in its name space."""
    model_config = {"extra": "forbid"}

    type_: str = ""
    value: str = ""

    @model_validator(mode="before")
    @classmethod
    def normalize_aas_json(cls, data: Any) -> Any:
        return _aas_json_reference_normalize(data)


class Reference(BaseModel):
    """Abstract superclass of ExternalReference and ModelReference.

    Reference to either a model element of the same or another AAS or to an
    external entity.  A reference is an ordered list of keys, each key
    referencing an element.  The complete list of keys may for example be
    concatenated to a path that then gives unique access to an element or
    entity.

    **Constraint AASd-121:** For References the value of Key/type of the
    first key of Reference/keys shall be one of GloballyIdentifiables.
    """
    model_config = {"extra": "forbid"}

    type_: Literal["ModelReference", "ExternalReference"] = "ModelReference"
    key: tuple[Key, ...] = ()
    referred_semantic_id: str = ""

    @model_validator(mode="before")
    @classmethod
    def normalize_aas_json(cls, data: Any) -> Any:
        return _aas_json_reference_normalize(data)

    @model_validator(mode="after")
    def dispatch_concrete(self) -> Any:
        """Dispatch to the concrete subclass matching ``type_`` so AAS-JSON
        input (validated against the base) yields a real
        ModelReference/ExternalReference and ``isinstance`` checks hold."""
        if self.type_ == "ModelReference" and not isinstance(self, ModelReference):
            return ModelReference(**self.model_dump())
        if self.type_ == "ExternalReference" and not isinstance(self, ExternalReference):
            return ExternalReference(**self.model_dump())
        return self


class ModelReference(Reference):
    """A Reference to a model element of the same or another AAS."""
    type_: Literal["ModelReference"] = "ModelReference"


class ExternalReference(Reference):
    """A Reference to an external entity (outside the AAS)."""
    type_: Literal["ExternalReference"] = "ExternalReference"


class ReferenceElement(SubmodelElement):
    id_short: AasIdString = "ReferenceElement"
    value: Optional[Reference] = None


class RelationshipElement(SubmodelElement):
    """A RelationshipElement whose endpoints (``first``/``second``) are
    References — mirroring basyx, where both must point at Referable
    elements (subject and object of the relationship)."""
    id_short: AasIdString = "RelationshipElement"
    first: Optional[Reference] = None
    second: Optional[Reference] = None


class File(SubmodelElement):
    """A File element matching basyx (``content_type``/``value``)."""
    id_short: AasIdString = "File"
    content_type: str = ""
    value: str = ""


class Blob(SubmodelElement):
    """A Blob element; ``content_type``/``value`` (aliases ``media_type``/``content``) match basyx."""
    model_config = {"populate_by_name": True}

    id_short: AasIdString = "Blob"
    content_type: str = ""
    value: Optional[bytes] = None


# All concrete SubmodelElement types.  Used by ``is_valid_submodel_element``
# to validate serialized (dict) elements under ``extra="forbid"``.
_CONCRETE_ELEMENT_TYPES: tuple = (
    Property, MultiLanguageProperty, Range, ReferenceElement, RelationshipElement,
    SubmodelElementCollection, SubmodelElementList, File, Blob, Entity,
    Operation, Capability,
)

# Meta keys that are not themselves submodel elements.
_ELEMENT_META_KEYS: frozenset = frozenset({
    "id_short", "description", "display_name", "semantic_id",
    "supplemental_semantic_ids", "qualifiers", "entity_type",
    "global_asset_id",
})


# ═══════════════════════════════════════════════════════════════════════════════
# Raw-dict → SubmodelElement coercion (AAS JSON / config / pydantic dumps)
# ═══════════════════════════════════════════════════════════════════════════════
# The base container fields (``value`` / ``submodel_element``) are typed
# ``Dict[str, SubmodelElement]``.  Raw element dicts (e.g. from a config or an
# AAS JSON dump) are coerced here into concrete element instances before
# pydantic validates the container, so the ``Dict[str, X]`` type check is real.

_ELEMENT_TYPE_BY_MODELTYPE = {
    "Property": Property,
    "MultiLanguageProperty": MultiLanguageProperty,
    "Range": Range,
    "ReferenceElement": ReferenceElement,
    "RelationshipElement": RelationshipElement,
    "File": File,
    "Blob": Blob,
    "Capability": Capability,
    "Operation": Operation,
    "Entity": Entity,
    "SubmodelElementCollection": SubmodelElementCollection,
    "SubmodelElementList": SubmodelElementList,
}


class _PlaceholderId:
    """Deterministic id_short generator for SMC items that carry none."""
    _counter = itertools.count()

    @classmethod
    def next(cls) -> str:
        return f"elem{next(cls._counter)}"


def _snake(name: str) -> str:
    """camelCase → snake_case (AAS JSON keys → pydantic field names)."""
    s = re.sub(r"(?<!^)(?=[A-Z])", "_", name)
    return s.replace("-", "_").lower()


def _resolve_annotation(annotation: Any) -> Any:
    """Strip Annotated/Optional wrappers; strings (forward refs) → None."""
    if isinstance(annotation, str):
        return None
    while typing.get_origin(annotation) is typing.Annotated:
        annotation = typing.get_args(annotation)[0]
    return annotation


def _container_item_type(annotation: Any) -> Any:
    """Dict[str, X] / List[X] → X (or None when unknown)."""
    annotation = _resolve_annotation(annotation)
    origin = typing.get_origin(annotation)
    if origin in (dict, list, set, tuple):
        args = typing.get_args(annotation)
        if args:
            return args[1] if origin is dict and len(args) == 2 else args[0]
    return None


def _infer_model_type(d: dict) -> str:
    """Best-effort inference for dicts without ``modelType`` (pydantic dumps)."""
    v = d.get("value")
    if isinstance(v, list):
        return "SubmodelElementList"
    if isinstance(v, dict):
        if v and all(isinstance(x, dict) for x in v.values()):
            return "SubmodelElementCollection"
        return "MultiLanguageProperty"
    if "statements" in d:
        return "Entity"
    if "min" in d or "max" in d:
        return "Range"
    if "first" in d and "second" in d:
        return "RelationshipElement"
    if "content_type" in d:
        return "File" if isinstance(v, str) else "Blob"
    if "key" in d or "keys" in d:
        return "ReferenceElement"
    if "input_variable" in d or "output_variable" in d:
        return "Operation"
    return "Property"


def _build_element(cls: type, d: dict) -> Any:
    """Build an element instance from a normalized dict, recursing into
    container children."""
    d = dict(d)
    # Drop non-field keys (e.g. AAS JSON "modelType" → model_type) — they are
    # not model fields and ``extra="forbid"`` would reject them.
    fields = set(cls.model_fields)
    d = {k: v for k, v in d.items() if k in fields}
    if issubclass(cls, MultiLanguageProperty):
        d = dict(d)
        v = d.get("value")
        if isinstance(v, list):  # AAS JSON: [{language, text}] → lang map
            d["value"] = {
                lang.get("language"): lang.get("text")
                for lang in v if isinstance(lang, dict)
            }
    elif issubclass(cls, SubmodelElementList):
        d = dict(d)
        kids = d.get("value") or []
        if isinstance(kids, list):
            # AASd-114: list items share the list's semanticId, so semanticId
            # resolution would pick the wrong class — target the declared item
            # class explicitly instead (already-typed instances pass through).
            item_tp = getattr(cls, "item_type", None)
            d["value"] = [
                coerce_submodel_element(c, target_type=item_tp) for c in kids
            ]
    elif issubclass(cls, (SubmodelElementCollection, Submodel, Entity)):
        d = dict(d)
        if issubclass(cls, Submodel):
            container = "submodel_element"
        elif issubclass(cls, Entity):
            container = "statements"
        else:
            container = "value"
        kids = d.get(container) or []
        if isinstance(kids, list):
            # AAS JSON lists children — convert to id_short-keyed dict (the
            # container's validators then coerce each child with its proper
            # target type; raw dicts stay raw here).
            d[container] = {
                (c.get("id_short") or c.get("idShort") or _PlaceholderId.next()): c
                for c in kids
                if isinstance(c, dict)
            }
    return cls(**d)


def _concrete_element_targets(target_type: Any) -> list:
    """Concrete (non-abstract) element classes named by a container's
    annotation — used for subclass-specialized ``Dict[str, X]`` containers."""
    if target_type is None:
        return []
    resolved = _resolve_annotation(target_type)
    origin = typing.get_origin(resolved)
    if origin in (typing.Union, _UnionType):
        members = typing.get_args(resolved)
    else:
        members = (resolved,)
    return [
        m for m in members
        if isinstance(m, type) and issubclass(m, SubmodelElement)
        and m is not SubmodelElement
    ]


def coerce_submodel_element(
    value: Any,
    id_short: Optional[str] = None,
    target_type: Optional[type] = None,
) -> Any:
    """Coerce a raw dict (AAS JSON / config / pydantic dump) into a concrete
    SubmodelElement instance.  Already-typed elements pass through unchanged.

    When ``target_type`` names a concrete element type (subclass-specialized
    container, e.g. ``Dict[str, Parameter]``), that type is enforced — a wrong
    element is left raw so pydantic reports the type error.  Otherwise the type
    is inferred from ``modelType`` / keys.
    """
    if isinstance(value, SubmodelElement):
        if (
            target_type is not None
            and isinstance(target_type, type)
            and issubclass(target_type, SubmodelElement)
            and not isinstance(value, target_type)
        ):
            # Upcast a base-class instance to the target subclass (e.g. a bare
            # ``Property`` into ``Dict[str, Mode]``) so the concept semanticId
            # carried by the subclass is applied.  The dump's empty
            # ``semantic_id`` is dropped so the subclass default wins.
            try:
                d = value.model_dump()
                if not d.get("semantic_id"):
                    d.pop("semantic_id", None)
                return _build_element(target_type, d)
            except Exception:
                pass
        return value
    if not isinstance(value, dict):
        return value

    d = {_snake(k): v for k, v in value.items()}
    if id_short and not d.get("id_short"):
        d["id_short"] = id_short

    concrete = _concrete_element_targets(target_type)
    if concrete:
        # specialized container — build exactly this element type (type safety)
        for cls in concrete:
            try:
                return _build_element(cls, d)
            except Exception:
                continue
        return value

    # generic container (Dict[str, SubmodelElement]) — a dump's ``modelType``
    # discriminator is authoritative; otherwise a UNIQUE semanticId (config
    # dicts) resolves the concrete class; otherwise infer from keys.
    mt = d.get("model_type")
    if mt:
        cls = _ELEMENT_CLASS_REGISTRY.get(mt) or _ELEMENT_TYPE_BY_MODELTYPE.get(mt)
        if cls is not None:
            try:
                return _build_element(cls, d)
            except Exception:
                pass
    sid = d.get("semantic_id")
    if isinstance(sid, str) and sid:
        cls = _resolve_semantic_id_cls(sid)
        if cls is not None:
            try:
                return _build_element(cls, d)
            except Exception:
                pass
    mt = _infer_model_type(d)
    cls = _ELEMENT_CLASS_REGISTRY.get(mt) or _ELEMENT_TYPE_BY_MODELTYPE.get(mt)
    if cls is None:
        return value
    try:
        return _build_element(cls, d)
    except Exception:
        return value


def _coerce_container_data(cls: Any, data: Any) -> Any:
    """model_validator(mode='before') helper: coerce raw dicts inside the
    ``value`` / ``submodel_element`` / ``statements`` containers.

    Values-model fields (``value: MyValues``) are left to pydantic — the
    values model's own ``coerce_values`` before-validator coerces each child
    (with per-field type enforcement) and fills omitted fields from defaults.

    ``Dict[str, X]`` containers (dynamic name-keyed maps, e.g. MQTT actions)
    and SML ``value`` lists are coerced here: each raw dict becomes a concrete
    element instance (targeted at ``X`` / the SML's ``item_type``), so a dump
    child's ``modelType`` discriminator is resolved via the registry."""
    if isinstance(data, BaseModel):
        data = data.model_dump()
    if not isinstance(data, dict):
        return data
    for key in ("value", "submodel_element", "statements"):
        if key not in data:
            continue
        field_tp = _resolve_annotation(_field_annotation(cls, key))
        if isinstance(field_tp, type) and issubclass(field_tp, ContainerValue):
            continue  # values model — pydantic + its coerce_values handle it
        item_tp = _container_item_type(_field_annotation(cls, key))
        val = data[key]
        if isinstance(val, dict):
            default_children = cls.model_fields.get(key)
            default_children = (
                default_children.default if default_children is not None else None
            )
            if isinstance(default_children, dict):
                merged = dict(val)
                for dk, dv in default_children.items():
                    if dk not in merged:
                        merged[dk] = copy.deepcopy(dv)
                val = merged
            data[key] = {
                k: coerce_submodel_element(
                    v, id_short=k,
                    target_type=(
                        None  # dump children carry modelType → registry resolves
                        if isinstance(v, dict) and "modelType" in v
                        else (
                            type(default_children[k])
                            if isinstance(default_children, dict) and k in default_children
                            else item_tp
                        )
                    ),
                )
                for k, v in val.items()
            }
        elif isinstance(val, list):
            item_tp = getattr(cls, "item_type", None) or item_tp
            data[key] = [
                coerce_submodel_element(v, target_type=item_tp) for v in val
            ]
    return data


def _field_annotation(cls: Any, name: str) -> Any:
    """Resolved annotation for a model field (handles forward refs)."""
    try:
        hints = typing.get_type_hints(cls, include_extras=True)
        if name in hints:
            return hints[name]
    except Exception:
        pass
    return cls.model_fields[name].annotation


PrimitiveSubmodelElement = int | float | str | bool | bytes


class Submodel(HasSemantics, Identifiable):
    """A Submodel whose children live in ``submodel_element`` (a values model,
    mirroring basyx ``Submodel.submodel_element`` and the IDTA JSON
    ``submodelElements`` container).  Subclasses specialise the value as a
    values model, e.g. ``submodel_element: MySubmodelValues``."""
    submodel_element: ContainerValue = ContainerValue()

    @field_serializer("submodel_element")
    def _ser_submodel_element_lossless(self, v, _info):
        return _dump_container(v)

    @model_validator(mode="before")
    @classmethod
    def coerce_containers(cls, data):
        return _coerce_container_data(cls, data)

    @model_validator(mode="after")
    def check_submodel_elements(self) -> Any:
        _stamp_container_id_shorts(self)
        for field_name in self.model_fields:
            if field_name in ["id", "id_short", "description", "display_name",
                              "semantic_id", "qualifiers",
                              "supplemental_semantic_ids"]:
                continue
            if field_name == "submodel_element":
                assert isinstance(getattr(self, field_name), (ContainerValue, dict)), \
                    f"Field {field_name} must be a ContainerValue or Dict"
                continue
            assert is_valid_submodel_element(getattr(self, field_name)), \
                f"Field {field_name} is not a valid SubmodelElement"
        return self
