# Workflow: IC Memo Intelligence

## Overview
A three-stage loop: Record → Analysis → Capture, closing back into a store the next run reads from. Triggered each time a deal is decided at IC — approved, approved with conditions, declined, or tabled. The stages are linear within a run, but the workflow is a loop across runs: each capture feeds the store, and the store feeds every future run and every workspace that takes a deal to committee. There is no arithmetic here — unlike the underwriting-backtest sibling, the whole loop is qualitative; the value is faithful capture and consistent tagging.

## Stage Map

| Stage | Purpose | Inputs | Output Location |
|---|---|---|---|
| 01_record | Assemble the factual decision record | The trigger (deal decided at IC), the IC memo + the committee's minutes/notes, store (for precedent context) | 01_record/output/ |
| 02_analysis | Forensic on what the committee weighed; stated vs. inferred rationale; precedent | Decision record, IC questions, store patterns | 02_analysis/output/ |
| 03_capture | Validate the analysis, write to the store, update patterns | Analysis, store schema, decision taxonomy | 03_capture/output/ + _store/ |

## How the Loop Closes
- 01 → 02: Record produces the factual decision — recommendation, decision lane, conditions imposed, dissents, concerns the committee raised, and the vote, drawn from the memo and the minutes. Analysis works from that record, never from impression. If analysis is reconstructing what the committee decided rather than explaining what it weighed, record did not finish.
- 02 → 03: Analysis produces the proposed reading — what actually drove the decision, structured against the canonical questions, with the committee's *stated* reasoning held distinct from the analyst's *inferred* reading. Capture is where a human validates that reading and then commits it to the store. Unvalidated rationale — and unvalidated precedent claims — do not enter the store.
- 03 → _store → 01 (the loop): Capture writes the record into `_store/records/` and updates `_store/patterns.md`. The next run's record and analysis stages read those back for context, so the firm analyzes each new decision against everything the committee has already decided. This back-edge is what makes it a loop rather than a queue.
- _store → other workspaces: `_store/patterns.md` is read by deal-pipeline's IC stage (so the next memo pre-empts standing conditions and cites precedent) and by deal-screening (so a deal the IC reliably declines in a segment is not advanced again). The loop pays off outside itself — its decision intelligence shapes how other workspaces frame and triage deals.

## Reference Material (in _config/)
- ic-questions.md: The canonical question set every analysis answers, in the same order. This is what makes records comparable. Loaded in stage 02.
- decision-taxonomy.md: The controlled tags (asset type, deal-size band, market, strategy, decision lane, the controlled list of condition categories and concern categories, decisive factor, dissent, precedent relationship) used to tag each record so patterns can aggregate. Loaded in stages 01 and 03.
- store-schema.md: The structure of a stored record and how the decision-intelligence patterns roll up. Loaded in stage 03.

## The Store (in _store/)
- records/: one structured record per IC decision.
- patterns.md: the rolled-up, firm-level decision intelligence — the conditions the committee imposes again and again, its revealed risk appetite by segment, the precedents a new deal is measured against, and the concerns it raises most — updated on each capture. This is the payoff-grain output.
- The store is read in stages 01 and 02 for context and written in stage 03. It is the workspace's memory.

## When to Add Stages
- **00_trigger** before record: if you want an explicit step that detects IC decisions from the deal system / committee calendar and queues them, rather than running the loop manually per decision.
- **04_review** after capture, periodically (not per-run): a standing precedent review that reads the whole store and writes a synthesis for the deal team ahead of a busy IC cycle — the committee's current standing conditions, its live risk-appetite boundaries, and the precedents most likely to come up — and proposes the concrete edits to deal-pipeline's IC-memo template and deal-screening's box. This is the loop's intelligence consumed deliberately rather than incidentally.
- **Optional concern-resolution back-edge** (a heavier extension): if you want to learn which IC concerns proved *predictive*, add a later step that revisits a stored record once the flagged concern resolves and notes whether the risk materialized. This turns the store into a concern-predictiveness calibration — but it reaches into realized-outcome territory the underwriting-backtest workspace already owns, so weigh the overlap before building it. The core loop deliberately stops at decision time.

## AI vs. Platform: Where Each Step Lives

The temptation here is to let the model paraphrase a cleaner decision rationale than the committee actually gave, or to assert a precedent the store does not support. The rule: rely on the memo and the minutes for what was decided, use AI to read what the committee weighed and propose the inferred rationale, keep a human on the causal claim. See Constraint 09.

| Step in this workflow | Layer | Who owns it |
|---|---|---|
| What was decided: the recommendation, the decision lane, the conditions imposed, the dissents, the concerns raised, the vote | Platform / source of record | The IC memo + the official IC minutes/notes. **The decision is an authoritative record AI narrates, never invents (Constraint 09).** |
| Assembling the record, reading what the committee weighed, proposing the inferred rationale, detecting precedent and pattern across the store | AI | You, on top of governed source documents |
| Validating the analysis — especially the inferred rationale and the precedent read — before it is captured | Human in the loop | The IC chair / deal lead |
| The accumulated store and its decision intelligence | Firm intelligence | This workspace (handle as confidential — it documents the firm's own decision patterns and dissents) |

The trap on this workflow: writing "the committee approved because it was confident in the sponsor" when the minutes show a split vote and a grudging approval conditioned on three guardrails. AI proposes the reading and keeps stated and inferred apart; the memo and minutes ground what was decided; a human signs off on the rationale before it becomes memory and shapes the next memo.
