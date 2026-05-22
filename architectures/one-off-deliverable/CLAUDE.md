# One-Off Deliverable Workspace

## What This Is
A workspace for producing a single serious deliverable from a messy, unvetted source set — an IC memo, a hold/sell case, a diligence brief, a one-time LP or lender letter. Built for the deliverable that matters but maps to no recurring lifecycle stage: someone hands you a folder of files of unknown age and authority, and the deliverable is due once.

This is the non-recurring cousin of the document-production workflows. lp-reporting runs a letter every quarter; asset-management reviews on a cycle. This workspace runs once and is done. Its discipline is the discipline of Constraint 10 (Source Provenance): inspect the source set before you draft, so the deliverable rests on the authoritative version of each fact instead of a confident blend of three.

The order is non-negotiable: **inventory the sources, have a human review the inventory, then draft.** The single most important artifact is not the deliverable — it is `01_inventory/output/source_inventory.md`. A draft produced before the inventory is reviewed is a draft produced on faith.

## Current State
- This is a reference architecture. No active deliverable.
- To use: copy the folder, rename it for the deliverable, drop the source set into `00_sources/`, and populate `_config/`.

## Structure
```
one-off-deliverable/
  CLAUDE.md              # You are here.
  CONTEXT.md             # Workflow routing.
  00_sources/            # Copied originals. Immutable provenance anchor. Never edited.
  01_inventory/
    CONTEXT.md           # Stage contract: the provenance pass + the review gate.
    output/              # source_inventory.md, the three logs, source summaries.
  02_draft/
    CONTEXT.md           # Stage contract: the grounded deliverable.
    output/              # The deliverable, citing every claim to a source ID.
  _config/               # Deliverable spec and source hierarchy for this run.
  _references/           # Cross-deliverable knowledge, if any applies.
```

## How to Use
1. Read CONTEXT.md for the full workflow.
2. Populate `_config/deliverable-spec.md` (what the deliverable is, who reads it, what it must do) and, once known, `_config/source-hierarchy.md` (the authority ladder for this source set).
3. Copy the raw source set into `00_sources/`. Copy, never move — the originals are the provenance anchor every citation points back to.
4. Run 01_inventory. It runs the provenance pass (Constraint 10): inventory every file, rank authority, summarize the high-relevance sources, and log duplicates, conflicts, and missing context. **Then it stops and hands the room back for review.**
5. Review the inventory — this is the checkpoint that matters. Spot-check what was marked authoritative vs. superseded. If the agent cannot explain why one source outranks another, do not let it draft.
6. Run 02_draft. It writes the deliverable from the reviewed inventory, citing every claim to a source ID, labeling inferences, and flagging anything the inventory does not support.

## Key Decisions
- **Inventory is a stage, not a preamble.** The most common cause of a confidently wrong deliverable is not a bad prompt; it is a source set no one inspected. Making the provenance pass its own gated stage forces the inspection to happen before a sentence is written. See Constraint 10.
- **The review gate sits inside 01, not 02.** The build stops after the inventory and hands back to a human. Drafting does not begin until the inventory is reviewed. This is the one rule the workspace exists to enforce.
- **One deliverable, then done.** This is a unit of work, not infrastructure. A project that changes purpose gets a fresh copy of the workspace. If the same deliverable starts recurring on a cycle, it has outgrown this shape — move it to a document-production workflow (lp-reporting, asset-management). For a standing, org-wide knowledge base, that is a wiki, built elsewhere.
- **The room owns language; the platform owns numbers.** This workspace prepares language and judgment. NAV, capital balances, the waterfall, IRR, and any audited figure come from the fund-administration platform or the financial model — cited, never invented, never blended across versions. See Constraint 09.
- **`00_sources/` is immutable.** Originals are copied in and never modified, renamed, or deleted. Superseded and duplicate files are flagged in the logs, not removed. History is part of provenance (Constraint 10).

## Constraints That Apply
Built against the GP Operating Toolkit. Most relevant: **10 (Source Provenance)** — this workspace is that constraint given a folder structure; the inventory, the authority ladder, and the duplicate/conflict/missing-context logs are its four artifacts. Plus **01 (AI Writing Patterns)** and **02 (Output Drift)** so the deliverable reads clean and stays internally consistent, and the universal **06 (Layer Triage)** and **09 (Platform Boundary)** so the model narrates figures and never computes them.

## Layer Annotations
- CLAUDE.md: L0 (always loaded, orientation)
- CONTEXT.md: L1 (workflow routing)
- Stage CONTEXT.md files: L2 (stage contracts)
- _config/ files: L3 (this deliverable: spec, source hierarchy)
- _references/ files: L3 (cross-deliverable, if any applies)
- Copied sources, the inventory, and the draft: L4 (working artifacts)
