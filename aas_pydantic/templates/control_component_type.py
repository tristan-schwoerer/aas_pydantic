"""ControlComponentType — generated from IDTA template."""

from typing import ClassVar, List, Optional
from pydantic import Field
from aas_pydantic import Submodel, SubmodelElementCollection, Capability, Qualifier

class Interface(SubmodelElementCollection):
    semantic_id: str = "https://admin-shell.io/idta/ControlComponent/Type/Interface/2/0"
    description: str = "An interface description"
    qualifiers: List[Qualifier] = [
        Qualifier(type_="SMT/SMT/Cardinality", value="ZeroToMany", semantic_id="https://admin-shell.io/SubmodelTemplates/SMT/SMT/Cardinality/1/0"),
        Qualifier(type_="EditIdShort", value="True"),
        Qualifier(type_="EditDescription", value="True"),
    ]

    interface_profile: str = Field("", json_schema_extra={"aas": {"semantic_id": "https://admin-shell.io/idta/ControlComponent/Type/Interface/Profile/2/0", "description": "The profile according to which the referred control interface operates.", "qualifiers": [{"type": "SMT/SMT/Cardinality", "value": "One", "semantic_id": "https://admin-shell.io/SubmodelTemplates/SMT/SMT/Cardinality/1/0"}]}})
    interface_profile_supplement: str = Field("", json_schema_extra={"aas": {"semantic_id": "https://admin-shell.io/idta/ControlComponent/Type/Interface/ProfileSupplement/2/0", "description": "Supplemental information to further specify the interface.", "qualifiers": [{"type": "SMT/SMT/Cardinality", "value": "ZeroToOne", "semantic_id": "https://admin-shell.io/SubmodelTemplates/SMT/SMT/Cardinality/1/0"}]}})
    interface_reference: str = Field("", json_schema_extra={"aas": {"semantic_id": "https://admin-shell.io/idta/ControlComponent/Type/Interface/Reference/2/0", "description": "A reference to a control interface supported by the component type and described by the interfaceProfile and the optional supplement", "qualifiers": [{"type": "SMT/SMT/Cardinality", "value": "ZeroToOne", "semantic_id": "https://admin-shell.io/SubmodelTemplates/SMT/SMT/Cardinality/1/0"}]}})

class Interfaces(SubmodelElementCollection):
    semantic_id: str = "https://admin-shell.io/idta/ControlComponent/Type/Interfaces/2/0"
    description: str = "Collection of references to control interfaces supported by the component type, e.g. to elements of the Interface Metadata SMC of the Asset Interface Description submodel, the MTP submodel or OPC UA Server Datasheet submodel."
    qualifiers: List[Qualifier] = [
        Qualifier(type_="SMT/SMT/Cardinality", value="One", semantic_id="https://admin-shell.io/SubmodelTemplates/SMT/SMT/Cardinality/1/0"),
    ]

    interface: Optional[Interface] = None

class Error(SubmodelElementCollection):
    semantic_id: str = "https://admin-shell.io/idta/ControlComponent/Type/Error/2/0"
    description: str = "A container representing an error."
    qualifiers: List[Qualifier] = [
        Qualifier(type_="SMT/SMT/Cardinality", value="ZeroToMany", semantic_id="https://admin-shell.io/SubmodelTemplates/SMT/SMT/Cardinality/1/0"),
        Qualifier(type_="EditIdShort", value="True"),
        Qualifier(type_="EditDescription", value="True"),
        Qualifier(type_="PresetIdShort", value="To be filled; normally same as idShort, might be with {00}"),
    ]

    error_code: str = Field("", json_schema_extra={"aas": {"semantic_id": "https://admin-shell.io/idta/ControlComponent/Type/Error/Code/2/0", "description": "The error code.", "qualifiers": [{"type": "SMT/SMT/Cardinality", "value": "One", "semantic_id": "https://admin-shell.io/SubmodelTemplates/SMT/SMT/Cardinality/1/0"}]}})

class Errors(SubmodelElementCollection):
    semantic_id: str = "https://admin-shell.io/idta/ControlComponent/Skill/Errors/2/0"
    description: str = "Collection of references to the error codes of the component that may be raised by this skill."
    qualifiers: List[Qualifier] = [
        Qualifier(type_="SMT/SMT/Cardinality", value="One", semantic_id="https://admin-shell.io/SubmodelTemplates/SMT/SMT/Cardinality/1/0"),
    ]

    error_reference__00__: str = Field("", json_schema_extra={"aas": {"semantic_id": "https://admin-shell.io/idta/ControlComponent/Skill/ErrorReference/2/0", "description": "A reference to an SMC \u201cError\u201d (Table 5) that that can be ", "qualifiers": [{"type": "SMT/SMT/Cardinality", "value": "ZeroToMany", "semantic_id": "https://admin-shell.io/SubmodelTemplates/SMT/SMT/Cardinality/1/0"}, {"type": "EditIdShort", "value": "True"}, {"type": "EditDescription", "value": "True"}, {"type": "PresetIdShort", "value": "To be filled; normally same as idShort, might be with {00}"}]}})

class Modes(SubmodelElementCollection):
    semantic_id: str = "https://admin-shell.io/idta/ControlComponent/Skill/Modes/2/0"
    description: str = "Collection of operation, operating, operational or execution modes (depending on the standard), in which the skill is available/allowed to execute."
    qualifiers: List[Qualifier] = [
        Qualifier(type_="SMT/SMT/Cardinality", value="One", semantic_id="https://admin-shell.io/SubmodelTemplates/SMT/SMT/Cardinality/1/0"),
    ]

    mode__00__: str = Field("", json_schema_extra={"aas": {"semantic_id": "https://admin-shell.io/idta/ControlComponent/Skill/Mode/2/0", "description": "Name of the operation, operating, operational or execution modes (depending on the standard), in which the skill is available/allowed to execute.", "qualifiers": [{"type": "PresetIdShort", "value": "To be filled; normally same as idShort, might be with {00}"}, {"type": "SMT/SMT/Cardinality", "value": "OneToMany", "semantic_id": "https://admin-shell.io/SubmodelTemplates/SMT/SMT/Cardinality/1/0"}]}})

class Values(SubmodelElementCollection):
    semantic_id: str = "https://admin-shell.io/idta/ControlComponent/Skill/Parameter/Values/2/0"
    description: str = "Collection of properties of the accepted values that the parameter may take."
    qualifiers: List[Qualifier] = [
        Qualifier(type_="SMT/SMT/Cardinality", value="One", semantic_id="https://admin-shell.io/SubmodelTemplates/SMT/SMT/Cardinality/1/0"),
    ]

    pass

class Parameter(SubmodelElementCollection):
    semantic_id: str = "https://admin-shell.io/idta/ControlComponent/Skill/Parameter/2/0"
    description: str = "Parameter used for the configuration of the skill."
    qualifiers: List[Qualifier] = [
        Qualifier(type_="SMT/SMT/Cardinality", value="ZeroToMany", semantic_id="https://admin-shell.io/SubmodelTemplates/SMT/SMT/Cardinality/1/0"),
        Qualifier(type_="EditIdShort", value="True"),
        Qualifier(type_="EditDescription", value="True"),
        Qualifier(type_="PresetIdShort", value="To be filled; normally same as idShort, might be with {00}"),
    ]

    direction: str = Field("", json_schema_extra={"aas": {"semantic_id": "https://admin-shell.io/idta/ControlComponent/Skill/Parameter/Direction/2/0", "description": "Indicates whether the parameter is an input (In) or an output (Out) of the skill. An InOut parameter can be set from outside and can also be changed from skill itself. ", "qualifiers": [{"type": "SMT/SMT/Cardinality", "value": "One", "semantic_id": "https://admin-shell.io/SubmodelTemplates/SMT/SMT/Cardinality/1/0"}, {"type": "FormChoices", "value": "In;Out;InOut"}]}})
    type: str = Field("", json_schema_extra={"aas": {"semantic_id": "https://admin-shell.io/idta/ControlComponent/Skill/Parameter/Type/2/0", "description": "Data type as string used to interpret the parameter. ", "qualifiers": [{"type": "SMT/SMT/Cardinality", "value": "One", "semantic_id": "https://admin-shell.io/SubmodelTemplates/SMT/SMT/Cardinality/1/0"}]}})
    values: Optional[Values] = None

class Parameters(SubmodelElementCollection):
    semantic_id: str = "https://admin-shell.io/idta/ControlComponent/Skill/Parameters/2/0"
    description: str = "Collection of parameters used for the configuration of the skill."
    qualifiers: List[Qualifier] = [
        Qualifier(type_="SMT/SMT/Cardinality", value="One", semantic_id="https://admin-shell.io/SubmodelTemplates/SMT/SMT/Cardinality/1/0"),
    ]

    parameter: Optional[Parameter] = None

class Uses(SubmodelElementCollection):
    semantic_id: str = "https://admin-shell.io/idta/ControlComponent/Skill/Uses/2/0"
    description: str = "Collection of references to other skills, that this skill uses."
    qualifiers: List[Qualifier] = [
        Qualifier(type_="SMT/SMT/Cardinality", value="One", semantic_id="https://admin-shell.io/SubmodelTemplates/SMT/SMT/Cardinality/1/0"),
    ]

    skill_reference__00__: str = Field("", json_schema_extra={"aas": {"semantic_id": "https://admin-shell.io/idta/ControlComponent/Skill/SkillReference/2/0", "description": "A reference to an SMC \u201cSkill\u201d (Table 7) of this or another ", "qualifiers": [{"type": "SMT/SMT/Cardinality", "value": "ZeroToMany", "semantic_id": "https://admin-shell.io/SubmodelTemplates/SMT/SMT/Cardinality/1/0"}, {"type": "EditIdShort", "value": "True"}, {"type": "EditDescription", "value": "True"}, {"type": "PresetIdShort", "value": "To be filled; normally same as idShort, might be with {00}"}]}})

class Skill(SubmodelElementCollection):
    semantic_id: str = "https://admin-shell.io/idta/ControlComponent/Skill/2/0"
    description: str = "Contains the basic information to call (request the execution of) a skill, e.g. its signature"
    qualifiers: List[Qualifier] = [
        Qualifier(type_="SMT/SMT/Cardinality", value="ZeroToMany", semantic_id="https://admin-shell.io/SubmodelTemplates/SMT/SMT/Cardinality/1/0"),
        Qualifier(type_="EditIdShort", value="True"),
        Qualifier(type_="EditDescription", value="True"),
        Qualifier(type_="PresetIdShort", value="To be filled; normally same as idShort, might be with {00}"),
    ]

    disabled: str = Field("", json_schema_extra={"aas": {"semantic_id": "https://admin-shell.io/idta/ControlComponent/Skill/Disabled/2/0", "description": "Boolean property that defines if the skill is (currently) disabled, e.g. not licensed, tested, suitable.", "qualifiers": [{"type": "SMT/SMT/Cardinality", "value": "One", "semantic_id": "https://admin-shell.io/SubmodelTemplates/SMT/SMT/Cardinality/1/0"}, {"type": "FormChoices", "value": "true;false"}]}})
    modes: Optional[Modes] = None
    parameters: Optional[Parameters] = None
    errors: Optional[Errors] = None
    uses: Optional[Uses] = None

class Skills(SubmodelElementCollection):
    semantic_id: str = "https://admin-shell.io/idta/ControlComponent/Skills/2/0"
    description: str = "Collection of skills offered by the component type"
    qualifiers: List[Qualifier] = [
        Qualifier(type_="SMT/SMT/Cardinality", value="One", semantic_id="https://admin-shell.io/SubmodelTemplates/SMT/SMT/Cardinality/1/0"),
    ]

    skill: Optional[Skill] = None

class ControlComponentType(Submodel):
    semantic_id: str = "https://admin-shell.io/idta/ControlComponent/Type/2/0"
    qualifiers: List[Qualifier] = [
        Qualifier(type_="FormTitle", value="ControlComponentType V2 (IDTA 02015-2-0)"),
        Qualifier(type_="FormTag", value="CCT"),
        Qualifier(type_="FormInfo", value="ControlComponentType"),
        Qualifier(type_="FormUrl", value="https://github.com/admin-shell-io/submodel-templates/tree/main/published/Control%20Component%20Type/2/0"),
    ]
    VERSION: ClassVar[str] = "2"
    REVISION: ClassVar[str] = "0"

    interfaces: Optional[Interfaces] = None
    errors: Optional[Errors] = None
    skills: Optional[Skills] = None
