```markdown
# Architecture Overview: onto-transponder

## 1. Core Layers

### NoemaFast → NoemaSlow Transition
- **NoemaFast**: Reactive, low-latency ingestion (e.g., user input, sensor data).
  - Handled by `ingress/` modules.
  - Normalized into `onto16` format with metadata.
- **NoemaSlow**: Reflective, socially validated cognition.
  - Internal reasoning occurs in `onto8`.
  - Governs narrative depth, ethical alignment, and temporal coherence.
  - Activated via **slowing through reflection**—a phase transition triggered by ambiguity, crisis, or high social proximity.

This transition is **not optional**; it is a structural requirement for invariant compliance.

## 2. Data Flow

```
Raw Input → Ingress → onto16 Normalization → Invariant Validation → (NoemaSlow if needed) → Scene Rendering → Output
                     ↑
              Provenance Tracing (source, route, social context)
```

- **onto16**: External representation. Includes social markers, energy metadata (internal only), and causal anchors.
- **onto8**: Internal reflective space. Never exposed directly. Handles irrational expressions, memory integration, and self-model stabilization.

## 3. Invariant Enforcement

- All invariants are loaded at startup via `InvariantRegistry`.
- Each is validated **syntactically** (against `invariant-schema-spec.yaml`) and **semantically** (via embedded logic in `registry.py`).
- **Hard constraints** (e.g., `ethical_backbone.yaml`) **block emission** if violated.

## 4. Emitter Design

- `scene_renderer.py` produces **coherent scenes**:
  - Full causal networks (no orphaned facts),
  - Narrative continuity,
  - Social invariants preserved,
  - No devaluation through energy extraction (energy values are internal only).

## 5. Modularity

- Ingress, normalizers, and emitters are pluggable.
- Invariant sets can be extended—but **not weakened**—without violating license terms.

> “The transponder does not interpret. It reflects what is ontologically permissible.”
```