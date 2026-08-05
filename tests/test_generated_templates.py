"""Generated IDTA template structure tests.

Ensures the JSON→pydantic generator (scripts/idta_generate.py) produces the
full SML structure: for an SML whose items are SMCs, BOTH the item class
(e.g. ``Source``) and the SML class (e.g. ``Sources``) with a typed
``value: List[ItemClass]`` are generated — the SML's semantic_id/description
must not be lost.
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
    Sink,
)
from aas_pydantic.submodel_templates.hierarchical_structures import (
    HierarchicalStructures,
    EntryNode,
    Node,
)


def test_aimc_generates_sml_class_and_item_class():
    """Sources/Sinks/MappingConfigurations keep their SML identity + metadata,
    while Source/Sink/MappingConfiguration item classes are fully defined."""
    # SML classes exist, subclass SubmodelElementList, and carry semantic_id
    for sml_cls in (Sources, Sinks, MappingConfigurations):
        assert issubclass(sml_cls, SubmodelElementList)
        assert sml_cls.model_fields["semantic_id"].default, (
            f"{sml_cls.__name__} must keep its semantic_id"
        )

    # SML value lists hold generated item instances by default
    assert isinstance(Sources.model_fields["value"].default[0], Source)
    assert isinstance(Sinks.model_fields["value"].default[0], Sink)
    assert isinstance(
        MappingConfigurations.model_fields["value"].default[0], MappingConfiguration
    )

    # Item classes carry their own children in a typed values model
    assert set(Source.model_fields["value"].default.model_fields) == {
        "source", "polling_interval", "source_id",
    }
    assert set(Sink.model_fields["value"].default.model_fields) == {"sink", "sink_id"}
    assert set(MappingConfiguration.model_fields["value"].default.model_fields) == {
        "default_polling_interval", "transformation", "sources", "sinks",
    }


def test_aimc_round_trip_preserves_sml_metadata():
    """Nested SMLs keep their semantic_ids through pydantic→basyx→pydantic."""
    mc = MappingConfiguration(
        id_short="MappingConfiguration",
        value={
            "default_polling_interval": Property(
                id_short="DefaultPollingInterval", value="1.5", value_type="xs:double"
            ),
            "transformation": Blob(
                id_short="Transformation", content_type="text/x-lua", value=b"x"
            ),
            "sources": Sources(
                id_short="Sources",
                value=[
                    Source(
                        id_short="Source",
                        value={
                            "source": ReferenceElement(
                                id_short="Source",
                                value=ExternalReference(
                                    key=(Key(type_="GlobalReference", value="https://x/s"),)
                                ),
                            ),
                            "source_id": Property(id_short="SourceId", value="src1"),
                        },
                    )
                ],
            ),
            "sinks": Sinks(
                id_short="Sinks",
                value=[
                    Sink(
                        id_short="Sink",
                        value={
                            "sink": ReferenceElement(
                                id_short="Sink",
                                value=ExternalReference(
                                    key=(Key(type_="GlobalReference", value="https://x/k"),)
                                ),
                            ),
                            "sink_id": Property(id_short="SinkId", value="snk1"),
                        },
                    )
                ],
            ),
        },
    )
    sm = AssetInterfacesMappingConfiguration(
        id="https://x/aas/AIMC",
        id_short="AIMC",
        submodel_element={
            "mapping_configurations": MappingConfigurations(
                id_short="MappingConfigurations", value=[mc]
            )
        },
    )

    basyx = convert_pydantic_model.convert_model_to_submodel(sm)
    back = convert_aas_instance.convert_submodel_to_model_instance(
        basyx, model_type=type(sm)
    )

    # Values-model round-trip with concrete types restored: the SML and its
    # items resolve to their generated classes via semanticId (SML) and the
    # SML's declared item_type (items — AASd-114 strips their semanticIds).
    mc_back = back.submodel_element.mapping_configurations.value[0]
    assert type(mc_back).__name__ == "MappingConfiguration"
    sources = mc_back.value.sources
    assert type(sources).__name__ == "Sources"
    assert sources.id_short == "sources"
    assert sources.semantic_id == (
        "https://admin-shell.io/idta/AssetInterfacesMappingConfiguration/2/0/"
        "MappingConfiguration/Sources"
    )
    assert type(sources.value[0]).__name__ == "Source"
    assert sources.value[0].value.source_id.value == "src1"
    sinks = mc_back.value.sinks
    assert type(sinks).__name__ == "Sinks"
    assert type(sinks.value[0]).__name__ == "Sink"
    assert sinks.value[0].value.sink_id.value == "snk1"

    # SML semantic_ids survive
    def _find_sml(container, id_short):
        children = getattr(container, "submodel_element", None) or container.value
        for el in children:
            if el.__class__.__name__ == "SubmodelElementList":
                if el.id_short == id_short:
                    return el
        raise AssertionError(f"SML {id_short} not found")

    mcs = _find_sml(basyx, "mapping_configurations")
    assert (
        mcs.semantic_id.key[0].value
        == "https://admin-shell.io/idta/AssetInterfacesMappingConfiguration/1/0/MappingConfigurations"
    )
    for item in mcs.value:
        sources = _find_sml(item, "sources")
        assert (
            sources.semantic_id.key[0].value
            == "https://admin-shell.io/idta/AssetInterfacesMappingConfiguration/2/0/MappingConfiguration/Sources"
        )


def test_hsem_generates_entity_tree():
    """The HSEM template's Entity tree survives generation: EntryNode and Node
    are real Entities with entity_type/global_asset_id and statements.  The
    recursive inner Node is a multi-cardinality ``Dict[str, Node]`` map — an
    empty default, so nothing recurses."""
    assert issubclass(EntryNode, Entity)
    assert issubclass(Node, Entity)
    # Entities carry their type + asset id + statement containers
    assert EntryNode.model_fields["entity_type"].default == "SelfManagedEntity"
    assert EntryNode.model_fields["global_asset_id"].default
    # Default structure: EntryNode → Node (Entity); Node → BulkCount (Property)
    entry = EntryNode(id_short="entry_node")
    node_fields = Node.model_fields["statements"].default_factory().model_fields
    entry_field = EntryNode.model_fields["statements"]
    entry_fields = (
        entry_field.default_factory().model_fields
        if entry_field.default is None
        else entry_field.default.model_fields
    )
    assert set(node_fields) == {"node", "same_as", "is_part_of", "has_part", "bulk_count"}
    assert set(entry_fields) == {"node", "same_as", "is_part_of", "has_part"}
    # Multi-cardinality children are name-keyed maps; single ones stay fields.
    assert isinstance(entry.statements.node, dict)
    assert entry.statements.node == {}
    assert isinstance(entry.statements.same_as, dict)
    # bulk_count is ZeroToOne → single typed field on Node
    node = Node(id_short="node")
    assert isinstance(node.statements.bulk_count, Property)


def test_hsem_entity_round_trip():
    """Entities keep their type, entity_type, global_asset_id and statements
    through pydantic → basyx → pydantic, including multi-cardinality children
    (many same_as / node entries) regrouped by concept semanticId."""
    hs = HierarchicalStructures(id_short="HStructures", id="https://x/aas/HS")
    SAME_AS = "https://admin-shell.io/idta/HierarchicalStructures/SameAs/1/0"
    NODE = "https://admin-shell.io/idta/HierarchicalStructures/Node/1/0"

    def _rel(a, b):
        return RelationshipElement(
            semantic_id=SAME_AS,
            first=ExternalReference(key=(Key(type_="GlobalReference", value=a),)),
            second=ExternalReference(key=(Key(type_="GlobalReference", value=b),)),
        )

    hs.submodel_element.entry_node.statements.same_as = {
        "rel_a": _rel("https://x/a", "https://x/b"),
        "rel_b": _rel("https://x/c", "https://x/d"),
    }
    hs.submodel_element.entry_node.statements.node = {
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

    back = convert_aas_instance.convert_submodel_to_model_instance(
        basyx, model_type=HierarchicalStructures
    )
    en = back.submodel_element.entry_node
    # Type-preserving round-trip: EntryNode and its Node children resolve to
    # their generated classes; multi-cardinality children regroup into the
    # name-keyed Dict fields by concept semanticId.
    assert type(en).__name__ == "EntryNode"
    assert type(en.statements.node["sub1"]).__name__ == "Node"
    assert type(en.statements.node["sub2"]).__name__ == "Node"
    assert en.entity_type == "SelfManagedEntity"
    assert en.global_asset_id
    assert set(en.statements.same_as) == {"rel_a", "rel_b"}
    assert en.statements.same_as["rel_a"].first.key[0].value == "https://x/a"
    assert en.statements.same_as["rel_a"].second.key[0].value == "https://x/b"
    assert en.statements.same_as["rel_b"].first.key[0].value == "https://x/c"
