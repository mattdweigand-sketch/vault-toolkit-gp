# GP Operating Toolkit — Setup & Build Engine

## What This File Is

You are an AI agent. This file is the **setup engine** for the GP Operating Toolkit. It runs
the firm's one-time orientation, builds workspaces, keeps the operating-system map current, and
(when the firm is ready) finalizes the repository into the firm's own AI operating system.

You did not start here. Codex reads the root `AGENTS.md` directly. Claude Code auto-loads
`CLAUDE.md`, which is only a thin wrapper that imports `AGENTS.md`. The root `AGENTS.md` is the
bootstrap that sends you here when setup has not run yet. From here on, this file is the
machinery; `AGENTS.md` is the artifact.

Read this file first, then navigate to the specific files each step calls for. Do not load
everything at once. That is the whole point of the toolkit.

This repository is the GP Operating Toolkit, built for private equity and commercial real
estate firms. Its worked examples name commercial-real-estate systems of record (Argus, Yardi,
MRI, RealPage); when building for a PE deal team, read those as placeholders for the firm's own
deal model and portfolio or fund-accounting systems — the logic transfers unchanged. It has
three parts:

- **architectures/** — reference workspaces for the high-judgment layer above GP platforms:
  IC pressure testing, diligence evidence mapping, underwriting backtests, portfolio intervention,
  hold/sell/refi decisions, market thesis to investment-box updates, LP narrative and issue prep,
  firm memory loops, plus lifecycle and one-off variants. Each is a working folder structure with
  its own `CLAUDE.md`, `CONTEXT.md`, and stage contracts. You copy and customize one to build the
  user's workspace.
- **constraints/** — ten reference files, each solving a specific problem GPs hit when
  working with AI. You load these selectively, matched to the workflow being built.
- **skill-starters/** — builder skills, one per architecture or variant. Each runs a diagnostic
  interview, then assembles a workspace from the answers. These do the actual building.

Legacy lifecycle templates live under `architectures/_variants/` and
`skill-starters/_variants/`. They are reference material, not primary setup routes.

> **Where the toolkit lives.** Before the firm finalizes, these three folders and this
> `SETUP.md` sit at the repo root. After finalize, they move together into `_kit/` and this
> file becomes `_kit/SETUP.md`. Everything in this file works in both states; where a path
> differs, it is called out as "root before finalize, `_kit/` after."

## A Note on Context Layers (ICM)

The architectures and builders tag every file with a context layer (L0–L4) under the
Interpreted Context Methodology (ICM). The layer says *when* a file loads: L0 the
always-loaded map (`AGENTS.md` at the root, `CLAUDE.md` inside workspaces), L1 routing
(`CONTEXT.md`), L2 the per-task stage contract, L3 reference the model should follow
(voice, standards), and L4 working files the model
should transform (source data, drafts). The discipline is to load only what a step needs, and
to keep "rules to follow" (L3) distinct from "content to transform" (L4) so the model does
not confuse the two. Constraint 03 (Context Hygiene) defines the full model — read it before
you start stamping layer tags on the files you build.

The word *layer* shows up in two unrelated ways across this toolkit; keep them separate.
**Context layers (L0–L4)**, the subject of this note, describe *when* a file loads. **Solution
layers (60/30/10)**, named in the constraint routing table below, describe *what kind of tool*
should solve a problem — traditional software, a rule-based system, or a language model. Same
word, different question.

## Context Matrix

The matrix below is the load contract for setup. It says what to read for each workflow, and at
what depth, before a builder starts asking diagnostic questions. It complements the context-layer
tags: ICM says *when* a file loads; this matrix says *how much* of each shared file a builder needs.

Load levels:
- **full:** read the whole file.
- **summary:** use only the relevant digest or top-line facts.
- **section:** read only the named section.
- **pointer:** know the file exists; open it only when the builder or current answer requires it.
- **writes:** the builder creates or updates this file.
- **none:** do not load.

| Workflow | `_shared-config/firm-profile.md` | `_shared-config/voice-and-tone.md` | `_shared-config/learnings.md` | Constraints | Architecture | Builder |
|---|---|---|---|---|---|---|
| `underwriting-backtest` | full | summary | `## General`, `## underwriting-backtest` | routed list | pointer | full |
| `ic-pressure-test` | full | summary | `## General`, `## ic-pressure-test` | routed list | pointer | full |
| `diligence-evidence-map` | full | summary | `## General`, `## diligence-evidence-map` | routed list | pointer | full |
| `portfolio-intervention` | full | summary | `## General`, `## portfolio-intervention` | routed list | pointer | full |
| `hold-sell-refi` | full | summary | `## General`, `## hold-sell-refi` | routed list | pointer | full |
| `market-thesis-to-investment-box` | full | full | `## General`, `## market-thesis-to-investment-box` | routed list | pointer | full |
| `lp-narrative-and-issue-prep` | full | full | `## General`, `## lp-narrative-and-issue-prep` | routed list | pointer | full |
| `firm-memory-loop` | full | summary | `## General`, `## firm-memory-loop` | routed list | pointer | full |

Load only what the matrix names. Do not open every constraint, every architecture, or all of
`_shared-config/` because it feels safer. If a build truly needs extra context, say why, then
load the smallest file or section that answers the question.

## Run Setup Starts Here

This is the entry point. When the user says **"Run setup"**, **"add a workflow"**, **"build a
&lt;workflow&gt;"**, or opens a session with no specific task, do this first:

1. Run `python3 scripts/setup_state.py status`. If you need machine-readable output, run
   `python3 scripts/setup_state.py status --json`.
2. If the status is `not_started`, run `python3 scripts/setup_state.py init-session`, then run
   **Firm Orientation** and **Value Triage Before Workflow Routing**.
3. If the status is `in_progress` or `ready_to_build`, read `_shared-config/setup-session.json`
   and follow **Resume Rules**. Do not restart orientation or re-ask answered questions.
4. If the status is `complete`, read `_shared-config/firm-profile.md` and
   `_shared-config/setup-progress.md`, greet the firm by name, summarize what has been built, and
   offer to add another workflow, set up another instance of one already built, update shared
   config, or resume an unfinished one. Do not re-run orientation. After the build, run
   **Keeping the OS Map Current**.
5. For any confusing or contradictory state, run `python3 scripts/setup_state.py doctor`, report
   the open items, and fix only the item needed to continue.

`_shared-config/setup-session.json` is temporary working state. `_shared-config/setup-progress.md`
is still the durable signal that first-time setup completed.

Always ask before building, and stop with a working, populated workspace the firm can use. Do not
make onboarding feel like a form. Ask one question at a time, skip anything already answered in a
prior response, and acknowledge the skip briefly so the user knows you heard it. Show the full
workflow menu only if the user asks for it or the mapping is genuinely ambiguous.

### Resume Rules

If `_shared-config/setup-session.json` exists, resume from it:

- Use `current_phase`, `current_step`, and `current_question` to find the next action.
- Treat populated `firm_orientation`, `value_triage`, `selected_workflow`, and `answers` as
  already answered unless the user says they changed.
- After each setup answer, record it with
  `python3 scripts/setup_state.py record --field <dotted.path> --value '<json-or-text>'`.
- Record high-stakes unknowns in `open_confirmations`; do not silently fill them.
- Clear the session only after setup completes, or when the user explicitly asks to restart setup:
  `python3 scripts/setup_state.py clear-session`.

### Value Triage Before Workflow Routing

Before naming a workflow, apply the platform-boundary filter. If the user wants AI to own records,
workflow state, entitlement, calculations, audit, dashboards, data extraction, fund accounting,
capital activity, DDQ execution, or pipeline tracking, route that work to the relevant platform.
The toolkit may still build the judgment layer above it: interpretation, narrative, exception
handling, decision framing, or memory.

Then ask what recurring or high-stakes work is painful, expensive, risky, or slow today. Score each
candidate from 1 to 5 on:

- **Frequency:** how often the work recurs.
- **Risk:** how expensive a wrong output or missed handoff would be.
- **Data readiness:** whether the source material is accessible and has an owner.
- **Decision leverage:** whether better synthesis changes an investment, reporting, or operating
  decision.
- **Adoption ease:** whether one team can use the workspace without a platform migration.

Recommend the highest-scoring workflow and explain why. If the user has no strong preference and
the scores tie, use this tie-breaker: `ic-pressure-test`, then `diligence-evidence-map`, then
`portfolio-intervention`, then `firm-memory-loop`. If the user clearly names a workflow, still
apply the platform-boundary filter before building.

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

## Shared Builder Kernel

Every workflow builder uses the same kernel. The `skill-starters/` files add workflow-specific
questions and assembly rules; they do not replace this protocol.

1. Read `_shared-config/firm-profile.md`.
2. Read `_shared-config/voice-and-tone.md` only at the depth named in the **Context Matrix**.
3. Read `_shared-config/learnings.md`, but only `## General` and the current workflow section.
4. Ask builder questions one at a time. After each answer, record it in
   `_shared-config/setup-session.json` with `scripts/setup_state.py record`.
5. Load only the constraints named in **Constraint Routing** for the workflow being built.
6. Copy the architecture into `workspaces/<name>/` and customize from the user's answers. Do not
   improvise a new structure when a matching architecture exists.
7. Populate `_config/` with real values from shared config and the diagnostic answers. Mark
   high-stakes unknowns as `[NEEDS CONFIRMATION - <owner>]` and routine missing inputs as `[TBD]`.
8. Populate `_config/before-you-trust-this.md` with every high-stakes unknown, owner, and status.
9. Name the loaded constraints in the workspace `CLAUDE.md`.
10. Run the Onboarding Complete checklist and report `MVP ready` or `Operating ready`.

## The Onboarding Sequence

Run these steps in order. Each one names the file to read or run next.

1. **Route the work.** The firm itself is already captured in `_shared-config/` (from Firm
   Orientation). Use **Value Triage Before Workflow Routing** unless the user already named a
   workflow. Map the highest-value answer to one workflow using the routing table below. If they
   name more than one, handle the highest-priority workflow first and return for the others. Do not
   build them all at once. Record the selected workflow in `_shared-config/setup-session.json`.

2. **Pick the skill-starter.** Check the **Context Matrix** for the workflow, then open the
   matching builder in `skill-starters/` (root before
   finalize, `_kit/skill-starters/` after). It is the instruction set for the build. Do not
   improvise a workspace; the builder's diagnostic questions are the work. Load only the
   firm-profile, voice, learnings, constraints, and architecture files named by the matrix and
   routing table.

3. **Run the diagnostic interview.** Use the **Shared Builder Kernel** and the selected builder's
   questions. Ask one question at a time and wait for each answer. The answers become the content
   of the workspace. Do not skip ahead to assembly.

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
| Pressure-testing a pending IC memo before committee | ic-pressure-test | `skill-starters/ic-pressure-test-builder.md` |
| Inspecting a diligence room, ranking sources, and mapping open questions | diligence-evidence-map | `skill-starters/diligence-evidence-map-builder.md` |
| Turning portfolio signals or variances into diagnosis and owned actions | portfolio-intervention | `skill-starters/portfolio-intervention-builder.md` |
| Deciding whether to hold, sell, refinance, recapitalize, or revisit an asset | hold-sell-refi | `skill-starters/hold-sell-refi-builder.md` |
| Turning a market thesis into a sourcing or screening criteria change | market-thesis-to-investment-box | `skill-starters/market-thesis-to-investment-box-builder.md` |
| Preparing LP narrative, likely questions, and issue posture around platform-verified facts | lp-narrative-and-issue-prep | `skill-starters/lp-narrative-and-issue-prep-builder.md` |
| Creating a reusable memory loop for repeated GP judgment | firm-memory-loop | `skill-starters/firm-memory-loop-builder.md` |
| Learning why realized deals beat or missed their underwriting, to calibrate future models | underwriting-backtest | `skill-starters/underwriting-backtest-builder.md` |

If the user is unsure which they need, or wants to know where AI belongs at all before
building anything, start them with **Constraint 06 (Layer Triage)** and **Constraint 09
(Platform Boundary)**. Those two answer "what should AI do, and what should my platform own"
before a single folder is created.

Recurring back-office operations — capital calls, distributions, transfers, onboarding — are
deliberately not on this list. They are platform-governed transactions (capital accounts, the
waterfall, the audit trail), and they belong on the fund-administration platform, not in an AI
workspace. Do not build a workspace to process them. AI's role around these events is the
language and the judgment on top of the platform: preparing LP narrative and issue posture around
platform-verified facts. See Constraint 09.

Capital formation — the raise itself, subscriptions, investor onboarding, DDQ execution, and the
data room — is out of scope for the same reason: the investor-management and fund-administration
platform owns that pipeline and the investor record. AI's contribution is the language and judgment
around it (narrative, tailoring, and the LP-commit/pass debrief that feeds a memory loop), not a
workspace that runs the raise.

### If the work matches none of the rows

The rows above are not an exhaustive catalog. They are instances of five structural *shapes*,
and most GP work is a variant of one of them. Do not jam an off-list workflow into the closest
row by topic. Classify it by shape first:

- **Gated decision pipeline** (ic-pressure-test, hold-sell-refi): advance one item
  through sequential stages, each a go/no-go, toward a terminal decision or action. Use when the
  work has review gates (e.g., a development project to delivery, a refinancing to close).
- **Recurring operations queue** (portfolio-intervention, lp-narrative-and-issue-prep): intake → process → deliver, repeated per
  request. Use when the same *type* of request arrives over and over (e.g., vendor onboarding,
  a tenant-credit review queue). Note the boundary: this shape fits the *language and judgment*
  around recurring requests, not the platform-governed processing of capital events themselves
  (see Constraint 09).
- **Recurring document production** (market-thesis-to-investment-box, lp-narrative-and-issue-prep): verified
  data → drafted narrative → distribution, on a cycle. Use when you produce a document from
  numbers you do not invent and the output changes downstream behavior.
- **Source provenance** (diligence-evidence-map): inspect a source set,
  rank authority, log conflicts, then map evidence to claims or questions. Use when the risk is
  that the model will blend stale, duplicate, or conflicting sources before a human knows what is
  in the room.
- **Learning loop** (firm-memory-loop, underwriting-backtest): capture
  an outcome → analyze why → write to a store → read it back to inform the next time. Use when the
  goal is to make a repeated activity compound — the deliverable is the accumulating store, not any
  single record. `underwriting-backtest` is the specialized flagship instance; `firm-memory-loop`
  covers new post-mortem patterns such as bid strategy, LP objections, portfolio interventions, or
  fundraising commit/pass learning.

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
enterprise platform already owns the workflow — CRM, pipeline, fund accounting, DDQ execution,
data extraction, dashboards, investor records, entitlement, calculations, or audit — do not
rebuild it. Build the language-and-judgment layer that rides on top of it.

## Constraint Routing

Load the constraints named for the workflow you are building. Read them before assembly, and
name them in the workspace `CLAUDE.md` so the user's team can find them later. Do not load the
whole library. (Constraint files are under `constraints/` before finalize, `_kit/constraints/`
after.)

| Workflow | Load these constraints | Why |
|---|---|---|
| **All workflows** | 06 (Layer Triage), 09 (Platform Boundary) | Decide what is AI vs. deterministic vs. platform before building. Roughly 60% traditional, 30% rule-based, 10% AI. |
| **underwriting-backtest** | + 04 (Session Consistency), 10 (Source Provenance), 03 (Context Hygiene), 08 (Handoff Readiness) | Records must be comparable to aggregate into a calibration table (04, load-bearing); the approved model and actuals are sourced data — pin which model version is the underwriting of record (10); the store stays clean and handoff-readable (03, 08). |
| **ic-pressure-test** | + 02 (Output Drift), 08 (Handoff Readiness), 10 (Source Provenance) | The pressure test must stay tied to source evidence and produce IC-ready questions and conditions. |
| **diligence-evidence-map** | + 10 (Source Provenance), 02 (Output Drift), 08 (Handoff Readiness) | The workspace is a source-control pass for diligence evidence and open questions. |
| **portfolio-intervention** | + 02 (Output Drift), 04 (Session Consistency), 08 (Handoff Readiness), 10 (Source Provenance) | Repeated interventions must be comparable, source-backed, and action-ready. |
| **hold-sell-refi** | + 01 (AI Writing Patterns), 02 (Output Drift), 08 (Handoff Readiness), 10 (Source Provenance) | The alternatives case must read clean, cite model outputs, and hand off to execution. |
| **market-thesis-to-investment-box** | + 01 (AI Writing Patterns), 02 (Output Drift), 10 (Source Provenance), 08 (Handoff Readiness) | The thesis must change downstream sourcing or screening behavior. |
| **lp-narrative-and-issue-prep** | + 01 (AI Writing Patterns), 02 (Output Drift), 05 (Voice Architecture), 08 (Handoff Readiness) | LP-facing explanation must stay on voice, source platform-verified facts, and route sensitive issues. |
| **firm-memory-loop** | + 03 (Context Hygiene), 04 (Session Consistency), 08 (Handoff Readiness), 10 (Source Provenance) | Records must be comparable and causal claims must be validated before becoming memory. |
| **Scaling any workflow** | + 07 (Scaling vs. Automating) | When the same workflow runs many times, decide what to template vs. automate. |
| **Context degrading mid-build** | + 03 (Context Hygiene) | If your own context gets noisy during a long onboarding, this is the fix. |
| **Ingesting a data room or unvetted source set** | + 10 (Source Provenance) | Inventory and rank inputs before any stage drafts. AI flags provenance, duplicates, and conflicts; the platform owns the figures. |

## Onboarding Complete

Onboarding has two valid completion states. Report every item below as pass or open, then name the
state.

**MVP ready** means the workspace is configured, gates are present, open confirmations are listed,
and the team can use it when the first live input arrives.

**Operating ready** means MVP ready plus one stage has run end to end against live or sample input.

- [ ] **Workflow identified.** The user confirmed which workflow(s) they are building.
- [ ] **Workspace instantiated.** The architecture was copied and renamed; it has a
      `CLAUDE.md`, a `CONTEXT.md`, and a `CONTEXT.md` for every processing stage. (A raw
      input-drop folder such as diligence-evidence-map's `00_sources/` intentionally has none.)
- [ ] **`_config` populated.** The required reference files hold the user's real values, not
      placeholder text. Any value the firm did not supply is flagged, not invented: use
      `[NEEDS CONFIRMATION - <owner>]` for high-stakes values (compliance language, financial
      thresholds, rosters) and `[TBD]` for data not yet available. See Constraint 08.
- [ ] **High-stakes values gated.** `_config/before-you-trust-this.md` lists every
      `[NEEDS CONFIRMATION]` value with its owner and status. Nothing client-facing ships until
      the high-stakes rows are cleared. (Constraint 08 defines the convention.)
- [ ] **Constraints loaded and named.** The constraints from the routing table were read, and
      the workspace `CLAUDE.md` names which ones apply.
- [ ] **MVP state recorded.** `_shared-config/setup-progress.md` and the OS map describe the
      workspace as `MVP ready` when no live stage has run yet, with open confirmations named.
- [ ] **One stage run end to end.** For `Operating ready`, at least one stage produced real output,
      checked against
      its "Done Looks Like" line. Compare it to the architecture's `_example`, when present, to see
      what finished output looks like. If there is no live input yet (a backtest with no realized
      deal, a learning loop with no resolved record, a brand-new cycle), the workspace's own
      `_example/` is the stand-in run, and the workspace is marked "stands up now, activates on
      first &lt;exit / cycle / inquiry&gt;."
- [ ] **Handoff-ready.** A new team member could open the workspace folder and understand it
      without you in the room (Constraint 08 is the test for this).

If a required MVP box is open, return to the step that produces it. Do not call the workspace
`Operating ready` until the stage-run box is complete. A half-built workspace handed off as "done"
is the failure mode this checklist exists to prevent.

## After a Build

Ask: "Anything about this workflow setup that should be remembered for next time?"

If yes, write the reusable rule to `_shared-config/learnings.md` under the workflow section. If
the lesson applies across workflows, write it under `## General`. Do not write task logs here.
Good entries name the date, the reusable rule, and the evidence for it. Bad entries merely say
what was built.

## Registry Reconciliation

Before adding or modifying a workflow, compare:
- `architectures/<workflow>/`
- `skill-starters/<workflow>-builder.md`
- the Diagnose -> Route table
- the Constraint Routing table
- the README workflow list

If a workflow exists on disk but is missing from the tables, add it silently and report what
changed.

If a workflow is listed in the tables but missing on disk, stop and ask before removing it from
docs.

## After First Setup: Write the OS Map

At the end of the **first** setup — after the first workspace is built and
`_shared-config/setup-progress.md` is written — overwrite the root `AGENTS.md` with the
operating-system map below. This is the content metamorphosis: the canonical instruction file
stops being a toolkit bootstrap and becomes the firm's own OS map. `CLAUDE.md` stays a thin
wrapper that imports `AGENTS.md`. The change is safe and automatic: nothing of value is lost,
because the machinery already lives here in `SETUP.md`.

Fill the parametric fields from the firm's files:
- `{FIRM_NAME}` — from `_shared-config/firm-profile.md`.
- `{KIT_POINTER}` — `SETUP.md` before finalize, `_kit/SETUP.md` after. (At first-setup time it
  is always `SETUP.md`; the finalize step updates it.)
- `{KIT_LOCATION}` — a bare phrase naming where the toolkit currently lives: before finalize,
  `the repo root` (the kit folders and `SETUP.md` sit at the top level); after finalize, `` `_kit/` ``.
  It appears in **two** places in the template below; fill both with the same value.
- `{BUILT_LIST}` — one line per workspace in `_shared-config/setup-progress.md`.
- `{AVAILABLE_LIST}` — the workflow types not yet built.

Write exactly this structure (substituting the fields):

```markdown
# {FIRM_NAME} — AI Operating System

This repository is {FIRM_NAME}'s operating system for working with AI. It was set up from the
GP Operating Toolkit, and it keeps growing: you can add workflows at any time. The toolkit
machinery — the setup engine and the library of workflow templates — lives at {KIT_LOCATION}
and runs whenever you add or change a workflow.

## How this repository is organized
- `_shared-config/` — the firm, captured once: `firm-profile.md`, `voice-and-tone.md`, and
  `learnings.md`. Every workspace reads these by contract. This is the firm-level context that is
  true regardless of workflow.
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
example, a second `ic-pressure-test` for a different committee cycle — just give it a distinct name).

Workflow types still available to build:
{AVAILABLE_LIST}

## Working in a workspace

To use a workspace that already exists, open its folder and read its `CLAUDE.md` — that file is
the map for that workspace. This file is the map for the firm.

## A note on the `L0`–`L4` tags you'll see
Files across the workspaces are tagged with a context layer, which just says *when* the file is
meant to be read: **L0** the always-on map (`AGENTS.md` at the root, `CLAUDE.md` inside a
workspace), **L1** the workflow router (`CONTEXT.md`), **L2** a single step's instructions (a stage
`CONTEXT.md`), **L3** reference the model follows (voice, rules, schemas), **L4** the working files
it transforms (source data, drafts). You do not have to manage these; they are there so each step
loads only what it needs.
```

### `_shared-config/setup-progress.md` template

Write this file at the end of the first setup, and keep it in sync with the OS map on every later
build (the two must always agree). Use exactly this structure so it stays consistent across sessions:

```markdown
# Setup Progress — {FIRM_NAME}

Records what has been built from the GP Operating Toolkit. The existence of this file is the signal
that first-time setup has already run. This file and the OS-map `AGENTS.md` must always agree.

## Firm
- {FIRM_NAME} — {one-line strategy}. Orientation completed: {YYYY-MM-DD}.

## Workspaces built
| # | Workspace | Workflow type | Built | State |
|---|---|---|---|---|
| 1 | `workspaces/{name}/` | {workflow} | {YYYY-MM-DD} | {one-line state} |

## Workflow types still available to build
{comma-separated list of workflow types not yet built}

## Finalized
{Omit until finalize runs. Then add one dated line per finalize/restore event.}
```

After writing the OS map, tell the user setup is complete and that they can keep building any
time by saying "add a workflow." Mention finalize as an optional, reversible tidy-up step they
can run whenever they want the repo root to read purely as their operating system.

## Keeping the OS Map Current

After **every** subsequent build (on the returning path), refresh the root `AGENTS.md`:
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
move — by this point `AGENTS.md` is already the OS map, so there is no entry-file rewrite.

Run finalize **only when the user explicitly asks** ("finalize," "make this our operating
system," "tuck the toolkit away"). Never finalize automatically, and never finalize the source
toolkit repo — only a firm's own working copy.

Steps:
1. Create `_kit/` at the repo root.
2. Move the toolkit into it: `SETUP.md`, `architectures/`, `constraints/`, and `skill-starters/`
   all move into `_kit/`. (This file becomes `_kit/SETUP.md`.) Do **not** move `_shared-config/`,
   `workspaces/`, `AGENTS.md`, `CLAUDE.md`, `README.md`, or `LICENSE` — those stay at the root.
3. Update the OS-map `AGENTS.md`: change `{KIT_POINTER}` from `SETUP.md` to `_kit/SETUP.md`, and
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
- Updated `AGENTS.md` (the OS map) so "add a workflow" points to `_kit/SETUP.md`.
- Noted in `README.md` that the toolkit folders now live under `_kit/`.
- Recorded the finalize in `_shared-config/setup-progress.md`.

## To restore the original root layout
1. Move the four items back to the repo root:
   `mv _kit/SETUP.md _kit/architectures _kit/constraints _kit/skill-starters .`
2. In `AGENTS.md`, change the kit pointer from `_kit/SETUP.md` back to `SETUP.md`, and change
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
for that workspace, the same way the root `AGENTS.md` is the map for the firm.

A note on support-folder naming: every workspace has a `_config/` (the firm's own rules, voice,
and terms). The second support folder is named for the job that workspace does, not by accident —
`_references/` for cross-deal knowledge shared across runs (comps, standards, prior records),
`_prompts/` for reusable prompt fragments, `_store/` for the accumulating memory of a learning-loop
workspace (where the store *is* the deliverable), `_templates/` for reusable output patterns, and
`_example/` for a fully worked sample run. The variation is deliberate; match the folder to the
work, not to a uniform name.
