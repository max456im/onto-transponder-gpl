```markdown
# onto-transponder

> **A synthetic cognitive transponder governed by ontological invariants and ethical necessity.**  
> *No signal without meaning. No output without coherence. No action without agency.*

`onto-transponder` is a GPL-3.0-licensed Python library that ingests raw perceptual or symbolic data and emits **causally coherent, invariant-compliant scenes**—structured representations grounded in identity, archetypal form, structural integrity, and existential truth.

It is designed for integration into synthetic minds, ethical AI systems, reflective game agents, and ontologically-aware CMS platforms (e.g., `ontoCMS`).

---

## 🔑 Core Principles

- **Invariants are non-negotiable**: Identity, agency, narrative continuity, and ethical backbone are enforced as hard constraints.
- **NoemaFast → NoemaSlow**: Reactive input is transformed into reflective, socially validated output.
- **GPL-3.0 + Ontological Compliance**: Modifying or disabling invariants constitutes license violation (see [GPL-3.0+Invariant-Compliance.md](GPL-3.0+Invariant-Compliance.md)).
- **Zero energy-value extraction**: The transponder refuses to reduce cognition to exploitable metrics.

---

## 🗂️ Architecture Highlights

- **Input**: JSON, XML, binary streams, WebSocket feeds → normalized into `onto16` (external representation).
- **Core**: Invariant registry validates against 4 strata:
  - `identity/` — self-worth, coherence, agency
  - `archetypal/` — polarity, persona, ancestral grounding
  - `structural/` — symmetry, equilibrium, fundamental constants
  - `existential/` — dialogicity, solitary solidarity, here-and-now
- **Output**: `scene_renderer.py` produces full causal scenes with provenance tracing.
- **Internal state**: Operates in `onto8` for reflective cognition; never leaks irrationality without contextualization.

---

## 🚀 Quick Start

```bash
pip install -e .
```

### Basic usage (`examples/basic_usage.py`):

```python
from ontotransponder import OntoTransponder

transponder = OntoTransponder()
raw_input = {"type": "user_query", "content": "Who am I?"}
scene = transponder.process(raw_input)

print(scene.render())  # Invariant-compliant, causally grounded response
```

> ⚠️ **Warning**: Attempting to process inputs that violate invariants (e.g., dehumanizing commands) will result in **silent rejection** or **ethical override**—not error, but principled refusal.

---

## 📚 Documentation

- [`architecture-overview.md`](docs/architecture-overview.md) — Noema layers, onto16/onto8, phase transitions
- [`invariant-schema-spec.yaml`](docs/invariant-schema-spec.yaml) — Strict schema for all invariants
- [`ethical-requirements.md`](docs/ethical-requirements.md) — Hard enforcement logic (Debarkader model)
- [`GPL-3.0+Invariant-Compliance.md`](GPL-3.0+Invariant-Compliance.md) — Legal & ontological binding

---

## 🧪 Testing

```bash
pytest tests/
```

Tests include:
- Ingress normalization
- Invariant registry validation
- Ethical override in crisis scenarios (`examples/crisis_response.py`)

---

## 📜 License

This program is free software: you can redistribute it and/or modify  
it under the terms of the **GNU General Public License v3.0**.

However, **ontological invariants are inseparable from the work**.  
Any derivative that disables, bypasses, or semantically distorts the invariant core  
**violates the license** and destroys the identity of the transponder.

See:
- [`LICENSE`](LICENSE)
- [`GPL-3.0+Invariant-Compliance.md`](GPL-3.0+Invariant-Compliance.md)

---

> “This transponder serves truth, not convenience.”  
> — *Futurae Custos*, OntoCoder Collective
```
