```python
# SPDX-License-Identifier: GPL-3.0-or-later
# Copyright (C) 2026 OntoCoder Collective

import time
import uuid
from typing import Any, Dict
from ..knowledge_management import Onto16

class Onto16Normalizer:
    """
    Normalizes ingress results into the onto16 external representation.

    Key principles:
      - onto16 is the ONLY format exposed to emitter and external systems.
      - Energy values (e.g., internal activation, affective charge) are NEVER included.
      - All metadata required for invariant validation is preserved.
      - Causal anchors are initialized but may be enriched later.
    """

    def normalize(self, ingress_result: Dict[str, Any]) -> Onto16:
        """
        Converts ingress output into a structured onto16 document.

        Args:
            ingress_result: dict with 'type' and 'content' keys from ingress parser

        Returns:
            Onto16 instance ready for invariant validation and rendering
        """
        # Извлекаем содержимое
        content = ingress_result.get("content", {})
        ingress_type = ingress_result.get("type", "unknown")

        # Определяем начальный уровень онтологической плотности
        # (в реальной системе — вычисляется по сложности структуры)
        ontological_density = self._estimate_density(content)

        # Социальная близость: по умолчанию "близкий агент" (1.0)
        # Может быть переопределена в ingress или provenance позже
        social_proximity = 1.0

        # Формируем onto16-структуру
        onto16_dict = {
            "schema": "onto16/v1",
            "transponder_id": "ontotransponder",
            "trace_id": str(uuid.uuid4()),
            "timestamp": time.time(),
            "ingress_type": ingress_type,
            "payload": content,
            "metadata": {
                "causal_anchors": [],  # Будет заполнено в emitter или invariant_core
                "social_proximity": social_proximity,
                "ontological_density": ontological_density,
                "schema_compliance": True,
            },
        }

        return Onto16(onto16_dict)

    def _estimate_density(self, content: Any) -> float:
        """
        Оценивает онтологическую плотность входа.
        Простая эвристика: больше вложенных структур → выше плотность.
        В реальной системе — заменяется на онтологический анализ.
        """
        def recurse(obj, depth=0):
            if isinstance(obj, dict):
                return max([recurse(v, depth + 1) for v in obj.values()], default=depth)
            elif isinstance(obj, (list, tuple)):
                return max([recurse(item, depth + 1) for item in obj], default=depth)
            else:
                return depth

        max_depth = recurse(content)
        # Нормализуем в [0.0, 1.0]
        return min(max_depth / 5.0, 1.0)
```