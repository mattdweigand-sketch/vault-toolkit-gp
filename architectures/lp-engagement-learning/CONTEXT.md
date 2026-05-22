# Workflow: LP Engagement Learning

## Overview
A three-stage loop: Signal → Analysis → Capture, closing back into a store the next run reads from. Triggered each time an LP engagement resolves — a commitment or a decline. The stages are linear within a run, but the workflow is a loop across runs: each capture feeds the store, and the store feeds every future run and every workspace that preps an engagement.

## Stage Map

| Stage | Purpose | Inputs | Output Location |
|---|---|---|---|
| 01_signal | Assemble the factual engagement record | The trigger (LP resolved), CRM engagement data, store (for context) | 01_signal/output/ |
| 02_analysis | Forensic on why, against the canonical questions | Engagement record, debrief questions, store patterns | 02_analysis/output/ |
| 03_capture | Validate the why, write to the store, update patterns | Analysis, store schema, segment taxonomy | 03_capture/output/ + _store/ |

## How the Loop Closes
- 01 → 02: Signal produces the factual record — what happened, with whom, over what timeline, ending in the outcome. Analysis works from facts, never from impression. If analysis is reconstructing what happened rather than explaining why, signal did not finish.
- 02 → 03: Analysis produces the proposed "why," structured against the canonical questions. Capture is where a human validates that explanation and then commits it to the store. Unvalidated causal claims do not enter the store.
- 03 → _store → 01 (the loop): Capture writes the record into `_store/records/` and updates `_store/patterns.md`. The next run's signal and analysis stages read those back for context, so the firm analyzes each new outcome against everything it has already learned. This back-edge is what makes it a loop rather than a queue.
- _store → other workspaces: `_store/patterns.md` is read by capital-raising prep and prospect work. The loop pays off outside itself.

## Reference Material (in _config/)
- debrief-questions.md: The canonical question set every analysis answers, in the same order. This is what makes records comparable. Loaded in stage 02.
- segment-taxonomy.md: The LP segment and check-size taxonomy used to tag each record so patterns can aggregate by segment. Loaded in stages 01 and 03.
- store-schema.md: The structure of a stored record and how patterns roll up. Loaded in stage 03.

## The Store (in _store/)
- records/: one structured record per resolved LP engagement.
- patterns.md: the rolled-up, fund-level intelligence — what is converting, what objections recur, where the raise stalls — updated on each capture. This is the payoff-grain output.
- The store is read in stages 01 and 02 for context and written in stage 03. It is the workspace's memory.

## When to Add Stages
- **00_trigger** before signal: if you want an explicit step that detects resolved engagements from the CRM and queues them, rather than running the loop manually per LP.
- **04_review** after capture, periodically (not per-run): a standing pattern review that reads the whole store and writes a synthesis for the partners ahead of a raise. This is the loop's intelligence consumed deliberately rather than incidentally.

## AI vs. Platform: Where Each Step Lives

The temptation here is to let the model recall an interaction or assert a "why" without grounding. The rule: rely on the CRM for what happened, use AI to propose the why, keep a human on the causal claim. See Constraint 09.

| Step in this workflow | Layer | Who owns it |
|---|---|---|
| Touchpoints, timeline, materials shared, who was involved, the outcome of record | Platform / data foundation | Enterprise CRM |
| Assembling the record, structuring the analysis, proposing the why, detecting patterns across the store | AI | You, on top of governed data |
| Validating the causal explanation before it is captured | Human in the loop | The IR / capital-raising owner |
| The accumulated store and its patterns | Firm intelligence | This workspace (handle as confidential) |

The trap on this workflow: capturing a plausible-but-unvalidated "why" into the store, where it then shapes future decisions as if it were fact. AI proposes the explanation; the CRM grounds what happened; a human signs off on the why before it becomes memory.
