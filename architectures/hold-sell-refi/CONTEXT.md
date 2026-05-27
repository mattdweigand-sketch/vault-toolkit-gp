# Workflow: Hold / Sell / Refi

## Overview
Four-stage gated decision workflow: Position -> Alternatives -> Decision -> Handoff.

## Modules Used
- `modules/verified-fact-pack/CONTRACT.md`
- `modules/decision-challenge/CONTRACT.md`
- `modules/grounded-draft/CONTRACT.md`
- `modules/handoff-brief/CONTRACT.md`

## Stage Map

| Stage | Purpose | Inputs | Output Location |
|---|---|---|---|
| 01_position | Establish current asset standing | Portfolio review, model scenarios, market read | 01_position/output/ |
| 02_alternatives | Compare hold, sell, refi, recap | Position pack, criteria, model outputs | 02_alternatives/output/ |
| 03_decision | Produce IC-ready recommendation and conditions | Alternatives pack, IC standards | 03_decision/output/ |
| 04_handoff | Hand approved path to execution owner | Decision, owner, next process | 04_handoff/output/ |

## AI vs. Platform

| Step | Layer | Owner |
|---|---|---|
| Asset actuals, ownership, investor record | Platform | Property / portfolio / fund-admin systems |
| Return scenarios, BOV, debt proceeds, valuation | Deterministic / modeled | Underwriting model, valuation process, brokers, lenders |
| Alternative framing, timing thesis, risks, recommendation language | AI | Asset management lead on governed data |
| Final decision | Human | IC |

## Reference Material
- `_config/asset-profile.md`
- `_config/decision-criteria.md`
- `_config/before-you-trust-this.md`
