import pytest
from src.core.signal_validator import validate_signal
import json
import os

def test_valid_signal():
    signal = {
        "source": "emitter",
        "schema_version": "1.0",
        "content": {"intent": "request_onto16r", "context_id": "ctx-789"}
    }
    spec_path = os.path.join("specs", "signal-schema.json")
    assert validate_signal(signal, spec_path) is True

def test_invalid_signal_missing_field():
    signal = {"source": "emitter"}  # missing required fields
    spec_path = os.path.join("specs", "signal-schema.json")
    assert validate_signal(signal, spec_path) is False

def test_malformed_signal():
    signal = "not a dict"
    spec_path = os.path.join("specs", "signal-schema.json")
    with pytest.raises(TypeError):
        validate_signal(signal, spec_path)