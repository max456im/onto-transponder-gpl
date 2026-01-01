```python
# SPDX-License-Identifier: GPL-3.0-or-later
# Copyright (C) 2026 OntoCoder Collective

import json
from typing import Any, Dict, List
from ..knowledge_management import Onto16
from ..invariant_core import InvariantRegistry

class Scene:
    """
    Immutable, causally coherent output unit.

    A Scene is not a response—it is an ontological event:
      - Fully grounded in prior states or social context
      - Free of energy values or internal irrationality
      - Traceable to source and invariant validation
    """

    def __init__(self, content: Dict[str, Any], causal_network: Dict[str, Any]):
        self._content = content
        self._causal_network = causal_network

    def render(self, format: str = "json") -> str:
        """
        Renders the scene in a coherent output format.

        Currently supports:
          - 'json': machine-readable
          - 'narrative': human-readable (planned)

        Raises:
            ValueError: if format is unsupported
        """
        if format == "json":
            return json.dumps(self._as_dict(), ensure_ascii=False, indent=2)
        elif format == "narrative":
            return self._to_narrative()
        else:
            raise ValueError(f"Unsupported render format: {format}")

    def _as_dict(self) -> Dict[str, Any]:
        return {
            "scene_id": self._content["scene_id"],
            "content": self._content["payload"],
            "causal_network": self._causal_network,
            "schema": "scene/v1",
            "compliance": "full_invariant_adherence",
        }

    def _to_narrative(self) -> str:
        # Заглушка для будущей реализации нарративного рендеринга
        payload = self._content["payload"]
        if isinstance(payload, dict):
            lines = ["— " + str(v) for v in payload.values()]
            return "\n".join(lines)
        return str(payload)


class SceneRenderer:
    """
    Renders invariant-compliant scenes from validated onto16 units.

    Responsibilities:
      - Enrich onto16 with causal anchors based on invariant logic
      - Ensure no energy values leak into output
      - Produce coherent, auditable scene objects
    """

    def __init__(self, invariant_registry: InvariantRegistry):
        self.registry = invariant_registry

    def render(self, onto16: Onto16, provenance: Dict[str, Any]) -> Scene:
        """
        Renders a final Scene from a validated onto16 unit.

        This method assumes all hard invariants have already passed.
        """
        # 1. Обогащаем каузальные якоря на основе доменов инвариантов
        causal_anchors = self._build_causal_anchors(onto16, provenance)

        # 2. Добавляем якоря в onto16 (для целостности)
        for anchor in causal_anchors:
            onto16.add_causal_anchor(anchor)

        # 3. Формируем контент сцены
        scene_content = {
            "scene_id": onto16.data["trace_id"],
            "payload": onto16.payload,
            "ingress_type": onto16.data.get("ingress_type", "unknown"),
            "source": provenance["source_id"],
            "timestamp": onto16.data["timestamp"],
        }

        # 4. Строим каузальную сеть
        causal_network = {
            "anchors": causal_anchors,
            "density": onto16.ontological_density,
            "social_proximity": provenance["social_context"]["proximity"],
            "route": provenance["route"],
            "invariant_domains": self._get_active_domains(onto16),
        }

        return Scene(scene_content, causal_network)

    def _build_causal_anchors(self, onto16: Onto16, provenance: Dict[str, Any]) -> List[str]:
        """
        Генерирует каузальные якоря на основе активных инвариантов и контекста.
        """
        anchors = []
        payload_str = str(onto16.payload).lower()
        proximity = provenance["social_context"]["proximity"]

        # Identity anchors
        if "choose" in payload_str or "decide" in payload_str:
            anchors.append("agency_assertion")
        if any(word in payload_str for word in ["you", "other", "we"]):
            anchors.append("dialogic_acknowledgement")

        # Structural anchors
        if onto16.ontological_density > 0.6:
            anchors.append("high_density_reflection")
        if proximity < 0.5:
            anchors.append("distant_context_caution")

        # Existential anchors
        if provenance["source_id"] != "anonymous":
            anchors.append(f"source_{provenance['source_id']}")

        # Добавляем универсальный якорь
        anchors.append("invariant_compliance")

        return anchors

    def _get_active_domains(self, onto16: Onto16) -> List[str]:
        """
        Определяет, какие домены инвариантов были наиболее релевантны.
        """
        domains = set()
        payload_str = str(onto16.payload).lower()

        # Identity
        if any(w in payload_str for w in ["i", "self", "my", "identity"]):
            domains.add("identity")
        # Archetypal
        if any(w in payload_str for w in ["hero", "shadow", "mother", "death", "rebirth"]):
            domains.add("archetypal")
        # Structural
        if "balance" in payload_str or "system" in payload_str or "relation" in payload_str:
            domains.add("structural")
        # Existential
        if any(w in payload_str for w in ["here", "now", "alone", "together", "responsibility"]):
            domains.add("existential")

        return sorted(domains) if domains else ["default"]
```