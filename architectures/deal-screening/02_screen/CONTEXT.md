# Stage 02: Screen

## Purpose
Measure the opportunity against the firm's investment box, run a rough economics sanity check, test for deal-breakers, and produce a pursue / pass / need-more recommendation with a clear rationale. Fast and consistent — the same kind of deal should get the same read every time.

## Inputs
- **01_capture/output/snapshot-[deal-name]-[date].md**: The standardized opportunity.
- **_config/investment-box.md**: What the firm buys. The fit standard.
- **_config/screening-criteria.md**: The go/no-go thresholds and automatic deal-breakers.
- **_config/economics-assumptions.md**: Standard rough-screen assumptions for the quick economics.
- **_references/** (selectively): Prior screens of similar deals, submarket comps.

## Process
1. Read the snapshot and the investment box. Assess fit on each box dimension: asset type, geography, size, strategy, return profile. Fit / partial / miss on each, with a one-line reason.
2. Run the deal-breaker checks from screening-criteria.md. A deal-breaker is automatic and ends the screen — a non-core asset type, a market the firm will not enter, a size outside the range, a structure the firm will not do. If one trips, the recommendation is pass; say which breaker and stop.
3. If no breaker trips, run the rough economics: a back-of-envelope check on basis, going-in yield, and a rough return on the standard assumptions. This is a filter to catch deals that cannot work even before underwriting, not an underwrite. Label every number as a rough screen figure.
4. Weigh fit and economics together against the criteria. Form a recommendation: pursue, pass, or need-more (a specific missing fact that would change the call).
5. Write the rationale so a reader who never saw the OM understands why. The rationale is the product; the recommendation is one line of it.

## Output
Write to: 02_screen/output/screen-[deal-name]-[date].md

Format:
```
# Screen: [Deal Name]
Snapshot reference: [filename from capture]

## Recommendation
[Pursue / Pass / Need-more] — one-line reason.

## Fit vs. the Box
[Each box dimension: fit / partial / miss, with a reason.]

## Deal-Breaker Check
[Each criterion: clear / tripped. If tripped, which and why.]

## Rough Economics (screen-level, not an underwrite)
[Basis, rough going-in yield, rough return on standard assumptions.
 Every figure labeled as a rough screen estimate. State the assumptions used.]

## Rationale
[Why this recommendation. Enough that a reader who never saw the OM
 follows the logic. The strongest reasons for and against.]

## If Need-More
[The specific fact that would change the call, and where to get it.]
```

## Done Looks Like
A recommendation with a rationale that stands on its own, measured against the box and the criteria, with the economics clearly marked as a rough filter. Fast enough that screening keeps pace with deal flow.

## Common Failure Modes
- **Underwriting instead of screening.** The rough economics is a filter. If you are building a real model here, you have left screening and entered diligence. Stop and pursue it properly in deal-pipeline, or pass.
- **Letting marginal economics override a strategic breaker.** A great-looking price on an asset type the firm does not buy is still a pass. Deal-breakers are automatic.
- **A recommendation with no rationale.** "Pass" with no reason teaches the firm nothing and is not auditable. The rationale is the deliverable.

## Layer Annotation
L2 stage contract. The snapshot is L4 (this deal). The investment box, screening criteria, and economics assumptions from _config/ are L3. Prior screens and comps from _references/ are L3.
