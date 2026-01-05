# onto-transponder-gpl/src/architectures/behav_mod.py
# Copyright (C) 2026 [Your Name]
# Licensed under GPL-3.0-only

from ..core.signal_validator import validate_signal
from ..protocols.vma_signer import sign_with_vma_if_needed


class BehavMod:
    """Сангвинико-холерическая архитектура:
       вход NoemaSlow → быстрая реакция через NoemaFast.
       Приоритет: адаптация, скорость, социальное взаимодействие.
    """

    def __init__(self, profile):
        self.profile = profile
        self.mode = "reactive"
        self.context_short_memory = []

    def process(self, raw_signal):
        """Обработка сигнала с акцентом на быстрый вывод."""
        if not validate_signal(raw_signal, schema="signal-schema.json"):
            raise ValueError("Invalid input signal for BehavMod")

        # Шаг 1: Восприятие как каузальный фрагмент (NoemaSlow-имитация)
        slow_hint = self._simulate_slow_context(raw_signal)

        # Шаг 2: Генерация быстрого ответа (NoemaFast)
        fast_response = self._noema_fast_emit(slow_hint)

        # Шаг 3: VMA-подпись при необходимости
        if self._is_high_stakes(fast_response):
            fast_response = sign_with_vma_if_needed(fast_response, profile=self.profile)

        return fast_response

    def _simulate_slow_context(self, signal):
        # Имитация глубокого контекста на основе профиля и истории
        recent = self.context_short_memory[-3:] if self.context_short_memory else []
        return {
            "profile_bias": self.profile.get("activity_vector", []),
            "recent_interactions": recent,
            "signal_intent": signal.get("intent"),
            "social_proximity": signal.get("social_proximity", "neutral")
        }

    def _noema_fast_emit(self, context):
        # Генерация быстрого онтологического излучения (onto16r-совместимого)
        base_emission = {
            "intent_response": self._choose_intent_response(context),
            "urgency": "high" if context["social_proximity"] == "close" else "medium",
            "energy_state": self._estimate_energy(context),
            "timestamp": context.get("signal_timestamp", None)
        }
        # Сохраняем в краткосрочную память
        self.context_short_memory.append(base_emission)
        if len(self.context_short_memory) > 5:
            self.context_short_memory.pop(0)
        return base_emission

    def _choose_intent_response(self, ctx):
        # Простая реактивная логика
        intent = ctx["signal_intent"]
        if "query" in intent:
            return "offer_option"
        elif "request" in intent:
            return "commit_action"
        else:
            return "acknowledge"

    def _estimate_energy(self, ctx):
        # Энергия как функция социальной близости и активности (без численной оценки!)
        # Возвращает категориальное состояние, а не скаляр
        proximity = ctx["social_proximity"]
        return "engaged" if proximity == "close" else "neutral"

    def _is_high_stakes(self, response):
        return "commit_action" in response.get("intent_response", "")