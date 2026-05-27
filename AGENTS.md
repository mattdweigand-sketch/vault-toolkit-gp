# GP Operating Toolkit

Shared project instructions for the GP Operating Toolkit.

`AGENTS.md` is canonical. Codex and other AGENTS-aware tools read it directly. Claude Code reads
it through the thin `CLAUDE.md` wrapper.

## Setup Entry Point

When the user says **"Run setup"**, **"add a workflow"**, or **"build a <workflow>"**, read
`SETUP.md` and follow **Run Setup Starts Here**.

Setup now uses `_shared-config/setup-session.json` as temporary resumable state. If setup is
interrupted, resume from that file instead of restarting orientation. `_shared-config/setup-progress.md`
remains the durable signal that setup completed.

## What This Repository Is

The GP Operating Toolkit helps private equity and commercial real estate firms put AI on the
high-judgment layer above their platforms. It has five parts:

- `architectures/` - eight active reference workspaces, plus `_variants/` for archived lifecycle examples.
- `constraints/` - ten reference files for safe AI workflow design.
- `modules/` - reusable Office Truth Layer contracts used by the architectures.
- `skill-starters/` - active workflow builders, plus `_variants/` for archived builders.
- `workspaces/` - the live workflows created during setup.

Do not load the whole toolkit by default. `SETUP.md` routes you to the smallest files needed for
the current setup step.

## Finalize

When the user explicitly asks to finalize, make this repo read purely as the firm's operating
system by following the **Finalize** section in `SETUP.md`. Finalize is optional and reversible.
