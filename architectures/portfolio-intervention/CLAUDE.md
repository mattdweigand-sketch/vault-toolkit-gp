# Portfolio Intervention Workspace

## What This Is
A workspace for turning portfolio signals into diagnosis and action. It starts from platform-verified operating data, portfolio dashboards, or asset reports, then identifies what needs attention, why, who owns the next step, and what evidence should change the read.

This is not a portfolio-monitoring platform and does not compute valuations or revised returns. The platform owns actuals, dashboards, and marks. This workspace owns intervention judgment.

## Structure
```
portfolio-intervention/
  CLAUDE.md
  CONTEXT.md
  01_signal/CONTEXT.md
  02_diagnosis/CONTEXT.md
  03_action_plan/CONTEXT.md
  04_follow_up/CONTEXT.md
  _config/
```

## Key Decisions
- **Signals are not interventions.** A variance becomes useful only when the workspace explains why it matters and what action follows.
- **Owners and dates are part of the output.** An action plan without an owner is a narrative, not an intervention.
- **The platform owns actuals.** AI never calculates the official variance, mark, NAV, IRR, or MOIC.

## Modules Used
- `modules/verified-fact-pack/CONTRACT.md`
- `modules/decision-challenge/CONTRACT.md`
- `modules/response-posture/CONTRACT.md`
- `modules/artifact-review/CONTRACT.md`
- `modules/handoff-brief/CONTRACT.md`

## Constraints That Apply
Universal **06** and **09**, plus **02**, **04**, **08**, and **10** when asset reports are unvetted.
