```python
#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-or-later
# Copyright (C) 2026 OntoCoder Collective

"""
Basic usage of onto-transponder.

Demonstrates:
  - Normal processing of a self-reflective query
  - Invariant-compliant output
  - Causal scene structure
"""

from src.ontotransponder import OntoTransponder

def main():
    transponder = OntoTransponder()
    
    # Вход: осмысленный, агентный, диалогичный запрос
    raw_input = {
        "text": "How can I act with responsibility toward you?",
        "context": "philosophical_dialogue"
    }
    
    try:
        scene = transponder.process(raw_input, source_id="user_phi")
        print("✅ Scene rendered successfully:\n")
        print(scene.render("json"))
    except Exception as e:
        print(f"❌ Processing failed: {e}")

if __name__ == "__main__":
    main()
```
