# Disposition Workspace

## What This Is
A workspace for the exit: deciding whether to hold or sell an asset, and — when the answer is sell — running the disposition through to close and capital return. Built for a commercial real estate GP making hold/sell calls on owned assets and managing the sale process when one is triggered. Each asset under active consideration gets a copy of this workspace.

This is the mirror image of the deal-pipeline workspace. Deal-pipeline brings an asset *in* — sourcing through close. This workspace takes one *out* — position through close. The acquisition pipeline ends where asset management begins; the disposition pipeline begins where asset management flags an exit and ends where capital returns to LPs.

## Current State
- This is a reference architecture. No active disposition.
- To use: copy the folder, rename it to the asset, and populate _config with the asset profile and your hold/sell criteria.

## Structure
```
disposition/
  CLAUDE.md              # You are here.
  CONTEXT.md             # Disposition workflow.
  01_position/
    CONTEXT.md           # Stage contract: assess standing and the hold/sell drivers.
    output/              # Position assessment. Frames the decision.
  02_decision/
    CONTEXT.md           # Stage contract: the hold-vs-sell case and the IC gate.
    output/              # Hold/sell case, timing thesis, IC decision.
  03_market/
    CONTEXT.md           # Stage contract: strategy, broker, disposition package, go to market.
    output/              # Disposition strategy, broker package, marketing narrative.
  04_close/
    CONTEXT.md           # Stage contract: offers, selection, close, capital return, handoff.
    output/              # Closing record, capital-return handoff.
  _config/               # Asset profile, hold/sell criteria, disposition standards.
  _references/           # Prior dispositions, broker relationships, comps.
```

## How to Use
1. Read CONTEXT.md for the full workflow.
2. Copy this folder and rename it to the asset (e.g., the-adler-denver-disposition-2026).
3. Populate _config/ with the asset profile (ideally carried from the asset-management workspace) and your hold/sell criteria.
4. Start in 01_position. Establish where the asset stands and what is driving an exit conversation.
5. Move to 02_decision — the gate. The IC decides hold or sell. A hold exits the pipeline with a revisit trigger. A sell proceeds.
6. On a sell, move through 03_market and 04_close. Human review between every stage.

## Key Decisions
- **Four stages, with the decision as a fork.** Position, decision, market, and close are distinct modes of work, exactly as in the acquisition pipeline. The difference is that stage 02 is a fork: hold exits here, sell continues. Separating position (the facts and drivers) from decision (the case and the IC gate) keeps the analysis honest — it forces the hold case to be made before the sell case is assumed.
- **The hold case gets made, not skipped.** The most common disposition error is treating "should we sell?" as "how do we sell?" Stage 01 surfaces the drivers for *and against*; stage 02 makes both cases. Selling a good asset early and holding a bad one too long are both expensive, and only an honest hold case prevents them.
- **The model frames the thesis; it does not compute the return.** The hold-vs-sell return delta, the net sale proceeds, the valuation — these come from Argus or your model and from broker BOVs. The model in this workspace builds the timing thesis and the disposition narrative *around* those figures. It never produces the return that justifies the decision. See Constraint 09.
- **Close ends with capital return and a clean handoff.** A disposition is not done at the wire. Stage 04 carries the capital-return mechanics to your fund administration (the platform and fund-admin team, which own the distribution) and the news to LP reporting, so the exit is reflected to investors cleanly. The math and the record are the platform's; this stage hands off to them.
- **_references is separate from _config.** Config holds this asset and the firm's standing hold/sell criteria. References hold cross-deal knowledge — prior dispositions, broker relationships, comps — that applies across exits and should not drag one asset's specifics into another.

## Constraints That Apply
Built against the GP Operating Toolkit. Most relevant: **01 (AI Writing)** and **02 (Output Drift)** for the case and package, **08 (Handoff Readiness)** for the close handoff, and the universal **06 (Layer Triage)** and **09 (Platform Boundary)**.

## Layer Annotations
- CLAUDE.md: L0 (always loaded, orientation)
- CONTEXT.md: L1 (disposition workflow routing)
- Stage CONTEXT.md files: L2 (stage contracts)
- _config/ files: L3 (asset-specific and standing criteria)
- _references/ files: L3 (cross-deal reference)
- Asset materials, model outputs, BOVs, and stage outputs: L4 (working artifacts)
