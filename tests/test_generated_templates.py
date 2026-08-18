"""Generated IDTA template structure tests.

Ensures the JSON→pydantic generator (scripts/idta_generate.py) produces the
full named-field container structure: SML classes keep their identity +
metadata, SMC/Submodel classes hold their children as DIRECT named fields
(no ``value``/``submodel_element`` wrapper), and recursive children are
``Dict[str, X]`` maps / ``Optional[X] = None``.
"""

from __future__ import annotations

import pytest

from aas_pydantic.aas_model import (
    Blob,
    Entity,
    Property,
    ReferenceElement,
    RelationshipElement,
    SubmodelElementList,
    ExternalReference,
    Key,
)
from aas_pydantic import convert_pydantic_model, convert_aas_instance

from aas_pydantic.submodel_templates.asset_interfaces_mapping_configuration import (
    AssetInterfacesMappingConfiguration,
    MappingConfigurations,
    MappingConfiguration,
    Sources,
    Sinks,
    Source,
    Source_source,
    SourceId,
    Sink,
    Sink_sink,
    SinkId,
    DefaultPollingInterval,
    Transformation,
)
from aas_pydantic.submodel_templates.hierarchical_structures import (
    HierarchicalStructures,
    EntryNode,
    ArcheType,
    Node,
)


def test_aimc_generates_sml_class_and_item_class():
    """Sources/Sinks/MappingConfigurations keep their SML identity + metadata,
    while Source/Sink/MappingConfiguration item classes hold children as
    DIRECT named fields."""
    # SML classes exist, subclass SubmodelElementList, and carry semantic_id
    for sml_cls in (Sources, Sinks, MappingConfigurations):
        assert issubclass(sml_cls, SubmodelElementList)
        assert sml_cls.model_fields["semantic_id"].default, (
            f"{sml_cls.__name__} must keep its semantic_id"
        )

    # SML value lists start EMPTY; item_type is kept for back-conversion.
    for sml_cls, item_cls in (
        (Sources, Source),
        (Sinks, Sink),
        (MappingConfigurations, MappingConfiguration),
    ):
        assert sml_cls.model_fields["value"].default == []
        assert sml_cls.item_type is item_cls

    # Item classes carry their children as direct named fields (required
    # children have no default).
    assert set(Source.model_fields) >= {"source", "polling_interval", "source_id"}
    assert set(Sink.model_fields) >= {"sink", "sink_id"}
    assert set(MappingConfiguration.model_fields) >= {
        "default_polling_interval", "transformation", "sources", "sinks",
    }
    assert not Source.model_fields["source"].is_required() is False  # required
    assert not Sink.model_fields["sink"].is_required() is False


def test_aimc_round_trip_preserves_sml_metadata():
    """Nested SMLs keep their semantic_ids through pydantic→basyx→pydantic."""
    mc = MappingConfiguration(
        id_short="MappingConfiguration",
        default_polling_interval=DefaultPollingInterval(value="1.5"),
        transformation=Transformation(value=b"x"),
        sources=Sources(value=[
            Source(
                id_short="Source",
                source=Source_source(
                    value=ExternalReference(
                        key=(Key(type_="GlobalReference", value="https://x/s"),)
                    ),
                ),
                source_id=SourceId(value="src1"),
            )
        ]),
        sinks=Sinks(value=[
            Sink(
                id_short="Sink",
                sink=Sink_sink(
                    value=ExternalReference(
                        key=(Key(type_="GlobalReference", value="https://x/k"),)
                    ),
                ),
                sink_id=SinkId(value="snk1"),
            )
        ]),
    )
    sm = AssetInterfacesMappingConfiguration(
        id="https://x/aas/AIMC",
        id_short="AIMC",
        mapping_configurations=MappingConfigurations(value=[mc]),
    )

    basyx = convert_pydantic_model.convert_model_to_submodel(sm)
    back = convert_aas_instance.convert_submodel_to_model_instance(
        basyx, model_type=type(sm)
    )

    mc_back = back.mapping_configurations.value[0]
    assert type(mc_back).__name__ == "MappingConfiguration"
    sources = mc_back.sources
    assert type(sources).__name__ == "Sources"
    assert sources.semantic_id == (
        "https://admin-shell.io/idta/AssetInterfacesMappingConfiguration/2/0/"
        "MappingConfiguration/Sources"
    )
    assert type(sources.value[0]).__name__ == "Source"
    assert sources.value[0].source_id.value == "src1"
    sinks = mc_back.sinks
    assert type(sinks).__name__ == "Sinks"
    assert type(sinks.value[0]).__name__ == "Sink"
    assert sinks.value[0].sink_id.value == "snk1"


def test_hsem_generates_entity_tree():
    """The HSEM template's Entity tree survives generation: EntryNode and Node
    are real Entities with entity_type/global_asset_id and DIRECT named child
    maps.  The recursive inner Node is a multi-cardinality ``Dict[str, Node]``
    map — an empty default, so nothing recurses."""
    assert issubclass(EntryNode, Entity)
    assert issubclass(Node, Entity)
    assert EntryNode.model_fields["entity_type"].default == "SelfManagedEntity"
    assert EntryNode.model_fields["global_asset_id"].default
    assert set(Node.model_fields) >= {"node", "same_as", "is_part_of", "has_part", "bulk_count"}
    assert set(EntryNode.model_fields) >= {"node", "same_as", "is_part_of", "has_part"}
    # Multi-cardinality children are name-keyed maps; single ones stay fields.
    entry = EntryNode(id_short="entry_node")
    assert entry.node == {}
    assert entry.same_as == {}
    # bulk_count is ZeroToOne → single optional field on Node, None until set
    node = Node(id_short="node")
    assert node.bulk_count is None
    node.bulk_count = Property(value="42")
    assert node.bulk_count.value == "42"


def test_hsem_entity_round_trip():
    """Entities keep their type, entity_type, global_asset_id and children
    through pydantic → basyx → pydantic, including multi-cardinality children
    (many same_as / node entries) regrouped by concept semanticId."""
    hs = HierarchicalStructures(
        id_short="HStructures",
        id="https://x/aas/HS",
        entry_node=EntryNode(id_short="entry_node"),
        arche_type=ArcheType(id_short="arche_type"),
    )
    SAME_AS = "https://admin-shell.io/idta/HierarchicalStructures/SameAs/1/0"
    NODE = "https://admin-shell.io/idta/HierarchicalStructures/Node/1/0"

    def _rel(a, b):
        return RelationshipElement(
            semantic_id=SAME_AS,
            first=ExternalReference(key=(Key(type_="GlobalReference", value=a),)),
            second=ExternalReference(key=(Key(type_="GlobalReference", value=b),)),
        )

    hs.entry_node.same_as = {
        "rel_a": _rel("https://x/a", "https://x/b"),
        "rel_b": _rel("https://x/c", "https://x/d"),
    }
    hs.entry_node.node = {
        "sub1": Node(semantic_id=NODE),
        "sub2": Node(semantic_id=NODE),
    }

    basyx = convert_pydantic_model.convert_model_to_submodel(hs)
    entry = [el for el in basyx.submodel_element if el.id_short == "entry_node"][0]
    assert entry.__class__.__name__ == "Entity"
    assert entry.entity_type.__class__.__name__ == "EntityType"
    assert entry.global_asset_id
    stmt_ids = {s.id_short for s in entry.statement}
    assert {"rel_a", "rel_b", "sub1", "sub2"} <= stmt_ids
