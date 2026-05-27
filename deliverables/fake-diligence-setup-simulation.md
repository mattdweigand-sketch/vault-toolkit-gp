# Fake Diligence Setup Simulation

Date: 2026-05-27

## Scope
Run a realistic setup simulation for `diligence-evidence-map` using fake firm and deal data.

The simulation was run in `_sandbox/real-setup-simulation/` so the source toolkit and real `workspaces/` folder stayed clean.

## Fake Inputs
- Firm type: private equity / commercial real estate GP.
- Workflow: `diligence-evidence-map`.
- Workspace name: `cedar-crossing-diligence`.
- Source set: three fake source files covering property actuals, current rent roll, and broker memo.
- Reviewer roles: diligence lead, counsel, acquisitions lead.

## What Was Built
Copied `architectures/diligence-evidence-map/` into:

```text
_sandbox/real-setup-simulation/workspaces/cedar-crossing-diligence/
```

Populated:
- `_config/source-standards.md`
- `_config/diligence-questions.md`
- `_config/before-you-trust-this.md`

Ran sample outputs:
- `01_inventory/output/source_inventory.md`
- `01_inventory/output/duplicate_log.md`
- `01_inventory/output/missing_context.md`
- `02_authority/output/authority_map.md`
- `02_authority/output/conflict_log.md`
- `03_questions/output/diligence_question_map.md`
- `03_questions/output/handoff_brief.md`

## Checks

### Module Loading
Pass.

The workspace references:
- `modules/source-provenance/CONTRACT.md`
- `modules/handoff-brief/CONTRACT.md`

No `modules/` folder was copied into the workspace.

### Source Provenance
Pass.

The source set produced:
- stable source IDs,
- authority rankings,
- duplicate/version-family notes,
- missing context,
- conflict log.

### Handoff Brief
Pass.

The stage 03 output produced a handoff brief suitable for an IC pressure test. It carried:
- origin,
- sourced figures,
- open items,
- `[NEEDS CONFIRMATION]` flag.

## Findings

No structural blocker found.

The setup flow is usable for a first real `diligence-evidence-map` workspace. The next improvement should come from the first live workspace build, not more abstract module editing.
