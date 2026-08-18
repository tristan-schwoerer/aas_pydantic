"""CapabilityDescription — generated from IDTA template."""

from __future__ import annotations

from typing import Any, ClassVar, List, Dict, Optional
from aas_pydantic import (
    Capability, ExternalReference, File, Key, ModelReference, MultiLanguageProperty, Property, Range, ReferenceElement, RelationshipElement, Submodel, SubmodelElement, SubmodelElementCollection, SubmodelElementList,
)

class CapabilityComment(MultiLanguageProperty):
    semantic_id: str = "https://admin-shell.io/idta/CapabilityDescription/CapabilityComment/1/0"
    description: str = "Individual comment of the capability."

class SameProperty(RelationshipElement):
    semantic_id: str = "https://admin-shell.io/idta/CapabilityDescription/SameProperty/1/0"
    description: str = "Relationship of the Property described in the Property container as first element and the identical property as second element in another Submodel or an external information source."
    first: ExternalReference = ExternalReference(
        key=(
            Key(type_="GlobalReference", value="urn:example:capability-description:same-property:first"),
        ),
    ),
    second: ExternalReference = ExternalReference(
        key=(
            Key(type_="GlobalReference", value="urn:example:capability-description:same-property:second"),
        ),
    ),

class PropertyRange(Range):
    semantic_id: str = "https://admin-shell.io/idta/CapabilityPropertyEnumType/Range/1/0"
    description: str = "Range made of min and max values forming an interval. A valueId shall be set to define the semantic for the values."
    value_type: str = "xs:string"

class PropertyProperty(Property):
    semantic_id: str = "https://admin-shell.io/idta/CapabilityPropertyType/Property/1/0"
    description: str = "Property with a value describing an information data point. A valueId shall be set to define the semantic for the value."
    value_type: str = "xs:string"

class PropertyMultiLanguageProperty(MultiLanguageProperty):
    semantic_id: str = "https://admin-shell.io/idta/CapabilityPropertyType/MultiLanguageProperty/1/0"
    description: str = "Property with a value for one or more language entries with corresponding text describing an information data point. A valueId shall be set to define the semantic for the value."

class PropertySubmodelList(SubmodelElementList):
    semantic_id: str = "https://admin-shell.io/idta/CapabilityPropertyType/SubmodelElementList/1/0"
    description: str = "A list of one or more elements defined by only the enum type CapabilityPropertyType. "
    value: List[Any] = []

class PropertyComment(MultiLanguageProperty):
    semantic_id: str = "https://admin-shell.io/idta/CapabilityDescription/PropertyComment/1/0"
    description: str = "General description of the property."

class PropertyContainer(SubmodelElementCollection):
    semantic_id: str = "https://admin-shell.io/idta/CapabilityDescription/PropertyContainer/1/0"
    description: str = "Information for a certain property as defined by CapabilityPropertyType and its descriptive elements."
    same_property: Dict[str, SameProperty] = {}
    property_range: Dict[str, PropertyRange] = {}
    property_property: Dict[str, PropertyProperty] = {}
    property_multi_language_property: Dict[str, PropertyMultiLanguageProperty] = {}
    property_submodel_list: Dict[str, PropertySubmodelList] = {}
    property_comment: Optional[PropertyComment] = None

class PropertySet(SubmodelElementCollection):
    semantic_id: str = "https://admin-shell.io/idta/CapabilityDescription/PropertySet/1/0"
    description: str = "Set of properties describing the capability in more detail, if existing."
    property_container: Dict[str, PropertyContainer] = {}

class CapabilityRealizedBy(RelationshipElement):
    semantic_id: str = "https://admin-shell.io/idta/CapabilityDescription/CapabilityRealizedBy/1/0"
    description: str = "Relationship between the Capability element in the CapabilityContainer as first element and a Skill implementation, not defined in this Submodel template, as second element."
    first: ModelReference = ModelReference(
        key=(
            Key(type_="Submodel", value="https://admin-shell.io/idta/CapabilityDescription/1/0/Submodel"),
            Key(type_="SubmodelElementCollection", value="CapabilitySet"),
            Key(type_="SubmodelElementCollection", value="CapabilityContainer"),
            Key(type_="Capability", value="Capability"),
        ),
    ),
    second: ExternalReference = ExternalReference(
        key=(
            Key(type_="GlobalReference", value="urn:example:capability-description:capability-realized-by:skill"),
        ),
    ),

class CapabilityComposedOf(RelationshipElement):
    semantic_id: str = "https://admin-shell.io/idta/CapabilityDescription/CapabilityComposedOf/1/0"
    description: str = "Relationship between a composed capability as first element and one of its minimum two subordinate capabilities as second element."
    first: ModelReference = ModelReference(
        key=(
            Key(type_="Submodel", value="https://admin-shell.io/idta/CapabilityDescription/1/0/Submodel"),
            Key(type_="SubmodelElementCollection", value="CapabilitySet"),
            Key(type_="SubmodelElementCollection", value="CapabilityContainer"),
            Key(type_="Capability", value="Capability"),
        ),
    ),
    second: ModelReference = ModelReference(
        key=(
            Key(type_="Submodel", value="https://admin-shell.io/idta/CapabilityDescription/1/0/Submodel"),
            Key(type_="SubmodelElementCollection", value="CapabilitySet"),
            Key(type_="SubmodelElementCollection", value="CapabilityContainer"),
            Key(type_="Capability", value="Capability"),
        ),
    ),

class ComposedOfComment(MultiLanguageProperty):
    semantic_id: str = "https://admin-shell.io/idta/CapabilityDescription/ComposedOfComment/1/0"
    description: str = "Comment to describe the composition in human readable form."

class ComposedOfContainer(SubmodelElementCollection):
    semantic_id: str = "https://admin-shell.io/idta/CapabilityDescription/ComposedOfContainer/1/0"
    description: str = "Container corresponding to one composition for the Capability in the CapabilityContainer."
    capability_composed_of: Dict[str, CapabilityComposedOf] = {}
    composed_of_comment: Optional[ComposedOfComment] = None

class ComposedOfSet(SubmodelElementCollection):
    semantic_id: str = "https://admin-shell.io/idta/CapabilityDescription/ComposedOfSet/1/0"
    description: str = "If composition(s) for the Capability element in the CapabilityContainer exists, this set has to be created."
    composed_of_container: Dict[str, ComposedOfContainer] = {}

class CapabilityGeneralizedBy(RelationshipElement):
    semantic_id: str = "https://admin-shell.io/idta/CapabilityDescription/CapabilityGeneralizedBy/1/0"
    description: str = "Relationship between the Capability as first element, described in the CapabilityContainer, and a more general Capability as second element."
    first: ModelReference = ModelReference(
        key=(
            Key(type_="Submodel", value="https://admin-shell.io/idta/CapabilityDescription/1/0/Submodel"),
            Key(type_="SubmodelElementCollection", value="CapabilitySet"),
            Key(type_="SubmodelElementCollection", value="CapabilityContainer"),
            Key(type_="Capability", value="Capability"),
        ),
    ),
    second: ModelReference = ModelReference(
        key=(
            Key(type_="Submodel", value="https://admin-shell.io/idta/CapabilityDescription/1/0/Submodel"),
            Key(type_="SubmodelElementCollection", value="CapabilitySet"),
            Key(type_="SubmodelElementCollection", value="CapabilityContainer"),
            Key(type_="Capability", value="Capability"),
        ),
    ),

class GeneralizedBySet(SubmodelElementCollection):
    semantic_id: str = "https://admin-shell.io/idta/CapabilityDescription/GeneralizedBySet/1/0"
    description: str = "If generalization(s) for the Capability element in the CapabilityContainer exists, this set has to be created."
    capability_generalized_by: Dict[str, CapabilityGeneralizedBy] = {}

class BasicConstraint(Property):
    semantic_id: str = "https://admin-shell.io/idta/CapabilityDescription/PropertyConstraintType/BasicConstraint/1/0"
    description: str = "Property element which can be used to validate the constraint for the considered Properties in this PropertyConstraintContainer against other properties."
    value_type: str = "xs:string"

class CustomConstraint(SubmodelElementCollection):
    semantic_id: str = "https://admin-shell.io/idta/CapabilityDescription/PropertyConstraintType/CustomConstraint/1/0"
    description: str = "SubmodelElement which can be used to validate the constraint for the considered Properties in this PropertyConstraintContainer against other properties. This can be freely defined for the purpose of constraining a property and is not specified in this Submodel Template."
    pass

class OCLConstraint(File):
    semantic_id: str = "https://admin-shell.io/idta/CapabilityDescription/PropertyConstraintType/OCLConstraint/1/0"
    description: str = "Object Contraint Language (OCL) as File element which can be used to validate the constraint for the considered Properties in this PropertyConstraintContainer against other properties."

class OperationConstraint(ReferenceElement):
    semantic_id: str = "https://admin-shell.io/idta/CapabilityDescription/PropertyConstraintType/OperationConstraint/1/0"
    description: str = "Reference to an (external) Operation element which can be used to validate the constraint for the considered Properties in this PropertyConstraintContainer against other properties."

class ConstraintType(Property):
    semantic_id: str = "https://admin-shell.io/idta/CapabilityDescription/ConstraintType/1/0"
    description: str = "Abstract Enum type of allowed SubmodelElements for these Properties constraints. Exactly one of the SubmodelElements below must be instanciated, e.g., similar to SubmodelElementList with exactly one element."
    value_type: str = "xs:string"

class PropertyConditionalType(Property):
    semantic_id: str = "https://admin-shell.io/idta/CapabilityDescription/PropertyConditionalType/1/0"
    description: str = "Defines the type of the property conditions as defined in the ConceptDescription with the same name (PropertyConditionalType)."
    value_type: str = "xs:string"

class ConstraintHasProperty(RelationshipElement):
    semantic_id: str = "https://admin-shell.io/idta/CapabilityDescription/ConstraintHasProperty/1/0"
    description: str = "Relates the PropertyConstraint as first element to a Property from a PropertyContainer as second element."
    first: ModelReference = ModelReference(
        key=(
            Key(type_="Submodel", value="https://admin-shell.io/idta/CapabilityDescription/1/0/Submodel"),
            Key(type_="SubmodelElementCollection", value="CapabilitySet"),
            Key(type_="SubmodelElementCollection", value="CapabilityContainer"),
            Key(type_="SubmodelElementCollection", value="CapabilityRelations"),
            Key(type_="SubmodelElementCollection", value="ConstraintSet"),
            Key(type_="SubmodelElementCollection", value="PropertyConstraintContainer"),
            Key(type_="Property", value="BasicConstraint"),
        ),
    ),
    second: ModelReference = ModelReference(
        key=(
            Key(type_="Submodel", value="https://admin-shell.io/idta/CapabilityDescription/1/0/Submodel"),
            Key(type_="SubmodelElementCollection", value="CapabilitySet"),
            Key(type_="SubmodelElementCollection", value="CapabilityContainer"),
            Key(type_="SubmodelElementCollection", value="PropertySet"),
            Key(type_="SubmodelElementCollection", value="PropertyContainer"),
            Key(type_="Property", value="PropertyProperty"),
        ),
    ),

class ConstraintPropertyRelations(SubmodelElementCollection):
    semantic_id: str = "https://admin-shell.io/idta/CapabilityDescription/ConstraintPropertyRelations/1/0"
    description: str = "Contains all relationships for the constraint in the PropertyConstraintContainer."
    constraint_has_property: Dict[str, ConstraintHasProperty] = {}

class PropertyConstraintContainer(SubmodelElementCollection):
    semantic_id: str = "https://admin-shell.io/idta/CapabilityDescription/PropertyConstraintContainer/1/0"
    description: str = "If one or more constraints exist for a Capability Property, then for every constraint a PropertyConstraintContainer has to be created."
    basic_constraint: BasicConstraint
    custom_constraint: CustomConstraint
    o_c_l_constraint: OCLConstraint
    operation_constraint: OperationConstraint
    constraint_type: ConstraintType
    property_conditional_type: PropertyConditionalType
    constraint_property_relations: ConstraintPropertyRelations

class TransitionConstrainedBy(RelationshipElement):
    semantic_id: str = "https://admin-shell.io/idta/CapabilityDescription/TransitionConstrainedBy/1/0"
    description: str = "Relates the constrained Capability as first element to a constraining Capability from another CapabilityContainer as second element."
    first: ModelReference = ModelReference(
        key=(
            Key(type_="Submodel", value="https://admin-shell.io/idta/CapabilityDescription/1/0/Submodel"),
            Key(type_="SubmodelElementCollection", value="CapabilitySet"),
            Key(type_="SubmodelElementCollection", value="CapabilityContainer"),
            Key(type_="Capability", value="Capability"),
        ),
    ),
    second: ModelReference = ModelReference(
        key=(
            Key(type_="Submodel", value="https://admin-shell.io/idta/CapabilityDescription/1/0/Submodel"),
            Key(type_="SubmodelElementCollection", value="CapabilitySet"),
            Key(type_="SubmodelElementCollection", value="CapabilityContainer"),
            Key(type_="Capability", value="Capability"),
        ),
    ),

class TransitionConditionalType(Property):
    semantic_id: str = "https://admin-shell.io/idta/CapabilityDescription/TransitionConditionalType/1/0"
    description: str = "Defines the element TransitionConstrainedBy of TransitionConstraintType."
    value_type: str = "xs:string"

class TransitionConstraintContainer(SubmodelElementCollection):
    semantic_id: str = "https://admin-shell.io/idta/CapabilityDescription/TransitionConstraintContainer/1/0"
    description: str = "If one or more constraints exist for a Capability, then for every transitional constraint a TransitionConstraintContainer has to be created."
    transition_constrained_by: TransitionConstrainedBy
    transition_conditional_type: TransitionConditionalType

class ConstraintSet(SubmodelElementCollection):
    semantic_id: str = "https://admin-shell.io/idta/CapabilityDescription/ConstraintSet/1/0"
    description: str = "If constraint(s) for the Capability element in the CapabilityContainer exists, this set has to be created."
    property_constraint_container: Dict[str, PropertyConstraintContainer] = {}
    transition_constraint_container: Dict[str, TransitionConstraintContainer] = {}

class CapabilityRelations(SubmodelElementCollection):
    semantic_id: str = "https://admin-shell.io/idta/CapabilityDescription/CapabilityRelations/1/0"
    description: str = "Collection of relationships for the capability, if existing."
    capability_realized_by: Dict[str, CapabilityRealizedBy] = {}
    composed_of_set: Optional[ComposedOfSet] = None
    generalized_by_set: Dict[str, GeneralizedBySet] = {}
    constraint_set: Dict[str, ConstraintSet] = {}

class CapabilityContainer(SubmodelElementCollection):
    semantic_id: str = "https://admin-shell.io/idta/CapabilityDescription/CapabilityContainer/1/0"
    description: str = "A Container for one capability and all its additional descriptive elements."
    capability: Capability
    capability_comment: Optional[CapabilityComment] = None
    property_set: Dict[str, PropertySet] = {}
    capability_relations: Optional[CapabilityRelations] = None

class CapabilitySet(SubmodelElementCollection):
    semantic_id: str = "https://admin-shell.io/idta/CapabilityDescription/CapabilitySet/1/0"
    description: str = "A Set of CapabilityContainer for a Use Case for the asset."
    capability_container: Dict[str, CapabilityContainer] = {}

class CapabilityDescription(Submodel):
    semantic_id: str = "https://admin-shell.io/idta/SubmodelTemplate/CapabilityDescription/1/0"
    description: str = "Definition of the Submodel CapabilityDescription identified by its semanticId. The Submodel idShort can be picked freely."
    VERSION: ClassVar[str] = "1"
    REVISION: ClassVar[str] = "0"
    capability_set: Dict[str, CapabilitySet] = {}

# ── Resolve forward references (Pydantic circular refs) ──
CapabilityComment.model_rebuild()
SameProperty.model_rebuild()
PropertyRange.model_rebuild()
PropertyProperty.model_rebuild()
PropertyMultiLanguageProperty.model_rebuild()
PropertySubmodelList.model_rebuild()
PropertyComment.model_rebuild()
PropertyContainer.model_rebuild()
PropertySet.model_rebuild()
CapabilityRealizedBy.model_rebuild()
CapabilityComposedOf.model_rebuild()
ComposedOfComment.model_rebuild()
ComposedOfContainer.model_rebuild()
ComposedOfSet.model_rebuild()
CapabilityGeneralizedBy.model_rebuild()
GeneralizedBySet.model_rebuild()
BasicConstraint.model_rebuild()
CustomConstraint.model_rebuild()
OCLConstraint.model_rebuild()
OperationConstraint.model_rebuild()
ConstraintType.model_rebuild()
PropertyConditionalType.model_rebuild()
ConstraintHasProperty.model_rebuild()
ConstraintPropertyRelations.model_rebuild()
PropertyConstraintContainer.model_rebuild()
TransitionConstrainedBy.model_rebuild()
TransitionConditionalType.model_rebuild()
TransitionConstraintContainer.model_rebuild()
ConstraintSet.model_rebuild()
CapabilityRelations.model_rebuild()
CapabilityContainer.model_rebuild()
CapabilitySet.model_rebuild()
CapabilityDescription.model_rebuild()
