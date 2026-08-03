"""AssetInterfacesMappingConfiguration — generated from IDTA template."""

from __future__ import annotations

from typing import ClassVar, Dict, List, Optional
from aas_pydantic import (
    Blob, Property, Qualifier, ReferenceElement, Submodel, SubmodelElement, SubmodelElementCollection, SubmodelElementList,
)

class Sources(SubmodelElementList):
    semantic_id: str = "https://admin-shell.io/idta/AssetInterfacesMappingConfiguration/2/0/MappingConfiguration/Sources"
    description: str = "This list includes all data sources that are used in this MappingConfiguration."

    value: List[None] = []

class Sinks(SubmodelElementList):
    semantic_id: str = "https://admin-shell.io/idta/AssetInterfacesMappingConfiguration/2/0/MappingConfiguration/Sinks"
    description: str = "This list includes all data sinks that are used in this MappingConfiguration."

    value: List[None] = []

class MappingConfigurations(SubmodelElementList):
    semantic_id: str = "https://admin-shell.io/idta/AssetInterfacesMappingConfiguration/1/0/MappingConfigurations"
    description: str = "List of MappingConfigurations that each map and transform data from their sources to their sinks."

    value: List[None] = []

class AssetInterfacesMappingConfiguration(Submodel):
    semantic_id: str = "https://admin-shell.io/idta/AssetInterfacesMappingConfiguration/2/0/Submodel"
    description: str = "The AIMC 2.0 is used to describe how data is mapped from asset to AAS or from AAS to AAS."
    VERSION: ClassVar[str] = "2"
    REVISION: ClassVar[str] = "0"

    mapping_configurations: MappingConfigurations = MappingConfigurations(id_short="MappingConfigurations")


# ── Resolve forward references (Pydantic circular refs) ──
Sources.model_rebuild()
Sinks.model_rebuild()
MappingConfigurations.model_rebuild()
AssetInterfacesMappingConfiguration.model_rebuild()