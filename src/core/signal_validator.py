# SPDX-License-Identifier: GPL-3.0-only
"""
Валидация входных сигналов по JSON-схеме signal-schema.json.
Интегрируется с NoemaFast: только структурно корректные сигналы допускаются.
"""

import json
import jsonschema
from pathlib import Path


class SignalValidator:
    _schema = None

    @classmethod
    def load_schema(cls):
        if cls._schema is None:
            schema_path = Path(__file__).parent.parent.parent / "specs" / "signal-schema.json"
            with open(schema_path, "r", encoding="utf-8") as f:
                cls._schema = json.load(f)
        return cls._schema

    @classmethod
    def validate(cls, signal: dict) -> bool:
        """
        Проверяет сигнал на соответствие внешней схеме.
        Возвращает True, если валиден; иначе вызывает jsonschema.ValidationError.
        """
        schema = cls.load_schema()
        jsonschema.validate(instance=signal, schema=schema)
        return True  # Явный успех; исключение = провал