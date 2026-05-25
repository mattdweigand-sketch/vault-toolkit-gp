# _shared-config — the firm, captured once

This folder holds the firm-level configuration that every workspace shares. It is filled in **once**,
during Run Setup's firm orientation, and read by every builder and every workspace afterward — so the
firm's name, systems of record, team, and voice are stated in one place instead of re-collected for
each workflow.

## What lives here
- **`firm-profile.md`** — the firm: what it invests in, its systems of record (the platform
  boundary), and its team/roles. Builders read this instead of re-asking firm-level questions.
- **`voice-and-tone.md`** — the firm's core written voice (the "direction" file from Constraint 05).
  Every writing workspace references this for the firm's voice, then adds its own register on top
  (a letter, an LP email, a thesis, and an IC memo differ in register, not in firm voice).
- **`setup-progress.md`** — created by Run Setup once the firm is onboarded: which workspaces have
  been built, when, and what is next. (Not present until the first setup runs.)

## How workspaces reference it
A workspace built under `workspaces/` reaches this folder by a stable relative path
(`../../_shared-config/...`). Each writing workspace's local voice file is a thin pointer to
`voice-and-tone.md` plus that workspace's register overlay — so updating the firm voice once updates
every workspace. If a workspace is ever moved out of this repo, update its pointer to wherever the
firm keeps this shared config.

## How Run Setup uses it
The presence of `setup-progress.md` is how Run Setup distinguishes a first-time setup (orientate,
then build) from a returning one (greet, offer to add a workflow or update config). That file is
written at the end of the first setup, so its absence is the signal that setup has not run yet —
the same flag the root `CLAUDE.md` bootstrap and `SETUP.md` key off.
