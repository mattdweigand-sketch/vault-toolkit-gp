# SKILL: Diligence Evidence Map Workspace Builder

## Description
Builds a source-provenance workspace for acquisition diligence data rooms.

## When to Use
When the team needs to inspect, rank, and map data-room evidence before relying on it in diligence, underwriting, or IC.

## Process

### Phase 1: Diagnosis

Read `_shared-config/firm-profile.md`, `_shared-config/voice-and-tone.md` at summary depth, and `_shared-config/learnings.md` sections `## General` and `## diligence-evidence-map`.

Ask one question at a time:

1. What source set or data room is this for?
2. What fact classes matter most: financials, legal, rent roll, customer, capex, environmental, market, or other?
3. What is authoritative for each fact class?
4. How messy is the room: duplicates, drafts, missing dates, conflicting versions?
5. Who reviews the authority ranking before the evidence map is used?

### Phase 2: Assembly

Copy `architectures/diligence-evidence-map/` to `workspaces/<name>/`. Populate `_config/source-standards.md`, `_config/diligence-questions.md`, and `_config/before-you-trust-this.md`.

Load and name constraints: 06, 09, 10, 02, 08.

### Phase 3: Orientation

Explain that the deliverable is the evidence map and question list, not an underwrite.
