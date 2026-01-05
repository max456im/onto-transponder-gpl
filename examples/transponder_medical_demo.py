#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-only
# Copyright (C) 2026 Maksim Zapevalov
#
# Medical transponder demo: ontologically reflective (melancholic) mode
# No user biometrics. Identity via onto144 profile only.
# High-stakes context → VMA-signed emission.

import os
import sys
from pathlib import Path

# Enforce GPL compliance early
from src.protocols.license_guard import enforce_gpl_only
enforce_gpl_only()

# Core components
from src.core.transponder import Transponder
from src.protocols.vma_signer import sign_emission_for_context

def main():
    # Use static medical profile (melancholic → onto-richness)
    profile_path = Path(__file__).parent.parent / "config" / "profiles" / "medical_melancholic.yaml"
    if not profile_path.exists():
        print("ERROR: Medical profile not found. Expected:", profile_path)
        sys.exit(1)

    # Initialize transponder in reflective (melancholic) mode
    transponder = Transponder(
        profile_path=str(profile_path),
        architecture_hint="melancholic"  # forces onto_richness.py
    )

    # Simulate diagnostic signal (NoemaFast format)
    diagnostic_signal = {
        "signal_id": "DX-2026-001",
        "domain": "clinical_advice",
        "content": {
            "symptom_cluster": ["fever", "cough", "fatigue"],
            "urgency": "medium",
            "context": "telemedicine_consult"
        },
        "trust_level": "verified_professional"
    }

    # Process through NoemaFast → NoemaSlow pipeline
    emission = transponder.process(diagnostic_signal)

    # High-stakes context → VMA signature required
    signed_emission = sign_emission_for_context(
        emission=emission,
        context="medical_recommendation",
        stake_level="high"
    )

    print("✅ Medical transponder emission (VMA-signed):")
    print(signed_emission)

if __name__ == "__main__":
    main()