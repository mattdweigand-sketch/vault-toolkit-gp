# Workflow: Deal Win/Loss Learning

## Overview
A three-stage loop: Signal → Analysis → Capture, closing back into a store the next run reads from. Triggered each time a competitive acquisition process resolves — we won, or we lost. (Withdrawing late is allowed as a sub-case, flagged as a different lesson.) The stages are linear within a run, but the workflow is a loop across runs: each capture feeds the store, and the store feeds every future run and every workspace that sets bid strategy or chases a process.

## Stage Map

| Stage | Purpose | Inputs | Output Location |
|---|---|---|---|
| 01_signal | Assemble the factual bid record | The trigger (process resolved), deal record + broker debrief + clearing price, store (for context) | 01_signal/output/ |
| 02_analysis | Forensic on why, against the canonical questions | Bid record, win/loss questions, store patterns | 02_analysis/output/ |
| 03_capture | Validate the why, write to the store, update patterns | Analysis, store schema, deal taxonomy | 03_capture/output/ + _store/ |

## How the Loop Closes
- 01 → 02: Signal produces the factual record — how the deal reached us, what we bid, the clearing price, and our gap, ending in the won/lost outcome. Analysis works from facts, never from impression. If analysis is reconstructing what happened rather than explaining why, signal did not finish.
- 02 → 03: Analysis produces the proposed "why," structured against the canonical questions, with the broker's *stated* reason held distinct from our *assessed* real reason. Capture is where a human validates that explanation and then commits it to the store. Unvalidated causal claims do not enter the store.
- 03 → _store → 01 (the loop): Capture writes the record into `_store/records/` and updates `_store/patterns.md`. The next run's signal and analysis stages read those back for context, so the firm analyzes each new outcome against everything it has already learned. This back-edge is what makes it a loop rather than a queue.
- _store → other workspaces: `_store/patterns.md` is read by deal-pipeline sourcing and bid strategy and by deal-screening prioritization. The loop pays off outside itself.

## Reference Material (in _config/)
- win-loss-questions.md: The canonical question set every analysis answers, in the same order. This is what makes records comparable. Loaded in stage 02.
- deal-taxonomy.md: The controlled tags (asset type, deal-size band, process type, seller type, broker, market, outcome, decisive dimension) used to tag each record so patterns can aggregate. Loaded in stages 01 and 03.
- store-schema.md: The structure of a stored record and how patterns roll up. Loaded in stage 03.

## The Store (in _store/)
- records/: one structured record per resolved competitive process.
- patterns.md: the rolled-up, firm-level intelligence — which processes we win, where our bids fall short, which dimension decides outcomes, which brokers' feedback proves reliable — updated on each capture. This is the payoff-grain output.
- The store is read in stages 01 and 02 for context and written in stage 03. It is the workspace's memory.

## When to Add Stages
- **00_trigger** before signal: if you want an explicit step that detects resolved competitive processes from the pipeline and queues them, rather than running the loop manually per process.
- **04_review** after capture, periodically (not per-run): a standing pattern review that reads the whole store and writes a synthesis for the deal team ahead of a deployment push or a major bid. This is the loop's intelligence consumed deliberately rather than incidentally.

## AI vs. Platform: Where Each Step Lives

The temptation here is to let the model recall a process or assert a "why" without grounding — or to take the broker's polite stated reason at face value. The rule: rely on the deal record and market data for what happened, use AI to propose the why, keep a human on the causal claim. See Constraint 09.

| Step in this workflow | Layer | Who owns it |
|---|---|---|
| What happened: our bid, the timeline, the clearing price, the broker of record | Platform / data foundation | Deal system + market data (broker-shared or public record) |
| Assembling the record, structuring the analysis, proposing the why, detecting patterns across the store | AI | You, on top of governed data |
| Validating the causal explanation before it is captured | Human in the loop | The deal lead / head of acquisitions |
| The accumulated store and its patterns | Firm intelligence | This workspace (handle as confidential competitive intelligence) |

The trap on this workflow: capturing the broker's polite stated reason ("they had a higher bid") as the real reason, when the assessed driver was something else ("they didn't trust our certainty of close"). AI proposes the explanation and keeps stated and assessed reasons distinct; the deal record and market data ground what happened; a human signs off on the why before it becomes memory.
