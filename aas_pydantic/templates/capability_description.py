"""CapabilityDescription — generated from IDTA template."""

from typing import ClassVar, List, Optional
from pydantic import Field
from aas_pydantic import Submodel, SubmodelElementCollection, Capability, Qualifier

class PropertyContainer(SubmodelElementCollection):
    semantic_id: str = "https://admin-shell.io/idta/CapabilityDescription/PropertyContainer/1/0"
    description: str = "Information for a certain property as defined by CapabilityPropertyType and its descriptive elements."
    qualifiers: List[Qualifier] = [
        Qualifier(type_="SMT/Cardinality", value="OneToMany", semantic_id="https://admin-shell.io/SubmodelTemplates/Cardinality/1/0"),
        Qualifier(type_="EditIdShort", value="True"),
    ]

    same_property: str = Field("", json_schema_extra={"aas": {"semantic_id": "https://admin-shell.io/idta/CapabilityDescription/SameProperty/1/0", "description": "Relationship of the Property described in the Property container as first element and the identical property as second element in another Submodel or an external information source.", "qualifiers": [{"type": "SMT/Cardinality", "value": "ZeroToMany", "semantic_id": "https://admin-shell.io/SubmodelTemplates/Cardinality/1/0"}]}})
    property_range: str = Field("", json_schema_extra={"aas": {"semantic_id": "https://admin-shell.io/idta/CapabilityPropertyEnumType/Range/1/0", "description": "Range made of min and max values forming an interval. A valueId shall be set to define the semantic for the values.", "qualifiers": [{"type": "SMT/Cardinality", "value": "ZeroToMany", "semantic_id": "https://admin-shell.io/SubmodelTemplates/Cardinality/1/0"}, {"type": "EditIdShort", "value": "True"}]}})
    property_property: str = Field("", json_schema_extra={"aas": {"semantic_id": "https://admin-shell.io/idta/CapabilityPropertyType/Property/1/0", "description": "Property with a value describing an information data point. A valueId shall be set to define the semantic for the value.", "qualifiers": [{"type": "SMT/Cardinality", "value": "ZeroToMany", "semantic_id": "https://admin-shell.io/SubmodelTemplates/Cardinality/1/0"}, {"type": "EditIdShort", "value": "True"}]}})
    property_multi_language_property: str = Field("", json_schema_extra={"aas": {"semantic_id": "https://admin-shell.io/idta/CapabilityPropertyType/MultiLanguageProperty/1/0", "description": "Property with a value for one or more language entries with corresponding text describing an information data point. A valueId shall be set to define the semantic for the value.", "qualifiers": [{"type": "SMT/Cardinality", "value": "ZeroToMany", "semantic_id": "https://admin-shell.io/SubmodelTemplates/Cardinality/1/0"}, {"type": "EditIdShort", "value": "True"}]}})
    property_submodel_list: List[str] = Field([], json_schema_extra={"aas": {"semantic_id": "https://admin-shell.io/idta/CapabilityPropertyType/SubmodelElementList/1/0", "description": "A list of one or more elements defined by only the enum type CapabilityPropertyType. ", "qualifiers": [{"type": "SMT/Cardinality", "value": "ZeroToMany", "semantic_id": "https://admin-shell.io/SubmodelTemplates/Cardinality/1/0"}, {"type": "SMT/Cardinality", "value": "Recursive", "semantic_id": "https://admin-shell.io/SubmodelTemplates/Recursion/1/0"}, {"type": "EditIdShort", "value": "True"}]}})
    property_comment: str = Field("", json_schema_extra={"aas": {"semantic_id": "https://admin-shell.io/idta/CapabilityDescription/PropertyComment/1/0", "description": "General description of the property.", "qualifiers": [{"type": "SMT/Cardinality", "value": "ZeroToOne", "semantic_id": "https://admin-shell.io/SubmodelTemplates/Cardinality/1/0"}]}})

class PropertySet(SubmodelElementCollection):
    semantic_id: str = "https://admin-shell.io/idta/CapabilityDescription/PropertySet/1/0"
    description: str = "Set of properties describing the capability in more detail, if existing."
    qualifiers: List[Qualifier] = [
        Qualifier(type_="SMT/Cardinality", value="ZeroToMany", semantic_id="https://admin-shell.io/SubmodelTemplates/Cardinality/1/0"),
        Qualifier(type_="EditIdShort", value="True"),
    ]

    property_container: Optional[PropertyContainer] = None

class ComposedOfContainer(SubmodelElementCollection):
    semantic_id: str = "https://admin-shell.io/idta/CapabilityDescription/ComposedOfContainer/1/0"
    description: str = "Container corresponding to one composition for the Capability in the CapabilityContainer."
    qualifiers: List[Qualifier] = [
        Qualifier(type_="SMT/Cardinality", value="OneToMany", semantic_id="https://admin-shell.io/SubmodelTemplates/Cardinality/1/0"),
        Qualifier(type_="EditIdShort", value="True"),
    ]

    capability_composed_of: str = Field("", json_schema_extra={"aas": {"semantic_id": "https://admin-shell.io/idta/CapabilityDescription/CapabilityComposedOf/1/0", "description": "Relationship between a composed capability as first element and one of its minimum two subordinate capabilities as second element.", "qualifiers": [{"type": "SMT/Cardinality", "value": "TwoToMany", "semantic_id": "https://admin-shell.io/SubmodelTemplates/Cardinality/1/0"}, {"type": "EditIdShort", "value": "True"}]}})
    composed_of_comment: str = Field("", json_schema_extra={"aas": {"semantic_id": "https://admin-shell.io/idta/CapabilityDescription/ComposedOfComment/1/0", "description": "Comment to describe the composition in human readable form.", "qualifiers": [{"type": "SMT/Cardinality", "value": "ZeroToOne", "semantic_id": "https://admin-shell.io/SubmodelTemplates/Cardinality/1/0"}]}})

class ComposedOfSet(SubmodelElementCollection):
    semantic_id: str = "https://admin-shell.io/idta/CapabilityDescription/ComposedOfSet/1/0"
    description: str = "If composition(s) for the Capability element in the CapabilityContainer exists, this set has to be created."
    qualifiers: List[Qualifier] = [
        Qualifier(type_="SMT/Cardinality", value="ZeroToOne", semantic_id="https://admin-shell.io/SubmodelTemplates/Cardinality/1/0"),
    ]

    composed_of_container: Optional[ComposedOfContainer] = None

class GeneralizedBySet(SubmodelElementCollection):
    semantic_id: str = "https://admin-shell.io/idta/CapabilityDescription/GeneralizedBySet/1/0"
    description: str = "If generalization(s) for the Capability element in the CapabilityContainer exists, this set has to be created."
    qualifiers: List[Qualifier] = [
        Qualifier(type_="SMT/Cardinality", value="ZeroToMany", semantic_id="https://admin-shell.io/SubmodelTemplates/Cardinality/1/0"),
        Qualifier(type_="EditIdShort", value="True"),
    ]

    capability_generalized_by: str = Field("", json_schema_extra={"aas": {"semantic_id": "https://admin-shell.io/idta/CapabilityDescription/CapabilityGeneralizedBy/1/0", "description": "Relationship between the Capability as first element, described in the CapabilityContainer, and a more general Capability as second element.", "qualifiers": [{"type": "SMT/Cardinality", "value": "OneToMany", "semantic_id": "https://admin-shell.io/SubmodelTemplates/Cardinality/1/0"}, {"type": "EditIdShort", "value": "True"}]}})

class CustomConstraint(SubmodelElementCollection):
    semantic_id: str = "https://admin-shell.io/idta/CapabilityDescription/PropertyConstraintType/CustomConstraint/1/0"
    description: str = "SubmodelElement which can be used to validate the constraint for the considered Properties in this PropertyConstraintContainer against other properties. This can be freely defined for the purpose of constraining a property and is not specified in this Submodel Template."
    qualifiers: List[Qualifier] = [
        Qualifier(type_="SMT/Cardinality", value="One", semantic_id="https://admin-shell.io/SubmodelTemplates/Cardinality/1/0"),
    ]

    pass

class ConstraintPropertyRelations(SubmodelElementCollection):
    semantic_id: str = "https://admin-shell.io/idta/CapabilityDescription/ConstraintPropertyRelations/1/0"
    description: str = "Contains all relationships for the constraint in the PropertyConstraintContainer."
    qualifiers: List[Qualifier] = [
        Qualifier(type_="SMT/Cardinality", value="One", semantic_id="https://admin-shell.io/SubmodelTemplates/Cardinality/1/0"),
    ]

    constraint_has_property: str = Field("", json_schema_extra={"aas": {"semantic_id": "https://admin-shell.io/idta/CapabilityDescription/ConstraintHasProperty/1/0", "description": "Relates the PropertyConstraint as first element to a Property from a PropertyContainer as second element.", "qualifiers": [{"type": "SMT/Cardinality", "value": "OneToMany", "semantic_id": "https://admin-shell.io/SubmodelTemplates/Cardinality/1/0"}, {"type": "EditIdShort", "value": "True"}]}})

class PropertyConstraintContainer(SubmodelElementCollection):
    semantic_id: str = "https://admin-shell.io/idta/CapabilityDescription/PropertyConstraintContainer/1/0"
    description: str = "If one or more constraints exist for a Capability Property, then for every constraint a PropertyConstraintContainer has to be created."
    qualifiers: List[Qualifier] = [
        Qualifier(type_="SMT/Cardinality", value="ZeroToMany", semantic_id="https://admin-shell.io/SubmodelTemplates/Cardinality/1/0"),
        Qualifier(type_="EditIdShort", value="True"),
    ]

    basic_constraint: str = Field("", json_schema_extra={"aas": {"semantic_id": "https://admin-shell.io/idta/CapabilityDescription/PropertyConstraintType/BasicConstraint/1/0", "description": "Property element which can be used to validate the constraint for the considered Properties in this PropertyConstraintContainer against other properties.", "qualifiers": [{"type": "SMT/Cardinality", "value": "One", "semantic_id": "https://admin-shell.io/SubmodelTemplates/Cardinality/1/0"}, {"type": "PredicateRelationTemplate", "value": "ALL"}]}})
    custom_constraint: Optional[CustomConstraint] = None
    o_c_l_constraint: str = Field("", json_schema_extra={"aas": {"semantic_id": "https://admin-shell.io/idta/CapabilityDescription/PropertyConstraintType/OCLConstraint/1/0", "description": "Object Contraint Language (OCL) as File element which can be used to validate the constraint for the considered Properties in this PropertyConstraintContainer against other properties.", "qualifiers": [{"type": "SMT/Cardinality", "value": "One", "semantic_id": "https://admin-shell.io/SubmodelTemplates/Cardinality/1/0"}]}})
    operation_constraint: str = Field("", json_schema_extra={"aas": {"semantic_id": "https://admin-shell.io/idta/CapabilityDescription/PropertyConstraintType/OperationConstraint/1/0", "description": "Reference to an (external) Operation element which can be used to validate the constraint for the considered Properties in this PropertyConstraintContainer against other properties.", "qualifiers": [{"type": "SMT/Cardinality", "value": "One", "semantic_id": "https://admin-shell.io/SubmodelTemplates/Cardinality/1/0"}]}})
    constraint_type: str = Field("", json_schema_extra={"aas": {"semantic_id": "https://admin-shell.io/idta/CapabilityDescription/ConstraintType/1/0", "description": "Abstract Enum type of allowed SubmodelElements for these Properties constraints. Exactly one of the SubmodelElements below must be instanciated, e.g., similar to SubmodelElementList with exactly one element.", "qualifiers": [{"type": "SMT/Cardinality", "value": "One", "semantic_id": "https://admin-shell.io/SubmodelTemplates/Cardinality/1/0"}, {"type": "FormChoices", "value": "OperationConstraint;OCLConstraint;BasicConstraint;CustomConstraint"}]}})
    property_conditional_type: str = Field("", json_schema_extra={"aas": {"semantic_id": "https://admin-shell.io/idta/CapabilityDescription/PropertyConditionalType/1/0", "description": "Defines the type of the property conditions as defined in the ConceptDescription with the same name (PropertyConditionalType).", "qualifiers": [{"type": "SMT/Cardinality", "value": "One", "semantic_id": "https://admin-shell.io/SubmodelTemplates/Cardinality/1/0"}]}})
    constraint_property_relations: Optional[ConstraintPropertyRelations] = None

class TransitionConstraintContainer(SubmodelElementCollection):
    semantic_id: str = "https://admin-shell.io/idta/CapabilityDescription/TransitionConstraintContainer/1/0"
    description: str = "If one or more constraints exist for a Capability, then for every transitional constraint a TransitionConstraintContainer has to be created."
    qualifiers: List[Qualifier] = [
        Qualifier(type_="SMT/Cardinality", value="ZeroToMany", semantic_id="https://admin-shell.io/SubmodelTemplates/Cardinality/1/0"),
        Qualifier(type_="EditIdShort", value="True"),
    ]

    transition_constrained_by: str = Field("", json_schema_extra={"aas": {"semantic_id": "https://admin-shell.io/idta/CapabilityDescription/TransitionConstrainedBy/1/0", "description": "Relates the constrained Capability as first element to a constraining Capability from another CapabilityContainer as second element.", "qualifiers": [{"type": "SMT/Cardinality", "value": "One", "semantic_id": "https://admin-shell.io/SubmodelTemplates/Cardinality/1/0"}]}})
    transition_conditional_type: str = Field("", json_schema_extra={"aas": {"semantic_id": "https://admin-shell.io/idta/CapabilityDescription/TransitionConditionalType/1/0", "description": "Defines the element TransitionConstrainedBy of TransitionConstraintType.", "qualifiers": [{"type": "SMT/Cardinality", "value": "One", "semantic_id": "https://admin-shell.io/SubmodelTemplates/Cardinality/1/0"}]}})

class ConstraintSet(SubmodelElementCollection):
    semantic_id: str = "https://admin-shell.io/idta/CapabilityDescription/ConstraintSet/1/0"
    description: str = "If constraint(s) for the Capability element in the CapabilityContainer exists, this set has to be created."
    qualifiers: List[Qualifier] = [
        Qualifier(type_="SMT/Cardinality", value="ZeroToMany", semantic_id="https://admin-shell.io/SubmodelTemplates/Cardinality/1/0"),
    ]

    property_constraint_container: Optional[PropertyConstraintContainer] = None
    transition_constraint_container: Optional[TransitionConstraintContainer] = None

class CapabilityRelations(SubmodelElementCollection):
    semantic_id: str = "https://admin-shell.io/idta/CapabilityDescription/CapabilityRelations/1/0"
    description: str = "Collection of relationships for the capability, if existing."
    qualifiers: List[Qualifier] = [
        Qualifier(type_="SMT/Cardinality", value="ZeroToOne", semantic_id="https://admin-shell.io/SubmodelTemplates/Cardinality/1/0"),
    ]

    capability_realized_by: str = Field("", json_schema_extra={"aas": {"semantic_id": "https://admin-shell.io/idta/CapabilityDescription/CapabilityRealizedBy/1/0", "description": "Relationship between the Capability element in the CapabilityContainer as first element and a Skill implementation, not defined in this Submodel template, as second element.", "qualifiers": [{"type": "SMT/Cardinality", "value": "ZeroToMany", "semantic_id": "https://admin-shell.io/SubmodelTemplates/Cardinality/1/0"}, {"type": "EditIdShort", "value": "True"}]}})
    composed_of_set: Optional[ComposedOfSet] = None
    generalized_by_set: Optional[GeneralizedBySet] = None
    constraint_set: Optional[ConstraintSet] = None

class CapabilityContainer(SubmodelElementCollection):
    semantic_id: str = "https://admin-shell.io/idta/CapabilityDescription/CapabilityContainer/1/0"
    description: str = "A Container for one capability and all its additional descriptive elements."
    qualifiers: List[Qualifier] = [
        Qualifier(type_="SMT/Cardinality", value="OneToMany", semantic_id="https://admin-shell.io/SubmodelTemplates/Cardinality/1/0"),
        Qualifier(type_="EditIdShort", value="True"),
    ]

    capability: Capability = Field(Capability(), json_schema_extra={"aas": {"semantic_id": "https://admin-shell.io/idta/CapabilityDescription/Capability/1/0", "description": "[A capability is a] implementation-independent specification of a function in industrial production to achieve an effect in the physical or virtual world. ", "qualifiers": [{"type": "Required", "value": "[1, 0]", "semantic_id": "https://admin-shell.io/idta/CapabilityDescription/CapabilityRoleQualifier/Required/1/0"}, {"type": "Offered", "value": "[1, 0]", "semantic_id": "https://admin-shell.io/idta/CapabilityDescription/CapabilityRoleQualifier/Offered/1/0"}, {"type": "NotAssigned", "value": "[1, 0]", "semantic_id": "https://admin-shell.io/idta/CapabilityDescription/CapabilityRoleQualifier/NotAssigned/1/0"}, {"type": "SMT/Cardinality", "value": "One", "semantic_id": "https://admin-shell.io/SubmodelTemplates/Cardinality/1/0"}, {"type": "EditIdShort", "value": "True"}]}})
    capability_comment: str = Field("", json_schema_extra={"aas": {"semantic_id": "https://admin-shell.io/idta/CapabilityDescription/CapabilityComment/1/0", "description": "Individual comment of the capability.", "qualifiers": [{"type": "SMT/Cardinality", "value": "ZeroToOne", "semantic_id": "https://admin-shell.io/SubmodelTemplates/Cardinality/1/0"}]}})
    property_set: Optional[PropertySet] = None
    capability_relations: Optional[CapabilityRelations] = None

class CapabilitySet(SubmodelElementCollection):
    semantic_id: str = "https://admin-shell.io/idta/CapabilityDescription/CapabilitySet/1/0"
    description: str = "A Set of CapabilityContainer for a Use Case for the asset."
    qualifiers: List[Qualifier] = [
        Qualifier(type_="SMT/Cardinality", value="OneToMany", semantic_id="https://admin-shell.io/SubmodelTemplates/Cardinality/1/0"),
        Qualifier(type_="EditIdShort", value="True"),
    ]

    capability_container: Optional[CapabilityContainer] = None

class CapabilityDescription(Submodel):
    semantic_id: str = "https://admin-shell.io/idta/SubmodelTemplate/CapabilityDescription/1/0"
    description: str = "Definition of the Submodel CapabilityDescription identified by its semanticId. The Submodel idShort can be picked freely."
    VERSION: ClassVar[str] = "1"
    REVISION: ClassVar[str] = "0"

    capability_set: Optional[CapabilitySet] = None
