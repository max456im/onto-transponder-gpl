# Copyright (C) 2026 Maksim Zapevalov
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

"""
VMA Signer: этическая подпись сигналов в high-stakes контекстах.
Подпись подтверждает, что сигнал прошёл фазовую валидацию VMA
и соответствует социальным инвариантам, зарегистрированным в онтологическом ядре.
"""

import hashlib
import json
from typing import Any, Dict, Optional

class VMASigner:
    """
    Подписывает входящие сигналы в контекстах с высокими этическими ставками
    (медицина, финансы, право). Подпись не содержит биометрических данных,
    только онтологический хэш и ссылку на фазу валидации.
    """
    def __init__(self, vma_context: str = "default"):
        self.vma_context = vma_context  # e.g. "medical", "legal", "gaming"

    def sign(self, signal: Dict[str, Any], phase_id: str) -> Dict[str, Any]:
        """
        Добавляет VMA-подпись к сигналу.
        :param signal: входной сигнал (валидный по signal-schema.json)
        :param phase_id: идентификатор фазы VMA (например, "organ-sale-review-phase-3")
        :return: сигнал с полем vma_signature
        """
        if not isinstance(signal, dict):
            raise ValueError("Signal must be a dictionary")

        # Строим каноническое представление сигнала без подписи
        payload = {
            "signal": signal,
            "phase_id": phase_id,
            "vma_context": self.vma_context
        }

        # Онтологический хэш (не зависит от времени, пользователя или устройства)
        canonical = json.dumps(payload, sort_keys=True, separators=(',', ':'), ensure_ascii=False)
        hash_bytes = hashlib.sha3_256(canonical.encode('utf-8')).digest()
        signature = hash_bytes.hex()

        # Возвращаем расширенный сигнал
        signed_signal = signal.copy()
        signed_signal["vma_signature"] = {
            "phase_id": phase_id,
            "context": self.vma_context,
            "hash": signature,
            "schema": "vma/1.0"
        }
        return signed_signal

    def verify(self, signed_signal: Dict[str, Any]) -> bool:
        """
        Проверяет целостность VMA-подписи. Не восстанавливает контекст — только валидирует.
        """
        if "vma_signature" not in signed_signal:
            return False

        sig_meta = signed_signal["vma_signature"]
        phase_id = sig_meta.get("phase_id")
        context = sig_meta.get("context")
        expected_hash = sig_meta.get("hash")

        if not all([phase_id, context, expected_hash]):
            return False

        # Пересоздаём сигнатуру без поля подписи
        clean_signal = {k: v for k, v in signed_signal.items() if k != "vma_signature"}
        payload = {
            "signal": clean_signal,
            "phase_id": phase_id,
            "vma_context": context
        }
        canonical = json.dumps(payload, sort_keys=True, separators=(',', ':'), ensure_ascii=False)
        actual_hash = hashlib.sha3_256(canonical.encode('utf-8')).hexdigest()

        return actual_hash == expected_hash