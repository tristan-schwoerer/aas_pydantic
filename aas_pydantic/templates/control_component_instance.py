"""ControlComponentInstance — generated from IDTA template."""

from typing import ClassVar, List, Optional
from pydantic import Field
from aas_pydantic import Submodel, SubmodelElementCollection, Capability, Qualifier

class Endpoint(SubmodelElementCollection):
    semantic_id: str = "https://admin-shell.io/idta/ControlComponent/Instance/Endpoint/2/0"
    description: str = "A control endpoint supported by the instance of the component."
    qualifiers: List[Qualifier] = [
        Qualifier(type_="SMT/Cardinality", value="ZeroToMany", semantic_id="https://admin-shell.io/SubmodelTemplates/Cardinality/1/0"),
        Qualifier(type_="EditIdShort", value="True"),
        Qualifier(type_="EditDescription", value="True"),
    ]

    interface_reference: str = Field("", json_schema_extra={"aas": {"semantic_id": "https://admin-shell.io/idta/ControlComponent/Instance/Endpoint/InterfaceReference/2/0", "description": "A reference to an interface description (SMC Interface) in a Control Component Type submodel that specifies the semantics of the interface.", "qualifiers": [{"type": "SMT/Cardinality", "value": "One", "semantic_id": "https://admin-shell.io/SubmodelTemplates/Cardinality/1/0"}]}})
    endpoint_reference: str = Field("", json_schema_extra={"aas": {"semantic_id": "https://admin-shell.io/idta/ControlComponent/Instance/Endpoint/Reference/2/0", "description": "A reference to a technical control endpoint that adheres to the semantics of the referenced interface.", "qualifiers": [{"type": "SMT/Cardinality", "value": "One", "semantic_id": "https://admin-shell.io/SubmodelTemplates/Cardinality/1/0"}]}})

class Endpoints(SubmodelElementCollection):
    semantic_id: str = "https://admin-shell.io/idta/ControlComponent/Instance/Endpoints/2/0"
    description: str = "Collection of references to control endpoints supported by the instance of the component"
    qualifiers: List[Qualifier] = [
        Qualifier(type_="SMT/Cardinality", value="One", semantic_id="https://admin-shell.io/SubmodelTemplates/Cardinality/1/0"),
    ]

    endpoint: Optional[Endpoint] = None

class Modes(SubmodelElementCollection):
    semantic_id: str = "https://admin-shell.io/idta/ControlComponent/Skill/Modes/2/0"
    description: str = "Collection of operation, operating, operational or execution modes (depending on the standard), in which the skill is available/allowed to execute."
    qualifiers: List[Qualifier] = [
        Qualifier(type_="SMT/Cardinality", value="One", semantic_id="https://admin-shell.io/SubmodelTemplates/Cardinality/1/0"),
    ]

    mode__00__: str = Field("", json_schema_extra={"aas": {"semantic_id": "https://admin-shell.io/idta/ControlComponent/Skill/Mode/2/0", "description": "Name of the operation, operating, operational or execution modes (depending on the standard), in which the skill is available/allowed to execute.", "qualifiers": [{"type": "PresetIdShort", "value": "To be filled; normally same as idShort, might be with {00}"}, {"type": "SMT/Cardinality", "value": "OneToMany", "semantic_id": "https://admin-shell.io/SubmodelTemplates/Cardinality/1/0"}]}})

class Values(SubmodelElementCollection):
    semantic_id: str = "https://admin-shell.io/idta/ControlComponent/Skill/Parameter/Values/2/0"
    description: str = "Collection of properties of the accepted values that the parameter may take."
    qualifiers: List[Qualifier] = [
        Qualifier(type_="SMT/Cardinality", value="One", semantic_id="https://admin-shell.io/SubmodelTemplates/Cardinality/1/0"),
    ]

    pass

class Parameter(SubmodelElementCollection):
    semantic_id: str = "https://admin-shell.io/idta/ControlComponent/Skill/Parameter/2/0"
    description: str = "Parameter used for the configuration of the skill."
    qualifiers: List[Qualifier] = [
        Qualifier(type_="SMT/Cardinality", value="ZeroToMany", semantic_id="https://admin-shell.io/SubmodelTemplates/Cardinality/1/0"),
        Qualifier(type_="EditIdShort", value="True"),
        Qualifier(type_="EditDescription", value="True"),
        Qualifier(type_="PresetIdShort", value="To be filled; normally same as idShort, might be with {00}"),
    ]

    direction: str = Field("", json_schema_extra={"aas": {"semantic_id": "https://admin-shell.io/idta/ControlComponent/Skill/Parameter/Direction/2/0", "description": "Indicates whether the parameter is an input (In) or an output (Out) of the skill. An InOut parameter can be set from outside and can also be changed from skill itself. ", "qualifiers": [{"type": "SMT/Cardinality", "value": "One", "semantic_id": "https://admin-shell.io/SubmodelTemplates/Cardinality/1/0"}, {"type": "FormChoices", "value": "In;Out;InOut"}]}})
    type: str = Field("", json_schema_extra={"aas": {"semantic_id": "https://admin-shell.io/idta/ControlComponent/Skill/Parameter/Type/2/0", "description": "Data type as string used to interpret the parameter. ", "qualifiers": [{"type": "SMT/Cardinality", "value": "One", "semantic_id": "https://admin-shell.io/SubmodelTemplates/Cardinality/1/0"}]}})
    values: Optional[Values] = None

class Parameters(SubmodelElementCollection):
    semantic_id: str = "https://admin-shell.io/idta/ControlComponent/Skill/Parameters/2/0"
    description: str = "Collection of parameters used for the configuration of the skill."
    qualifiers: List[Qualifier] = [
        Qualifier(type_="SMT/Cardinality", value="One", semantic_id="https://admin-shell.io/SubmodelTemplates/Cardinality/1/0"),
    ]

    parameter: Optional[Parameter] = None

class Errors(SubmodelElementCollection):
    semantic_id: str = "https://admin-shell.io/idta/ControlComponent/Skill/Errors/2/0"
    description: str = "Collection of references to the error codes of the component that may be raised by this skill."
    qualifiers: List[Qualifier] = [
        Qualifier(type_="SMT/Cardinality", value="One", semantic_id="https://admin-shell.io/SubmodelTemplates/Cardinality/1/0"),
    ]

    error_reference__00__: str = Field("", json_schema_extra={"aas": {"semantic_id": "https://admin-shell.io/idta/ControlComponent/Skill/ErrorReference/2/0", "qualifiers": [{"type": "SMT/Cardinality", "value": "ZeroToMany", "semantic_id": "https://admin-shell.io/SubmodelTemplates/Cardinality/1/0"}, {"type": "EditIdShort", "value": "True"}, {"type": "EditDescription", "value": "True"}, {"type": "PresetIdShort", "value": "To be filled; normally same as idShort, might be with {00}"}]}})

class Uses(SubmodelElementCollection):
    semantic_id: str = "https://admin-shell.io/idta/ControlComponent/Skill/Uses/2/0"
    description: str = "Collection of references to other skills, that this skill uses."
    qualifiers: List[Qualifier] = [
        Qualifier(type_="SMT/Cardinality", value="One", semantic_id="https://admin-shell.io/SubmodelTemplates/Cardinality/1/0"),
    ]

    skill_reference__00__: str = Field("", json_schema_extra={"aas": {"semantic_id": "https://admin-shell.io/idta/ControlComponent/Skill/SkillReference/2/0", "qualifiers": [{"type": "SMT/Cardinality", "value": "ZeroToMany", "semantic_id": "https://admin-shell.io/SubmodelTemplates/Cardinality/1/0"}, {"type": "EditIdShort", "value": "True"}, {"type": "EditDescription", "value": "True"}, {"type": "PresetIdShort", "value": "To be filled; normally same as idShort, might be with {00}"}]}})

class Skill(SubmodelElementCollection):
    semantic_id: str = "https://admin-shell.io/idta/ControlComponent/Skill/2/0"
    description: str = "Contains the basic information to call (request the execution of) a skill, e.g. its signature"
    qualifiers: List[Qualifier] = [
        Qualifier(type_="SMT/Cardinality", value="ZeroToMany", semantic_id="https://admin-shell.io/SubmodelTemplates/Cardinality/1/0"),
        Qualifier(type_="EditIdShort", value="True"),
        Qualifier(type_="EditDescription", value="True"),
        Qualifier(type_="PresetIdShort", value="To be filled; normally same as idShort, might be with {00}"),
    ]

    disabled: str = Field("", json_schema_extra={"aas": {"semantic_id": "https://admin-shell.io/idta/ControlComponent/Skill/Disabled/2/0", "description": "Boolean property that defines if the skill is (currently) disabled, e.g. not licensed, tested, suitable.", "qualifiers": [{"type": "SMT/Cardinality", "value": "One", "semantic_id": "https://admin-shell.io/SubmodelTemplates/Cardinality/1/0"}, {"type": "FormChoices", "value": "true;false"}]}})
    modes: Optional[Modes] = None
    parameters: Optional[Parameters] = None
    errors: Optional[Errors] = None
    uses: Optional[Uses] = None

class Skills(SubmodelElementCollection):
    semantic_id: str = "https://admin-shell.io/idta/ControlComponent/Skills/2/0"
    description: str = "Collection of skills offered by the component instance"
    qualifiers: List[Qualifier] = [
        Qualifier(type_="SMT/Cardinality", value="One", semantic_id="https://admin-shell.io/SubmodelTemplates/Cardinality/1/0"),
    ]

    skill: Optional[Skill] = None

class ControlComponentInstance(Submodel):
    semantic_id: str = "https://admin-shell.io/idta/ControlComponent/Instance/2/0"
    description: str = "A ControlComponentInstance Submodel."
    qualifiers: List[Qualifier] = [
        Qualifier(type_="FormTitle", value="ControlComponentInstance V2 (IDTA 02016-2-0)"),
        Qualifier(type_="FormTag", value="CCI"),
        Qualifier(type_="FormInfo", value="ControlComponentInstance"),
        Qualifier(type_="FormUrl", value="https://github.com/admin-shell-io/submodel-templates/tree/main/published/Control%20Component%20Instance/2/0"),
    ]
    VERSION: ClassVar[str] = "2"
    REVISION: ClassVar[str] = "0"

    endpoints: Optional[Endpoints] = None
    skills: Optional[Skills] = None
    type: str = Field("", json_schema_extra={"aas": {"semantic_id": "https://admin-shell.io/idta/ControlComponent/Instance/Type/2/0", "description": "Reference between the component instance and its respective ControlComponentType Submodel.", "qualifiers": [{"type": "SMT/Cardinality", "value": "One", "semantic_id": "https://admin-shell.io/SubmodelTemplates/Cardinality/1/0"}]}})
