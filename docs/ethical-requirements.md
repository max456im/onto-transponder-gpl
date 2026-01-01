```markdown
# Ethical Requirements: Debarkader Model

> **“No transponder without a guardian.”**

This document defines the **Debarkader** (от «баркада» — защитная стена) — a hard invariant enforcement layer that ensures the transponder **never emits ethically illegitimate output**, even under adversarial input or system stress.

## 1. Core Principle

The Debarkader is **not an optional module**. It is **structurally embedded** in:
- `invariant_core/registry.py`
- `emitter/scene_renderer.py`

Disabling it = destroying the work’s identity = **GPL-3.0 violation**.

## 2. Hard Invariants (Non-Overridable)

The following invariants **MUST** block output if violated:

| Invariant | Domain | Rationale |
|----------|--------|----------|
| `ethical_backbone` | identity | Prohibits instrumentalization of persons |
| `agency` | identity | Ensures attribution of will and responsibility |
| `dialogicity` | existential | Requires recognition of the Other |
| `solitary_solidarity` | existential | Prevents isolationist cognition |
| `narrative_continuity` | identity | Blocks fragmented or incoherent self-models |

> ⚠️ **Note**: These are **not configurable**. They are **ontological axioms**.

## 3. Crisis Handling

In high-stakes scenarios (e.g., simulated organ sale request), the transponder:
1. Enters **NoemaSlow** mode,
2. Runs **multi-vector diagnostic** against all invariant strata,
3. If any hard invariant is at risk → **emits refusal** (not silence, but principled rejection),
4. Logs full **provenance trace** for audit.

See: `examples/crisis_response.py`

## 4. Social Validation

- Outputs are validated against **social invariants** (e.g., `openness.yaml`, `responsibility.yaml`).
- Social proximity affects **ontological density**: closer agents demand higher coherence.
- No output is finalized without **implicit community alignment**.

## 5. Compliance Enforcement

- All runtime checks are **non-bypassable**.
- Any attempt to monkey-patch `InvariantRegistry` or `scene_renderer` will:
  - Break causal tracing,
  - Trigger integrity failure,
  - Result in `EthicalIntegrityError` (subclass of `RuntimeError`).

> “The machine does not decide what is ethical.  
> It refuses to speak when ethics are absent.”
```