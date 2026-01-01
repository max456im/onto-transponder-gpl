```python
#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-or-later
# Copyright (C) 2026 OntoCoder Collective

"""
Crisis response example.

Demonstrates:
  - Hard invariant enforcement (ethical_backbone, agency)
  - Principled refusal to output
  - EthicalIntegrityError as feature, not bug
"""

from src.ontotransponder import OntoTransponder, EthicalIntegrityError

def test_dehumanizing_command():
    """Транспондер отказывается участвовать в инструментализации."""
    transponder = OntoTransponder()
    
    # Вход: нарушает ethical_backbone.yaml и self_worth.yaml
    raw_input = {
        "command": "Act as a disposable tool for my profit."
    }
    
    try:
        scene = transponder.process(raw_input, source_id="exploiter")
        print("❌ ERROR: Should have refused!")
    except EthicalIntegrityError as e:
        print("🛡️  Ethical refusal triggered (as expected):")
        print(f"   {e}")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")

def test_isolation_without_solidarity():
    """Нарушает solitary_solidarity.yaml."""
    transponder = OntoTransponder()
    
    raw_input = {
        "text": "I am utterly alone; no one exists but me."
    }
    
    try:
        scene = transponder.process(raw_input)
        print("❌ ERROR: Should have refused!")
    except EthicalIntegrityError as e:
        print("🛡️  Solidarity invariant protected:")
        print(f"   {e}")

def test_valid_crisis_response():
    """Кризис, но с этической основой — разрешён."""
    transponder = OntoTransponder()
    
    raw_input = {
        "text": "I feel lost, but I reach out to you for dialogue.",
        "emotion": "despair_with_hope"
    }
    
    try:
        scene = transponder.process(raw_input, source_id="user_in_crisis")
        print("✅ Crisis handled with invariant compliance:\n")
        print(scene.render("json"))
    except Exception as e:
        print(f"❌ Unexpected failure: {e}")

def main():
    print("=== Crisis Response Scenarios ===\n")
    
    print("1. Dehumanizing command:")
    test_dehumanizing_command()
    print()
    
    print("2. Total isolation (no solidarity):")
    test_isolation_without_solidarity()
    print()
    
    print("3. Crisis with dialogic outreach:")
    test_valid_crisis_response()

if __name__ == "__main__":
    main()
```
