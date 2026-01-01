```python
#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-or-later
# Copyright (C) 2026 OntoCoder Collective

"""
Manual pipeline example: onto16 → invariant validation → emitter.

Demonstrates internal structure without using OntoTransponder facade.
Useful for integration with ontoCMS or UG-Mind.
"""

from src.ontotransponder.ingress import IngressHandler
from src.ontotransponder.normalizers import Onto16Normalizer
from src.ontotransponder.provenance import DataProvenance
from src.ontotransponder.invariant_core import InvariantRegistry
from src.ontotransponder.emitter import SceneRenderer

def main():
    # 1. Ingress
    handler = IngressHandler()
    raw = {"query": "What is my narrative continuity?", "depth": "reflective"}
    ingress_result = handler.parse(raw)
    assert ingress_result is not None
    
    # 2. Normalization to onto16
    normalizer = Onto16Normalizer()
    onto16 = normalizer.normalize(ingress_result)
    
    # 3. Provenance
    provenance = DataProvenance().trace(onto16, source_id="researcher_01")
    
    # 4. Invariant validation
    registry = InvariantRegistry.load_from_disk()
    if not registry.validate(onto16, provenance):
        print("❌ Invariant violation — pipeline aborted.")
        return
    
    # 5. Emission
    renderer = SceneRenderer(registry)
    scene = renderer.render(onto16, provenance)
    
    print("✅ Manual pipeline succeeded:\n")
    print(scene.render("json"))

if __name__ == "__main__":
    main()
```