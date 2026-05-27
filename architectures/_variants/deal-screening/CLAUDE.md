# Deal Screening Workspace

## What This Is
A workspace for the top of the acquisition funnel: triaging inbound opportunities fast against the firm's investment box, so the few worth real diligence advance and the many that are not get a clean, fast, defensible pass. Built for a commercial real estate GP (or PE deal team) that sees far more deals than it pursues and wants to apply its criteria consistently instead of screening from memory under time pressure.

This is the front door that the deal-pipeline workspace assumes you have already walked through. Deal-pipeline runs a single opportunity from sourcing through close. This workspace decides which opportunities earn a deal-pipeline at all. Its output on a "pursue" is the handoff that seeds deal-pipeline's sourcing stage.

## Current State
- This is a reference architecture. No active screening queue.
- To use: copy the folder, populate _config with your investment box, screening criteria, and rough-screen assumptions.

## Structure
```
deal-screening/
  CLAUDE.md              # You are here.
  CONTEXT.md             # Workflow routing.
  01_capture/
    CONTEXT.md           # Stage contract: normalize the inbound opportunity.
    output/              # Standard opportunity snapshot. Input for 02_screen.
  02_screen/
    CONTEXT.md           # Stage contract: fit, rough economics, deal-breakers.
    output/              # Screen assessment with a pursue/pass recommendation.
  03_decision/
    CONTEXT.md           # Stage contract: the go/no-go gate and handoff or pass log.
    output/              # The decision, the handoff brief, or the pass record.
  _config/               # Investment box, screening criteria, rough-screen assumptions.
  _references/           # Prior screens, the pass log, comps and standards.
```

## How to Use
1. Read CONTEXT.md for the full workflow.
2. Populate _config/ with your investment box (what you buy), your screening criteria (the go/no-go thresholds and automatic deal-breakers), and your rough-screen economics assumptions.
3. A new opportunity enters through 01_capture. The OM, teaser, or broker email gets normalized into a standard snapshot.
4. The snapshot moves to 02_screen, where it is measured against the box, given a rough economics sanity check, and tested for deal-breakers, producing a pursue / pass / need-more recommendation.
5. The recommendation moves to 03_decision — the gate. A "pursue" produces the handoff brief that seeds a deal-pipeline workspace. A "pass" is logged with its reason.

## Key Decisions
- **Kill fast is the goal, not thoroughness.** This workspace exists to spend the least possible effort reaching a defensible pass on the deals that do not fit, so attention is reserved for the ones that do. The stages are deliberately lean. If a screen is taking as long as diligence, the criteria are not sharp enough.
- **Screen against the box, not the broker's pitch.** The offering memo is the seller's case. The investment box in _config is what the firm actually buys. The screen measures the opportunity against the box, not against the OM's framing.
- **The rough economics is a filter, not an underwrite.** The quick numbers in the screen are a sanity check to catch obvious non-starters, run on standard assumptions for consistency. The real underwrite happens in deal-pipeline diligence with the model. Never present a screen-stage number as an underwrite. See Constraint 09.
- **A pass is an output, not a non-event.** Every pass is logged with its reason in _references. This keeps screening consistent (the same kind of deal gets the same answer), creates an audit trail, and over time reveals patterns in what the firm sees and rejects.
- **The pursue handoff is the bridge to deal-pipeline.** A "pursue" does not just say yes; it produces the structured brief that becomes deal-pipeline's input, so the sourcing stage starts with the screen's work, not from scratch.

## Constraints That Apply
Built against the GP Operating Toolkit. Most relevant: **02 (Output Drift)** so every screen comes out comparable, the universal **06 (Layer Triage)** and **09 (Platform Boundary)**, and **10 (Source Provenance)** when an opportunity arrives with a fuller data set.

## Layer Annotations
- CLAUDE.md: L0 (always loaded, orientation)
- CONTEXT.md: L1 (workflow routing)
- Stage CONTEXT.md files: L2 (stage contracts)
- _config/ files: L3 (reference: box, criteria, assumptions)
- _references/ files: L3 (cross-deal: prior screens, pass log, comps)
- Inbound opportunity materials and stage outputs: L4 (working artifacts)
