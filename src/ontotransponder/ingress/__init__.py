```python
# SPDX-License-Identifier: GPL-3.0-or-later
# Copyright (C) 2026 OntoCoder Collective

from .base import BaseIngress
from .json_ingress import JSONIngress
from .binary_ingress import BinaryIngress
from .websocket_ingress import WebSocketIngress

__all__ = [
    "BaseIngress",
    "JSONIngress",
    "BinaryIngress",
    "WebSocketIngress",
    "IngressHandler",
]


class IngressHandler:
    """
    Orchestrator for ingress parsers.
    Tries parsers in order of specificity (JSON → WebSocket → Binary).
    """

    def __init__(self):
        self.parsers = [
            JSONIngress(),
            WebSocketIngress(),
            BinaryIngress(),
        ]

    def parse(self, raw: object) -> dict | None:
        """
        Parse raw input using the first compatible ingress parser.

        Returns:
            dict: Normalized ingress result with 'type' and 'content' keys
            None: If no parser supports the input
        """
        for parser in self.parsers:
            result = parser.parse(raw)
            if result is not None:
                return result
        return None
```