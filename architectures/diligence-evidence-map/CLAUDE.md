# Diligence Evidence Map Workspace

## What This Is
A source-control workspace for acquisition diligence. It inspects the data room, ranks source authority, flags conflicts and stale versions, and maps evidence to open diligence questions before the team relies on the material.

This is not underwriting. The model of record computes returns. The data room or deal platform stores documents. This workspace answers: what evidence do we have, how trustworthy is it, what conflicts, and what questions remain.

## Structure
```
diligence-evidence-map/
  CLAUDE.md
  CONTEXT.md
  00_sources/
  01_inventory/CONTEXT.md
  02_authority/CONTEXT.md
  03_questions/CONTEXT.md
  _config/
```

## Key Decisions
- **Evidence before narrative.** Do not write the diligence view until the source set has been inspected.
- **Authority is explicit.** If three files disagree, the workspace flags the conflict. It does not pick a winner silently.
- **Questions are the output.** A good evidence map gives diligence owners the next questions to resolve.

## Constraints That Apply
Universal **06** and **09**, plus **10 (Source Provenance)**, **02 (Output Drift)**, and **08 (Handoff Readiness)**.
