# Workflow: Deal Screening

## Overview
Three-stage gated pipeline: Capture → Screen → Decision. Each opportunity advances toward a single go/no-go: pursue (hand off to deal-pipeline) or pass (logged with a reason). The stages are lean by design — the point is a fast, consistent, defensible triage, not a diligence-grade analysis.

## Stage Map

| Stage | Purpose | Key Inputs | Output Location | Decision Checkpoint |
|---|---|---|---|---|
| 01_capture | Normalize the inbound opportunity into a standard snapshot | OM, teaser, broker email, listing data | 01_capture/output/ | Enough captured to screen? |
| 02_screen | Fit against the box, rough economics, deal-breakers | Snapshot, investment box, screening criteria, assumptions | 02_screen/output/ | Pursue / pass / need-more |
| 03_decision | The go/no-go gate; handoff or pass log | Screen assessment | 03_decision/output/ | Pursue → deal-pipeline; Pass → logged |

## How Stages Connect
- 01 → 02: Capture produces a normalized snapshot of the opportunity — the facts pulled out of the OM and listing data into a standard shape. Screen works from the snapshot, so every deal is screened on comparable terms regardless of how the broker presented it.
- 02 → 03: Screen produces a recommendation with rationale. Decision records the go/no-go. A "need-more" loops back to capture for the specific missing fact, not a vague "look closer."
- 03 → deal-pipeline (on pursue): The decision stage produces a handoff brief that becomes the input to a new deal-pipeline workspace's sourcing stage. The screen's work carries forward; sourcing does not restart it.
- 03 → _references (on pass): The pass and its reason are logged, building the pass record that keeps screening consistent and creates the audit trail.

## Reference Material (in _config/)
- investment-box.md: What the firm buys — geography, asset type, deal size, strategy, return profile. The standard the screen measures against. Loaded in stage 02.
- screening-criteria.md: The go/no-go thresholds and the automatic deal-breakers. Testable rules. Loaded in stage 02.
- economics-assumptions.md: Standard rough-screen assumptions (market cap rates, financing, hurdle) so every quick economics check uses the same basis. Loaded in stage 02.

## Reference Material (in _references/)
- Prior screens and the pass log (consistency and audit trail), submarket comps, and the firm's underwriting standards as they apply at the screen level.

## When to Add Stages
- **01a_authorization** for off-market or relationship-sourced deals that need a partner's sign-off to even spend screening time.
- Keep the pipeline lean otherwise. The most common mistake here is over-building a process whose entire value is speed.

## AI vs. Platform: Where Each Step Lives

The temptation here is to treat the screen's rough numbers as an underwrite, or to let the model "decide." The rule: rely on your data sources for the deal facts, use AI for the fit judgment and the rough filter, keep the decision human. See Constraint 09.

| Step in this workflow | Layer | Who owns it |
|---|---|---|
| Deal facts, listing data, ownership, submarket comps | Platform / data foundation | Deal and market data sources (Dealpath, CoStar) |
| The real underwrite — model, returns, valuation | Deterministic / modeled | Argus or your model, in deal-pipeline diligence (not here) |
| Normalizing the opportunity, assessing fit against the box, the rough economics filter, surfacing deal-breakers, drafting the rationale | AI | You, on top of governed data |
| The pursue / pass decision | Human in the loop | The deal team |

The trap on this workflow: presenting a screen-stage rough number as if it were an underwrite, or letting the rough economics override an obvious strategic deal-breaker. AI normalizes, filters, and surfaces; the deal facts come from your data sources; the real underwrite is deal-pipeline's; the pursue/pass call is the team's.
