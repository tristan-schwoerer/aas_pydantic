"""HierarchicalStructures — generated from IDTA template."""

from __future__ import annotations

from typing import Any, ClassVar, List, Dict, Optional
from aas_pydantic import (
    Entity, ExternalReference, Key, Property, RelationshipElement, Submodel, SubmodelElement, SubmodelElementCollection, SubmodelElementList,
)

class SameAs(RelationshipElement):
    semantic_id: str = "https://admin-shell.io/idta/HierarchicalStructures/SameAs/1/0"
    description: str = "Reference between two Entities in the same Submodel or across Submodels."
    first: ExternalReference = ExternalReference(
        key=(
            Key(type_="GlobalReference", value="https://admin-shell.io/SMT/General/IntentionallyEmpty"),
        ),
    ),
    second: ExternalReference = ExternalReference(
        key=(
            Key(type_="GlobalReference", value="https://admin-shell.io/SMT/General/IntentionallyEmpty"),
        ),
    ),

class IsPartOf(RelationshipElement):
    semantic_id: str = "https://admin-shell.io/idta/HierarchicalStructures/IsPartOf/1/0"
    description: str = "Modeling of logical connections between components and sub-components. Either this or \"HasPart\" must be used, not both."
    first: ExternalReference = ExternalReference(
        key=(
            Key(type_="GlobalReference", value="https://admin-shell.io/SMT/General/IntentionallyEmpty"),
        ),
    ),
    second: ExternalReference = ExternalReference(
        key=(
            Key(type_="GlobalReference", value="https://admin-shell.io/SMT/General/IntentionallyEmpty"),
        ),
    ),

class HasPart(RelationshipElement):
    semantic_id: str = "https://admin-shell.io/idta/HierarchicalStructures/HasPart/1/0"
    description: str = "Modeling of logical connections between components and sub-components. Either this or \"IsPartOf\" must be used, not both."
    first: ExternalReference = ExternalReference(
        key=(
            Key(type_="GlobalReference", value="https://admin-shell.io/SMT/General/IntentionallyEmpty"),
        ),
    ),
    second: ExternalReference = ExternalReference(
        key=(
            Key(type_="GlobalReference", value="https://admin-shell.io/SMT/General/IntentionallyEmpty"),
        ),
    ),

class BulkCount(Property):
    semantic_id: str = "https://admin-shell.io/idta/HierarchicalStructures/BulkCount/1/0"
    description: str = "To be used if bulk components are referenced, e.g., a 10x M4x30 screw."
    value_type: str = "xs:unsignedLong"

class Node(Entity):
    semantic_id: str = "https://admin-shell.io/idta/HierarchicalStructures/Node/1/0"
    description: str = "Base entry point for the Entity tree in this Submodel, this must be a Self-managed Entity reflecting the Assets administrated in the Asset Administration Shell this Submodel is part of. The idShort of the EntryNode can be picked freely and may reflect a name of the asset."
    entity_type: str = "SelfManagedEntity"
    global_asset_id: str = "https://admin-shell.io/idta/HierarchicalStructures/EntryNode/1/0"
    node: Dict[str, Node] = {}
    same_as: Dict[str, SameAs] = {}
    is_part_of: Dict[str, IsPartOf] = {}
    has_part: Dict[str, HasPart] = {}
    bulk_count: Optional[BulkCount] = None

class EntryNode(Entity):
    semantic_id: str = "https://admin-shell.io/idta/HierarchicalStructures/EntryNode/1/0"
    description: str = "Base entry point for the Entity tree in this Submodel, this must be a Self-managed Entity reflecting the Assets administrated in the AAS this Submodel is part of."
    entity_type: str = "SelfManagedEntity"
    global_asset_id: str = "https://admin-shell.io/idta/HierarchicalStructures/EntryNode/1/0"
    node: Dict[str, Node] = {}
    same_as: Dict[str, SameAs] = {}
    is_part_of: Dict[str, IsPartOf] = {}
    has_part: Dict[str, HasPart] = {}

class ArcheType(Property):
    semantic_id: str = "https://admin-shell.io/idta/HierarchicalStructures/ArcheType/1/0"
    description: str = "ArcheType of the Submodel, there are three allowed enumeration entries: 1. \u201cFull\u201d, 2. \u201cOneDown\u201d and 3. \u201cOneUp\u201d. "
    value_type: str = "xs:string"

class HierarchicalStructures(Submodel):
    semantic_id: str = "https://admin-shell.io/idta/HierarchicalStructures/1/1/Submodel"
    description: str = "The Submodel HierarchicalStructures identified by its semanticId. The Submodel idShort can be picked freely."
    VERSION: ClassVar[str] = "1"
    REVISION: ClassVar[str] = "0"
    entry_node: EntryNode
    arche_type: ArcheType

# ── Resolve forward references (Pydantic circular refs) ──
SameAs.model_rebuild()
IsPartOf.model_rebuild()
HasPart.model_rebuild()
BulkCount.model_rebuild()
Node.model_rebuild()
EntryNode.model_rebuild()
ArcheType.model_rebuild()
HierarchicalStructures.model_rebuild()
