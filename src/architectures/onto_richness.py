# onto-transponder-gpl/src/architectures/onto_richness.py
# Copyright (C) 2026 [Your Name]
# Licensed under GPL-3.0-only

from ..core.signal_validator import validate_signal
from ..protocols.vma_signer import sign_with_vma_if_needed


class OntoRichness:
    """Меланхолическая архитектура: 
       вход NoemaFast → внутренняя обработка → выход через NoemaSlow.
       Приоритет: глубина, причинность, ретроспекция.
    """

    def __init__(self, profile):
        self.profile = profile
        self.mode = "reflective"
        self.causal_buffer = []

    def process(self, raw_signal):
        """Обработка входного сигнала через рефлексивную петлю."""
        if not validate_signal(raw_signal, schema="signal-schema.json"):
            raise ValueError("Invalid input signal for OntoRichness")

        # Шаг 1: Быстрое восприятие (NoemaFast)
        fast_context = self._noema_fast_decode(raw_signal)

        # Шаг 2: Погружение в каузальную реконструкцию (NoemaSlow)
        slow_context = self._noema_slow_reconstruct(fast_context)

        # Шаг 3: Этическая фильтрация через VMA (если high-stakes)
        if self._is_high_stakes(slow_context):
            slow_context = sign_with_vma_if_needed(slow_context, profile=self.profile)

        return slow_context

    def _noema_fast_decode(self, signal):
        # Простая трансляция в промежуточное состояние
        return {
            "intent": signal.get("intent"),
            "urgency": signal.get("urgency", "low"),
            "source_trust": signal.get("source_trust", 0.5),
            "timestamp": signal.get("ts")
        }

    def _noema_slow_reconstruct(self, fast_context):
        # Восстановление причинно-следственных связей
        self.causal_buffer.append(fast_context)
        if len(self.causal_buffer) > 10:
            self.causal_buffer.pop(0)

        # Пример: взвешенная реконструкция истории
        reconstructed = {
            "causal_chain": self.causal_buffer.copy(),
            "stability_score": self._compute_stability(),
            "reflective_verdict": self._generate_verdict()
        }
        return reconstructed

    def _compute_stability(self):
        # Простой показатель онтологической устойчивости
        return sum(ctx["source_trust"] for ctx in self.causal_buffer) / max(len(self.causal_buffer), 1)

    def _generate_verdict(self):
        # Пример: вердикт через внутреннюю онтологию
        return "reflective_accept" if self._compute_stability() > 0.7 else "causal_inquiry_needed"

    def _is_high_stakes(self, context):
        # Определяет, требует ли контекст VMA-подписи
        return any(
            key in str(context).lower() 
            for key in ("medical", "consent", "transaction", "identity")
        )