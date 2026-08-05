"""CapabilityDescription — generated from IDTA template."""

from __future__ import annotations

from typing import Any, ClassVar, List, Dict
from aas_pydantic import (
    Capability, ContainerValue, File, Key, ModelReference, MultiLanguageProperty, Property, Range, ReferenceElement, RelationshipElement, Submodel, SubmodelElement, SubmodelElementCollection, SubmodelElementList,
)

class SameProperty(RelationshipElement):
    semantic_id: str = "https://admin-shell.io/idta/CapabilityDescription/SameProperty/1/0"
    description: str = "Relationship of the Property described in the Property container as first element and the identical property as second element in another Submodel or an external information source."

class PropertyRange(Range):
    semantic_id: str = "https://admin-shell.io/idta/CapabilityPropertyEnumType/Range/1/0"
    description: str = "Range made of min and max values forming an interval. A valueId shall be set to define the semantic for the values."

class PropertyProperty(Property):
    semantic_id: str = "https://admin-shell.io/idta/CapabilityPropertyType/Property/1/0"
    description: str = "Property with a value describing an information data point. A valueId shall be set to define the semantic for the value."

class PropertyMultiLanguageProperty(MultiLanguageProperty):
    semantic_id: str = "https://admin-shell.io/idta/CapabilityPropertyType/MultiLanguageProperty/1/0"
    description: str = "Property with a value for one or more language entries with corresponding text describing an information data point. A valueId shall be set to define the semantic for the value."

class PropertySubmodelList(SubmodelElementList):
    semantic_id: str = "https://admin-shell.io/idta/CapabilityPropertyType/SubmodelElementList/1/0"
    description: str = "A list of one or more elements defined by only the enum type CapabilityPropertyType. "
    value: List[Any] = []

class PropertyContainerValues(ContainerValue):
    model_config = {'extra': 'forbid'}
    same_property: Dict[str, SameProperty] = {}
    property_range: Dict[str, PropertyRange] = {}
    property_property: Dict[str, PropertyProperty] = {}
    property_multi_language_property: Dict[str, PropertyMultiLanguageProperty] = {}
    property_submodel_list: Dict[str, PropertySubmodelList] = {}
    property_comment: MultiLanguageProperty = MultiLanguageProperty(
        semantic_id="https://admin-shell.io/idta/CapabilityDescription/PropertyComment/1/0",
        description="General description of the property.",
    )

class PropertyContainer(SubmodelElementCollection):
    semantic_id: str = "https://admin-shell.io/idta/CapabilityDescription/PropertyContainer/1/0"
    description: str = "Information for a certain property as defined by CapabilityPropertyType and its descriptive elements."
    value: PropertyContainerValues = PropertyContainerValues()

class PropertySetValues(ContainerValue):
    model_config = {'extra': 'forbid'}
    property_container: Dict[str, PropertyContainer] = {}

class PropertySet(SubmodelElementCollection):
    semantic_id: str = "https://admin-shell.io/idta/CapabilityDescription/PropertySet/1/0"
    description: str = "Set of properties describing the capability in more detail, if existing."
    value: PropertySetValues = PropertySetValues()

class CapabilityRealizedBy(RelationshipElement):
    semantic_id: str = "https://admin-shell.io/idta/CapabilityDescription/CapabilityRealizedBy/1/0"
    description: str = "Relationship between the Capability element in the CapabilityContainer as first element and a Skill implementation, not defined in this Submodel template, as second element."

class CapabilityComposedOf(RelationshipElement):
    semantic_id: str = "https://admin-shell.io/idta/CapabilityDescription/CapabilityComposedOf/1/0"
    description: str = "Relationship between a composed capability as first element and one of its minimum two subordinate capabilities as second element."

class ComposedOfContainerValues(ContainerValue):
    model_config = {'extra': 'forbid'}
    capability_composed_of: Dict[str, CapabilityComposedOf] = {}
    composed_of_comment: MultiLanguageProperty = MultiLanguageProperty(
        semantic_id="https://admin-shell.io/idta/CapabilityDescription/ComposedOfComment/1/0",
        description="Comment to describe the composition in human readable form.",
    )

class ComposedOfContainer(SubmodelElementCollection):
    semantic_id: str = "https://admin-shell.io/idta/CapabilityDescription/ComposedOfContainer/1/0"
    description: str = "Container corresponding to one composition for the Capability in the CapabilityContainer."
    value: ComposedOfContainerValues = ComposedOfContainerValues()

class ComposedOfSetValues(ContainerValue):
    model_config = {'extra': 'forbid'}
    composed_of_container: Dict[str, ComposedOfContainer] = {}

class ComposedOfSet(SubmodelElementCollection):
    semantic_id: str = "https://admin-shell.io/idta/CapabilityDescription/ComposedOfSet/1/0"
    description: str = "If composition(s) for the Capability element in the CapabilityContainer exists, this set has to be created."
    value: ComposedOfSetValues = ComposedOfSetValues()

class CapabilityGeneralizedBy(RelationshipElement):
    semantic_id: str = "https://admin-shell.io/idta/CapabilityDescription/CapabilityGeneralizedBy/1/0"
    description: str = "Relationship between the Capability as first element, described in the CapabilityContainer, and a more general Capability as second element."

class GeneralizedBySetValues(ContainerValue):
    model_config = {'extra': 'forbid'}
    capability_generalized_by: Dict[str, CapabilityGeneralizedBy] = {}

class GeneralizedBySet(SubmodelElementCollection):
    semantic_id: str = "https://admin-shell.io/idta/CapabilityDescription/GeneralizedBySet/1/0"
    description: str = "If generalization(s) for the Capability element in the CapabilityContainer exists, this set has to be created."
    value: GeneralizedBySetValues = GeneralizedBySetValues()

class CustomConstraintValues(ContainerValue):
    model_config = {'extra': 'forbid'}
    pass

class CustomConstraint(SubmodelElementCollection):
    semantic_id: str = "https://admin-shell.io/idta/CapabilityDescription/PropertyConstraintType/CustomConstraint/1/0"
    description: str = "SubmodelElement which can be used to validate the constraint for the considered Properties in this PropertyConstraintContainer against other properties. This can be freely defined for the purpose of constraining a property and is not specified in this Submodel Template."
    value: CustomConstraintValues = CustomConstraintValues()

class ConstraintHasProperty(RelationshipElement):
    semantic_id: str = "https://admin-shell.io/idta/CapabilityDescription/ConstraintHasProperty/1/0"
    description: str = "Relates the PropertyConstraint as first element to a Property from a PropertyContainer as second element."

class ConstraintPropertyRelationsValues(ContainerValue):
    model_config = {'extra': 'forbid'}
    constraint_has_property: Dict[str, ConstraintHasProperty] = {}

class ConstraintPropertyRelations(SubmodelElementCollection):
    semantic_id: str = "https://admin-shell.io/idta/CapabilityDescription/ConstraintPropertyRelations/1/0"
    description: str = "Contains all relationships for the constraint in the PropertyConstraintContainer."
    value: ConstraintPropertyRelationsValues = ConstraintPropertyRelationsValues()

class PropertyConstraintContainerValues(ContainerValue):
    model_config = {'extra': 'forbid'}
    basic_constraint: Property = Property(
        semantic_id="https://admin-shell.io/idta/CapabilityDescription/PropertyConstraintType/BasicConstraint/1/0",
        description="Property element which can be used to validate the constraint for the considered Properties in this PropertyConstraintContainer against other properties.",
        value_type="xs:string",
    )
    custom_constraint: CustomConstraint = CustomConstraint()
    o_c_l_constraint: File = File(
        semantic_id="https://admin-shell.io/idta/CapabilityDescription/PropertyConstraintType/OCLConstraint/1/0",
        description="Object Contraint Language (OCL) as File element which can be used to validate the constraint for the considered Properties in this PropertyConstraintContainer against other properties.",
    )
    operation_constraint: ReferenceElement = ReferenceElement(
        semantic_id="https://admin-shell.io/idta/CapabilityDescription/PropertyConstraintType/OperationConstraint/1/0",
        description="Reference to an (external) Operation element which can be used to validate the constraint for the considered Properties in this PropertyConstraintContainer against other properties.",
    )
    constraint_type: Property = Property(
        semantic_id="https://admin-shell.io/idta/CapabilityDescription/ConstraintType/1/0",
        description="Abstract Enum type of allowed SubmodelElements for these Properties constraints. Exactly one of the SubmodelElements below must be instanciated, e.g., similar to SubmodelElementList with exactly one element.",
        value_type="xs:string",
    )
    property_conditional_type: Property = Property(
        semantic_id="https://admin-shell.io/idta/CapabilityDescription/PropertyConditionalType/1/0",
        description="Defines the type of the property conditions as defined in the ConceptDescription with the same name (PropertyConditionalType).",
        value_type="xs:string",
    )
    constraint_property_relations: ConstraintPropertyRelations = ConstraintPropertyRelations()

class PropertyConstraintContainer(SubmodelElementCollection):
    semantic_id: str = "https://admin-shell.io/idta/CapabilityDescription/PropertyConstraintContainer/1/0"
    description: str = "If one or more constraints exist for a Capability Property, then for every constraint a PropertyConstraintContainer has to be created."
    value: PropertyConstraintContainerValues = PropertyConstraintContainerValues()

class TransitionConstraintContainerValues(ContainerValue):
    model_config = {'extra': 'forbid'}
    transition_constrained_by: RelationshipElement = RelationshipElement(
        semantic_id="https://admin-shell.io/idta/CapabilityDescription/TransitionConstrainedBy/1/0",
        description="Relates the constrained Capability as first element to a constraining Capability from another CapabilityContainer as second element.",
        first=ModelReference(
            key=(
                Key(type_="Submodel", value="https://admin-shell.io/idta/CapabilityDescription/1/0/Submodel"),
                Key(type_="SubmodelElementCollection", value="CapabilitySet"),
                Key(type_="SubmodelElementCollection", value="CapabilityContainer"),
                Key(type_="Capability", value="Capability"),
            ),
        ),
        second=ModelReference(
            key=(
                Key(type_="Submodel", value="https://admin-shell.io/idta/CapabilityDescription/1/0/Submodel"),
                Key(type_="SubmodelElementCollection", value="CapabilitySet"),
                Key(type_="SubmodelElementCollection", value="CapabilityContainer"),
                Key(type_="Capability", value="Capability"),
            ),
        ),
    )
    transition_conditional_type: Property = Property(
        semantic_id="https://admin-shell.io/idta/CapabilityDescription/TransitionConditionalType/1/0",
        description="Defines the element TransitionConstrainedBy of TransitionConstraintType.",
        value_type="xs:string",
    )

class TransitionConstraintContainer(SubmodelElementCollection):
    semantic_id: str = "https://admin-shell.io/idta/CapabilityDescription/TransitionConstraintContainer/1/0"
    description: str = "If one or more constraints exist for a Capability, then for every transitional constraint a TransitionConstraintContainer has to be created."
    value: TransitionConstraintContainerValues = TransitionConstraintContainerValues()

class ConstraintSetValues(ContainerValue):
    model_config = {'extra': 'forbid'}
    property_constraint_container: Dict[str, PropertyConstraintContainer] = {}
    transition_constraint_container: Dict[str, TransitionConstraintContainer] = {}

class ConstraintSet(SubmodelElementCollection):
    semantic_id: str = "https://admin-shell.io/idta/CapabilityDescription/ConstraintSet/1/0"
    description: str = "If constraint(s) for the Capability element in the CapabilityContainer exists, this set has to be created."
    value: ConstraintSetValues = ConstraintSetValues()

class CapabilityRelationsValues(ContainerValue):
    model_config = {'extra': 'forbid'}
    capability_realized_by: Dict[str, CapabilityRealizedBy] = {}
    composed_of_set: ComposedOfSet = ComposedOfSet()
    generalized_by_set: Dict[str, GeneralizedBySet] = {}
    constraint_set: Dict[str, ConstraintSet] = {}

class CapabilityRelations(SubmodelElementCollection):
    semantic_id: str = "https://admin-shell.io/idta/CapabilityDescription/CapabilityRelations/1/0"
    description: str = "Collection of relationships for the capability, if existing."
    value: CapabilityRelationsValues = CapabilityRelationsValues()

class CapabilityContainerValues(ContainerValue):
    model_config = {'extra': 'forbid'}
    capability: Capability = Capability(
        semantic_id="https://admin-shell.io/idta/CapabilityDescription/Capability/1/0",
        description="[A capability is a] implementation-independent specification of a function in industrial production to achieve an effect in the physical or virtual world. ",
    )
    capability_comment: MultiLanguageProperty = MultiLanguageProperty(
        semantic_id="https://admin-shell.io/idta/CapabilityDescription/CapabilityComment/1/0",
        description="Individual comment of the capability.",
    )
    property_set: Dict[str, PropertySet] = {}
    capability_relations: CapabilityRelations = CapabilityRelations()

class CapabilityContainer(SubmodelElementCollection):
    semantic_id: str = "https://admin-shell.io/idta/CapabilityDescription/CapabilityContainer/1/0"
    description: str = "A Container for one capability and all its additional descriptive elements."
    value: CapabilityContainerValues = CapabilityContainerValues()

class CapabilitySetValues(ContainerValue):
    model_config = {'extra': 'forbid'}
    capability_container: Dict[str, CapabilityContainer] = {}

class CapabilitySet(SubmodelElementCollection):
    semantic_id: str = "https://admin-shell.io/idta/CapabilityDescription/CapabilitySet/1/0"
    description: str = "A Set of CapabilityContainer for a Use Case for the asset."
    value: CapabilitySetValues = CapabilitySetValues()

class CapabilityDescriptionValues(ContainerValue):
    model_config = {'extra': 'forbid'}
    capability_set: Dict[str, CapabilitySet] = {}

class CapabilityDescription(Submodel):
    semantic_id: str = "https://admin-shell.io/idta/SubmodelTemplate/CapabilityDescription/1/0"
    description: str = "Definition of the Submodel CapabilityDescription identified by its semanticId. The Submodel idShort can be picked freely."
    VERSION: ClassVar[str] = "1"
    REVISION: ClassVar[str] = "0"
    submodel_element: CapabilityDescriptionValues = CapabilityDescriptionValues()

# ── Resolve forward references (Pydantic circular refs) ──
SameProperty.model_rebuild()
PropertyRange.model_rebuild()
PropertyProperty.model_rebuild()
PropertyMultiLanguageProperty.model_rebuild()
PropertySubmodelList.model_rebuild()
PropertyContainerValues.model_rebuild()
PropertyContainer.model_rebuild()
PropertySetValues.model_rebuild()
PropertySet.model_rebuild()
CapabilityRealizedBy.model_rebuild()
CapabilityComposedOf.model_rebuild()
ComposedOfContainerValues.model_rebuild()
ComposedOfContainer.model_rebuild()
ComposedOfSetValues.model_rebuild()
ComposedOfSet.model_rebuild()
CapabilityGeneralizedBy.model_rebuild()
GeneralizedBySetValues.model_rebuild()
GeneralizedBySet.model_rebuild()
CustomConstraintValues.model_rebuild()
CustomConstraint.model_rebuild()
ConstraintHasProperty.model_rebuild()
ConstraintPropertyRelationsValues.model_rebuild()
ConstraintPropertyRelations.model_rebuild()
PropertyConstraintContainerValues.model_rebuild()
PropertyConstraintContainer.model_rebuild()
TransitionConstraintContainerValues.model_rebuild()
TransitionConstraintContainer.model_rebuild()
ConstraintSetValues.model_rebuild()
ConstraintSet.model_rebuild()
CapabilityRelationsValues.model_rebuild()
CapabilityRelations.model_rebuild()
CapabilityContainerValues.model_rebuild()
CapabilityContainer.model_rebuild()
CapabilitySetValues.model_rebuild()
CapabilitySet.model_rebuild()
CapabilityDescriptionValues.model_rebuild()
CapabilityDescription.model_rebuild()
