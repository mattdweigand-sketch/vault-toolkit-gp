# Assumption Taxonomy

<!--
ANNOTATION: The fixed vocabulary for tagging each record, so the store can
aggregate into a calibration table. Patterns emerge by tag — "our exit-cap
assumption runs ~40bps optimistic in secondary-market value-add" is only visible
if assumption category, segment, and direction are tagged consistently. A
free-text field will not aggregate; a controlled taxonomy will.

The assumption-category list is a controlled list on purpose: "which assumptions
the firm systematically gets wrong" is the highest-value pattern this store can
surface, and it requires a stable, controlled vocabulary of the assumptions you
underwrite on. The skill/luck attribution tag is the second: it is what lets the
store answer "how much of our track record is edge vs. market."

This is L3 reference, loaded in stages 01 and 03. Keep it stable; add categories
deliberately, not ad hoc.
-->

## Asset Type
[A controlled list of asset types the firm underwrites. Tag exactly one (or a
primary) per record. Examples: multifamily, industrial, office, retail,
hospitality, mixed-use, land/development.]

## Deal-Size Band
[Controlled bands so deal scale aggregates. Set the boundaries to your fund.
Example bands:
- < $25M
- $25M – $75M
- $75M – $250M
- $250M – $500M
- > $500M]

## Market / Submarket
[Controlled geography tags at the grain you actually underwrite in. Keep the list
to the markets you invest in; add a submarket only when you will query by it.]

## Strategy
[The business-plan type, as a controlled tag, so calibration can differ by risk
profile. Examples: core, core-plus, value-add, opportunistic, development.]

## Hold-Period Band
[Controlled bands for realized hold, so vintage and duration effects aggregate.
Example: < 2 yrs, 2–4 yrs, 4–7 yrs, > 7 yrs.]

## Vintage Year
[The underwriting / acquisition year, so cohorts aggregate and you can see whether
a bias is era-specific (e.g., everything underwritten in a low-rate vintage). Tag
the year the deal was approved at IC.]

## Assumption Category
[A CONTROLLED list of the assumptions you underwrite on — the highest-value tag,
because the store's core job is "which assumptions do we systematically miss."
Keep it a fixed list, not free text. Examples:
- Going-in cap rate
- Rent / revenue growth
- Opex growth
- Lease-up / absorption pace
- Exit cap rate
- Hold period
- Leverage / cost of debt
- Capex / renovation budget
- Terminal value
Tag every material miss in a record to one of these.]

## Outcome vs. Underwriting
[Outperformed / In-line / Underperformed. Tag exactly one. Interim-checkpoint is a
flagged sub-case — a partial backtest, a different weight than a realized result.]

## Decisive Driver
[The single assumption category that drove the variance, so the store can answer
"what actually decides whether we beat or miss our underwriting." Tag the primary
one; note a secondary in the record if needed.]

## Cause Class
[Why the assumption missed, as a controlled tag: forecasting error / execution /
exogenous. This separates "we predicted wrong" from "we executed off-plan" from
"the market moved" — three different lessons.]

## Skill / Luck Attribution
[The headline read on the realized return, as a controlled tag:
skill-dominant / luck-dominant / mixed. This is what lets the store answer the
hardest question — how much of the track record is the firm's edge vs. market
beta. Treat with care; it is candid internal intelligence.]
