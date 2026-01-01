```python
# SPDX-License-Identifier: GPL-3.0-or-later
# Copyright (C) 2026 OntoCoder Collective

from src.ontotransponder.invariant_core import InvariantRegistry
from src.ontotransponder.knowledge_management import Onto16
from src.ontotransponder.emitter import SceneRenderer

def test_emitter_renders_valid_scene():
    registry = InvariantRegistry.load_from_disk()
    renderer = SceneRenderer(registry)
    
    onto16 = Onto16({
        "schema": "onto16/v1",
        "trace_id": "scene-123",
        "timestamp": 1700000000.0,
        "payload": {"response": "I am here with you."},
        "ingress_type": "json_query",
        "metadata": {
            "causal_anchors": [],
            "social_proximity": 1.0,
            "ontological_density": 0.5,
        }
    })
    
    provenance = {
        "source_id": "user-alpha",
        "social_context": {"proximity": 1.0, "ontological_density": 0.5},
        "route": ["ingress", "normalizer", "validation", "renderer"],
    }
    
    scene = renderer.render(onto16, provenance)
    output = scene.render("json")
    
    # Проверяем структуру
    assert '"scene_id": "scene-123"' in output
    assert '"I am here with you."' in output
    assert '"causal_network"' in output
    assert '"invariant_compliance"' in output
    
    # Проверяем, что нет энергии
    assert "energy" not in output.lower()

def test_emitter_adds_causal_anchors():
    registry = InvariantRegistry.load_from_disk()
    renderer = SceneRenderer(registry)
    
    onto16 = Onto16({
        "schema": "onto16/v1",
        "trace_id": "test",
        "timestamp": 0,
        "payload": {"text": "We decide together."},
        "ingress_type": "json_query",
        "metadata": {
            "causal_anchors": [],
            "social_proximity": 0.8,
            "ontological_density": 0.6,
        }
    })
    
    provenance = {
        "source_id": "community-beta",
        "social_context": {"proximity": 0.8, "ontological_density": 0.6},
        "route": ["ingress", "normalizer", "validation", "renderer"],
    }
    
    scene = renderer.render(onto16, provenance)
    network = scene._causal_network
    
    assert "agency_assertion" in network["anchors"]
    assert "dialogic_acknowledgement" in network["anchors"]
    assert "source_community-beta" in network["anchors"]
    assert "invariant_compliance" in network["anchors"]
```