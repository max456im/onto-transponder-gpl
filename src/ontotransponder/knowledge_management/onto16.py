```python
# SPDX-License-Identifier: GPL-3.0-or-later
# Copyright (C) 2026 OntoCoder Collective

from typing import Any, Dict, List, Optional

class Onto16:
    """
    External knowledge representation format (onto16).

    Principles:
      - Used for ingress normalization, invariant validation, and emitter output
      - NEVER contains internal energy values, affective charge, or irrational expressions
      - Always includes causal anchors, social proximity, and ontological density
      - Schema: onto16/v1

    This is the ONLY format that leaves the transponder core.
    """

    def __init__(self,  Dict[str, Any]):
        self._validate(data)
        self.data = data

    def _validate(self, data: Dict[str, Any]) -> None:
        if data.get("schema") != "onto16/v1":
            raise ValueError("Invalid or missing onto16 schema")
        if "payload" not in data:
            raise ValueError("onto16 requires 'payload'")
        if "metadata" not in data:
            raise ValueError("onto16 requires 'metadata'")
        meta = data["metadata"]
        required_meta = {"causal_anchors", "social_proximity", "ontological_density"}
        if not required_meta.issubset(meta.keys()):
            raise ValueError(f"Missing required metadata: {required_meta - meta.keys()}")
        # Энергетические поля строго запрещены
        if any(key for key in data.keys() if "energy" in key.lower()):
            raise ValueError("Energy values are forbidden in onto16")

    @property
    def payload(self) -> Any:
        return self.data["payload"]

    @property
    def metadata(self) -> Dict[str, Any]:
        return self.data["metadata"]

    @property
    def causal_anchors(self) -> List[str]:
        return self.data["metadata"]["causal_anchors"]

    @property
    def social_proximity(self) -> float:
        return self.data["metadata"]["social_proximity"]

    @property
    def ontological_density(self) -> float:
        return self.data["metadata"]["ontological_density"]

    def add_causal_anchor(self, anchor: str) -> None:
        """Добавляет каузальную привязку (используется в emitter)."""
        if anchor not in self.causal_anchors:
            self.data["metadata"]["causal_anchors"].append(anchor)
```