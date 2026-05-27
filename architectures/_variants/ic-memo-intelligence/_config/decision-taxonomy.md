# Decision Taxonomy

<!--
ANNOTATION: The fixed vocabulary for tagging each record, so the store can
aggregate into a body of decision precedent. Patterns emerge by tag — "the IC
conditions a DSCR stress test on ~70% of value-add multifamily approvals" is only
visible if condition category, segment, and decision lane are tagged consistently.
A free-text field will not aggregate; a controlled taxonomy will.

The condition-category and concern-category lists are controlled lists on purpose:
"which conditions the committee imposes again and again" and "what it worries
about most" are the highest-value patterns this store can surface, and they
require a stable, controlled vocabulary. The decision-lane tag is the spine — every
pattern is read against what the committee actually decided.

This is L3 reference, loaded in stages 01 and 03. Keep it stable; add categories
deliberately, not ad hoc.
-->

## Asset Type
[A controlled list of asset types the firm invests in. Tag exactly one (or a
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
[Controlled geography tags at the grain you actually invest in. Keep the list to
the markets you invest in; add a submarket only when you will query by it.]

## Strategy
[The business-plan type, as a controlled tag, so decision patterns can differ by
risk profile. Examples: core, core-plus, value-add, opportunistic, development.]

## Decision Lane
[The committee's decision, as a controlled tag. Tag exactly one:
- Approved
- Approved-with-conditions
- Declined
- Tabled (deferred for more information — note what was asked for)]

## Condition Category
[A CONTROLLED list of the kinds of conditions the committee imposes — one of the
two highest-value tags, because the store's core job is "what does the IC always
require." Keep it a fixed list, not free text. Examples:
- Debt-service / DSCR stress test
- Leverage cap / max LTV
- Reserve or contingency requirement
- Sponsor / guarantor terms
- Third-party report (PCA, environmental, appraisal)
- Lease-up / pre-leasing milestone
- Pricing / structure change before close
- Reporting / monitoring requirement
Tag every condition in a record to one of these.]

## Concern Category
[A CONTROLLED list of the kinds of risks the committee raises — the second
high-value tag. Keep it a fixed list. Examples:
- Market / submarket softness
- Leverage / financing risk
- Execution / sponsor capability
- Basis / pricing
- Lease-up / absorption risk
- Tenant / credit concentration
- Exit / liquidity risk
- Capital-markets / rate exposure
Tag every concern in a record to one of these.]

## Decisive Factor
[The single thing that drove the decision, so the store can answer "what actually
decides whether this committee approves or declines." Tag the primary one; note a
secondary in the record if needed.]

## Dissent
[Whether the decision carried dissent, as a controlled tag: none / stated
reservation / formal no-vote. A split decision is a different precedent than a
clean one — tag it so the store does not read every approval as wholehearted.]

## Precedent Relationship
[How this decision sits against the store, as a controlled tag: sets-precedent
(first of its kind) / consistent-with-precedent / departs-from-precedent. A
departure is the signal that the committee's mind has changed — tag it so it is
not lost.]
