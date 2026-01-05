#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-only
# Copyright (C) 2026 Maksim Zapevalov 
#
# Gaming transponder demo: reactive (choleric/sanguine) mode
# Optimized for low-latency interaction. No persistent user data.
# Emission in onto16r format for game engine consumption.

import os
import sys
from pathlib import Path

# Enforce GPL compliance early
from src.protocols.license_guard import enforce_gpl_only
enforce_gpl_only()

from src.core.transponder import Transponder

def main():
    # Use dynamic gaming profile (choleric → behav_mod)
    profile_path = Path(__file__).parent.parent / "config" / "profiles" / "gamer_choleric.yaml"
    if not profile_path.exists():
        print("WARN: Gaming profile not found. Using default choleric binding.")
        # fallback: rely on config/temperament_bindings.yaml
        profile_path = None

    # Initialize in reactive (choleric) mode
    transponder = Transponder(
        profile_path=str(profile_path) if profile_path else None,
        temperament_override="choleric"  # forces behav_mod.py
    )

    # Simulate in-game event (fast-paced, NoemaFast input)
    game_event = {
        "event_id": "GAME-QUEST-77",
        "domain": "narrative_progression",
        "content": {
            "player_choice": "confront_villain",
            "era": "shadow_reign",
            "narrative_phase": "climax"
        },
        "latency_budget_ms": 50
    }

    # Process via NoemaSlow → NoemaFast (reactive loop)
    emission = transponder.process(game_event)

    print("🎮 Gaming transponder emission (onto16r):")
    print(emission)

if __name__ == "__main__":
    main()