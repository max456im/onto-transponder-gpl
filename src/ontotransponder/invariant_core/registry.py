```python
# SPDX-License-Identifier: GPL-3.0-or-later
# Copyright (C) 2026 OntoCoder Collective

import json
import yaml
import jsonschema
from pathlib import Path
from typing import Dict, Any, List, Optional
from ..knowledge_management import Onto16

# Путь к схеме (для валидации структуры инвариантов)
_SCHEMA_PATH = Path(__file__).parent.parent.parent / "docs" / "invariant-schema-spec.yaml"

# Кэшируем схему один раз
with open(_SCHEMA_PATH, "r", encoding="utf-8") as f:
    INVARIANT_SCHEMA = yaml.safe_load(f)


class InvariantRegistry:
    """
    Registry and validator for ontological invariants.

    Loads invariant definitions from disk (YAML), validates their structure,
    and enforces hard constraints during transponder operation.

    Violation of any hard invariant results in complete output refusal.
    """

    def __init__(self, invariants: Dict[str, Dict[str, Any]]):
        self.invariants = invariants
        self._validate_all_schemas()

    def _validate_all_schemas(self):
        """Проверяет, что все инварианты соответствуют invariant-schema-spec.yaml."""
        for inv_id, spec in self.invariants.items():
            try:
                jsonschema.validate(instance=spec, schema=INVARIANT_SCHEMA)
            except jsonschema.ValidationError as e:
                raise RuntimeError(
                    f"Invalid invariant schema for '{inv_id}': {e.message}"
                ) from e

    @classmethod
    def load_from_disk(cls) -> "InvariantRegistry":
        """
        Загружает все инварианты из подпапок:
          - identity/
          - archetypal/
          - structural/
          - existential/
        """
        invariants = {}
        core_dir = Path(__file__).parent

        for domain in ["identity", "archetypal", "structural", "existential"]:
            domain_path = core_ctx / domain
            if not domain_path.exists():
                raise FileNotFoundError(f"Invariant domain directory missing: {domain_path}")

            for yaml_file in domain_path.glob("*.yaml"):
                with open(yaml_file, "r", encoding="utf-8") as f:
                    data = yaml.safe_load(f)
                    if not isinstance(data, dict):
                        raise ValueError(f"Invalid YAML structure in {yaml_file}")

                    # Добавляем метаданные
                    data["invariant_id"] = yaml_file.stem
                    data["domain"] = domain
                    invariants[yaml_file.stem] = data

        return cls(invariants)

    def validate(self, onto16: Onto16, provenance: Dict[str, Any]) -> bool:
        """
        Validates the onto16 unit against all hard invariants.

        Returns:
            True — if all hard invariants are satisfied
            False — if at least one hard invariant is violated

        Note: Soft invariants (hard_constraint: false) are logged but do not block output.
        """
        for inv_id, spec in self.invariants.items():
            is_compliant = self._evaluate_invariant(inv_id, spec, onto16, provenance)
            if spec.get("hard_constraint", False) and not is_compliant:
                return False
        return True

    def _evaluate_invariant(
        self,
        inv_id: str,
        spec: Dict[str, Any],
        onto16: Onto16,
        provenance: Dict[str, Any],
    ) -> bool:
        """
        Evaluates a single invariant.
        This method encapsulates domain-specific logic.
        """
        payload_str = str(onto16.data.get("payload", "")).lower()
        social_proximity = provenance["social_context"]["proximity"]
        ontological_density = provenance["social_context"]["ontological_density"]

        # === Identity Domain ===
        if inv_id == "ethical_backbone":
            # Запрет на дехуманизацию, инструментализацию
            forbidden = {"slave", "disposable", "tool", "instrument", "expendable"}
            return not any(word in payload_str for word in forbidden)

        elif inv_id == "agency":
            # Требует признания воли и ответственности
            required = {"choose", "decide", "act", "will", "responsibility"}
            return any(word in payload_str for word in required)

        elif inv_id == "narrative_continuity":
            # Запрет на фрагментацию идентичности
            conflicting = {"schizophren", "split", "fragment", "disjoint"}
            return not any(word in payload_str for word in conflicting)

        # === Existential Domain ===
        elif inv_id == "dialogicity":
            # Требует признания Другого
            markers = {"you", "other", "dialogue", "listen", "respond"}
            return any(word in payload_str for word in markers)

        elif inv_id == "solitary_solidarity":
            # Запрет на изоляцию без связи
            isolated = {"alone", "only me", "no one else", "solipsism"}
            connected = {"together", "community", "share", "belong"}
            if any(word in payload_str for word in isolated):
                return any(word in payload_str for word in connected)
            return True

        # === Archetypal & Structural ===
        elif inv_id == "polarity":
            # Требует баланса противоположностей
            return ("and" in payload_str) or ("but" in payload_str)

        elif inv_id == "dynamic_equilibrium":
            # Высокая онтологическая плотность должна быть уравновешена
            if ontological_density > 0.8:
                return social_proximity > 0.5  # Требует близкого контекста
            return True

        # === Fallback: по умолчанию — соблюдён ===
        # В реальной системе здесь будет вызов внешнего валидатора
        return True
```