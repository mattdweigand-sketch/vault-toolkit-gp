# SKILL: LP Narrative And Issue Prep Workspace Builder

## Description
Builds a platform-adjacent workspace for LP narrative, likely questions, sensitive issue prep, and response posture.

## When to Use
When IR needs language and judgment around platform-verified facts, without duplicating Juniper Square or another investor platform.

## Process

### Phase 1: Diagnosis

Read `_shared-config/firm-profile.md`, `_shared-config/voice-and-tone.md` at full depth, and `_shared-config/learnings.md` sections `## General` and `## lp-narrative-and-issue-prep`.

Ask one question at a time:

1. What topic, reporting cycle, or issue needs LP-facing preparation?
2. Which platform owns the figures, investor records, entitlements, portal, DDQ, and audit?
3. What facts are verified and what must not be stated?
4. What LP questions or sensitivities do you expect?
5. Who approves the posture before anything goes out?

### Phase 2: Assembly

Copy `architectures/lp-narrative-and-issue-prep/` to `workspaces/<name>/`. Populate `_config/response-standards.md`, `_config/investor-context.md`, and `_config/before-you-trust-this.md`.

Load and name constraints: 06, 09, 01, 02, 05, 08.

Load and name modules: `verified-fact-pack`, `grounded-draft`, `response-posture`, `handoff-brief`.

### Phase 3: Orientation

Explain that Juniper Square or the investor platform owns DDQ, figures, records, entitlements, portal delivery, and audit; this workspace owns explanation and prep.
