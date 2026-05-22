# Stage 01: Capture

## Purpose
Turn an inbound opportunity — however it arrived — into a standard snapshot the screen stage can evaluate on the same terms as every other deal. Extract the facts; do not yet judge them.

## Inputs
- **The opportunity**: offering memo, teaser, broker email, off-market intro, or listing. Paste or reference it here.
- **Deal and market data** (Dealpath / CoStar, if available): listing details, submarket comps, ownership.
- **_config/investment-box.md**: Referenced only to know which facts matter for the screen (so capture pulls the right fields), not to judge fit yet.

## Process
1. Read the opportunity in full. If it came with a fuller data set (a small data room rather than a teaser), note provenance and which document is authoritative for each fact (Constraint 10) — but do not deep-dive; this is still screening.
2. Extract the standard fields the screen needs: asset type, location/submarket, size, asking price and implied basis, in-place income and occupancy, the seller's stated business plan, debt assumability, timeline, and how the deal was sourced.
3. Pull comparable context from the data sources where available (submarket comps, recent trades), tagged to source.
4. Note what is missing. A teaser rarely has everything; flag the gaps the screen will have to reason around or request.
5. Produce the snapshot. State facts and their source. Do not editorialize on fit — that is the screen stage.

## Output
Write to: 01_capture/output/snapshot-[deal-name]-[date].md

Format:
```
# Opportunity Snapshot: [Deal Name]

Source: [broker / off-market / listing], received [date]
Sourced by: [name / relationship]

## The Asset
[Type, location/submarket, size, condition, year built.]

## The Ask
[Asking price, implied basis (per unit / per SF / cap rate as presented),
 structure, timeline.]

## In-Place
[Income, occupancy, in-place vs. market rents as presented, debt and
 assumability. Each tagged to its source.]

## Seller's Business Plan
[What the seller says the opportunity is. Their case, captured as theirs.]

## Submarket Context
[Comps and recent trades from the data sources, tagged to source.]

## Gaps
[What the materials do not say that the screen will need.]
```

## Done Looks Like
A snapshot that lets the screen stage evaluate this deal on the same standard fields as every other deal, with facts tagged to source and gaps named. No fit judgment yet.

## Common Failure Modes
- **Screening while capturing.** The job here is extraction, not evaluation. Mixing them means the snapshot is shaped by an early opinion, which is exactly what consistent screening is meant to avoid.
- **Repeating the OM's framing as fact.** The asking cap rate and the "value-add upside" are the seller's claims. Capture them as the seller's, not as established figures.
- **Over-investing.** This is a teaser-level capture, not diligence. Pull the standard fields and the obvious comps; stop there.

## Layer Annotation
L2 stage contract. The opportunity materials and pulled data are L4 (this deal). The investment box from _config/ is L3, referenced here only to know which fields to capture.
