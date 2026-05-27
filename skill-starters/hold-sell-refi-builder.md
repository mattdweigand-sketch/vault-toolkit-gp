# SKILL: Hold Sell Refi Workspace Builder

## Description
Builds a decision workspace for hold, sell, refinance, recapitalize, or revisit-later decisions.

## When to Use
When a portfolio team needs to frame alternatives and take an asset decision to IC.

## Process

### Phase 1: Diagnosis

Read `_shared-config/firm-profile.md`, `_shared-config/voice-and-tone.md` at summary depth, and `_shared-config/learnings.md` sections `## General` and `## hold-sell-refi`.

Ask one question at a time:

1. Which asset or portfolio segment is under review?
2. What alternatives are live: hold, sell, refi, recap, or revisit later?
3. Which model outputs, BOVs, lender terms, and fund constraints are authoritative?
4. What criteria determine the preferred path?
5. Who approves the decision and who owns the handoff?

### Phase 2: Assembly

Copy `architectures/hold-sell-refi/` to `workspaces/<name>/`. Populate `_config/asset-profile.md`, `_config/decision-criteria.md`, and `_config/before-you-trust-this.md`.

Load and name constraints: 06, 09, 01, 02, 08, 10 when source packs are unvetted.

Load and name modules: `verified-fact-pack`, `decision-challenge`, `grounded-draft`, `handoff-brief`.

### Phase 3: Orientation

Explain that AI frames the alternative decision, but model, broker, lender, and fund-admin systems own the numbers.
