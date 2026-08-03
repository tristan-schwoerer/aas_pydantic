"""HierarchicalStructures — generated from IDTA template."""

from __future__ import annotations

from typing import ClassVar, Dict, List, Optional
from aas_pydantic import (
    Entity, Property, Qualifier, RelationshipElement, Submodel, SubmodelElement, SubmodelElementCollection, SubmodelElementList,
)

class Node(Entity):
    semantic_id: str = "https://admin-shell.io/idta/HierarchicalStructures/Node/1/0"
    description: str = "Base entry point for the Entity tree in this Submodel, this must be a Self-managed Entity reflecting the Assets administrated in the Asset Administration Shell this Submodel is part of. The idShort of the EntryNode can be picked freely and may reflect a name of the asset."
    qualifiers: List[Qualifier] = [
        Qualifier(type_="EditIdShort", value="True"),
    ]
    entity_type: str = "SelfManagedEntity"

    node_: Optional[Node] = None
    same_as: RelationshipElement = RelationshipElement(
        semantic_id="https://admin-shell.io/idta/HierarchicalStructures/SameAs/1/0",
        description="Reference between two Entities in the same Submodel or across Submodels.",
        qualifiers=[
            Qualifier(type_="EditIdShort", value="True"),
        ],
    )
    is_part_of: RelationshipElement = RelationshipElement(
        semantic_id="https://admin-shell.io/idta/HierarchicalStructures/IsPartOf/1/0",
        description="Modeling of logical connections between components and sub-components. Either this or \"HasPart\" must be used, not both.",
        qualifiers=[
            Qualifier(type_="EditIdShort", value="True"),
        ],
    )
    has_part: RelationshipElement = RelationshipElement(
        semantic_id="https://admin-shell.io/idta/HierarchicalStructures/HasPart/1/0",
        description="Modeling of logical connections between components and sub-components. Either this or \"IsPartOf\" must be used, not both.",
        qualifiers=[
            Qualifier(type_="EditIdShort", value="True"),
        ],
    )
    bulk_count: Property = Property(
        semantic_id="https://admin-shell.io/idta/HierarchicalStructures/BulkCount/1/0",
        description="To be used if bulk components are referenced, e.g., a 10x M4x30 screw.",
    )

class EntryNode(Entity):
    semantic_id: str = "https://admin-shell.io/idta/HierarchicalStructures/EntryNode/1/0"
    description: str = "Base entry point for the Entity tree in this Submodel, this must be a Self-managed Entity reflecting the Assets administrated in the AAS this Submodel is part of."
    qualifiers: List[Qualifier] = [
        Qualifier(type_="EditIdShort", value="True"),
    ]
    entity_type: str = "SelfManagedEntity"

    node: Optional[Node] = None
    same_as: RelationshipElement = RelationshipElement(
        semantic_id="https://admin-shell.io/idta/HierarchicalStructures/SameAs/1/0",
        description="Reference between two Entities in the same Submodel or across Submodels.",
        qualifiers=[
            Qualifier(type_="EditIdShort", value="True"),
        ],
    )
    is_part_of: RelationshipElement = RelationshipElement(
        semantic_id="https://admin-shell.io/idta/HierarchicalStructures/IsPartOf/1/0",
        description="Modeling of logical connections between asset and sub-asset. Either this or \"HasPart\" must be used, not both.",
        qualifiers=[
            Qualifier(type_="EditIdShort", value="True"),
        ],
    )
    has_part: RelationshipElement = RelationshipElement(
        semantic_id="https://admin-shell.io/idta/HierarchicalStructures/HasPart/1/0",
        description="Modeling of logical connections between components and sub-components. Either this or \"IsPartOf\" must be used, not both.",
        qualifiers=[
            Qualifier(type_="EditIdShort", value="True"),
        ],
    )

class HierarchicalStructures(Submodel):
    semantic_id: str = "https://admin-shell.io/idta/HierarchicalStructures/1/1/Submodel"
    description: str = "The Submodel HierarchicalStructures identified by its semanticId. The Submodel idShort can be picked freely."
    qualifiers: List[Qualifier] = [
        Qualifier(type_="EditIdShort", value="True"),
    ]
    VERSION: ClassVar[str] = "1"
    REVISION: ClassVar[str] = "0"

    entry_node: Optional[EntryNode] = None
    arche_type: Property = Property(
        semantic_id="https://admin-shell.io/idta/HierarchicalStructures/ArcheType/1/0",
        description="ArcheType of the Submodel, there are three allowed enumeration entries: 1. \u201cFull\u201d, 2. \u201cOneDown\u201d and 3. \u201cOneUp\u201d. ",
        qualifiers=[
            Qualifier(type_="FormChoices", value="Full;OneDown;OneUp"),
        ],
    )


# ── Resolve forward references (Pydantic circular refs) ──
Node.model_rebuild()
EntryNode.model_rebuild()
HierarchicalStructures.model_rebuild()