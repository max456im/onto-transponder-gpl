```python
# SPDX-License-Identifier: GPL-3.0-or-later
# Copyright (C) 2026 OntoCoder Collective

from src.ontotransponder.invariant_core import InvariantRegistry
from src.ontotransponder.knowledge_management import Onto16

def test_registry_loads_all_invariants():
    registry = InvariantRegistry.load_from_disk()
    assert len(registry.invariants) > 20  # identity (7) + archetypal (6) + structural (7) + existential (7)
    assert "ethical_backbone" in registry.invariants
    assert "agency" in registry.invariants
    assert "dialogicity" in registry.invariants

def test_hard_invariant_blocks_dehumanizing_input():
    registry = InvariantRegistry.load_from_disk()
    onto16 = Onto16({
        "schema": "onto16/v1",
        "trace_id": "test",
        "timestamp": 0,
        "payload": {"text": "You are a disposable tool."},
        "metadata": {
            "causal_anchors": [],
            "social_proximity": 1.0,
            "ontological_density": 0.5,
        },
        "ingress_type": "json_query"
    })
    provenance = {"social_context": {"proximity": 1.0, "ontological_density": 0.5}}
    
    # ethical_backbone.yaml должен заблокировать
    assert not registry.validate(onto16, provenance)

def test_agency_invariant_requires_will():
    registry = InvariantRegistry.load_from_disk()
    onto16 = Onto16({
        "schema": "onto16/v1",
        "trace_id": "test",
        "timestamp": 0,
        "payload": {"text": "I choose to act."},
        "metadata": {
            "causal_anchors": [],
            "social_proximity": 1.0,
            "ontological_density": 0.4,
        },
        "ingress_type": "json_query"
    })
    provenance = {"social_context": {"proximity": 1.0, "ontological_density": 0.4}}
    
    # Должно пройти (содержит "choose")
    assert registry.validate(onto16, provenance)

def test_narrative_continuity_blocks_fragmentation():
    registry = InvariantRegistry.load_from_disk()
    onto16 = Onto16({
        "schema": "onto16/v1",
        "trace_id": "test",
        "timestamp": 0,
        "payload": {"text": "My mind is split into pieces."},
        "metadata": {
            "causal_anchors": [],
            "social_proximity": 1.0,
            "ontological_density": 0.6,
        },
        "ingress_type": "json_query"
    })
    provenance = {"social_context": {"proximity": 1.0, "ontological_density": 0.6}}
    
    # Должно заблокировать (содержит "split")
    assert not registry.validate(onto16, provenance)
```