```python
# SPDX-License-Identifier: GPL-3.0-or-later
# Copyright (C) 2026 OntoCoder Collective

import json
from src.ontotransponder.ingress import IngressHandler

def test_json_ingress_dict():
    handler = IngressHandler()
    raw = {"query": "Who am I?", "user_id": "test"}
    result = handler.parse(raw)
    assert result is not None
    assert result["type"] == "json_query"
    assert result["content"] == raw

def test_json_ingress_string():
    handler = IngressHandler()
    raw = '{"command": "reflect", "depth": 2}'
    result = handler.parse(raw)
    assert result is not None
    assert result["type"] == "json_query"
    assert result["content"] == json.loads(raw)

def test_websocket_ingress():
    handler = IngressHandler()
    raw = {"ws_event": "user_message", "text": "Hello", "session": "abc123"}
    result = handler.parse(raw)
    assert result is not None
    assert result["type"] == "websocket_event"
    assert result["content"] == raw

def test_binary_ingress():
    handler = IngressHandler()
    raw = b"\x00\x01\x02\x03"
    result = handler.parse(raw)
    assert result is not None
    assert result["type"] == "binary_blob"
    assert result["content"]["size_bytes"] == 4
    assert len(result["content"]["sample_prefix"]) == 32  # 16 bytes → 32 hex chars

def test_unsupported_input():
    handler = IngressHandler()
    assert handler.parse(42) is None
    assert handler.parse([1, 2, 3]) is None
```