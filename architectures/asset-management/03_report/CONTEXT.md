# Stage 03: Report

## Purpose
Produce the internal asset review and the portfolio watchlist from the analysis pack, in the firm's format. This stage formats and frames; it does not re-analyze. The output is what goes to the investment committee and feeds downstream LP reporting.

## Inputs
- **02_review/output/analysis-[period].md**: The analysis pack. The basis for the report.
- **_config/reporting-format.md**: The structure of the internal review, plus the JV/co-GP and watchlist variants.
- **01_data/output/data-pack-[period].md**: Available to cite specific verified figures.

## Process
1. Read the analysis pack. Confirm it covers the scope of this review.
2. Select the format from reporting-format.md: the base internal asset review, or a variant (JV/co-GP partner report, watchlist memo).
3. Write the report in that format. Lead with the portfolio-level read and the watchlist; follow with per-asset detail. The figures come from the data pack; the judgment from the analysis pack. Do not introduce a number or a conclusion that is not in those two inputs.
4. Build the watchlist section: the assets flagged in review, the trigger, the cause, the recommended action and owner.
5. For a variant: apply the variant's framing and tone (a co-GP wants promote/waterfall position and granular detail; a watchlist memo is direct and action-oriented) without changing the underlying figures or analysis.
6. Record the report in output.

## Output
Write to: 03_report/output/asset-review-[period].md (or the variant name)

Format (base internal review):
```
# Asset Review: [Portfolio] [Period]
Prepared for: [IC / internal]
Figures source: 01_data/output/data-pack-[period].md
Analysis source: 02_review/output/analysis-[period].md

## Portfolio Read
[The top-level picture: how the portfolio is tracking against plan,
 the headline movements, the count and severity of watchlist items.]

## Watchlist
[Per flagged asset: trigger, cause, recommended action, owner, timing.]

## Per-Asset Detail
[Per asset: status vs. plan, key variances and attribution, leasing and
 operating notes. Drawn from the analysis pack.]

## Signals for the IC
[Hold / sell / refi signals surfaced in review, for the committee to weigh.
 Not decisions.]
```

## Done Looks Like
An internal review the IC can act on: a clear portfolio read, a watchlist with actions and owners, and per-asset detail traceable to verified data. No figure or conclusion appears that is not in the data pack or the analysis pack.

## Common Failure Modes
- **Re-analyzing in the report.** If the report reaches a conclusion not in the analysis pack, the review stage is being redone here, without its standards. Send analysis questions back to stage 02.
- **A variant that changes the numbers.** A JV/co-GP report and a watchlist memo change framing and tone, never the figures. Same data, different audience.
- **A watchlist without owners or actions.** A list of troubled assets with no recommended action and no owner is a worry, not a tool. Each watchlist item carries an action and a name.

## Layer Annotation
L2 stage contract. The analysis pack and data pack are L4 (this cycle). The report format from _config/ is L3 (stable reference).
