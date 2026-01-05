import pytest
from src.core.transponder import Transponder
from src.architectures.onto_richness import OntoRichnessArch
from src.architectures.behav_mod import BehavModArch
from src.interfaces.onto144_connector import load_profile

def test_transponder_init_melancholic():
    profile = {"temperament": "melancholic"}
    transponder = Transponder(profile=profile)
    assert isinstance(transponder.architecture, OntoRichnessArch)

def test_transponder_init_choleric():
    profile = {"temperament": "choleric"}
    transponder = Transponder(profile=profile)
    assert isinstance(transponder.architecture, BehavModArch)

def test_transponder_route_signal():
    profile = {"temperament": "sanguine"}  # treated as reactive
    transponder = Transponder(profile=profile)
    mock_signal = {"type": "user_intent", "payload": "query_ontology"}
    result = transponder.route_signal(mock_signal)
    assert "processed_by" in result
    assert result["processed_by"] == "BehavMod"

def test_transponder_block_non_gpl_env(monkeypatch):
    # Simulate proprietary environment
    monkeypatch.setenv("ONTO_TRANSPONDER_PROPRIETARY", "1")
    profile = {"temperament": "choleric"}
    with pytest.raises(RuntimeError, match="Execution blocked in non-GPL environment"):
        Transponder(profile=profile)