```python
# SPDX-License-Identifier: GPL-3.0-or-later
# Copyright (C) 2026 OntoCoder Collective

from typing import Any, Dict, Optional

class Onto8:
    """
    Internal reflective knowledge representation (onto8).

    Principles:
      - Used ONLY within NoemaSlow for deep cognition
      - May contain irrational expressions, energy states, temporal gaps
      - NEVER exposed to emitter, ingress, or external systems
      - Supports pre-linguistic decision models and social distance dynamics

    This format is the cognitive "shadow" of onto16.
    """

    def __init__(self, internal_state: Dict[str, Any]):
        self._validate(internal_state)
        self.state = internal_state

    def _validate(self, state: Dict[str, Any]) -> None:
        # onto8 не имеет фиксированной схемы — но должен содержать флаг режима
        if "mode" not in state:
            raise ValueError("onto8 requires 'mode' (e.g., 'reflective', 'crisis', 'stabilization')")
        # Может содержать энергетику — но только внутренне
        if "energy_state" in state and not isinstance(state["energy_state"], dict):
            raise ValueError("energy_state must be a structured dict")

    @property
    def mode(self) -> str:
        return self.state["mode"]

    @property
    def energy_state(self) -> Optional[Dict[str, Any]]:
        return self.state.get("energy_state")

    @property
    def internal_dialogue(self) -> Optional[str]:
        return self.state.get("internal_dialogue")

    @classmethod
    def from_onto16(cls, onto16: "Onto16", mode: str = "reflective") -> "Onto8":
        """
        Создаёт onto8 из onto16 при переходе в NoemaSlow.
        """
        return cls({
            "mode": mode,
            "source_trace_id": onto16.data["trace_id"],
            "payload_snapshot": onto16.payload,
            "social_proximity": onto16.social_proximity,
            "energy_state": {
                "activation": 0.0,      # Инициализируется нулями
                "stability": 1.0,
                "social_tension": 0.0,
            },
            "internal_dialogue": None,
        })
```