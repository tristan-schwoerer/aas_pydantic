"""HierarchicalStructures — generated from IDTA template."""

from __future__ import annotations

from typing import Any, ClassVar, List, Dict
from aas_pydantic import (
    ContainerValue, Entity, Property, RelationshipElement, Submodel, SubmodelElement, SubmodelElementCollection, SubmodelElementList,
)
from pydantic import Field

class SameAs(RelationshipElement):
    semantic_id: str = "https://admin-shell.io/idta/HierarchicalStructures/SameAs/1/0"
    description: str = "Reference between two Entities in the same Submodel or across Submodels."

class IsPartOf(RelationshipElement):
    semantic_id: str = "https://admin-shell.io/idta/HierarchicalStructures/IsPartOf/1/0"
    description: str = "Modeling of logical connections between components and sub-components. Either this or \"HasPart\" must be used, not both."

class HasPart(RelationshipElement):
    semantic_id: str = "https://admin-shell.io/idta/HierarchicalStructures/HasPart/1/0"
    description: str = "Modeling of logical connections between components and sub-components. Either this or \"IsPartOf\" must be used, not both."

class NodeValues(ContainerValue):
    model_config = {'extra': 'forbid'}
    node: Dict[str, Node] = {}
    same_as: Dict[str, SameAs] = {}
    is_part_of: Dict[str, IsPartOf] = {}
    has_part: Dict[str, HasPart] = {}
    bulk_count: Property = Property(
        semantic_id="https://admin-shell.io/idta/HierarchicalStructures/BulkCount/1/0",
        description="To be used if bulk components are referenced, e.g., a 10x M4x30 screw.",
        value_type="xs:unsignedLong",
    )

class Node(Entity):
    semantic_id: str = "https://admin-shell.io/idta/HierarchicalStructures/Node/1/0"
    description: str = "Base entry point for the Entity tree in this Submodel, this must be a Self-managed Entity reflecting the Assets administrated in the Asset Administration Shell this Submodel is part of. The idShort of the EntryNode can be picked freely and may reflect a name of the asset."
    entity_type: str = "SelfManagedEntity"
    global_asset_id: str = "https://admin-shell.io/idta/HierarchicalStructures/EntryNode/1/0"
    statements: NodeValues = Field(default_factory=NodeValues)

class EntryNodeValues(ContainerValue):
    model_config = {'extra': 'forbid'}
    node: Dict[str, Node] = {}
    same_as: Dict[str, SameAs] = {}
    is_part_of: Dict[str, IsPartOf] = {}
    has_part: Dict[str, HasPart] = {}

class EntryNode(Entity):
    semantic_id: str = "https://admin-shell.io/idta/HierarchicalStructures/EntryNode/1/0"
    description: str = "Base entry point for the Entity tree in this Submodel, this must be a Self-managed Entity reflecting the Assets administrated in the AAS this Submodel is part of."
    entity_type: str = "SelfManagedEntity"
    global_asset_id: str = "https://admin-shell.io/idta/HierarchicalStructures/EntryNode/1/0"
    statements: EntryNodeValues = EntryNodeValues()

class HierarchicalStructuresValues(ContainerValue):
    model_config = {'extra': 'forbid'}
    entry_node: EntryNode = EntryNode()
    arche_type: Property = Property(
        semantic_id="https://admin-shell.io/idta/HierarchicalStructures/ArcheType/1/0",
        description="ArcheType of the Submodel, there are three allowed enumeration entries: 1. \u201cFull\u201d, 2. \u201cOneDown\u201d and 3. \u201cOneUp\u201d. ",
        value_type="xs:string",
    )

class HierarchicalStructures(Submodel):
    semantic_id: str = "https://admin-shell.io/idta/HierarchicalStructures/1/1/Submodel"
    description: str = "The Submodel HierarchicalStructures identified by its semanticId. The Submodel idShort can be picked freely."
    VERSION: ClassVar[str] = "1"
    REVISION: ClassVar[str] = "0"
    submodel_element: HierarchicalStructuresValues = HierarchicalStructuresValues()

# ── Resolve forward references (Pydantic circular refs) ──
SameAs.model_rebuild()
IsPartOf.model_rebuild()
HasPart.model_rebuild()
NodeValues.model_rebuild()
Node.model_rebuild()
EntryNodeValues.model_rebuild()
EntryNode.model_rebuild()
HierarchicalStructuresValues.model_rebuild()
HierarchicalStructures.model_rebuild()
