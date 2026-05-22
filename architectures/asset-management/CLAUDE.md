# Asset Management Workspace

## What This Is
A workspace for portfolio monitoring: turning per-asset operating data into a business-plan-versus-actual review that tells the firm how each asset is tracking against the underwriting, what is drifting, and what needs attention. Built for an asset-management or portfolio team at a commercial real estate GP that reviews owned assets on a recurring cycle (monthly or quarterly) and produces an internal review that feeds the investment committee and, downstream, LP reporting.

This is internal-facing analysis, not investor communication. The quarterly LP letter is a different workflow (see the lp-reporting workspace), and it draws on what this workspace produces. This workspace reports on what the fund already owns and how it is performing against plan.

## Current State
- This is a reference architecture. No active review cycle.
- To use: copy the folder, populate _config with your assets' business-plan targets, your review standards, and your report format.

## Structure
```
asset-management/
  CLAUDE.md              # You are here.
  CONTEXT.md             # Workflow routing.
  01_data/
    CONTEXT.md           # Stage contract: gather and verify operating data.
    output/              # Verified data pack. Input for 02_review.
  02_review/
    CONTEXT.md           # Stage contract: analyze vs. plan, flag variances and risks.
    output/              # Analysis pack and watchlist. Input for 03_report.
  03_report/
    CONTEXT.md           # Stage contract: produce the asset review and watchlist.
    output/              # Internal asset reviews, portfolio monitor, watchlist.
  _config/               # Business-plan targets, review standards, report format.
  _prompts/              # Reusable prompt fragments for recurring analysis tasks.
```

## How to Use
1. Read CONTEXT.md to understand the full workflow.
2. Populate _config/ with each asset's business-plan targets, your variance and watchlist thresholds, and your report format.
3. Start in 01_data. Gather and verify the operating data for the period. The numbers come from your property and modeling systems, not from the model.
4. Move to 02_review. Analyze actuals against the business plan, flag variances and risks, and build the watchlist.
5. Move to 03_report. Produce the internal asset review and the portfolio watchlist.
6. Human review happens between stages. The data and the judgment both get read before the review goes to the IC.

## Key Decisions
- **Three stages: gather, judge, write.** Assembling the operating data, analyzing it against plan, and writing the review are distinct modes of work. The data stage gates the others — an analysis built on unverified actuals is worse than no analysis, because it looks authoritative. Combining data assembly with analysis is how a stale occupancy figure becomes a confident, wrong conclusion.
- **The business plan is the measuring stick.** Variance analysis is meaningless without something to vary from. The underwriting targets in _config are what actuals are compared against. Keeping them in _config means you measure every period against the same baseline instead of re-deriving "what we expected" each time.
- **The model does not compute returns or marks.** Actuals come from Yardi/MRI/RealPage. The underwriting model, IRR, and valuation come from Argus or your model and your valuation process. The model in this workspace narrates the variance and flags the risk; it never recomputes a return or sets a mark. See Constraint 09.
- **This workspace is a host for two variants.** A JV/co-GP partner report and a distressed-asset watchlist memo share this workspace's data layer, analytical motion, and review path. They are not separate workspaces — they are format variants configured in `_config/reporting-format.md`. Build the base review first; add the variants when you need them. (See "Variants" below.)

## Variants
Two related outputs ride on this workspace as configured format variants, not separate builds:
- **JV / co-GP partner reporting** — the same asset analysis, reframed for a co-sponsor or operating partner who wants promote/waterfall position and asset-level detail rather than an LP-style summary. A format-and-tone variant in `_config/reporting-format.md`.
- **Watchlist / special-servicing memo** — an intensified review of a distressed or underperforming asset, more direct on bad news and action-oriented. A format variant in `_config/reporting-format.md`. (If workout becomes the firm's primary business, this re-promotes to its own gated decision workspace.)

## Constraints That Apply
Built against the GP Operating Toolkit. Most relevant: **02 (Output Drift)**, **04 (Session Consistency)**, **08 (Handoff Readiness)**, the universal **06 (Layer Triage)** and **09 (Platform Boundary)**, and **10 (Source Provenance)** when the operating data arrives as an unvetted set of asset reports.

## Layer Annotations
- CLAUDE.md: L0 (always loaded, orientation)
- CONTEXT.md: L1 (workflow routing)
- Stage CONTEXT.md files: L2 (stage contracts)
- _config/ files: L3 (reference: targets, standards, format)
- _prompts/ files: L3 (reference: reusable analysis fragments)
- Operating data and stage outputs: L4 (working artifacts, this cycle)
