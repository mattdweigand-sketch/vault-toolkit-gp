# Deal Pipeline Workspace

## What This Is
A workspace for running a single acquisition from sourcing through close. Built for commercial real estate GPs (and PE deal teams) who move an opportunity through screening, diligence, investment committee, and closing with a decision checkpoint at each stage. Each live deal gets a copy of this workspace.

## Current State
- This is a reference architecture. No active deal.
- To use: copy the folder, rename to the deal, populate _config with the opportunity and deal terms.

## Structure
```
deal-pipeline/
  CLAUDE.md              # You are here.
  CONTEXT.md             # Deal workflow.
  01_sourcing/
    CONTEXT.md           # Stage contract: screen the opportunity, set the thesis.
    output/              # Screen memo, investment thesis, go/no-go.
  02_diligence/
    CONTEXT.md           # Stage contract: underwrite and run diligence.
    output/              # Underwriting model summary, DD findings, risk register.
  03_ic/
    CONTEXT.md           # Stage contract: internal review then investment committee.
    output/              # IC memo, internal review, IC decision.
  04_close/
    CONTEXT.md           # Stage contract: close and transition to asset management.
    output/              # Closing checklist, funding confirmation, AM handoff.
  _config/               # Opportunity details, deal terms, investment thesis.
  _references/           # Market comps, underwriting standards, prior deals.
```

## How to Use
1. Copy this folder. Rename it to the deal (e.g., 1200-market-st-acquisition-q2-2026).
2. Populate _config/ with the opportunity and deal terms.
3. Start in 01_sourcing. This stage produces the screen and investment thesis that drive everything else.
4. Move through stages sequentially. Human review between every stage. When diligence opens on an unvetted data room, run a provenance pass first (Constraint 10) to inventory and rank the files before underwriting.
5. Investment committee review happens in stage 03. Internal underwriting review also happens here before anything goes to the committee.
6. Stage 04 is not just "wire the funds." It includes the closing checklist and a clean handoff to asset management.

## Key Decisions
- **Four stages, not three.** The IC stage is separate from diligence because combining them creates pressure to skip independent review when a deadline or a competitive process is tight. A separate stage makes committee review a non-negotiable gate.
- **Sourcing is its own stage.** The most common cause of a bad deal is a thin thesis dressed up as conviction. Making sourcing a stage with a contract and explicit outputs forces the team to test the thesis before spending diligence dollars.
- **Close is its own stage.** Funding a deal without a clean transition to asset management creates day-one chaos. The close stage produces the closing checklist and handoff materials so the asset manager can operate from day one.
- **_references/ is separate from _config/.** Config holds deal-specific context (this property, this sponsor, these terms). References hold knowledge that applies across deals (underwriting standards, market comps, prior deal records). Separating them means you can share references across deals without dragging one deal's confidential terms into another.

## Constraints That Apply
Built against the GP Operating Toolkit. Most relevant: **01 (AI Writing Patterns)** and **02 (Output Drift)** so the memo and thesis read clean and stay comparable deal to deal, **08 (Handoff Readiness)** so the deal survives the handoff to asset management at close, the universal **06 (Layer Triage)** and **09 (Platform Boundary)** so the model narrates and never recomputes a return, and **10 (Source Provenance)** when diligence opens on an unvetted data room.

## Layer Annotations
- CLAUDE.md: L0 (always loaded, orientation)
- CONTEXT.md: L1 (deal workflow routing)
- Stage CONTEXT.md files: L2 (stage contracts)
- _config/ files: L3 (deal-specific reference)
- _references/ files: L3 (cross-deal reference, potentially shared)
- Deal materials and stage outputs: L4 (working artifacts)
