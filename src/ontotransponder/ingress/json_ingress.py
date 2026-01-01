```python
# SPDX-License-Identifier: GPL-3.0-or-later
# Copyright (C) 2026 OntoCoder Collective

import json
from typing import Any, Optional, Dict
from .base import BaseIngress

class JSONIngress(BaseIngress):
    """
    Handles:
      - dict (already parsed JSON)
      - str (valid JSON string)
    """

    def parse(self, raw: Any) -> Optional[Dict[str, Any]]:
        if isinstance(raw, dict):
            return {
                "type": "json_query",
                "content": raw,
            }
        elif isinstance(raw, str):
            try:
                parsed = json.loads(raw)
                if isinstance(parsed, dict):
                    return {
                        "type": "json_query",
                        "content": parsed,
                    }
            except (json.JSONDecodeError, TypeError):
                pass
        return None
```