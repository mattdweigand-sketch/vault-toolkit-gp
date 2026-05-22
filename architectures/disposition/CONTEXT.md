# Workflow: Disposition

## Overview
Four-stage pipeline with a decision fork: Position → Decision → Market → Close. The decision stage is a go/no-go on the exit itself — hold exits the pipeline, sell continues to market and close. The acquisition pipeline (deal-pipeline) is the mirror: this one runs the same gated discipline in reverse, taking an asset out.

## Stage Map

| Stage | Purpose | Key Inputs | Output Location | Decision Checkpoint |
|---|---|---|---|---|
| 01_position | Assess standing and the hold/sell drivers | Asset-management review, model scenarios, BOV, market read | 01_position/output/ | Is an exit worth evaluating now? |
| 02_decision | Build the hold-vs-sell case; IC gate | Position assessment, hold/sell criteria | 02_decision/output/ | Hold (exit, revisit) or sell (proceed) |
| 03_market | Strategy, broker, disposition package, go to market | Sell decision, disposition standards | 03_market/output/ | Ready to launch; offers come in |
| 04_close | Offers, selection, close, capital return, handoff | Selected offer, final terms | 04_close/output/ | Deal closes and capital returns |

## How Stages Connect
- 01 → 02: Position produces the facts and the drivers for and against an exit. Decision builds both the hold case and the sell case from it and takes them to the IC. If decision is only building the sell case, position did not surface the hold drivers.
- 02 → 03 (sell): Decision produces an approved sell with a timing thesis. Market executes it — strategy, broker, package. A hold instead exits here with a revisit trigger (a date or a condition that would reopen the question).
- 03 → 04: Market produces a launched process and incoming offers. Close evaluates them, selects, executes the sale, and returns capital.
- 04 → fund administration / lp-reporting (handoff): Close hands the capital-return mechanics to your fund-administration platform and fund-admin team (which own the distribution) and the exit narrative to LP reporting. The disposition does not end at the wire; it ends when the exit is cleanly reflected to investors.

## Reference Material (in _config/)
- asset-profile.md: The asset, its original thesis, and current business-plan status — ideally carried from the asset-management workspace. Loaded in stage 01.
- hold-sell-criteria.md: The firm's framework for when to sell. Loaded in stage 02.
- disposition-standards.md: Standards for the sale process — broker selection, package contents, approval gates. Loaded in stages 03 and 04.

## Reference Material (in _references/)
- Prior dispositions, broker relationships and track records, submarket sale comps.

## When to Add Stages
- **02a_recap-vs-sale** within decision: if a recapitalization or partial sale is a live alternative to a full exit, evaluate it as a distinct option before the IC gate.
- **03a_pre-marketing** within market: if the firm runs a quiet/off-market pre-marketing phase before a broad process.

## AI vs. Platform: Where Each Step Lives

The temptation here is to let the model produce the return that decides the exit. The rule: rely on your model and brokers for the numbers, use AI for the thesis and the narrative, keep the decision with the IC. See Constraint 09.

| Step in this workflow | Layer | Who owns it |
|---|---|---|
| Asset operating data, ownership, the property record | Platform / data foundation | Property systems (Yardi / MRI / RealPage) |
| Hold-vs-sell return scenarios, net-proceeds and valuation math, the BOV | Deterministic / modeled | Argus or your model; the broker |
| Capital-return mechanics, the investor record, the audit trail | Platform | Juniper Square and fund admin |
| Framing the hold/sell case, the timing thesis, the disposition strategy and package narrative | AI | You, on top of governed data |
| The hold/sell decision and the buyer selection | Human in the loop | Asset management lead and the investment committee |

The trap on this workflow: AI generating the return delta that justifies selling, rather than building the thesis around the model's delta. AI argues the timing and writes the package; the numbers come from the model and the brokers; the IC decides.
