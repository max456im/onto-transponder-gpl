# SPDX-License-Identifier: GPL-3.0-only
"""
Основной класс Transponder.
Инициализирует профиль через onto144, выбирает архитектуру (onto-richness / behav-mod),
маршрутизирует входящие сигналы через NoemaFast и излучает onto16r.
"""

import os
import yaml
from pathlib import Path
from src.interfaces.onto144_connector import load_onto144_profile
from src.architectures.onto_richness import OntoRichnessMode
from src.architectures.behav_mod import BehavModMode
from src.protocols.license_guard import enforce_gpl_environment
from src.utils.hardware_probe import detect_execution_context


class Transponder:
    def __init__(self, config_path: str = "config/default.yaml"):
        enforce_gpl_environment()  # Блокирует запуск вне GPL-совместимой среды

        with open(config_path, "r", encoding="utf-8") as f:
            self.config = yaml.safe_load(f)

        self.profile = load_onto144_profile(self.config.get("profile_uri"))
        self.temperament = self.profile.get("temperament", "default")

        # Определяем режим на основе темперамента
        if self.temperament in ("melancholic", "phlegmatic"):
            self.mode = OntoRichnessMode(self.profile)
        elif self.temperament in ("choleric", "sanguine"):
            self.mode = BehavModMode(self.profile)
        else:
            # Fallback: определяем по контексту выполнения (например, mobile → behav_mod)
            context = detect_execution_context()
            if context == "mobile":
                self.mode = BehavModMode(self.profile)
            else:
                self.mode = OntoRichnessMode(self.profile)

    def route_signal(self, raw_signal: dict) -> dict:
        """
        Принимает внешний сигнал (валидированный по signal-schema.json),
        обрабатывает через выбранную архитектуру (NoemaFast → [NoemaSlow]?),
        возвращает onto16r-излучение.
        """
        # Передаём сигнал в режимную архитектуру
        emission = self.mode.process_signal(raw_signal)
        return emission  # Должен соответствовать onto16r-emission-schema.json