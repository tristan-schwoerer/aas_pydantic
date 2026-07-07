"""AssetInterfacesMappingConfiguration — generated from IDTA template."""

from __future__ import annotations

from typing import ClassVar, List, Optional
from pydantic import Field
from aas_pydantic import (
    Submodel, SubmodelElementCollection, Capability, Qualifier,
    Blob, File, MultiLanguageProperty, Property, Range, ReferenceElement, RelationshipElement,
)

class Source(SubmodelElementCollection):
    semantic_id: str = "https://admin-shell.io/idta/AssetInterfacesMappingConfiguration/2/0/MappingConfiguration/Source"
    description: str = "A data source is defined by a Source reference, PollingInterval and SourceId."
    qualifiers: List[Qualifier] = [
        Qualifier(type_="SMT/Cardinality", value="OneToMany", semantic_id="https://admin-shell.io/SubmodelTemplates/Cardinality/1/0"),
    ]

    source_: ReferenceElement = ReferenceElement(
        semantic_id="https://admin-shell.io/idta/AssetInterfacesMappingConfiguration/2/0/MappingConfiguration/Source/Source",
        description="This holds a reference to the respective SubmodelElement used as data source. A data source can be any SubmodelElement including those defined in the InteractionMetadata of AID Submodels for fetching live-data from assets.",
        qualifiers=[
            Qualifier(type_="SMT/Cardinality", value="One", semantic_id="https://admin-shell.io/SubmodelTemplates/Cardinality/1/0"),
        ],
    )
    polling_interval: Property = Property(
        semantic_id="https://admin-shell.io/idta/AssetInterfacesMappingConfiguration/2/0/MappingConfiguration/Source/PollingInterval",
        description="The PollingInterval defines the time interval in seconds for fetching new data from the given synchronous data source. It must be greater than zero for synchronous protocols (e.g. HTTP) that need polling and is ignored for asynchronous protocols (e.g. MQTT). It overwrites the DefaultPollingInterval of the respective MappingConfiguration of this source.",
        qualifiers=[
            Qualifier(type_="SMT/Cardinality", value="ZeroToOne", semantic_id="https://admin-shell.io/SubmodelTemplates/Cardinality/1/0"),
        ],
    )
    source_id: Property = Property(
        semantic_id="https://admin-shell.io/idta/AssetInterfacesMappingConfiguration/2/0/MappingConfiguration/Source/SourceId",
        description="This is a unique and non-empty identifier that facilitates data access in the Lua transformation or establishes a relationship to a corresponding sink when no transformation is given. It must only be unique with respect to the Sources-list of the parent MappingConfiguration and not globally.",
        qualifiers=[
            Qualifier(type_="SMT/Cardinality", value="One", semantic_id="https://admin-shell.io/SubmodelTemplates/Cardinality/1/0"),
        ],
    )

class Sink(SubmodelElementCollection):
    semantic_id: str = "https://admin-shell.io/idta/AssetInterfacesMappingConfiguration/2/0/MappingConfiguration/Sink"
    description: str = "A data sink is defined by a Sink reference and SinkId."
    qualifiers: List[Qualifier] = [
        Qualifier(type_="SMT/Cardinality", value="OneToMany", semantic_id="https://admin-shell.io/SubmodelTemplates/Cardinality/1/0"),
    ]

    sink_: ReferenceElement = ReferenceElement(
        semantic_id="https://admin-shell.io/idta/AssetInterfacesMappingConfiguration/2/0/MappingConfiguration/Sink/Sink",
        description="This holds a reference to the respective SubmodelElement used as data sink for live-data.",
        qualifiers=[
            Qualifier(type_="SMT/Cardinality", value="One", semantic_id="https://admin-shell.io/SubmodelTemplates/Cardinality/1/0"),
        ],
    )
    sink_id: Property = Property(
        semantic_id="https://admin-shell.io/idta/AssetInterfacesMappingConfiguration/2/0/MappingConfiguration/Sink/SinkId",
        description="This is a unique and non-empty identifier that facilitates data writing in the Lua transformation or establishes a relationship to a corresponding source when no transformation is given. It must only be unique with respect to the Sinks-list of the containing MappingConfiguration and not globally.",
        qualifiers=[
            Qualifier(type_="SMT/Cardinality", value="One", semantic_id="https://admin-shell.io/SubmodelTemplates/Cardinality/1/0"),
        ],
    )

class MappingConfiguration(SubmodelElementCollection):
    semantic_id: str = "https://admin-shell.io/idta/AssetInterfacesMappingConfiguration/2/0/MappingConfiguration"
    description: str = "A MappingConfiguration defines one logical unit of sources (inputs) and sinks (outputs) that are in relation to one another. The relation can be expressed via a transformation."
    qualifiers: List[Qualifier] = [
        Qualifier(type_="SMT/Cardinality", value="ZeroToMany", semantic_id="https://admin-shell.io/SubmodelTemplates/Cardinality/1/0"),
    ]

    default_polling_interval: Property = Property(
        semantic_id="https://admin-shell.io/idta/AssetInterfacesMappingConfiguration/2/0/MappingConfiguration/DefaultPollingInterval",
        description="The DefaultPollingInterval defines the default time interval in seconds for fetching new data from the synchronous data sources defined in this MappingConfiguration. It must be greater than zero for synchronous protocols (e.g. HTTP) that need polling and is ignored for asynchronous protocols (e.g. MQTT).",
        qualifiers=[
            Qualifier(type_="SMT/Cardinality", value="ZeroToOne", semantic_id="https://admin-shell.io/SubmodelTemplates/Cardinality/1/0"),
        ],
    )
    transformation: Blob = Blob(
        semantic_id="https://admin-shell.io/idta/AssetInterfacesMappingConfiguration/2/0/MappingConfiguration/Transformation",
        description="The transformation allows for transforming incoming data before writing it to the sinks. The transformation must contain an \"aimc_main(sources)\" entrypoint function in Lua.",
        qualifiers=[
            Qualifier(type_="SMT/Cardinality", value="ZeroToOne", semantic_id="https://admin-shell.io/SubmodelTemplates/Cardinality/1/0"),
        ],
    )
    sources: List[Source] = []
    sinks: List[Sink] = []

class AssetInterfacesMappingConfiguration(Submodel):
    semantic_id: str = "https://admin-shell.io/idta/AssetInterfacesMappingConfiguration/2/0/Submodel"
    description: str = "The AIMC 2.0 is used to describe how data is mapped from asset to AAS or from AAS to AAS."
    VERSION: ClassVar[str] = "2"
    REVISION: ClassVar[str] = "0"

    mapping_configurations: List[MappingConfiguration] = []
