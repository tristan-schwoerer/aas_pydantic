"""ControlComponentInstance — generated from IDTA template."""

from __future__ import annotations

from typing import Any, ClassVar, List, Dict
from aas_pydantic import (
    ContainerValue, Property, ReferenceElement, Submodel, SubmodelElement, SubmodelElementCollection, SubmodelElementList,
)

class EndpointValues(ContainerValue):
    model_config = {'extra': 'forbid'}
    interface_reference: ReferenceElement = ReferenceElement(
        semantic_id="https://admin-shell.io/idta/ControlComponent/Instance/Endpoint/InterfaceReference/2/0",
        description="A reference to an interface description (SMC Interface) in a Control Component Type submodel that specifies the semantics of the interface.",
    )
    endpoint_reference: ReferenceElement = ReferenceElement(
        semantic_id="https://admin-shell.io/idta/ControlComponent/Instance/Endpoint/Reference/2/0",
        description="A reference to a technical control endpoint that adheres to the semantics of the referenced interface.",
    )

class Endpoint(SubmodelElementCollection):
    semantic_id: str = "https://admin-shell.io/idta/ControlComponent/Instance/Endpoint/2/0"
    description: str = "A control endpoint supported by the instance of the component."
    value: EndpointValues = EndpointValues()

class EndpointsValues(ContainerValue):
    model_config = {'extra': 'forbid'}
    endpoint: Dict[str, Endpoint] = {}

class Endpoints(SubmodelElementCollection):
    semantic_id: str = "https://admin-shell.io/idta/ControlComponent/Instance/Endpoints/2/0"
    description: str = "Collection of references to control endpoints supported by the instance of the component"
    value: EndpointsValues = EndpointsValues()

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

class ErrorsValues(ContainerValue):
    model_config = {'extra': 'forbid'}
    error_reference: Dict[str, ErrorReference] = {}

class Errors(SubmodelElementCollection):
    semantic_id: str = "https://admin-shell.io/idta/ControlComponent/Skill/Errors/2/0"
    description: str = "Collection of references to the error codes of the component that may be raised by this skill."
    value: ErrorsValues = ErrorsValues()

class SkillReference(ReferenceElement):
    semantic_id: str = "https://admin-shell.io/idta/ControlComponent/Skill/SkillReference/2/0"

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
    description: str = "Collection of skills offered by the component instance"
    value: SkillsValues = SkillsValues()

class ControlComponentInstanceValues(ContainerValue):
    model_config = {'extra': 'forbid'}
    endpoints: Endpoints = Endpoints()
    skills: Skills = Skills()
    type: ReferenceElement = ReferenceElement(
        semantic_id="https://admin-shell.io/idta/ControlComponent/Instance/Type/2/0",
        description="Reference between the component instance and its respective ControlComponentType Submodel.",
    )

class ControlComponentInstance(Submodel):
    semantic_id: str = "https://admin-shell.io/idta/ControlComponent/Instance/2/0"
    description: str = "A ControlComponentInstance Submodel."
    VERSION: ClassVar[str] = "2"
    REVISION: ClassVar[str] = "0"
    submodel_element: ControlComponentInstanceValues = ControlComponentInstanceValues()

# ── Resolve forward references (Pydantic circular refs) ──
EndpointValues.model_rebuild()
Endpoint.model_rebuild()
EndpointsValues.model_rebuild()
Endpoints.model_rebuild()
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
ErrorsValues.model_rebuild()
Errors.model_rebuild()
SkillReference.model_rebuild()
UsesValues.model_rebuild()
Uses.model_rebuild()
SkillValues.model_rebuild()
Skill.model_rebuild()
SkillsValues.model_rebuild()
Skills.model_rebuild()
ControlComponentInstanceValues.model_rebuild()
ControlComponentInstance.model_rebuild()
