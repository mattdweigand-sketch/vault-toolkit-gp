# Trust Layer Module Smoke Test

Date: 2026-05-27

## Scope
Test the new module layer without creating a real client workspace.

Workflows tested:
- `diligence-evidence-map`
- `lp-narrative-and-issue-prep`

## Checks

### Setup Registry
Command:

```bash
python3 scripts/setup_state.py doctor --json
```

Result:
- 8 active architectures found.
- 8 active builders found.
- 10 constraints found.
- No missing or extra active workflow registry entries.

Expected first-run open items remain:
- `setup-progress.md` missing.
- `workspaces` has no real workspaces.
- `firm-profile.md` contains placeholders.

### Workspace Copy Smoke Test
Copied both reference architectures into `_sandbox/trust-layer-smoke/`.

Result:
- `diligence-evidence-map` copied with `00_sources`, three stages, `output/` folders, and `_config`.
- `lp-narrative-and-issue-prep` copied with four stages, `output/` folders, and `_config`.
- No `modules/` folder was copied into either workspace.

### Module References
Result:
- `diligence-evidence-map` references `source-provenance` and `handoff-brief`.
- `lp-narrative-and-issue-prep` references `verified-fact-pack`, `grounded-draft`, `response-posture`, and `handoff-brief`.
- Both workflow builders name the same modules that `SETUP.md` routes.

### Architecture Coverage
Result:
- All eight active architecture `CLAUDE.md` files include `## Modules Used`.
- All eight active architecture `CONTEXT.md` files include `## Modules Used`.

### Module Folder Contract
Result:
- All seven modules have `README.md`, `CONTRACT.md`, `templates/`, and `examples/`.

## Outcome
Pass.

The module layer is wired correctly for setup routing, architecture documentation, builder loading, and workspace-copy behavior.
