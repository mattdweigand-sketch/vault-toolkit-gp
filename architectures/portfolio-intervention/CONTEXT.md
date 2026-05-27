# Workflow: Portfolio Intervention

## Overview
Four-stage intervention loop: Signal -> Diagnosis -> Action Plan -> Follow-Up. It converts portfolio data into attention and action.

## Modules Used
- `modules/verified-fact-pack/CONTRACT.md`
- `modules/decision-challenge/CONTRACT.md`
- `modules/response-posture/CONTRACT.md`
- `modules/artifact-review/CONTRACT.md`
- `modules/handoff-brief/CONTRACT.md`

## Stage Map

| Stage | Purpose | Inputs | Output Location |
|---|---|---|---|
| 01_signal | Capture the verified signal or variance | Portfolio dashboard, operating actuals, asset report | 01_signal/output/ |
| 02_diagnosis | Explain cause and severity | Signal record, business plan, intervention standards | 02_diagnosis/output/ |
| 03_action_plan | Define response, owner, deadline, evidence | Diagnosis, action standards | 03_action_plan/output/ |
| 04_follow_up | Check whether the action changed the read | Action plan, updated signal | 04_follow_up/output/ |

## AI vs. Platform

| Step | Layer | Owner |
|---|---|---|
| Actuals, dashboards, KPIs, valuation, official variance | Platform | Portfolio monitoring / accounting / valuation system |
| Threshold routing | Rule-based | Watchlist criteria |
| Diagnosis, action framing, escalation language | AI | Asset manager / operating partner |
| Intervention decision | Human | Portfolio lead / IC |

## Reference Material
- `_config/business-plan-targets.md`
- `_config/intervention-standards.md`
- `_config/action-plan-format.md`
- `_config/before-you-trust-this.md`
