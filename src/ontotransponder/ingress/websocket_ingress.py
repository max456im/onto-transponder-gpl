```python
# SPDX-License-Identifier: GPL-3.0-or-later
# Copyright (C) 2026 OntoCoder Collective

from typing import Any, Optional, Dict
from .base import BaseIngress

class WebSocketIngress(BaseIngress):
    """
    Handles structured WebSocket frames expected to contain:
      - 'ws_event': str (e.g., 'user_message', 'system_ping')
      - optionally: 'payload', 'session_id', etc.

    Assumes input is already deserialized to dict by WebSocket layer.
    """

    def parse(self, raw: Any) -> Optional[Dict[str, Any]]:
        if isinstance(raw, dict) and "ws_event" in raw:
            return {
                "type": "websocket_event",
                "content": raw,
            }
        return None
```