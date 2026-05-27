# Sandbox First-Run Report

Date: 2026-05-27

## Scope
Run a full first-setup rehearsal in a sandbox copy so the source toolkit repo stays clean.

Sandbox path:

```text
_sandbox/toolkit-first-run/
```

## Setup Inputs
Fake firm:
- Ridgeline Partners
- Value-add multifamily and light industrial assets in secondary Sun Belt markets
- Systems of record: Juniper Square, RealPage, Argus/Excel, DealCloud
- First workflow: `diligence-evidence-map`
- First workspace: `workspaces/cedar-crossing-diligence/`

## What Ran
1. Created sandbox copy of the repo, excluding `.git` and `_sandbox`.
2. Ran `python3 scripts/setup_state.py init-session`.
3. Recorded fake orientation and workflow selection in setup session state.
4. Copied `architectures/diligence-evidence-map/` into `workspaces/cedar-crossing-diligence/`.
5. Populated shared config and workspace config.
6. Ran a sample source-provenance pass through inventory, authority, diligence questions, and handoff brief.
7. Wrote sandbox `setup-progress.md`.
8. Converted sandbox `AGENTS.md` into a firm OS map.
9. Cleared the temporary setup session.

## Verification
Command:

```bash
python3 scripts/setup_state.py doctor --json
```

Result in sandbox:
- `status`: `complete`
- 8 architectures
- 8 builders
- 10 constraints
- no registry drift
- no doctor open items

Workspace output created:
- `01_inventory/output/source_inventory.md`
- `01_inventory/output/duplicate_log.md`
- `01_inventory/output/missing_context.md`
- `02_authority/output/authority_map.md`
- `02_authority/output/conflict_log.md`
- `03_questions/output/diligence_question_map.md`
- `03_questions/output/handoff_brief.md`

## Findings
No source-toolkit patch required.

The first-run flow works in a sandbox copy. It correctly leaves the source toolkit clean, produces a complete sandbox OS state, and keeps open diligence risk inside the workspace's `before-you-trust-this.md` and handoff brief.

## Next Use
Use `_sandbox/toolkit-first-run/` as the reference rehearsal folder when reviewing the setup experience. Delete and recreate it whenever a fresh first-run test is needed.
