# IC Pressure Test Workspace

## What This Is
A workspace for stress-testing an investment memo before committee. It reads the memo, the model outputs of record, diligence evidence, and IC precedent, then produces the questions, fragile assumptions, missing evidence, and decision conditions the deal team should resolve before the IC meeting.

This is not the IC gate and not a memo-authoring tool. The deal platform owns workflow state. The underwriting model owns return math. This workspace owns the judgment layer: what deserves challenge, what would change the decision, and what the committee should condition if it proceeds.

## Structure
```
ic-pressure-test/
  CLAUDE.md
  CONTEXT.md
  01_memo/CONTEXT.md
  02_challenge/CONTEXT.md
  03_conditions/CONTEXT.md
  04_capture/CONTEXT.md
  _config/
  _store/
```

## Key Decisions
- **Pressure test before precedent capture.** A live IC challenge and the retrospective IC memory loop are related but distinct. This workspace improves the pending decision; `firm-memory-loop` captures what was learned after the decision.
- **Questions over answers.** The highest-value output is often the question that prevents a weak approval, not a polished memo paragraph.
- **No model math.** Return outputs, sensitivities, debt sizing, and valuation come from the model of record. AI challenges assumptions and evidence, but does not recompute them.

## Constraints That Apply
Universal **06 (Layer Triage)** and **09 (Platform Boundary)**, plus **02 (Output Drift)**, **08 (Handoff Readiness)**, and **10 (Source Provenance)**.

## Layer Annotations
CLAUDE.md is L0. CONTEXT.md is L1. Stage contracts are L2. `_config/` and `_store/` are L3. The memo, diligence evidence, model outputs, and stage outputs are L4.
