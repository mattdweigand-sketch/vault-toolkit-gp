# PRD: Trust Layer Modules For The GP Operating Toolkit

## Decision

Add a reusable `modules/` layer to the GP Operating Toolkit.

The kit should keep eight core architectures. Do not add more workflows for every new deliverable type. Extract the repeated Office Truth Layer patterns into modules, then let architectures compose those modules into complete workflows.

The product structure becomes:

```text
constraints/       principles and guardrails
modules/           reusable Office Truth Layer contracts
architectures/     packaged GP workflows
skill-starters/    setup interviews and assembly rules
workspaces/        instantiated firm operating system
```

This keeps the kit small while making the methodology easier to extend.

## Problem

The current architecture library has strong workflow patterns, but repeated logic is embedded inside individual architectures:

- Source inventory appears in `diligence-evidence-map`, `one-off-deliverable`, and Constraint 10.
- Source-backed drafting appears in `one-off-deliverable`, LP narrative, market thesis, and IC support.
- Human validation and pattern capture appear in `underwriting-backtest`, `ic-pressure-test`, and `firm-memory-loop`.
- Handoffs between workspaces are defined in Constraint 08 but not yet implemented as a reusable artifact.

The result is good methodology, but too much duplication. A new workflow either copies prior logic manually or risks drifting from the Trust Layer rules.

## Product Goal

Make the Office Truth Layer a reusable product layer inside the kit.

The kit should let a builder say:

```text
This workflow uses source-provenance, verified-fact-pack, grounded-draft,
decision-challenge, response-posture, validated-memory-store, and handoff-brief.
```

Then the architecture imports the relevant contracts instead of rewriting them.

## Non-Goals

Do not turn modules into executable software.

Do not rebuild systems of record, document registers, fund accounting, investor portals, CRM, dashboards, DDQ execution, data extraction, or approval controls.

Do not make `one-off-deliverable` a ninth core architecture. Promote its useful pattern into modules.

Do not force every architecture to use every module. A module should load only when a stage needs it.

## Users

Primary user: a GP team using the toolkit to build AI workspaces around investment judgment, diligence, portfolio decisions, and investor communication.

Builder user: Codex, Claude Code, Cursor, or another AGENTS-aware assistant running setup and assembling workspaces.

Maintainer user: Matt or a toolkit owner adding new architectures, improving existing ones, or packaging the methodology for reuse.

## Core Concepts

### Constraint

A principle or guardrail. Example: source provenance, platform boundary, handoff readiness.

### Module

A reusable contract that turns one or more constraints into a repeatable work unit. A module defines inputs, process, outputs, done criteria, and failure modes.

### Architecture

A productized GP workflow composed from stages and modules. Example: IC pressure test, diligence evidence map, LP narrative and issue prep.

### Workspace

A live firm-specific copy of an architecture populated with the firm's systems, owners, standards, and open confirmations.

## Proposed Modules

### 1. `source-provenance`

Purpose: inspect a source set before any drafting, analysis, or decision support uses it.

Used by:
- `diligence-evidence-map`
- `one-off-deliverable` pattern
- `ic-pressure-test`
- `lp-narrative-and-issue-prep`
- Any future lender package, board memo, or diligence brief workflow

Inputs:
- Raw sources or a platform document register
- Source hierarchy rules
- Fact classes that matter for the workflow

Outputs:
- `source_inventory.md`
- `duplicate_log.md`
- `conflict_log.md`
- `missing_context.md`
- Optional `summaries/Sxx.md`

Acceptance criteria:
- Every source has an ID.
- Authority is ranked.
- Duplicates and version families are flagged.
- Conflicts are surfaced, not resolved silently.
- Missing support is visible.
- The stage stops for human review when authority is unclear.

### 2. `verified-fact-pack`

Purpose: assemble only the platform-verified facts a downstream narrative or decision stage may use.

Used by:
- `lp-narrative-and-issue-prep`
- `ic-pressure-test`
- `portfolio-intervention`
- `hold-sell-refi`
- Future lender or board communication workflows

Inputs:
- Platform-verified figures
- Source IDs or system references
- Entitlement or audience restrictions
- Forbidden claims

Outputs:
- `fact_pack.md`
- `forbidden_claims.md`
- `entitlement_notes.md`
- `open_fact_checks.md`

Acceptance criteria:
- Every figure has a platform source.
- The pack distinguishes verified fact, inference, and forbidden claim.
- Audience restrictions are visible.
- Missing facts are flagged, not invented.

### 3. `grounded-draft`

Purpose: draft a serious artifact from reviewed sources, with citations and flags.

Used by:
- `one-off-deliverable` pattern
- `lp-narrative-and-issue-prep`
- `market-thesis-to-investment-box`
- Future lender packages, board memos, and investor updates

Inputs:
- Reviewed source inventory or verified fact pack
- Deliverable spec
- Voice and tone reference
- Response or drafting standards

Outputs:
- Draft artifact
- `open_items.md`
- `source_usage_map.md`

Acceptance criteria:
- Every factual claim cites a source ID or platform reference.
- Every inference is labeled.
- Unsupported claims are flagged.
- Conflicts that bear on the artifact appear in the draft or open items.
- The draft does not compute figures.

### 4. `decision-challenge`

Purpose: pressure-test a decision package before a human gate.

Used by:
- `ic-pressure-test`
- `hold-sell-refi`
- `market-thesis-to-investment-box`
- Future bid strategy or investment-box update workflows

Inputs:
- Decision packet
- Verified facts or evidence map
- Decision standards
- Prior patterns or precedent

Outputs:
- `challenge.md`
- `fragile_assumptions.md`
- `missing_evidence.md`
- `decision_conditions.md`

Acceptance criteria:
- Issues are ranked by decision impact.
- Missing evidence is separated from acceptable uncertainty.
- Approval blockers, conditions, disclosures, and monitoring items are distinct.
- Every condition names owner, evidence needed, and deadline.

### 5. `response-posture`

Purpose: decide how to answer, hold, escalate, or route sensitive external-facing issues.

Used by:
- `lp-narrative-and-issue-prep`
- Future LP inquiry, lender communication, and portfolio issue workflows

Inputs:
- Likely questions
- Investor or audience context
- Response standards
- Escalation rules
- Compliance boundaries

Outputs:
- `response_posture.md`
- `approved_language_boundaries.md`
- `escalation_log.md`

Acceptance criteria:
- Each issue has a posture: answer directly, answer with caveat, hold, escalate, or route to platform.
- Each escalation names the owner.
- Sensitive topics have approved language boundaries.
- Nothing client-facing ships while required confirmations are open.

### 6. `validated-memory-store`

Purpose: turn repeated judgment into validated institutional memory.

Used by:
- `underwriting-backtest`
- `firm-memory-loop`
- `ic-pressure-test`
- Future LP objection learning and bid win/loss learning workflows

Inputs:
- Event or outcome record
- Canonical questions
- Taxonomy
- Store schema
- Human validation owner

Outputs:
- Append-only records
- `patterns.md`
- Capture log
- Cross-workflow flags

Acceptance criteria:
- Records answer the same canonical questions in the same order.
- Taxonomy tags are controlled.
- Causal claims are confidence-marked.
- Human validation happens before capture.
- Patterns update when evidence supports, extends, or contradicts them.

### 7. `handoff-brief`

Purpose: move output from one workspace to another without making the downstream workspace re-derive it.

Used by:
- All architectures that feed another architecture

Inputs:
- Upstream output
- Open confirmations
- Source references
- Carried-forward decision or finding

Outputs:
- `handoff_brief.md`

Acceptance criteria:
- Brief names subject, origin, date, and upstream stage.
- It carries the conclusion or decision the downstream should inherit.
- It includes sourced figures.
- It lists open items and flags.
- It points back to source files rather than copying full upstream context.

## Repository Changes

Add:

```text
modules/
  README.md
  source-provenance/
    README.md
    CONTRACT.md
    templates/
    examples/
  verified-fact-pack/
    README.md
    CONTRACT.md
    templates/
    examples/
  grounded-draft/
    README.md
    CONTRACT.md
    templates/
    examples/
  decision-challenge/
    README.md
    CONTRACT.md
    templates/
    examples/
  response-posture/
    README.md
    CONTRACT.md
    templates/
    examples/
  validated-memory-store/
    README.md
    CONTRACT.md
    templates/
    examples/
  handoff-brief/
    README.md
    CONTRACT.md
    templates/
    examples/
```

Update:

- `README.md`: explain the new middle layer.
- `SETUP.md`: add the module layer to the kit explanation, context matrix, and builder kernel.
- `AGENTS.md`: mention `modules/` as reusable methodology.
- `scripts/setup_state.py`: update `WORKFLOWS` to the current eight active architectures, and ignore `_variants` when checking active architecture parity.
- `architectures/*/CLAUDE.md`: name which modules each architecture uses.
- `architectures/*/CONTEXT.md`: name module contracts in the stage map.
- Stage `CONTEXT.md` files: reference module contracts where applicable.
- `skill-starters/*-builder.md`: load module contracts only when the target architecture uses them.

## Architecture Composition Map

| Architecture | Modules |
|---|---|
| `diligence-evidence-map` | `source-provenance`, `handoff-brief` |
| `lp-narrative-and-issue-prep` | `verified-fact-pack`, `grounded-draft`, `response-posture`, `handoff-brief` |
| `ic-pressure-test` | `verified-fact-pack`, `decision-challenge`, `validated-memory-store`, `handoff-brief` |
| `underwriting-backtest` | `validated-memory-store`, `handoff-brief` |
| `firm-memory-loop` | `validated-memory-store`, `handoff-brief` |
| `hold-sell-refi` | `verified-fact-pack`, `decision-challenge`, `grounded-draft`, `handoff-brief` |
| `market-thesis-to-investment-box` | `source-provenance`, `grounded-draft`, `decision-challenge`, `handoff-brief` |
| `portfolio-intervention` | `verified-fact-pack`, `decision-challenge`, `response-posture`, `handoff-brief` |

## Setup Flow Changes

Current flow:

```text
user request -> workflow routing -> builder -> architecture copy -> workspace
```

New flow:

```text
user request -> workflow routing -> builder -> architecture copy
             -> module contracts referenced
             -> module config populated where needed
             -> workspace
```

Builders should not copy full module folders into every workspace by default. They should reference module contracts from the kit and copy only the templates needed for that workspace's outputs.

When finalized, module paths move with the rest of the kit:

```text
_kit/modules/
```

## File Contract

Each module gets the same internal shape:

```text
module-name/
  README.md
  CONTRACT.md
  templates/
    output-name.md
  examples/
    README.md
    output-name.md
```

`README.md` answers:
- What this module does.
- When to use it.
- When not to use it.
- Which constraints it implements.
- Which architectures use it.

`CONTRACT.md` defines:
- Purpose.
- Inputs.
- Process.
- Outputs.
- Done looks like.
- Common failure modes.
- Layer annotation.

`templates/` contains output skeletons.

`examples/` contains one compact worked example.

## Migration Plan

### Phase 1: Add the module layer

Create `modules/README.md` and the seven module folders with `README.md`, `CONTRACT.md`, templates, and one compact example each.

Start with `source-provenance` because it already exists in three places and has the clearest contract.

### Phase 2: Wire active architectures to modules

Update the four priority architectures first:

1. `diligence-evidence-map`
2. `lp-narrative-and-issue-prep`
3. `ic-pressure-test`
4. `underwriting-backtest`

For each:
- Add a "Modules Used" section to `CLAUDE.md`.
- Add module references to `CONTEXT.md`.
- Adjust stage contracts so shared method lives in the module and workflow-specific details stay in the stage.
- Add handoff brief outputs where the workflow feeds another workspace.

### Phase 3: Wire remaining active architectures

Update:

1. `firm-memory-loop`
2. `hold-sell-refi`
3. `market-thesis-to-investment-box`
4. `portfolio-intervention`

Keep changes light. The goal is module linkage, not a full rewrite.

### Phase 4: Update builders and setup

Update `SETUP.md` so setup knows modules exist and loads them selectively.

Update each builder so it names required modules and populates module-specific config.

Update `scripts/setup_state.py` to align with the current active workflow set.

### Phase 5: Archive and promotion cleanup

Keep archived variants under `_variants`.

Move useful one-off deliverable logic into:
- `source-provenance`
- `grounded-draft`
- `handoff-brief`

Leave `architectures/_variants/one-off-deliverable` as a worked reference.

## Acceptance Criteria

The PRD is complete when:

- `modules/` exists with seven module folders.
- Each module has `README.md`, `CONTRACT.md`, at least one template, and one compact example.
- `README.md`, `AGENTS.md`, and `SETUP.md` explain the module layer.
- The four priority architectures name their modules and reference module contracts in stage docs.
- The four remaining active architectures name their modules at least in `CLAUDE.md` and `CONTEXT.md`.
- Builders load module contracts selectively.
- `scripts/setup_state.py doctor --json` no longer reports archived variants as missing active workflows.
- `one-off-deliverable` stays archived as a variant, while its reusable logic exists in modules.

## Success Metrics

Quality:
- New architecture additions reuse modules instead of copying source provenance, drafting, or memory-store logic.
- A reviewer can trace any architecture stage to its module contract.
- Handoff briefs exist where workflows feed downstream work.

Maintainability:
- Shared changes to source provenance, grounded drafting, or memory capture happen once in `modules/`.
- Active architecture count stays at eight unless a genuinely new judgment pattern appears.
- Setup docs remain shorter because repeated stage logic moves into module contracts.

Trust:
- Factual outputs cite source IDs or platform references.
- Human review gates are visible.
- `[NEEDS CONFIRMATION]` values travel through handoff briefs.
- Memory stores require validation before capture.

## Risks

Risk: modules become abstract documentation nobody uses.

Mitigation: every module must be referenced by at least one active architecture and must include templates that builders actually copy or point to.

Risk: architecture docs become harder to read because logic moves out.

Mitigation: stage docs should say what is workflow-specific and link to the module contract for the shared method. Do not force a reader to jump for basic orientation.

Risk: setup loads too much context.

Mitigation: update the context matrix so builders load only the modules used by the selected architecture.

Risk: modules drift from constraints.

Mitigation: every module README names the constraints it implements. Constraint edits should include a quick pass over affected modules.

## Open Decisions

1. Should modules be copied into live workspaces, referenced from the kit, or both?

Recommendation: reference module contracts from the kit, copy only output templates into workspaces when useful.

2. Should module examples be generic or GP-specific?

Recommendation: keep them GP-specific but compact. The whole kit is for GPs, and examples should teach the operating pattern in the target domain.

3. Should `one-off-deliverable` get an active builder?

Recommendation: no. Keep it as a variant. Its reusable pieces belong in modules.

4. Should modules be part of finalize?

Recommendation: yes. Move `modules/` into `_kit/` with `architectures/`, `constraints/`, and `skill-starters/`.

## Implementation Order

1. Create `modules/source-provenance`.
2. Create `modules/handoff-brief`.
3. Update `diligence-evidence-map` to use both.
4. Create `modules/verified-fact-pack`, `grounded-draft`, and `response-posture`.
5. Update `lp-narrative-and-issue-prep`.
6. Create `modules/decision-challenge`.
7. Update `ic-pressure-test`.
8. Create `modules/validated-memory-store`.
9. Update `underwriting-backtest` and `firm-memory-loop`.
10. Update remaining active architectures.
11. Update `SETUP.md`, `README.md`, `AGENTS.md`, and builders.
12. Fix `scripts/setup_state.py`.
13. Run `python3 scripts/setup_state.py doctor --json`.

## Product Positioning

The Trust Layer is the layer above systems of record that makes firm judgment inspectable, source-backed, reusable, and safe to hand off.

The Office Truth Layer modules are the operating patterns inside that layer:

- What is the source?
- Which version is authoritative?
- What does the evidence support?
- What is inference?
- What needs a human?
- What should be remembered next time?

Architectures package those modules into GP workflows. Workspaces make them real for one firm.
