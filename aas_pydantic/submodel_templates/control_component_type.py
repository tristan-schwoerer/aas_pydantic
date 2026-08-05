"""ControlComponentType — generated from IDTA template."""

from __future__ import annotations

from typing import Any, ClassVar, List, Dict
from aas_pydantic import (
    ContainerValue, Property, ReferenceElement, Submodel, SubmodelElement, SubmodelElementCollection, SubmodelElementList,
)

class InterfaceValues(ContainerValue):
    model_config = {'extra': 'forbid'}
    interface_profile: Property = Property(
        semantic_id="https://admin-shell.io/idta/ControlComponent/Type/Interface/Profile/2/0",
        description="The profile according to which the referred control interface operates.",
        value_type="xs:string",
    )
    interface_profile_supplement: Property = Property(
        semantic_id="https://admin-shell.io/idta/ControlComponent/Type/Interface/ProfileSupplement/2/0",
        description="Supplemental information to further specify the interface.",
        value_type="xs:string",
    )
    interface_reference: ReferenceElement = ReferenceElement(
        semantic_id="https://admin-shell.io/idta/ControlComponent/Type/Interface/Reference/2/0",
        description="A reference to a control interface supported by the component type and described by the interfaceProfile and the optional supplement",
    )

class Interface(SubmodelElementCollection):
    semantic_id: str = "https://admin-shell.io/idta/ControlComponent/Type/Interface/2/0"
    description: str = "An interface description"
    value: InterfaceValues = InterfaceValues()

class InterfacesValues(ContainerValue):
    model_config = {'extra': 'forbid'}
    interface: Dict[str, Interface] = {}

class Interfaces(SubmodelElementCollection):
    semantic_id: str = "https://admin-shell.io/idta/ControlComponent/Type/Interfaces/2/0"
    description: str = "Collection of references to control interfaces supported by the component type, e.g. to elements of the Interface Metadata SMC of the Asset Interface Description submodel, the MTP submodel or OPC UA Server Datasheet submodel."
    value: InterfacesValues = InterfacesValues()

class ErrorValues(ContainerValue):
    model_config = {'extra': 'forbid'}
    error_code: Property = Property(
        semantic_id="https://admin-shell.io/idta/ControlComponent/Type/Error/Code/2/0",
        description="The error code.",
        value_type="xs:string",
    )

class Error(SubmodelElementCollection):
    semantic_id: str = "https://admin-shell.io/idta/ControlComponent/Type/Error/2/0"
    description: str = "A container representing an error."
    value: ErrorValues = ErrorValues()

class ErrorsValues(ContainerValue):
    model_config = {'extra': 'forbid'}
    error: Dict[str, Error] = {}

class Errors(SubmodelElementCollection):
    semantic_id: str = "https://admin-shell.io/idta/ControlComponent/Type/Errors/2/0"
    description: str = "Collection of all possible error codes that may appear in components of this type."
    value: ErrorsValues = ErrorsValues()

class Mode(Property):
    semantic_id: str = "https://admin-shell.io/idta/ControlComponent/Skill/Mode/2/0"
    description: str = "Name of the operation, operating, operational or execution modes (depending on the standard), in which the skill is available/allowed to execute."

class ModesValues(ContainerValue):
    model_config = {'extra': 'forbid'}
    mode: Dict[str, Mode] = {}

class Modes(SubmodelElementCollection):
    semantic_id: str = "https://admin-shell.io/idta/ControlComponent/Skill/Modes/2/0"
    description: str = "Collection of operation, operating, operational or execution modes (depending on the standard), in which the skill is available/allowed to execute."
    value: ModesValues = ModesValues()

class ValuesValues(ContainerValue):
    model_config = {'extra': 'forbid'}
    pass

class Values(SubmodelElementCollection):
    semantic_id: str = "https://admin-shell.io/idta/ControlComponent/Skill/Parameter/Values/2/0"
    description: str = "Collection of properties of the accepted values that the parameter may take."
    value: ValuesValues = ValuesValues()

class ParameterValues(ContainerValue):
    model_config = {'extra': 'forbid'}
    direction: Property = Property(
        semantic_id="https://admin-shell.io/idta/ControlComponent/Skill/Parameter/Direction/2/0",
        description="Indicates whether the parameter is an input (In) or an output (Out) of the skill. An InOut parameter can be set from outside and can also be changed from skill itself. ",
        value_type="xs:string",
    )
    type: Property = Property(
        semantic_id="https://admin-shell.io/idta/ControlComponent/Skill/Parameter/Type/2/0",
        description="Data type as string used to interpret the parameter. ",
        value_type="xs:string",
    )
    values: Values = Values()

class Parameter(SubmodelElementCollection):
    semantic_id: str = "https://admin-shell.io/idta/ControlComponent/Skill/Parameter/2/0"
    description: str = "Parameter used for the configuration of the skill."
    value: ParameterValues = ParameterValues()

class ParametersValues(ContainerValue):
    model_config = {'extra': 'forbid'}
    parameter: Dict[str, Parameter] = {}

class Parameters(SubmodelElementCollection):
    semantic_id: str = "https://admin-shell.io/idta/ControlComponent/Skill/Parameters/2/0"
    description: str = "Collection of parameters used for the configuration of the skill."
    value: ParametersValues = ParametersValues()

class ErrorReference(ReferenceElement):
    semantic_id: str = "https://admin-shell.io/idta/ControlComponent/Skill/ErrorReference/2/0"
    description: str = "A reference to an SMC \u201cError\u201d (Table 5) that that can be "

class SkillReference(ReferenceElement):
    semantic_id: str = "https://admin-shell.io/idta/ControlComponent/Skill/SkillReference/2/0"
    description: str = "A reference to an SMC \u201cSkill\u201d (Table 7) of this or another "

class UsesValues(ContainerValue):
    model_config = {'extra': 'forbid'}
    skill_reference: Dict[str, SkillReference] = {}

class Uses(SubmodelElementCollection):
    semantic_id: str = "https://admin-shell.io/idta/ControlComponent/Skill/Uses/2/0"
    description: str = "Collection of references to other skills, that this skill uses."
    value: UsesValues = UsesValues()

class SkillValues(ContainerValue):
    model_config = {'extra': 'forbid'}
    disabled: Property = Property(
        semantic_id="https://admin-shell.io/idta/ControlComponent/Skill/Disabled/2/0",
        description="Boolean property that defines if the skill is (currently) disabled, e.g. not licensed, tested, suitable.",
        value_type="xs:boolean",
    )
    modes: Modes = Modes()
    parameters: Parameters = Parameters()
    errors: Errors = Errors()
    uses: Uses = Uses()

class Skill(SubmodelElementCollection):
    semantic_id: str = "https://admin-shell.io/idta/ControlComponent/Skill/2/0"
    description: str = "Contains the basic information to call (request the execution of) a skill, e.g. its signature"
    value: SkillValues = SkillValues()

class SkillsValues(ContainerValue):
    model_config = {'extra': 'forbid'}
    skill: Dict[str, Skill] = {}

class Skills(SubmodelElementCollection):
    semantic_id: str = "https://admin-shell.io/idta/ControlComponent/Skills/2/0"
    description: str = "Collection of skills offered by the component type"
    value: SkillsValues = SkillsValues()

class ControlComponentTypeValues(ContainerValue):
    model_config = {'extra': 'forbid'}
    interfaces: Interfaces = Interfaces()
    errors: Errors = Errors()
    skills: Skills = Skills()

class ControlComponentType(Submodel):
    semantic_id: str = "https://admin-shell.io/idta/ControlComponent/Type/2/0"
    VERSION: ClassVar[str] = "2"
    REVISION: ClassVar[str] = "0"
    submodel_element: ControlComponentTypeValues = ControlComponentTypeValues()

# ── Resolve forward references (Pydantic circular refs) ──
InterfaceValues.model_rebuild()
Interface.model_rebuild()
InterfacesValues.model_rebuild()
Interfaces.model_rebuild()
ErrorValues.model_rebuild()
Error.model_rebuild()
ErrorsValues.model_rebuild()
Errors.model_rebuild()
Mode.model_rebuild()
ModesValues.model_rebuild()
Modes.model_rebuild()
ValuesValues.model_rebuild()
Values.model_rebuild()
ParameterValues.model_rebuild()
Parameter.model_rebuild()
ParametersValues.model_rebuild()
Parameters.model_rebuild()
ErrorReference.model_rebuild()
SkillReference.model_rebuild()
UsesValues.model_rebuild()
Uses.model_rebuild()
SkillValues.model_rebuild()
Skill.model_rebuild()
SkillsValues.model_rebuild()
Skills.model_rebuild()
ControlComponentTypeValues.model_rebuild()
ControlComponentType.model_rebuild()
