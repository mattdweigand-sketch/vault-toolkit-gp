# SKILL: IC Pressure Test Workspace Builder

## Description
Builds a workspace for stress-testing pending IC decisions before committee.

## When to Use
When the firm wants AI to challenge a memo, assumptions, evidence, risks, and approval conditions before IC, while the deal platform and model of record keep owning workflow state and math.

## Process

### Phase 1: Diagnosis

Read `_shared-config/firm-profile.md`, `_shared-config/voice-and-tone.md` at summary depth, and `_shared-config/learnings.md` sections `## General` and `## ic-pressure-test`.

Ask one question at a time:

1. What does the IC need to decide, and what document or memo goes to committee?
2. Where do the model outputs of record live, and who owns them?
3. What kinds of weak assumptions or missing evidence have caused bad IC decisions before?
4. What conditions does the committee commonly impose?
5. Who validates the pressure-test output before it is used?

### Phase 2: Assembly

Copy `architectures/ic-pressure-test/` to `workspaces/<name>/`. Customize `CLAUDE.md`, `CONTEXT.md`, stage contracts, `_config/ic-standards.md`, `_config/pressure-test-questions.md`, and `_config/before-you-trust-this.md` from the answers.

Load and name constraints: 06, 09, 02, 08, 10.

Load and name modules: `verified-fact-pack`, `decision-challenge`, `artifact-review`, `validated-memory-store`, `handoff-brief`.

### Phase 3: Orientation

Explain that this workspace improves a pending decision, does not run IC, does not author the memo, and never recomputes model outputs.
