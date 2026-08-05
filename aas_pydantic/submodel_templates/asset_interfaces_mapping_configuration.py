"""AssetInterfacesMappingConfiguration — generated from IDTA template."""

from __future__ import annotations

from typing import Any, ClassVar, List
from aas_pydantic import (
    Blob, ContainerValue, Property, ReferenceElement, Submodel, SubmodelElement, SubmodelElementCollection, SubmodelElementList,
)

class SourceValues(ContainerValue):
    model_config = {'extra': 'forbid'}
    source: ReferenceElement = ReferenceElement(
        semantic_id="https://admin-shell.io/idta/AssetInterfacesMappingConfiguration/2/0/MappingConfiguration/Source/Source",
        description="This holds a reference to the respective SubmodelElement used as data source. A data source can be any SubmodelElement including those defined in the InteractionMetadata of AID Submodels for fetching live-data from assets.",
    )
    polling_interval: Property = Property(
        semantic_id="https://admin-shell.io/idta/AssetInterfacesMappingConfiguration/2/0/MappingConfiguration/Source/PollingInterval",
        description="The PollingInterval defines the time interval in seconds for fetching new data from the given synchronous data source. It must be greater than zero for synchronous protocols (e.g. HTTP) that need polling and is ignored for asynchronous protocols (e.g. MQTT). It overwrites the DefaultPollingInterval of the respective MappingConfiguration of this source.",
        value_type="xs:double",
    )
    source_id: Property = Property(
        semantic_id="https://admin-shell.io/idta/AssetInterfacesMappingConfiguration/2/0/MappingConfiguration/Source/SourceId",
        description="This is a unique and non-empty identifier that facilitates data access in the Lua transformation or establishes a relationship to a corresponding sink when no transformation is given. It must only be unique with respect to the Sources-list of the parent MappingConfiguration and not globally.",
        value_type="xs:string",
    )

class Source(SubmodelElementCollection):
    semantic_id: str = "https://admin-shell.io/idta/AssetInterfacesMappingConfiguration/2/0/MappingConfiguration/Source"
    description: str = "A data source is defined by a Source reference, PollingInterval and SourceId."
    value: SourceValues = SourceValues()

class Sources(SubmodelElementList):
    semantic_id: str = "https://admin-shell.io/idta/AssetInterfacesMappingConfiguration/2/0/MappingConfiguration/Sources"
    description: str = "This list includes all data sources that are used in this MappingConfiguration."
    item_type: ClassVar = Source
    value: List[Source] = [
        Source(id_short="Source"),
    ]

class SinkValues(ContainerValue):
    model_config = {'extra': 'forbid'}
    sink: ReferenceElement = ReferenceElement(
        semantic_id="https://admin-shell.io/idta/AssetInterfacesMappingConfiguration/2/0/MappingConfiguration/Sink/Sink",
        description="This holds a reference to the respective SubmodelElement used as data sink for live-data.",
    )
    sink_id: Property = Property(
        semantic_id="https://admin-shell.io/idta/AssetInterfacesMappingConfiguration/2/0/MappingConfiguration/Sink/SinkId",
        description="This is a unique and non-empty identifier that facilitates data writing in the Lua transformation or establishes a relationship to a corresponding source when no transformation is given. It must only be unique with respect to the Sinks-list of the containing MappingConfiguration and not globally.",
        value_type="xs:string",
    )

class Sink(SubmodelElementCollection):
    semantic_id: str = "https://admin-shell.io/idta/AssetInterfacesMappingConfiguration/2/0/MappingConfiguration/Sink"
    description: str = "A data sink is defined by a Sink reference and SinkId."
    value: SinkValues = SinkValues()

class Sinks(SubmodelElementList):
    semantic_id: str = "https://admin-shell.io/idta/AssetInterfacesMappingConfiguration/2/0/MappingConfiguration/Sinks"
    description: str = "This list includes all data sinks that are used in this MappingConfiguration."
    item_type: ClassVar = Sink
    value: List[Sink] = [
        Sink(id_short="Sink"),
    ]

class MappingConfigurationValues(ContainerValue):
    model_config = {'extra': 'forbid'}
    default_polling_interval: Property = Property(
        semantic_id="https://admin-shell.io/idta/AssetInterfacesMappingConfiguration/2/0/MappingConfiguration/DefaultPollingInterval",
        description="The DefaultPollingInterval defines the default time interval in seconds for fetching new data from the synchronous data sources defined in this MappingConfiguration. It must be greater than zero for synchronous protocols (e.g. HTTP) that need polling and is ignored for asynchronous protocols (e.g. MQTT).",
        value_type="xs:double",
    )
    transformation: Blob = Blob(
        semantic_id="https://admin-shell.io/idta/AssetInterfacesMappingConfiguration/2/0/MappingConfiguration/Transformation",
        description="The transformation allows for transforming incoming data before writing it to the sinks. The transformation must contain an \"aimc_main(sources)\" entrypoint function in Lua.",
    )
    sources: Sources = Sources()
    sinks: Sinks = Sinks()

class MappingConfiguration(SubmodelElementCollection):
    semantic_id: str = "https://admin-shell.io/idta/AssetInterfacesMappingConfiguration/2/0/MappingConfiguration"
    description: str = "A MappingConfiguration defines one logical unit of sources (inputs) and sinks (outputs) that are in relation to one another. The relation can be expressed via a transformation."
    value: MappingConfigurationValues = MappingConfigurationValues()

class MappingConfigurations(SubmodelElementList):
    semantic_id: str = "https://admin-shell.io/idta/AssetInterfacesMappingConfiguration/1/0/MappingConfigurations"
    description: str = "List of MappingConfigurations that each map and transform data from their sources to their sinks."
    item_type: ClassVar = MappingConfiguration
    value: List[MappingConfiguration] = [
        MappingConfiguration(id_short="MappingConfiguration"),
    ]

class AssetInterfacesMappingConfigurationValues(ContainerValue):
    model_config = {'extra': 'forbid'}
    mapping_configurations: MappingConfigurations = MappingConfigurations()

class AssetInterfacesMappingConfiguration(Submodel):
    semantic_id: str = "https://admin-shell.io/idta/AssetInterfacesMappingConfiguration/2/0/Submodel"
    description: str = "The AIMC 2.0 is used to describe how data is mapped from asset to AAS or from AAS to AAS."
    VERSION: ClassVar[str] = "2"
    REVISION: ClassVar[str] = "0"
    submodel_element: AssetInterfacesMappingConfigurationValues = AssetInterfacesMappingConfigurationValues()

# ── Resolve forward references (Pydantic circular refs) ──
SourceValues.model_rebuild()
Source.model_rebuild()
Sources.model_rebuild()
SinkValues.model_rebuild()
Sink.model_rebuild()
Sinks.model_rebuild()
MappingConfigurationValues.model_rebuild()
MappingConfiguration.model_rebuild()
MappingConfigurations.model_rebuild()
AssetInterfacesMappingConfigurationValues.model_rebuild()
AssetInterfacesMappingConfiguration.model_rebuild()
