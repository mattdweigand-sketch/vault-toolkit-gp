# Stage 02: Review

## Purpose
Analyze the verified actuals against the business plan, attribute the variances, flag risks, and build the watchlist. The output is an analysis pack the report stage can write from directly. This is the judgment stage — where operating data becomes "here is how this asset is tracking and what needs attention."

## Inputs
- **01_data/output/data-pack-[period].md**: The verified data pack. The only source of figures for this stage.
- **_config/business-plan-targets.md**: The underwriting targets per asset — the baseline to measure against.
- **_config/review-standards.md**: Variance materiality thresholds and watchlist criteria.
- **_prompts/** (selectively): Reusable fragments for variance attribution and watchlist triage.

## Process
1. Read the data pack and the business-plan targets. Confirm you are measuring each asset against its own plan.
2. For each asset, compare actuals to plan on the key dimensions: NOI, occupancy, leasing pace, expense control, the business-plan milestones.
3. Attribute the material variances. Not just "occupancy is 8 points behind plan," but why: concession-driven demand softness, a delayed renovation, a move-out. Distinguish a timing variance from a structural one.
4. Assess the business-plan status per asset: on plan, ahead, behind, or at risk. Be specific about what "behind" means for the plan and the eventual return — qualitatively. Do not compute a revised return; that is the model's job (Constraint 09).
5. Apply the watchlist criteria from review-standards.md. Any asset that trips a threshold goes on the watchlist with a reason and a recommended action.
6. Note hold / sell / refinance signals where the data suggests one — as a flag for the IC, not a decision.
7. Produce the analysis pack.

## Output
Write to: 02_review/output/analysis-[period].md

Format:
```
# Asset Analysis: [Portfolio / Asset] [Period]

## Per-Asset Status
[Per asset: on plan / ahead / behind / at risk, with the key variances
 and their attribution. Reference the data-pack figures; do not restate
 unverified numbers.]

## Material Variances
[The variances that matter, with cause. Timing vs. structural.]

## Watchlist
[Assets tripping a threshold: the asset, the trigger, the cause, and the
 recommended action. This becomes the watchlist in the report.]

## Hold / Sell / Refi Signals
[Where the data points toward an action. Framed as a signal for the IC,
 not a decision. The return math that would support it lives in the model.]

## Open Questions
[What the analysis could not resolve from the data and needs from the
 asset team or the model.]
```

## Done Looks Like
An analysis pack that says, per asset, how it is tracking against its plan and why, with a watchlist of what needs attention. The report stage should be able to write from this without re-analyzing.

## Common Failure Modes
- **Variance without attribution.** "NOI missed by 6%" is data, not analysis. The job is the why, and whether it is timing or structural. Without that, the review tells the IC nothing it could not read off the export.
- **Computing a revised return or mark.** Tempting when an asset is off plan. The revised return comes from the model; here you describe the variance and flag the asset (Constraint 09).
- **Measuring against last period instead of the plan.** Period-over-period movement is context. The business plan is the standard. An asset can improve quarter-over-quarter and still be badly behind plan.

## Layer Annotation
L2 stage contract. The data pack is L4 (this cycle). Business-plan targets and review standards from _config/ are L3 (stable reference). Prompt fragments from _prompts/ are L3.
