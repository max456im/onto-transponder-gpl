# SPDX-License-Identifier: GPL-3.0-only
"""
Мост приёма onto16r-сигналов от внешнего эмиттера.
Не хранит и не идентифицирует отправителя — работает только с ontologically valid emission.
"""

import json
from typing import Dict, Any, Optional
from ..protocols.vma_signer import VMASigner
from ..utils.crypto_utils import decrypt_onto16r


class EmitterBridge:
    def __init__(self, trust_level: int = 1):
        self.trust_level = trust_level
        self.vma_signer = VMASigner()

    def receive_onto16r(self, encrypted_payload: bytes, signature: str = None) -> Optional[Dict[str, Any]]:
        """
        Принимает зашифрованный onto16r-сигнал от эмиттера.
        Валидирует подпись VMA (если в high-stakes контексте).
        Расшифровывает в соответствии с уровнем доверия.
        """
        # При высоком уровне доверия или high-stakes — требуется VMA-подпись
        if self.trust_level >= 3 and signature:
            if not self.vma_signer.verify_signature(encrypted_payload, signature):
                return None  # Невалидная подпись — отклонить

        try:
            decrypted = decrypt_onto16r(encrypted_payload, trust_level=self.trust_level)
            onto16r = json.loads(decrypted)
            # Онтологическая валидация происходит далее в signal_validator.py
            return onto16r
        except Exception:
            return None