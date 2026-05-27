# Workflow: Underwriting Backtest

## Overview
A three-stage loop: Reconcile → Attribution → Capture, closing back into a store the next run reads from. Triggered each time a deal realizes — exited, sold, or fully returned. (An interim checkpoint — end of a business-plan year, a refinance, stabilization — is allowed as a sub-case, flagged as a partial backtest against the assumptions due by that point.) The stages are linear within a run, but the workflow is a loop across runs: each capture feeds the store, and the store feeds every future run and every workspace that sets an underwriting assumption.

## Modules Used
- `modules/validated-memory-store/CONTRACT.md`: stage 03 capture and pattern updates.
- `modules/handoff-brief/CONTRACT.md`: flags calibration signals to diligence, IC pressure test, and investment-box updates.

## Stage Map

| Stage | Purpose | Inputs | Output Location |
|---|---|---|---|
| 01_reconcile | Assemble the factual variance record | The trigger (deal realized), the approved IC model of record + realized actuals from fund accounting / the exit, store (for context) | 01_reconcile/output/ |
| 02_attribution | Forensic on why each material assumption missed; skill vs. luck | Variance record, underwriting questions, store patterns | 02_attribution/output/ |
| 03_capture | Validate the attribution, write to the store, update patterns, and emit handoff flags | Attribution, store schema, assumption taxonomy | 03_capture/output/ + _store/ |

## How the Loop Closes
- 01 → 02: Reconcile produces the factual variance — what we underwrote, what actually happened, and the gap per material assumption and on the headline return, ending in the outperformed / in-line / underperformed outcome. Attribution works from facts, never from impression. If attribution is reconstructing the numbers rather than explaining the variance, reconcile did not finish.
- 02 → 03: Attribution produces the proposed "why," structured against the canonical questions, with the firm's *skill* held distinct from market *luck*. Capture is where a human validates that explanation and then commits it to the store. Unvalidated causal claims — and unvalidated skill-vs-luck splits — do not enter the store.
- 03 → _store → 01 (the loop): Capture writes the record into `_store/records/` and updates `_store/patterns.md`. The next run's reconcile and attribution stages read those back for context, so the firm analyzes each new realization against everything it has already learned. This back-edge is what makes it a loop rather than a queue.
- _store → future investment work: `_store/patterns.md` is read before underwriting, screening assumptions, diligence questions, and IC pressure tests. The loop pays off outside itself — its calibration adjusts the assumptions the firm underwrites on.

## Reference Material (in _config/)
- underwriting-questions.md: The canonical question set every attribution answers, in the same order. This is what makes records comparable. Loaded in stage 02.
- assumption-taxonomy.md: The controlled tags (asset type, deal-size band, market, strategy, hold-period band, vintage, the controlled list of assumption categories, outcome, decisive driver, cause class, skill/luck attribution) used to tag each record so patterns can aggregate. Loaded in stages 01 and 03.
- store-schema.md: The structure of a stored record and how the calibration patterns roll up. Loaded in stage 03.

## The Store (in _store/)
- records/: one structured record per realized deal.
- patterns.md: the rolled-up, firm-level calibration — which assumptions run optimistic or conservative and by roughly how much, in which segments, and how much of realized return has been skill vs. market beta — updated on each capture. This is the payoff-grain output.
- The store is read in stages 01 and 02 for context and written in stage 03. It is the workspace's memory.

## When to Add Stages
- **00_trigger** before reconcile: if you want an explicit step that detects realized deals from the fund-accounting / portfolio system and queues them, rather than running the loop manually per exit.
- **04_review** after capture, periodically (not per-run): a standing calibration review that reads the whole store and writes a synthesis for the deal team ahead of an underwriting push or a fund deployment — and proposes concrete edits to underwriting standards, screening assumptions, diligence questions, and IC pressure-test prompts. This is the loop's intelligence consumed deliberately rather than incidentally.

## AI vs. Platform: Where Each Step Lives

The temptation here is to let the model recompute or "estimate" a realized return, or to credit a market tailwind to the firm's own skill. The rule: rely on the approved model and fund accounting for what happened, use AI to explain the variance and propose the skill-vs-luck split, keep a human on the causal claim. See Constraint 09.

| Step in this workflow | Layer | Who owns it |
|---|---|---|
| What happened: the approved assumptions, the realized actuals (NOI, rents, exit price, hold, realized IRR/MOIC), and the computed variance | Platform / data foundation | The IC-approved model of record + fund accounting / realized-exit data. **The variance math is deterministic arithmetic (Constraint 06), not AI.** |
| Assembling the record, explaining why each assumption missed, splitting skill vs. luck, detecting calibration patterns across the store | AI | You, on top of governed data |
| Validating the causal attribution — especially the skill-vs-luck split — before it is captured | Human in the loop | The underwriter / head of acquisitions / IC |
| The accumulated store and its calibration patterns | Firm intelligence | This workspace (handle as confidential — it documents the firm's own systematic errors) |

The trap on this workflow: recording "our thesis was right" when the realized IRR was mostly cap-rate compression the whole market enjoyed. AI proposes the explanation and keeps skill and luck distinct; the approved model and fund accounting ground what happened; a human signs off on the attribution before it becomes memory and retunes the next underwrite.
