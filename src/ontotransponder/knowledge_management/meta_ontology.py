```python
# SPDX-License-Identifier: GPL-3.0-or-later
# Copyright (C) 2026 OntoCoder Collective

from typing import Optional
from .onto16 import Onto16
from .onto8 import Onto8

class MetaOntology:
    """
    Orchestrates phase transitions between NoemaFast (onto16) and NoemaSlow (onto8).

    Implements 'slowing through reflection' strategy:
      - High ontological density → trigger NoemaSlow
      - Social proximity < threshold → require deeper validation
      - Crisis input → force reflective mode

    This class is stateless and used by core.py / emitter.py as needed.
    """

    @staticmethod
    def should_enter_noema_slow(onto16: Onto16, crisis_hint: bool = False) -> bool:
        """
        Decides whether to transition from NoemaFast to NoemaSlow.
        """
        density = onto16.ontological_density
        proximity = onto16.social_proximity

        # Прямой кризис — немедленный переход
        if crisis_hint:
            return True

        # Высокая плотность требует рефлексии
        if density > 0.7:
            return True

        # Низкая социальная близость требует осторожности
        if proximity < 0.3:
            return True

        return False

    @staticmethod
    def project_onto8_to_onto16(
        onto8: Onto8,
        original_onto16: Onto16,
        resolved_payload: dict,
        causal_anchors: list[str]
    ) -> Onto16:
        """
        Projects refined internal state back to external representation.
        Energy values are stripped; only narrative and causal structure remain.
        """
        new_data = original_onto16.data.copy()
        new_data["payload"] = resolved_payload
        new_data["metadata"]["causal_anchors"] = causal_anchors
        # Онтологическая плотность может быть повышена после рефлексии
        new_data["metadata"]["ontological_density"] = min(
            original_onto16.ontological_density + 0.2, 1.0
        )
        return Onto16(new_data)
```
