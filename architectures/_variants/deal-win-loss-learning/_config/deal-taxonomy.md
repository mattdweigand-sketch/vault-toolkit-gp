# Deal Taxonomy

<!--
ANNOTATION: The fixed vocabulary for tagging each record, so the store can
aggregate. Patterns emerge by tag — "we lose limited processes to faster-closing
buyers" is only visible if process type and decisive dimension are tagged
consistently. A free-text field will not aggregate; a controlled taxonomy will.

The broker/intermediary list is a controlled list on purpose: "which brokers'
feedback proves reliable" and "which intermediaries we win through" are two of
the highest-value patterns this store can surface, and both require a stable,
controlled broker vocabulary.

This is L3 reference, loaded in stages 01 and 03. Keep it stable; add categories
deliberately, not ad hoc.
-->

## Asset Type
[A controlled list of asset types the firm bids on. Tag exactly one (or a
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

## Process Type
[How the deal was run, as a controlled tag. Examples:
- Broadly marketed
- Limited / select
- Off-market
- Bilateral / negotiated]

## Seller Type
[Who we bought from / bid against, as a controlled tag. Examples:
- Institutional
- Private / family
- Fund in wind-down
- Distressed
- Developer]

## Broker / Intermediary
[A CONTROLLED list of the brokers and intermediaries you transact with
repeatedly. This is the highest-value tag for two patterns — which intermediaries
you win through, and whose debrief feedback proves reliable — so keep it a fixed
list, not free text. Add a broker only when you have transacted with them.
"Off-market / none" is a valid value.]

## Market / Submarket
[Controlled geography tags at the grain you actually bid in. Keep the list to the
markets you compete in; add a submarket only when you will query by it.]

## Outcome
[Won / Lost / Withdrew-late. Tag exactly one. Withdrew-late is a flagged sub-case
— a different lesson than a clean loss.]

## Decisive Dimension
[The single dimension that decided the outcome, as a controlled tag, so the store
can answer "what actually wins and loses our deals." Examples: price, certainty /
speed of close, structure, financing, reputation / relationship, timing. Tag the
primary one; note a secondary in the record if needed.]
