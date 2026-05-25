# GP Operating Toolkit — Setup & Build Engine

## What This File Is

You are an AI agent. This file is the **setup engine** for the GP Operating Toolkit. It runs
the firm's one-time orientation, builds workspaces, keeps the operating-system map current, and
(when the firm is ready) finalizes the repository into the firm's own AI operating system.

You did not start here. Claude Code auto-loads `CLAUDE.md`, not this file. The root `CLAUDE.md`
is a thin bootstrap that sends you here when setup has not run yet. From here on, this file is
the machinery; `CLAUDE.md` is the artifact.

Read this file first, then navigate to the specific files each step calls for. Do not load
everything at once. That is the whole point of the toolkit.

This repository is the GP Operating Toolkit, built for private equity and commercial real
estate firms. Its worked examples name commercial-real-estate systems of record (Argus, Yardi,
MRI, RealPage); when building for a PE deal team, read those as placeholders for the firm's own
deal model and portfolio or fund-accounting systems — the logic transfers unchanged. It has
three parts:

- **architectures/** — eleven reference workspaces. Ten span the GP lifecycle (deal-screening,
  deal-pipeline, asset-management, disposition, lp-reporting, lp-inquiries,
  deal-win-loss-learning, underwriting-backtest, ic-memo-intelligence, market-thesis); the
  eleventh, one-off-deliverable, produces a single deliverable from an unvetted source set when the
  work maps to no lifecycle stage. Each is a working folder structure with its own `CLAUDE.md`,
  `CONTEXT.md`, and stage contracts. You copy and customize one to build the user's workspace.
- **constraints/** — ten reference files, each solving a specific problem GPs hit when
  working with AI. You load these selectively, matched to the workflow being built.
- **skill-starters/** — eleven builder skills, one per architecture. Each runs a diagnostic
  interview, then assembles a workspace from the answers. These do the actual building.

> **Where the toolkit lives.** Before the firm finalizes, these three folders and this
> `SETUP.md` sit at the repo root. After finalize, they move together into `_kit/` and this
> file becomes `_kit/SETUP.md`. Everything in this file works in both states; where a path
> differs, it is called out as "root before finalize, `_kit/` after."

## A Note on Context Layers (ICM)

The architectures and builders tag every file with a context layer (L0–L4) under the
Interpreted Context Methodology (ICM). The layer says *when* a file loads: L0 the
always-loaded map (`CLAUDE.md`), L1 routing (`CONTEXT.md`), L2 the per-task stage contract,
L3 reference the model should follow (voice, standards), and L4 working files the model
should transform (source data, drafts). The discipline is to load only what a step needs, and
to keep "rules to follow" (L3) distinct from "content to transform" (L4) so the model does
not confuse the two. Constraint 03 (Context Hygiene) defines the full model — read it before
you start stamping layer tags on the files you build.

The word *layer* shows up in two unrelated ways across this toolkit; keep them separate.
**Context layers (L0–L4)**, the subject of this note, describe *when* a file loads. **Solution
layers (60/30/10)**, named in the constraint routing table below, describe *what kind of tool*
should solve a problem — traditional software, a rule-based system, or a language model. Same
word, different question.

## Run Setup / Add a Workflow

This is the entry point. When the user says **"Run setup"**, **"add a workflow"**, **"build a
&lt;workflow&gt;"**, or opens a session with no specific task, do this first:

1. **Check whether the firm has been set up before** — does `_shared-config/setup-progress.md`
   exist? That file is written at the end of the first setup; its existence is the hard signal
   that setup has already run. (Do not judge by placeholder text — key off the file.)
   - **No (first-time setup):** run **Firm Orientation** (below), then **The Onboarding
     Sequence** to build the first workspace, then write `_shared-config/setup-progress.md`
     recording what was built, then run **After First Setup: Write the OS Map** to turn the root
     `CLAUDE.md` into the firm's operating-system map.
   - **Yes (returning):** read `_shared-config/firm-profile.md` and
     `_shared-config/setup-progress.md`, greet the firm by name, summarize what has been built,
     and offer to add another workflow, set up another instance of one already built, update
     shared config, or resume an unfinished one. Do **not** re-run orientation. "Run setup,"
     "add a workflow," and "build a &lt;workflow&gt;" are all the same add-a-workflow intent on
     this path. After the build, run **Keeping the OS Map Current**.
2. Always ask before building, and stop with a working, populated workspace the firm can use.

### Firm Orientation (first run only)

Before building any workflow, capture the firm once. Ask these one at a time, then write the
answers into `_shared-config/firm-profile.md` and seed `_shared-config/voice-and-tone.md`. Both
files ship as placeholder templates (bracketed prompts); overwrite the placeholders with the
firm's real values rather than appending alongside them:

1. **What is the firm, and what does it invest in?** Name, asset classes, strategy, geography,
   and the current vehicle(s) at a high level.
2. **What are your systems of record?** Where the authoritative data lives — fund administration
   / investor management (capital accounts, the waterfall, LP figures), property/fund accounting
   (operating actuals), the underwriting model, the CRM. This is the platform boundary: what AI
   will narrate but never compute or override (Constraint 09).
3. **Who is on the team, and who owns what?** The roles that own acquisitions, asset management,
   investor relations, and the IC sign-off, so workspaces route handoffs and approvals correctly.
4. **How does the firm sound in writing?** A first pass at the firm's voice (how it addresses
   investors, how direct it is about bad news, what it never sounds like). Seed
   `_shared-config/voice-and-tone.md`; it is fully refined the first time a writing workspace is
   built.

Orientation is firm-level and runs once. Every builder reads `_shared-config/` and does not
re-ask these facts.

## The Onboarding Sequence

Run these steps in order. Each one names the file to read or run next.

1. **Route the work.** The firm itself is already captured in `_shared-config/` (from Firm
   Orientation). Ask only what work the user wants to run with AI, and map their answer to one of
   the workflows using the routing table below. If they name more than one, handle the
   highest-priority workflow first and return for the others. Do not build them all at once.

2. **Pick the skill-starter.** Open the matching builder in `skill-starters/` (root before
   finalize, `_kit/skill-starters/` after). It is the instruction set for the build. Do not
   improvise a workspace; the builder's diagnostic questions are the work.

3. **Run the diagnostic interview.** Ask the builder's questions one at a time. Wait for each
   answer. The answers become the content of the workspace. Do not skip ahead to assembly.

4. **Load the constraints this workflow needs.** Before assembling, read the constraint files
   named for this workflow in the constraint routing table below. They shape the stage
   contracts and the `_config` files you are about to write. Load only those. Loading all ten
   is the context-hygiene mistake the toolkit exists to prevent.

5. **Instantiate the workspace.** Copy the matching architecture — `architectures/<workflow>/`
   before finalize, `_kit/architectures/<workflow>/` after — into `workspaces/<name>/` (rename it
   for the user's deal/fund/cycle), and follow the builder's assembly phase to write `CLAUDE.md`,
   `CONTEXT.md`, the stage contracts, and the `_config` files from the interview answers. Copying
   never consumes the template, so a workflow type can be built any number of times. The reference
   architecture's own files show you the target shape. (Live workspaces live under `workspaces/`;
   the firm's shared config lives in `_shared-config/`.) **If the architecture ships an `_example/`,
   it comes along in the copy — label it plainly so the client never mistakes it for their own data.**
   In the workspace `CLAUDE.md` structure map, mark `_example/` as "a different sample firm's worked
   cycle — read-only calibration reference, not your data." (It doubles as the stand-in run when the
   workspace has no live input yet; see the Onboarding Complete checklist.)

6. **Populate `_config` with real values.** Pull firm facts and the firm voice from
   `_shared-config/` rather than re-asking; fill the workspace's remaining `_config` files with
   workflow-specific rules, the register overlay, terms, and constraints. A workspace with empty
   `_config` is a template, not an operating system. Help them fill at least the required files
   before you call onboarding done.

7. **Verify.** Run the Onboarding Complete checklist below. Report each item as pass or open.
   Do not declare onboarding complete while any item is open.

## Diagnose → Route

Match the user's primary work to a workflow and its builder. (Builder paths are under
`skill-starters/` before finalize, `_kit/skill-starters/` after.)

| If the user's core work is… | Workflow | Builder to run |
|---|---|---|
| Triaging inbound deal flow — deciding which opportunities merit diligence | deal-screening | `skill-starters/deal-screening-builder.md` |
| Acquiring assets — sourcing, diligence, investment committee, closing | deal-pipeline | `skill-starters/deal-pipeline-builder.md` |
| Monitoring owned assets — business-plan-vs-actual reviews, watchlist | asset-management | `skill-starters/asset-management-builder.md` |
| Exiting an asset — hold/sell decision through sale and capital return | disposition | `skill-starters/disposition-builder.md` |
| Investor communications — quarterly letters, capital account statements, notices | lp-reporting | `skill-starters/lp-reporting-builder.md` |
| Handling inbound LP questions between formal events | lp-inquiries | `skill-starters/lp-inquiries-builder.md` |
| Learning why we win or lose competitive deals to sharpen the next bid | deal-win-loss-learning | `skill-starters/deal-win-loss-learning-builder.md` |
| Learning why realized deals beat or missed their underwriting, to calibrate future models | underwriting-backtest | `skill-starters/underwriting-backtest-builder.md` |
| Learning how the investment committee decides — its standing conditions, risk appetite, and precedent — to sharpen future memos | ic-memo-intelligence | `skill-starters/ic-memo-intelligence-builder.md` |
| Building the firm's market/sector view to guide acquisitions | market-thesis | `skill-starters/market-thesis-builder.md` |
| Producing one serious deliverable from a messy, unvetted source set, with no recurring cycle | one-off-deliverable | `skill-starters/one-off-deliverable-builder.md` |

If the user is unsure which they need, or wants to know where AI belongs at all before
building anything, start them with **Constraint 06 (Layer Triage)** and **Constraint 09
(Platform Boundary)**. Those two answer "what should AI do, and what should my platform own"
before a single folder is created.

Recurring back-office operations — capital calls, distributions, transfers, onboarding — are
deliberately not on this list. They are platform-governed transactions (capital accounts, the
waterfall, the audit trail), and they belong on the fund-administration platform, not in an AI
workspace. Do not build a workspace to process them. AI's role around these events is the
language and the judgment on top of the platform: drafting a notice from platform-verified
figures (lp-reporting) or fielding the questions they generate (lp-inquiries). See Constraint 09.

Capital formation — the raise itself, subscriptions, investor onboarding, and the data room — is
out of scope for the same reason: the investor-management and fund-administration platform owns
that pipeline and the investor record. AI's contribution is the language and judgment around it
(narrative, tailoring, and the LP-commit/pass debrief that feeds deal-win-loss-learning), not a
workspace that runs the raise.

### If the work matches none of the rows

The rows above are not an exhaustive catalog. They are instances of four structural *shapes*,
and most GP work is a variant of one of them. Do not jam an off-list workflow into the closest
row by topic. Classify it by shape first:

- **Gated decision pipeline** (deal-screening, deal-pipeline, disposition): advance one item
  through sequential stages, each a go/no-go, toward a terminal decision or action. Use when the
  work has review gates (e.g., a development project to delivery, a refinancing to close).
- **Recurring operations queue** (lp-inquiries): intake → process → deliver, repeated per
  request. Use when the same *type* of request arrives over and over (e.g., vendor onboarding,
  a tenant-credit review queue). Note the boundary: this shape fits the *language and judgment*
  around recurring requests, not the platform-governed processing of capital events themselves
  (see Constraint 09).
- **Recurring document production** (lp-reporting, asset-management, market-thesis): verified
  data → drafted narrative → distribution, on a cycle. Use when you produce a document from
  numbers you do not invent (e.g., a JV/co-GP partner report, an internal IC update). The
  *non-recurring* version of this shape — one serious deliverable from an unvetted source set,
  no cycle — has its own architecture, **one-off-deliverable**: inventory the sources, review,
  then draft. Reach for it when the deliverable matters but maps to no lifecycle stage.
- **Learning loop** (deal-win-loss-learning, underwriting-backtest, ic-memo-intelligence): capture
  an outcome → analyze why → write to a store → read it back to inform the next time. Use when the
  goal is to make a repeated activity compound — the deliverable is the accumulating store, not any
  single record. The toolkit ships three instances: deal-win-loss-learning (why we win or lose
  competitive bids), underwriting-backtest (why realized deals beat or missed their underwriting,
  the worked realized-deal post-mortem that sharpens future models), and ic-memo-intelligence (how
  the investment committee decides — its standing conditions, revealed risk appetite, and precedent
  — captured at decision time to sharpen future memos). The same loop also fits an LP-commit/pass
  debrief that sharpens the next raise — same loop, swap the config.

If the work maps to a shape, copy the nearest architecture, rename its stages, and run the
matching builder — the decomposition logic transfers; only the specifics change. If it maps to
no shape, build a new workspace from the meta-pattern using **Constraint 06 (Layer Triage)**,
**Constraint 03 (Context Hygiene)**, **Constraint 08 (Handoff Readiness)**, and **Constraint 09
(Platform Boundary)**, with any builder as the assembly recipe.

**A single request can span two shapes.** For example, "monitor loan covenants and produce the
quarterly lender package, and decide when to refinance" is recurring document production (the
package) *and* a gated decision pipeline (the refinance). When a request decomposes like this,
build the highest-priority shape first and return for the second — do not silently drop the half
that did not fit the first shape you reached for.

**An off-list build still needs the right constraints.** The meta-pattern names 06, 03, 08, and
09, but those are the floor. Also pull the constraints the nearest routing-table row would load,
by analogy to the shape you matched — a lender-facing compliance document inherits **02 (Output
Drift)** and **10 (Source Provenance)** for the same reasons the document-production workflows
above do. Match the constraints to the shape, not just to the fallback.

Before building anything new, apply the platform-boundary filter (Constraint 09): if an
enterprise platform already owns the workflow — CRM, pipeline, fund accounting — do not rebuild
it. Build the language-and-judgment layer that rides on top of it.

## Constraint Routing

Load the constraints named for the workflow you are building. Read them before assembly, and
name them in the workspace `CLAUDE.md` so the user's team can find them later. Do not load the
whole library. (Constraint files are under `constraints/` before finalize, `_kit/constraints/`
after.)

| Workflow | Load these constraints | Why |
|---|---|---|
| **All workflows** | 06 (Layer Triage), 09 (Platform Boundary) | Decide what is AI vs. deterministic vs. platform before building. Roughly 60% traditional, 30% rule-based, 10% AI. |
| **deal-pipeline** | + 01 (AI Writing Patterns), 02 (Output Drift), 08 (Handoff Readiness) | Memos and theses must read clean and survive a handoff to asset management. |
| **lp-reporting** | + 01 (AI Writing Patterns), 02 (Output Drift), 05 (Voice Architecture) | The letter must sound like the firm and stay consistent cycle to cycle. |
| **deal-screening** | + 02 (Output Drift); 10 (Source Provenance) when an opportunity arrives with a fuller data set | Screens must be comparable deal to deal; opportunities arrive as unvetted source sets. |
| **asset-management** | + 02 (Output Drift), 04 (Session Consistency), 08 (Handoff Readiness), 10 (Source Provenance) | Reviews repeat on a cycle, hand off to the IC, and ingest unvetted asset reports. |
| **disposition** | + 01 (AI Writing Patterns), 02 (Output Drift), 08 (Handoff Readiness) | The hold/sell case and disposition package must read clean and hand off cleanly at close. |
| **lp-inquiries** | + 02 (Output Drift), 04 (Session Consistency), 05 (Voice Architecture) | Responses must be consistent and on-voice across many responders. |
| **deal-win-loss-learning** | + 03 (Context Hygiene), 04 (Session Consistency), 08 (Handoff Readiness) | Records must be comparable to aggregate; the store stays clean and handoff-readable, and broker spin must be kept out of it. |
| **underwriting-backtest** | + 04 (Session Consistency), 10 (Source Provenance), 03 (Context Hygiene), 08 (Handoff Readiness) | Records must be comparable to aggregate into a calibration table (04, load-bearing); the approved model and actuals are sourced data — pin which model version is the underwriting of record (10); the store stays clean and handoff-readable (03, 08). |
| **ic-memo-intelligence** | + 04 (Session Consistency), 10 (Source Provenance), 03 (Context Hygiene), 08 (Handoff Readiness) | Records must be comparable to aggregate into decision precedent (04, load-bearing); the memo, minutes, and decision are sourced data the model narrates and never invents (10); the store stays clean and handoff-readable (03, 08). |
| **market-thesis** | + 01 (AI Writing Patterns), 02 (Output Drift), 10 (Source Provenance) | The thesis must read sharp, stay consistent, and rest on vetted sources. |
| **one-off-deliverable** | + 10 (Source Provenance), 01 (AI Writing Patterns), 02 (Output Drift) | The workspace *is* a provenance pass made concrete; the deliverable must also read clean and stay internally consistent. |
| **Scaling any workflow** | + 07 (Scaling vs. Automating) | When the same workflow runs many times, decide what to template vs. automate. |
| **Context degrading mid-build** | + 03 (Context Hygiene) | If your own context gets noisy during a long onboarding, this is the fix. |
| **Ingesting a data room or unvetted source set** | + 10 (Source Provenance) | Inventory and rank inputs before any stage drafts. AI flags provenance, duplicates, and conflicts; the platform owns the figures. |

## Onboarding Complete

Onboarding is done when every item below is true. Report each as pass or open.

- [ ] **Workflow identified.** The user confirmed which workflow(s) they are building.
- [ ] **Workspace instantiated.** The architecture was copied and renamed; it has a
      `CLAUDE.md`, a `CONTEXT.md`, and a `CONTEXT.md` for every processing stage. (A raw
      input-drop folder such as one-off-deliverable's `00_sources/` intentionally has none.)
- [ ] **`_config` populated.** The required reference files hold the user's real values, not
      placeholder text. Any value the firm did not supply is flagged, not invented: use
      `[NEEDS CONFIRMATION — <owner>]` for high-stakes values (compliance language, financial
      thresholds, rosters) and `[TBD]` for data not yet available. See Constraint 08.
- [ ] **High-stakes values gated.** `_config/before-you-trust-this.md` lists every
      `[NEEDS CONFIRMATION]` value with its owner and status. Nothing client-facing ships until
      the high-stakes rows are cleared. (Constraint 08 defines the convention.)
- [ ] **Constraints loaded and named.** The constraints from the routing table were read, and
      the workspace `CLAUDE.md` names which ones apply.
- [ ] **One stage run end to end.** At least one stage produced real output, checked against
      its "Done Looks Like" line. Compare it to the lp-reporting architecture's `_example` to see
      what finished output looks like. If there is no live input yet (a backtest with no realized
      deal, a learning loop with no resolved record, a brand-new cycle), the workspace's own
      `_example/` is the stand-in run, and the workspace is marked "stands up now, activates on
      first &lt;exit / cycle / inquiry&gt;."
- [ ] **Handoff-ready.** A new team member could open the workspace folder and understand it
      without you in the room (Constraint 08 is the test for this).

If any box is open, return to the step that produces it. A half-built workspace handed off as
"done" is the failure mode this checklist exists to prevent.

## After First Setup: Write the OS Map

At the end of the **first** setup — after the first workspace is built and
`_shared-config/setup-progress.md` is written — overwrite the root `CLAUDE.md` with the
operating-system map below. This is the content metamorphosis: the entry file stops being a
toolkit bootstrap and becomes the firm's own OS map. It is safe and automatic — nothing of value
is lost, because the machinery already lives here in `SETUP.md`.

Fill the parametric fields from the firm's files:
- `{FIRM_NAME}` — from `_shared-config/firm-profile.md`.
- `{KIT_POINTER}` — `SETUP.md` before finalize, `_kit/SETUP.md` after. (At first-setup time it
  is always `SETUP.md`; the finalize step updates it.)
- `{KIT_LOCATION}` — a bare phrase naming where the toolkit currently lives: before finalize,
  `the repo root` (the kit folders and `SETUP.md` sit at the top level); after finalize, `` `_kit/` ``.
  It appears in **two** places in the template below; fill both with the same value.
- `{BUILT_LIST}` — one line per workspace in `_shared-config/setup-progress.md`.
- `{AVAILABLE_LIST}` — the workflow types from the eleven not yet built.

Write exactly this structure (substituting the fields):

```markdown
# {FIRM_NAME} — AI Operating System

This repository is {FIRM_NAME}'s operating system for working with AI. It was set up from the
GP Operating Toolkit, and it keeps growing: you can add workflows at any time. The toolkit
machinery — the setup engine and the library of workflow templates — lives at {KIT_LOCATION}
and runs whenever you add or change a workflow.

## How this repository is organized
- `_shared-config/` — the firm, captured once: `firm-profile.md` and `voice-and-tone.md`. Every
  workspace reads these. This is the firm-level context that is true regardless of workflow.
- `workspaces/` — your live workspaces. Each has its own `CLAUDE.md` that maps it; open the
  workspace folder and read that file to work in it.
- The toolkit, at {KIT_LOCATION} — the setup engine (`SETUP.md`) and the workflow library
  (`architectures/`, `constraints/`, `skill-starters/`). You rarely open these directly; you
  reach them by saying "add a workflow."

## Workspaces built
{BUILT_LIST}

## Add a workflow

This operating system is not finished — it grows with the firm. To add a new workflow, set up
another instance of one you already run, or stand up any toolkit workflow type you have not built
yet, just say **"Run setup"**, **"add a workflow"**, or **"build a &lt;workflow&gt;"**. That
routes to {KIT_POINTER}, which runs the build.

Building *copies* a template into a new `workspaces/<name>/`; it never consumes the template. So
every workflow type stays available forever, and you can build the same type more than once (for
example, a second `deal-pipeline` for a different deal — just give it a distinct name).

Workflow types still available to build:
{AVAILABLE_LIST}

## Working in a workspace

To use a workspace that already exists, open its folder and read its `CLAUDE.md` — that file is
the map for that workspace. This file is the map for the firm.

## A note on the `L0`–`L4` tags you'll see
Files across the workspaces are tagged with a context layer, which just says *when* the file is
meant to be read: **L0** the always-on map (`CLAUDE.md`), **L1** the workflow router (`CONTEXT.md`),
**L2** a single step's instructions (a stage `CONTEXT.md`), **L3** reference the model follows
(voice, rules, schemas), **L4** the working files it transforms (source data, drafts). You do not
have to manage these; they are there so each step loads only what it needs.
```

### `_shared-config/setup-progress.md` template

Write this file at the end of the first setup, and keep it in sync with the OS map on every later
build (the two must always agree). Use exactly this structure so it stays consistent across sessions:

```markdown
# Setup Progress — {FIRM_NAME}

Records what has been built from the GP Operating Toolkit. The existence of this file is the signal
that first-time setup has already run. This file and the OS-map `CLAUDE.md` must always agree.

## Firm
- {FIRM_NAME} — {one-line strategy}. Orientation completed: {YYYY-MM-DD}.

## Workspaces built
| # | Workspace | Workflow type | Built | State |
|---|---|---|---|---|
| 1 | `workspaces/{name}/` | {workflow} | {YYYY-MM-DD} | {one-line state} |

## Workflow types still available to build
{comma-separated list of the eleven types not yet built}

## Finalized
{Omit until finalize runs. Then add one dated line per finalize/restore event.}
```

After writing the OS map, tell the user setup is complete and that they can keep building any
time by saying "add a workflow." Mention finalize as an optional, reversible tidy-up step they
can run whenever they want the repo root to read purely as their operating system.

## Keeping the OS Map Current

After **every** subsequent build (on the returning path), refresh the root `CLAUDE.md`:
- Add the new workspace to the **Workspaces built** list (`{BUILT_LIST}`).
- Remove that workflow type from **Workflow types still available to build** (`{AVAILABLE_LIST}`)
  the *first* time that type is built, and never re-add it. Building a second instance of an
  already-built type therefore does not change the available list — you can always build more
  instances regardless of what that list shows.
- Leave `{KIT_POINTER}` and `{KIT_LOCATION}` set to wherever the kit currently lives (`SETUP.md`
  / the repo root before finalize, `_kit/SETUP.md` / `_kit/` after).

Also append the new workspace to `_shared-config/setup-progress.md`. The OS map and
setup-progress.md must always agree on what has been built.

## Finalize (make this your operating system)

Finalize is an **explicit, reversible** step the firm runs when it wants the repo root to read
purely as its operating system, with the toolkit tucked out of the way. It is a near-pure folder
move — by this point `CLAUDE.md` is already the OS map, so there is no entry-file rewrite.

Run finalize **only when the user explicitly asks** ("finalize," "make this our operating
system," "tuck the toolkit away"). Never finalize automatically, and never finalize the source
toolkit repo — only a firm's own working copy.

Steps:
1. Create `_kit/` at the repo root.
2. Move the toolkit into it: `SETUP.md`, `architectures/`, `constraints/`, and `skill-starters/`
   all move into `_kit/`. (This file becomes `_kit/SETUP.md`.) Do **not** move `_shared-config/`,
   `workspaces/`, `CLAUDE.md`, `README.md`, or `LICENSE` — those stay at the root.
3. Update the OS-map `CLAUDE.md`: change `{KIT_POINTER}` from `SETUP.md` to `_kit/SETUP.md`, and
   change **both occurrences** of `{KIT_LOCATION}` from `the repo root` to `` `_kit/` ``.
4. Write `_kit/RESTORE.md` from the template below.
5. Update `README.md`: anywhere it locates the toolkit folders (`architectures/`, `constraints/`,
   `skill-starters/`) at the repo root, note they now live under `_kit/`. A standing parenthetical
   is enough — the goal is that a reader following `README.md` after finalize looks in the right
   place. (Restore reverses this.)
6. Record the finalize in `_shared-config/setup-progress.md` (a dated "Finalized" line).

After finalize, the firm keeps building exactly as before — "add a workflow" now routes to
`_kit/SETUP.md`, and builders copy from `_kit/architectures/`. Nothing about ongoing building
changes except the path the kit lives at.

### `_kit/RESTORE.md` template

Write exactly this when finalizing:

```markdown
# RESTORE — reverse the finalize step

This repository was finalized: the GP Operating Toolkit was moved from the repo root into
`_kit/` so the root reads as the firm's operating system. This file reverses that move.

## What finalize did
- Moved `SETUP.md`, `architectures/`, `constraints/`, and `skill-starters/` into `_kit/`.
- Updated `CLAUDE.md` (the OS map) so "add a workflow" points to `_kit/SETUP.md`.
- Noted in `README.md` that the toolkit folders now live under `_kit/`.
- Recorded the finalize in `_shared-config/setup-progress.md`.

## To restore the original root layout
1. Move the four items back to the repo root:
   `mv _kit/SETUP.md _kit/architectures _kit/constraints _kit/skill-starters .`
2. In `CLAUDE.md`, change the kit pointer from `_kit/SETUP.md` back to `SETUP.md`, and change
   both kit-location mentions from `_kit/` back to `the repo root`.
3. In `README.md`, remove the `_kit/` note so it again locates the toolkit at the repo root.
4. Note the reversal in `_shared-config/setup-progress.md`.
5. Delete the now-empty `_kit/` and this file.

Nothing in `_shared-config/` or `workspaces/` moves during finalize or restore — your firm
config and live workspaces stay at the root throughout. Building still works in both layouts;
only the path the toolkit lives at changes.
```

## How the Three Parts Relate

The constraints are the principles. The architectures are worked examples of those principles
applied to a GP workflow. The skill-starters turn an architecture into a customized workspace
for one firm. You move left to right: understand the constraint, study the architecture, run
the builder. Each workspace, once built, is self-documenting — its own `CLAUDE.md` is the map
for that workspace, the same way the root `CLAUDE.md` is the map for the firm.

A note on support-folder naming: every workspace has a `_config/` (the firm's own rules, voice,
and terms). The second support folder is named for the job that workspace does, not by accident —
`_references/` for cross-deal knowledge shared across runs (comps, standards, prior records),
`_prompts/` for reusable prompt fragments, `_store/` for the accumulating memory of a learning-loop
workspace (where the store *is* the deliverable), `_templates/` for reusable output patterns, and
`_example/` for a fully worked sample run. The variation is deliberate; match the folder to the
work, not to a uniform name.
