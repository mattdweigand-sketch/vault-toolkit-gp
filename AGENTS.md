# GP Operating Toolkit

Shared project instructions for the GP Operating Toolkit.

`AGENTS.md` is canonical. Codex and other AGENTS-aware tools read it directly. Claude Code reads
it through the thin `CLAUDE.md` wrapper.

## Where to go from here

**If `_shared-config/setup-progress.md` does not exist, setup has not run yet.** Read `SETUP.md`
and follow it. It runs the firm's one-time orientation, builds the first workspace, and then
rewrites this file into the firm's operating-system map. To begin, the user need only say
**"Run setup."**

**If `_shared-config/setup-progress.md` exists, setup has already run** and this file should
already be the firm's OS map. If you are still reading this bootstrap text, something interrupted
the first setup; re-read `SETUP.md` and resume from **After First Setup: Write the OS Map**.

## What this repository is

The GP Operating Toolkit, built for private equity and commercial real estate firms. It has
four parts: `architectures/` (eleven reference workspaces), `constraints/` (ten reference files),
`skill-starters/` (eleven builder skills), and `workspaces/` (the workflows you build). `SETUP.md`
is the engine that runs setup, builds workspaces, and, when the firm is ready, finalizes the repo
into its operating system. `SETUP.md` explains all of it; do not load the folders yourself unless
that file routes you there.

## Adding workflows, and after setup

You can keep building forever: new workflow types, or more instances of ones already built. Say
**"Run setup"**, **"add a workflow"**, or **"build a <workflow>"**. That routes to `SETUP.md`.
Once the first setup finishes, `SETUP.md` overwrites this file with the firm's OS map, which
headlines how to add a workflow and lists what is built and what is still available. The
`CLAUDE.md` wrapper stays thin and continues to import this file for Claude Code.

An optional, reversible **finalize** step later moves the toolkit into `_kit/` so the root reads
purely as the firm's operating system. `SETUP.md` describes it.
