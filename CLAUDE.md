# GP Operating Toolkit: Onboarding Map

## What This Is

You are an AI agent. Someone has handed you this repository and asked you to set up
their operating system for working with AI. This file is your starting point. It tells you
what is here and the order to use it in. Read it first, then navigate to the specific files
each step calls for. Do not load everything at once. That is the whole point of the toolkit.

This repository is the GP Operating Toolkit, built for private equity and commercial real
estate firms. It has three parts:

- **/constraints** — ten reference files, each solving a specific problem GPs hit when
  working with AI. You load these selectively, matched to the workflow being built.
- **/architectures** — nine reference workspaces. Eight span the GP lifecycle (deal-screening,
  deal-pipeline, asset-management, disposition, lp-reporting, lp-inquiries,
  deal-win-loss-learning, market-thesis); the ninth, one-off-deliverable,
  produces a single deliverable from an unvetted source set when the work maps to no lifecycle
  stage. Each is a working folder structure with its own `CLAUDE.md`, `CONTEXT.md`, and stage
  contracts. You copy and customize one to build the user's workspace.
- **/skill-starters** — nine builder skills, one per architecture. Each runs a diagnostic
  interview, then assembles a workspace from the answers. These do the actual building.

## Start Here

If you are reading this, the user already has the files. If they do not, tell them: clone
or download the repository to their working directory, then point you at this `CLAUDE.md`.
Everything below assumes the files are local and you can read and write them.

Your job is not to lecture the user about context management. It is to run the sequence
below, asking before building, and to stop with a working, populated workspace they can use.

## The Onboarding Sequence

Run these steps in order. Each one names the file to read or run next.

1. **Diagnose the firm.** Ask the user what work they want to run with AI. Map their answer
   to one of the workflows using the routing table below. If they name more than one, handle
   the highest-priority workflow first and return for the others. Do not build them all at
   once.

2. **Pick the skill-starter.** Open the matching builder in `/skill-starters`. It is the
   instruction set for the build. Do not improvise a workspace; the builder's diagnostic
   questions are the work.

3. **Run the diagnostic interview.** Ask the builder's questions one at a time. Wait for each
   answer. The answers become the content of the workspace. Do not skip ahead to assembly.

4. **Load the constraints this workflow needs.** Before assembling, read the constraint files
   named for this workflow in the constraint routing table below. They shape the stage
   contracts and the `_config` files you are about to write. Load only those. Loading all ten
   is the context-hygiene mistake the toolkit exists to prevent.

5. **Instantiate the workspace.** Copy the matching architecture from `/architectures`, rename
   it for the user's deal/fund/cycle, and follow the builder's assembly phase to write
   `CLAUDE.md`, `CONTEXT.md`, the stage contracts, and the `_config` files from the interview
   answers. The reference architecture's own files show you the target shape.

6. **Populate `_config` with real values.** Walk the user through filling the `_config` files
   with their actual rules, voice, terms, and constraints. A workspace with empty `_config` is
   a template, not an operating system. Help them fill at least the required files before you
   call onboarding done.

7. **Verify.** Run the Onboarding Complete checklist below. Report each item as pass or open.
   Do not declare onboarding complete while any item is open.

## Diagnose → Route

Match the user's primary work to a workflow and its builder.

| If the user's core work is… | Workflow | Builder to run |
|---|---|---|
| Triaging inbound deal flow — deciding which opportunities merit diligence | deal-screening | `skill-starters/deal-screening-builder.md` |
| Acquiring assets — sourcing, diligence, investment committee, closing | deal-pipeline | `skill-starters/deal-pipeline-builder.md` |
| Monitoring owned assets — business-plan-vs-actual reviews, watchlist | asset-management | `skill-starters/asset-management-builder.md` |
| Exiting an asset — hold/sell decision through sale and capital return | disposition | `skill-starters/disposition-builder.md` |
| Investor communications — quarterly letters, capital account statements, notices | lp-reporting | `skill-starters/lp-reporting-builder.md` |
| Handling inbound LP questions between formal events | lp-inquiries | `skill-starters/lp-inquiries-builder.md` |
| Learning why we win or lose competitive deals to sharpen the next bid | deal-win-loss-learning | `skill-starters/deal-win-loss-learning-builder.md` |
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
- **Learning loop** (deal-win-loss-learning): capture an outcome →
  analyze why → write to a store → read it back to inform the next time. Use when the goal is to
  make a repeated activity compound — the deliverable is the accumulating store, not any single
  record (e.g., a realized-deal post-mortem that sharpens future underwriting, or an
  LP-commit/pass debrief that sharpens the next raise — same loop, swap the config).

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
whole library.

| Workflow | Load these constraints | Why |
|---|---|---|
| **All workflows** | 06 (Layer Triage), 09 (Platform Boundary) | Decide what is AI vs. deterministic vs. platform before building. Roughly 60% traditional, 30% rule-based, 10% AI. |
| **deal-pipeline** | + 01 (AI Writing), 02 (Output Drift), 08 (Handoff) | Memos and theses must read clean and survive a handoff to asset management. |
| **lp-reporting** | + 01 (AI Writing), 02 (Output Drift), 05 (Voice Architecture) | The letter must sound like the firm and stay consistent cycle to cycle. |
| **deal-screening** | + 02 (Output Drift), 10 (Source Provenance) | Screens must be comparable deal to deal; opportunities arrive as unvetted source sets. |
| **asset-management** | + 02 (Output Drift), 04 (Session Consistency), 08 (Handoff), 10 (Source Provenance) | Reviews repeat on a cycle, hand off to the IC, and ingest unvetted asset reports. |
| **disposition** | + 01 (AI Writing), 02 (Output Drift), 08 (Handoff) | The hold/sell case and disposition package must read clean and hand off cleanly at close. |
| **lp-inquiries** | + 02 (Output Drift), 04 (Session Consistency), 05 (Voice Architecture) | Responses must be consistent and on-voice across many responders. |
| **deal-win-loss-learning** | + 03 (Context Hygiene), 04 (Session Consistency), 08 (Handoff) | Records must be comparable to aggregate; the store stays clean and handoff-readable, and broker spin must be kept out of it. |
| **market-thesis** | + 01 (AI Writing), 02 (Output Drift), 10 (Source Provenance) | The thesis must read sharp, stay consistent, and rest on vetted sources. |
| **one-off-deliverable** | + 10 (Source Provenance), 01 (AI Writing), 02 (Output Drift) | The workspace *is* a provenance pass made concrete; the deliverable must also read clean and stay internally consistent. |
| **Scaling any workflow** | + 07 (Scaling vs. Automating) | When the same workflow runs many times, decide what to template vs. automate. |
| **Context degrading mid-build** | + 03 (Context Hygiene) | If your own context gets noisy during a long onboarding, this is the fix. |
| **Ingesting a data room or unvetted source set** | + 10 (Source Provenance) | Inventory and rank inputs before any stage drafts. AI flags provenance, duplicates, and conflicts; the platform owns the figures. |

## Onboarding Complete

Onboarding is done when every item below is true. Report each as pass or open.

- [ ] **Workflow identified.** The user confirmed which workflow(s) they are building.
- [ ] **Workspace instantiated.** The architecture was copied and renamed; it has a
      `CLAUDE.md`, a `CONTEXT.md`, and a `CONTEXT.md` for every stage.
- [ ] **`_config` populated.** The required reference files hold the user's real values, not
      placeholder text.
- [ ] **Constraints loaded and named.** The constraints from the routing table were read, and
      the workspace `CLAUDE.md` names which ones apply.
- [ ] **One stage run end to end.** At least one stage produced real output, checked against
      its "Done Looks Like" line. Compare it to `/architectures/lp-reporting/_example` to see
      what finished output looks like.
- [ ] **Handoff-ready.** A new team member could open the workspace folder and understand it
      without you in the room (Constraint 08 is the test for this).

If any box is open, return to the step that produces it. A half-built workspace handed off as
"done" is the failure mode this checklist exists to prevent.

## How the Three Parts Relate

The constraints are the principles. The architectures are worked examples of those principles
applied to a GP workflow. The skill-starters turn an architecture into a customized workspace
for one firm. You move left to right: understand the constraint, study the architecture, run
the builder. Each workspace, once built, is self-documenting — its own `CLAUDE.md` is the map
for that workspace, the same way this file is the map for the toolkit.

A note on support-folder naming: every workspace has a `_config/` (the firm's own rules, voice,
and terms). The second support folder is named for the job that workspace does, not by accident —
`_references/` for cross-deal knowledge shared across runs (comps, standards, prior records),
`_prompts/` for reusable prompt fragments, `_store/` for the accumulating memory of a learning-loop
workspace (where the store *is* the deliverable), `_templates/` for reusable output patterns, and
`_example/` for a fully worked sample run. The variation is deliberate; match the folder to the
work, not to a uniform name.
