# Release Readiness

Date: 2026-05-27

## Scope
Verify the Trust Layer module release from a fresh clone-style sandbox and rehearse finalize/restore.

Sandbox path:

```text
_sandbox/fresh-clone-release-test/
```

## Fresh Clone First-Run Test
Created the sandbox with:

```bash
git clone . _sandbox/fresh-clone-release-test
```

Then ran a fake first setup:
- Firm: Ridgeline Partners
- First workflow: `diligence-evidence-map`
- Workspace: `workspaces/cedar-crossing-diligence/`

Result:
- `python3 scripts/setup_state.py doctor --json` returned `status: complete`.
- Registry passed with 8 architectures, 8 builders, and 10 constraints.
- No doctor open items.
- The workspace referenced `modules/source-provenance/CONTRACT.md` and `modules/handoff-brief/CONTRACT.md`.
- No module library was copied into the workspace.

## Finalize Rehearsal
Moved the toolkit into `_kit/` in the sandbox:

```text
SETUP.md
architectures/
constraints/
modules/
skill-starters/
```

Result:
- `_kit/modules/` moved with the rest of the toolkit.
- Sandbox `AGENTS.md` pointed to `_kit/SETUP.md`.
- `python3 scripts/setup_state.py doctor --json` passed after finalize.

## Restore Rehearsal
Moved the five toolkit items back from `_kit/` to the sandbox root.

Result:
- `SETUP.md`, `architectures/`, `constraints/`, `modules/`, and `skill-starters/` restored.
- `python3 scripts/setup_state.py doctor --json` passed after restore.

## Source Patch From Rehearsal
Finalize exposed one helper issue: `scripts/setup_state.py doctor` originally looked only at root-level toolkit folders. It now resolves the toolkit location from either:
- root layout, or
- finalized `_kit/` layout.

## Release Status
Ready.

The module layer works from tracked files, first setup works from a fresh clone-style copy, finalize moves `modules/`, restore works, and the setup-state helper now verifies both root and finalized layouts.
