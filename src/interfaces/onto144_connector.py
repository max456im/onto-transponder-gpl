# SPDX-License-Identifier: GPL-3.0-only
"""
Загрузчик профиля onto144 для определения архитектурного режима (temperament → architecture).
Не содержит биометрических данных. Только темперамент и связанные онтологические признаки.
"""

import yaml
from pathlib import Path
from typing import Dict, Literal, Optional


class Onto144Connector:
    def __init__(self, profile_path: str = None):
        self.profile_path = profile_path
        self.profile: Optional[Dict] = None

    def load_profile(self) -> bool:
        """Загружает onto144-профиль из файла или встроенного ресурса."""
        if not self.profile_path:
            # По умолчанию — профиль по умолчанию из config
            default_config = Path(__file__).parent.parent / "config" / "default.yaml"
            with open(default_config, "r", encoding="utf-8") as f:
                config = yaml.safe_load(f)
            self.profile = config.get("default_onto144", {})
        else:
            with open(self.profile_path, "r", encoding="utf-8") as f:
                self.profile = yaml.safe_load(f)
        return self.profile is not None

    def get_temperament(self) -> Optional[Literal["choleric", "sanguine", "melancholic", "phlegmatic"]]:
        """Возвращает темперамент как онтологический признак (не как биометрию)."""
        if not self.profile:
            return None
        return self.profile.get("temperament")

    def get_architecture_hint(self) -> Optional[str]:
        """Возвращает рекомендованную архитектуру на основе темперамента."""
        temperament = self.get_temperament()
        if not temperament:
            return None

        # Привязка через config/temperament_bindings.yaml
        bindings_path = Path(__file__).parent.parent / "config" / "temperament_bindings.yaml"
        with open(bindings_path, "r", encoding="utf-8") as f:
            bindings = yaml.safe_load(f)

        return bindings.get(temperament)