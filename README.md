# The GP Operating Toolkit

For private equity and commercial real estate GPs that want to build controlled AI workflows around the work their platforms do not already own.

This toolkit helps a firm put AI in the judgment layer: IC pressure testing, diligence evidence, portfolio intervention, LP issue prep, market thesis, and firm memory. Its reusable module layer packages the Office Truth Layer patterns behind those workflows: source provenance, verified fact packs, grounded drafts, decision challenge, response posture, validated memory, and handoff briefs. It does not replace fund accounting, fund administration, investor portals, CRM, pipeline software, data rooms, dashboards, valuation systems, or approval controls.

The rule is simple: platform for the record, deterministic tools for the math, rules for routing, AI for judgment, and humans for approval.

## Start here

You need an AI coding assistant that can read a folder and edit files: Claude Code, Codex, Cursor, Copilot agent mode, or the Gemini CLI all work.

1. Download or clone this repo.
2. Open the folder in your agent.
3. Say `Run setup`.

Setup asks a few questions about your firm, then builds your first workspace in `workspaces/`. Later, say `add a workflow` to build another.

Use the repo with any agent that can read files and make edits. If your agent does not automatically load repo instructions, tell it to read `AGENTS.md` first. A plain browser chat can still use the reference files, but it cannot run setup.

## Where AI belongs

Most GP work should not go to a language model.

Roughly 60% belongs in existing software or a normal process. Another 30% belongs in rules, scripts, or repeatable automation. The remaining 10% is where AI is useful: judgment, synthesis, exception handling, narrative, and institutional memory.

That matters because strong GP platforms already exist. Juniper Square and similar systems own fund administration, investor records, data rooms, reporting, capital activity, portals, entitlements, and audit trails. Dealpath, DealCloud, and other investment platforms own pipeline state and execution tracking. Chronograph, iLevel-style tools, Canoe, and portfolio-monitoring platforms own extraction, structured portfolio data, dashboards, and valuation workflows.

Do not rebuild those systems here. Use this toolkit for the work above them:

- investment judgment: thesis, diligence, IC challenge, bid strategy, market thesis
- portfolio intervention: variance diagnosis, watchlist review, action planning, hold / sell / refinance framing
- investor communication: LP narratives, issue prep, likely questions, response framing
- source control: data-room maps, authority ranking, conflict logs, source-backed deliverables
- firm memory: underwriting backtests, IC precedent, win/loss learning, LP objection learning, post-mortems

If you read only two constraints, read [Layer Triage](constraints/06-layer-triage.md) and [Platform Boundary](constraints/09-platform-boundary.md). Those two decide whether AI belongs in the workflow at all.

## What is in here

```
AGENTS.md        canonical agent instructions
CLAUDE.md        Claude Code wrapper that imports AGENTS.md
SETUP.md         setup engine for building workflows
_shared-config/  firm profile, voice, setup progress, and learnings
constraints/     design principles for reliable AI work
modules/         reusable Office Truth Layer contracts
architectures/   reference workflow structures
skill-starters/  builders that setup runs
workspaces/      workflows created for your firm
```

The toolkit keeps three layers separate:

- `_shared-config/` holds firm-level context.
- `workspaces/` holds live workflow context.
- `constraints/`, `modules/`, `architectures/`, and `skill-starters/` hold reusable methodology.

After finalize, the methodology moves into `_kit/` and the root reads like the firm's operating system rather than a setup kit.

## Core architectures

The active architectures are the high-judgment workflows most worth building first:

- `ic-pressure-test`
- `diligence-evidence-map`
- `portfolio-intervention`
- `hold-sell-refi`
- `market-thesis-to-investment-box`
- `lp-narrative-and-issue-prep`
- `underwriting-backtest`
- `firm-memory-loop`

Each architecture maps the AI's job, the human review point, and the system of record that stays authoritative. Older lifecycle examples are preserved under `architectures/_variants/` for reference and migration, but they are not the primary setup routes.

The active `underwriting-backtest` architecture includes a worked `_example/` so you can see finished output alongside the empty folder shape.

## Modules

The `modules/` folder turns repeated Trust Layer patterns into reusable contracts:

- `source-provenance`
- `verified-fact-pack`
- `grounded-draft`
- `decision-challenge`
- `response-posture`
- `validated-memory-store`
- `handoff-brief`

Architectures reference these contracts instead of rewriting the same rules in every workflow. Builders should load only the modules used by the selected architecture.

## Constraints

The ten files in `constraints/` explain how to keep AI work reliable: source authority, context separation, output drift, platform boundaries, handoff readiness, and related failure modes.

They are portable. You can use them in this repo, in Claude Projects, in Cursor or VS Code, or pasted into a browser chat when you only need the reference material.

## Skill starters

The files in `skill-starters/` ask diagnostic questions, then assemble a workspace skeleton from your answers. They are the builders setup uses when you say `Run setup` or `add a workflow`.

The active builders match the eight core architectures. Older lifecycle builders are archived under `skill-starters/_variants/`.

## Your data

This toolkit is plain files on your machine. It has no server or database of its own and uploads nothing by itself.

Whatever AI tool you use will send the context it reads to that tool's model provider. Apply your firm's policy on what may go to which model, and use an enterprise or zero-retention plan where the data requires it.

Systems of record stay authoritative. The workflows can read from them, but nothing writes back or goes to an LP without a human in the loop.

## Finalize

Once you have built the workflows you need, say `finalize` or `make this our operating system`.

Finalize moves `SETUP.md`, `architectures/`, `constraints/`, `modules/`, and `skill-starters/` into `_kit/`, leaving your firm's workspaces and operating-system map at the root. It is reversible: `_kit/RESTORE.md` explains how to put the setup kit back.

Built by Matt Weigand. Released under the [MIT License](LICENSE).
