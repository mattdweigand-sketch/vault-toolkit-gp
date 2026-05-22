# Workflow: Asset Management

## Overview
Three-stage pipeline: Data → Review → Report. Each stage has a defined contract, explicit inputs, and a clear output location. Human review between stages. The data stage gates the others: no analysis is built until the actuals are verified against source.

## Stage Map

| Stage | Purpose | Inputs | Output Location |
|---|---|---|---|
| 01_data | Gather and verify per-asset operating data | Property-system exports, asset reports, rent roll, budget | 01_data/output/ |
| 02_review | Analyze actuals vs. business plan; flag variances, risks, watchlist | Verified data pack, business-plan targets, review standards | 02_review/output/ |
| 03_report | Produce the internal asset review and the portfolio watchlist | Analysis pack, report format | 03_report/output/ |

## How Stages Connect
- 01 → 02: The verified data pack becomes the basis for analysis. The review stage reads the data pack and the business-plan targets, NOT the raw property-system export. If the data stage did its job, the review stage never reconciles a number itself.
- 02 → 03: The analysis pack and watchlist become the report input. The report stage formats and frames; it does not re-run the analysis. If the report stage is re-analyzing, the review stage needs tighter standards.

## Reference Material (in _config/)
- business-plan-targets.md: Per-asset underwriting targets — the baseline actuals are measured against. Loaded in stage 02.
- review-standards.md: Variance materiality thresholds and watchlist criteria. What counts as "off plan," what triggers a flag. Loaded in stage 02.
- reporting-format.md: The structure of the internal asset review, plus the JV/co-GP and watchlist format variants. Loaded in stage 03.

## Reference Material (in _prompts/)
- Reusable prompt fragments for the recurring analytical tasks: variance attribution, watchlist triage, hold/sell/refi signal framing.

## When to Add Stages
- **02a_valuation-input** between review and report: if the cycle includes a fair-value mark step. Note: the mark itself is set by your valuation process and modeling tools, not here. This stage would only assemble the inputs and the rationale narrative, never compute the mark (Constraint 09).
- **04_distribution** after report: if the internal review is formally circulated and you want the distribution and version tracked in the workspace.

Add a stage when the process consistently demands it, not preemptively.

## AI vs. Platform: Where Each Step Lives

The temptation here is to let the model compute the return or set the mark from the operating data. Do not. The rule: rely on your platform for the data and the math, use AI for the language and the judgment. See Constraint 09.

| Step in this workflow | Layer | Who owns it |
|---|---|---|
| Operating actuals, GL, rent roll, occupancy, NOI, the property-level record | Platform / data foundation | Property systems (Yardi / MRI / RealPage) |
| The underwriting model, IRR, equity multiple, valuation and the mark | Deterministic / modeled | Argus or your model; your valuation process |
| Recorded fund-level figures and investor reporting | Platform | Fund administration platform |
| Analyzing actuals vs. plan, attributing variance, flagging risks, building the watchlist, drafting the review | AI | You, on top of governed data |
| The hold / sell / refinance decision | Human in the loop | Asset management lead and the investment committee |

The trap on this workflow: letting the model state a return or a value it inferred from the operating data. AI explains why NOI missed plan and flags the asset for the watchlist. The return and the mark come from the model and the valuation process, and the hold/sell call is the IC's.
