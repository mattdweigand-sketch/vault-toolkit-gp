# SKILL: Portfolio Intervention Workspace Builder

## Description
Builds a workspace that turns verified portfolio signals into diagnosis, action plans, and follow-up.

## When to Use
When asset management, portfolio operations, or operating partners need to move from dashboard variance to intervention.

## Process

### Phase 1: Diagnosis

Read `_shared-config/firm-profile.md`, `_shared-config/voice-and-tone.md` at summary depth, and `_shared-config/learnings.md` sections `## General` and `## portfolio-intervention`.

Ask one question at a time:

1. What portfolio signals need attention, and on what cycle?
2. Which platform owns the actuals, KPIs, dashboards, and valuation outputs?
3. What baseline or business plan should signals be measured against?
4. What triggers monitor, investigate, intervene, escalate, or IC review?
5. Who owns actions and follow-up?

### Phase 2: Assembly

Copy `architectures/portfolio-intervention/` to `workspaces/<name>/`. Populate `_config/business-plan-targets.md`, `_config/intervention-standards.md`, `_config/action-plan-format.md`, and `_config/before-you-trust-this.md`.

Load and name constraints: 06, 09, 02, 04, 08, 10 when asset reports are unvetted.

### Phase 3: Orientation

Explain that the platform owns actuals and dashboards; this workspace owns diagnosis and action.
