# SKILL: One-Off Deliverable Workspace Builder

## Description
Builds a customized workspace for producing a single serious deliverable from a messy, unvetted source set — an IC memo, a hold/sell case, a diligence brief, a one-time LP or lender letter. Asks diagnostic questions about the deliverable, where the sources came from, and what the book of record is, then assembles an inventory → review → draft workspace tuned to the run.

## When to Use
When someone hands you a folder of files of unknown age and authority and needs one serious deliverable out of it, and the work maps to no recurring lifecycle stage. This is the non-recurring cousin of the document-production workflows. If the same deliverable recurs on a cycle, use lp-reporting or asset-management instead. If the sources are already clean and inventoried, the inventory stage is light — but it still runs, because "the sources are clean" is itself a judgment a human should confirm, not assume.

## Process

### Phase 1: Diagnosis

> **Firm facts are already captured.** Run Setup wrote the firm's name, asset classes, systems of record, team, and voice to `_shared-config/` (firm-profile.md and voice-and-tone.md). Read those first. Do NOT re-ask firm-level facts — confirm them if needed. Ask only the workflow-specific questions below. If `_shared-config/firm-profile.md` does not exist yet, the firm skipped orientation; capture the basics first, then continue.

Ask the following questions one at a time. Wait for each answer.

**Question 1: What is the deliverable?**
"What single artifact does this workspace produce — an IC memo, a hold/sell case, a diligence brief, a one-time letter? Who reads it, what decision does it inform, and what does it have to accomplish to be good? Is there a format, length, or template it must follow?"

**Question 2: Where did the source set come from?**
"Where do the raw materials live, and how did they arrive — through a platform with a document register and version history, or as a pile in a shared drive or an email thread? This matters: if a register already tracks versions and owners, that register is your inventory and the workspace reads it rather than rebuilding it. If it is an un-pruned pile, the inventory stage is doing real work."

**Question 3: What is your book of record for numbers?**
"Name the single authoritative source for figures — the fund admin export, the GL, the executed term sheet, the audited statement. This is the source the workspace is never allowed to adjudicate against or recompute. If you cannot name one for a given number, that ambiguity is the first thing the inventory will surface."

**Question 4: How messy is the source set, really?**
"How often do you get three versions of the same model, a transcript with two meetings in it, a deck that no longer matches reality? If the inputs are clean and controlled, the inventory is light. If they are a year of un-pruned drafts, the duplicate and version analysis is the highest-value part of the workspace. Tune the depth to the mess."

**Question 5: Is anything in the set sensitive?**
"Are there files that must be noted but never copied or quoted into summaries or the draft — personal data, privileged material, anything under NDA? The workspace will record their existence and structure only and never reproduce their contents."

**Question 6: Does anything carry across deliverables?**
"Is there house style, a prior comparable deliverable, or a standing standard the draft should follow? For a true one-off there often is not — the deliverable is grounded in its own sources. But if something reusable exists, it goes in _references/ rather than being re-derived."

### Phase 2: Assembly

Based on the answers:

1. Confirm the shape. The default is two stages (01_inventory, 02_draft) with a human review gate between them. Adjust only if an answer demands it:
   - If deciding what is even in scope is its own job (a very large set): add 01a_triage in front of the inventory.
   - If the deliverable must clear a compliance or legal pass before it ships (a lender letter, a regulated disclosure): add 02a_review after the draft. Do not fold compliance into the draft stage.
   - Resist adding more. If the work needs many recurring stages, it is not a one-off — route it to a document-production workflow instead.

2. Create the folder structure by starting from the template: copy the matching architecture (`architectures/one-off-deliverable/` before finalize, `_kit/architectures/one-off-deliverable/` after) as your starting point into `workspaces/<name>/` (the firm's live workspaces live there; rename <name> for the deal/fund/cycle) — its CLAUDE.md, CONTEXT.md, stage CONTEXT.md contracts, _config/ files, and worked `_example/` are drafts and a reference to customize against, not blank files to write from scratch (copy the folder contents, not any .DS_Store). Then apply the shape you confirmed in step 1: `00_sources/`, numbered stages with `output/`, `_config/`, `_references/` — adding 01a_triage or 02a_review only if step 1 called for them.

3. Write CLAUDE.md:
   - What this workspace is (their deliverable, their source situation)
   - Structure map
   - How to use (drop sources into 00_sources/, inventory, review, draft — one deliverable, then done)
   - Key decisions (especially the review gate and the platform boundary, citing their book-of-record answer)

4. Write CONTEXT.md routing file:
   - Stage map with the review gate as the checkpoint between 01 and 02
   - How the stages connect, and why the order cannot reverse (you cannot cite a source ID the inventory has not assigned)
   - Reference material locations
   - The AI vs. Platform table, with their book of record named in the platform row

5. Customize the stage contracts from the template (adjust the existing contracts, do not rewrite from scratch):
   - Inventory: the provenance pass tuned to their mess level (light if clean, deep duplicate/version analysis if not). If a document register exists, instruct it to read the register, not rebuild it. End the stage with the stop-and-hand-back review gate.
   - Draft: their deliverable's format from the spec, citing every claim to a source ID, labeling inferences, flagging unsupported claims, closing with Open Items and a Source Usage Map.

6. Populate _config:
   - deliverable-spec.md: filled from Question 1 (deliverable, audience, what it must accomplish, format, deadline, out of scope)
   - source-hierarchy.md: filled from Questions 2, 3, and 5 (book of record, the authority ladder as far as known, sensitive sources, where the sources came from)

7. If they named anything reusable in Question 6 — house style or voice is the usual one — create the file in _references/, or point to the firm's shared reference library if one exists. The firm's core voice already lives in `_shared-config/voice-and-tone.md` (from Run Setup) — reference it, do not redefine it; capture only this workflow's register overlay (how its deliverable differs from the firm's standard voice). Otherwise leave the README note and keep _references/ empty; a one-off rarely needs more. A single standing reference like voice does not make this a recurring workflow (see _references/README).
8. Flag what you could not confirm. Populate _config/before-you-trust-this.md: list every value you could not get directly from the firm — especially the book(s) of record for each figure class in source-hierarchy.md — mark each `[NEEDS CONFIRMATION — <owner>]`, name who signs off, and never invent these silently. Use `[TBD]` for values simply awaiting real data. (Constraint 08.)
9. Demonstrate the inventory stage. If the source set is already in 00_sources/, run the inventory and stop at the review gate, checking its output against the "Done Looks Like" line. If 00_sources/ is still empty at onboarding, point the client at the worked _example/ as the stand-in run, and mark the workspace "stands up now, activates when the source set lands."

### Phase 3: Orientation

Walk the user through. Highlight:
- "The inventory stage stops before drafting and hands the room back to you. That pause is the whole point — review the authority ranking before anything gets written. The most important artifact in here is source_inventory.md, not the draft."
- "Drop your sources into 00_sources/. They get copied, never modified — they are the provenance anchor every citation points back to."
- "The draft cites every claim to a source ID and flags anything the sources do not support. If you see a NOT SUPPORTED flag, that is the workspace being honest, not failing — it is telling you where a human still needs to verify."
- "This is a unit of work, not infrastructure. When the deliverable ships, the workspace has done its job. If this kind of deliverable starts recurring, tell me — it has outgrown this shape and belongs in a document-production workflow."

### Recommended Constraints

Load these constraint files for a one-off-deliverable workspace, and name them in the workspace CLAUDE.md so the team can find them. Load the one a stage needs when that stage runs, not all of them at once.

- **Constraint 10 (Source Provenance)** — the spine of this workspace. The inventory stage is this constraint given a folder structure: the inventory, the authority ladder, and the duplicate/conflict/missing-context logs are its four artifacts. Read it before building the inventory stage.
- **Constraint 06 (Layer Triage)** and **Constraint 09 (Platform Boundary)** — read first, with the user. They decide what AI does (inventorying, summarizing, surfacing conflicts, drafting), what a deterministic tool does (exact-duplicate hashing, the figures themselves), and what the platform owns (the book of record). The model narrates numbers; it never computes or blends them.
- **Constraint 01 (AI Writing Patterns)** — for the deliverable itself. It is a written artifact that must read clean.
- **Constraint 02 (Output Drift)** — to keep the draft internally consistent and matched to what the spec asked for. The "Done Looks Like" line in each stage contract is the anchor.

## Important Notes
- The inventory stage is the highest-value stage in the workspace. If the user wants to skip straight to drafting because "the sources are fine," explain that a confidently wrong deliverable almost never comes from a bad prompt — it comes from a source set no one inspected. The inventory is cheap insurance against an expensive error.
- The review gate is not optional. Do not let the workspace draft from an unreviewed inventory. If the user will not review, at minimum surface that the draft rests on an uninspected source ranking.
- A one-off that keeps coming back is not a one-off. The first time the user copies this workspace for the third instance of the same deliverable, raise it: the work is recurring, and a document-production workflow (lp-reporting, asset-management) will serve them better than rebuilding this by hand each time. See Constraint 07 (Scaling vs. Automating).
- This workspace prepares language and judgment, never figures. If the user expects it to calculate a return or reconcile a NAV, that is a platform job — point them at Constraint 09.
