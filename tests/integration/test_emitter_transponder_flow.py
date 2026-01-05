import pytest
import json
import os
from src.interfaces.emitter_bridge import receive_onto16r
from src.core.transponder import Transponder
from src.interfaces.onto144_connector import load_profile

# Helper: mock emitter output
@pytest.fixture
def mock_emitter_onto16r():
    return {
        "onto16r": {
            "subject_id": "sub-001",
            "energy_state": "neutral",
            "social_proximity": "public",
            "expressions": ["R12", "I07"]  # rational + irrational
        },
        "signature": "VMA-signed-fake"
    }

def test_full_emitter_to_transponder_flow(mock_emitter_onto16r):
    # Simulate loading a melancholic profile
    profile = {"temperament": "melancholic", "subject_id": "sub-001"}
    
    # Receive and validate emission
    emission = mock_emitter_onto16r
    assert "onto16r" in emission

    # Initialize transponder
    transponder = Transponder(profile=profile)

    # Route through architecture
    result = transponder.process_emission(emission["onto16r"])
    
    # Expect reflective processing
    assert result["mode"] == "NoemaSlow"
    assert result["causal_reconstruction"] is not None
    assert "stabilized_model" in result