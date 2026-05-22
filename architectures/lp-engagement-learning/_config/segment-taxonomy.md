# LP Segment Taxonomy

<!--
ANNOTATION: The fixed vocabulary for tagging each record by LP type and check
size, so the store can aggregate. Patterns emerge by segment — "endowments keep
stalling on the fee" is only visible if endowments are tagged consistently. A
free-text "type" field will not aggregate; a controlled taxonomy will.

This is L3 reference, loaded in stages 01 and 03. Keep it stable; add categories
deliberately, not ad hoc.
-->

## LP Type
[A controlled list of investor types the firm raises from. Tag exactly one (or
a primary) per record. Examples:
- Public pension
- Corporate pension
- Endowment / foundation
- Insurance
- Fund-of-funds
- Family office (single / multi)
- RIA / wealth platform
- Sovereign / SWF
- High-net-worth individual]

## Check-Size Band
[Controlled bands so commitment scale aggregates. Set the boundaries to your
fund. Example bands:
- < $1M
- $1M – $5M
- $5M – $25M
- $25M – $100M
- > $100M]

## Relationship Origin
[How the LP entered, as a controlled tag, so the firm can see which channels
convert. Examples: existing LP re-up, placement agent, partner network,
inbound, conference, referral.]

## Optional Tags
[Other dimensions worth aggregating if relevant to the firm: geography, first-
time vs. repeat LP, decision speed. Keep the list short — each tag is only
worth having if you will query by it.]
