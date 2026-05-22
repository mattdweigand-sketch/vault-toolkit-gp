# Workflow: One-Off Deliverable

## Overview
Two-stage flow: Inventory → Draft, with a human review gate between them. The gate is the point of the workspace. Skipping it — drafting from an uninspected source set — is the single failure this workflow exists to prevent. See Constraint 10.

## Stage Map

| Stage | Purpose | Key Inputs | Output Location | Decision Checkpoint |
|---|---|---|---|---|
| 01_inventory | Inspect the source set: inventory, rank authority, summarize, log duplicates/conflicts/gaps | Source set in 00_sources/, _config/ | 01_inventory/output/ | Human reviews the inventory; drafting is blocked until it passes |
| 02_draft | Write the deliverable from the reviewed inventory | Reviewed inventory, source summaries, _config/ | 02_draft/output/ | Deliverable is grounded, cited, and flags what the room does not support |

## How Stages Connect
- 01 → review: The inventory stage ends by stopping. It does not roll into drafting. It produces `source_inventory.md` and the three logs, then hands back to a human. The reviewer spot-checks the authority ranking — is the file marked authoritative actually the book of record, and is the one marked superseded actually stale? An inventory the reviewer cannot trust is not a basis to draft from.
- review → 02: Only a reviewed inventory feeds the draft. The draft stage cites by source ID against the inventory; a claim cannot carry `[S01]` unless the inventory assigned `S01`. This is why the order cannot reverse.

## Reference Material
- `_config/deliverable-spec.md`: What the deliverable is, who reads it, what it must accomplish, and any format or length constraints. Shapes the draft.
- `_config/source-hierarchy.md`: The authority ladder for this source set, plus any `sensitive` files that must be noted but never copied or quoted. Filled during the inventory, reviewed by a human, treated as ground truth by the draft.
- `_references/`: Cross-deliverable knowledge that applies beyond this one run (house style, prior comparable deliverables, standing standards). Often empty for a true one-off.

## When to Add Stages
- **01a_triage** before the inventory: If the source set is large enough that deciding what is even in scope is its own job, split a triage stage off the front. For most one-offs the inventory stage absorbs this.
- **02a_review** as a distinct compliance stage: If the deliverable must clear a compliance or legal pass before it ships (a lender letter, a regulated disclosure), add a review stage after the draft rather than folding it into 02.
- **If the deliverable starts recurring:** stop adding stages. It has outgrown this shape. Move it to a document-production workflow (lp-reporting, asset-management) where the cycle is the point.

## AI vs. Platform: Where Each Step Lives

Before you point AI at this workflow, decide what AI does, what a deterministic tool does, and what your enterprise platform must own. The rule: rely on your platform for the data and the record, use AI for the language and the judgment. See Constraint 09.

| Step in this workflow | Layer | Who owns it |
|---|---|---|
| The source files, their version history, the document register where one exists | Platform / data foundation | The data room, fund admin, or document-management system |
| Exact-duplicate detection (file hashing), the figures themselves | Deterministic | A checksum tool; the model or the platform's calculation engine |
| Inventorying and ranking sources, summarizing them, surfacing conflicts and gaps, drafting the deliverable | AI | You, on top of governed sources |
| Resolving a flagged conflict; approving the deliverable | Human in the loop | The reviewer and the deliverable's owner |

The trap on this workflow: letting AI treat the whole folder as one trustworthy corpus and blend a number from `model_v2` with one from `model_final`. The inventory exists to make that impossible — the model classifies and flags; it never reconciles figures or picks a winner silently (Constraint 10, boundary with Constraint 09).
