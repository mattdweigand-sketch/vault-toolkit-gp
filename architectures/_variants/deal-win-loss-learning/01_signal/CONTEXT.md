# Stage 01: Signal

## Purpose
Assemble the factual bid record for a competitive process that has resolved. Pull the facts from the deal record, the broker debrief, and the final clearing price into a structured record the analysis stage can reason over — without yet explaining anything. Facts in; the why comes later.

## Inputs
- **The trigger**: a competitive process has resolved. Name the deal, the outcome (Won / Lost, or Withdrew-late as a flagged sub-case), and the date.
- **Deal record** (the deal system / deal-pipeline workspace): how the opportunity reached us, our screen and underwrite, the price and structure we bid, our LOI, the timeline through best-and-final.
- **Broker debrief**: what the broker/intermediary told us about why we won or lost, recorded as *stated* — kept distinct from the *actual* reason, which analysis will probe.
- **Final transaction / clearing price**: the winning bid and terms, from the broker or public record.
- **_store/** (for context): any prior record involving this broker, seller, or submarket, and records for similar processes, so this record is assembled with awareness of what is already known.
- **_config/deal-taxonomy.md**: to tag the process per the controlled vocabulary.

## Process
1. Confirm the trigger: which deal, won or lost (or withdrew-late), and the date.
2. Pull how the opportunity reached us: the broker/intermediary or off-market path, and the process type (broadly marketed / limited / off-market / bilateral).
3. Record our thesis and what we bid: price, structure, financing, certainty/timing terms — from the deal record, not from memory.
4. Record the clearing price and winning terms, and compute our **gap** to it — in price *and* in terms. State the source (broker-shared or public record).
5. Record the broker's stated reason for the outcome, verbatim or close, as a logged fact — distinct from the assessed reason analysis will probe.
6. Note where in the process we gained or lost ground if known (first round, best-and-final, last look).
7. Tag the process per the taxonomy: asset type, deal-size band, process type, seller type, broker/intermediary, market/submarket, outcome.
8. Note what the record does not capture — gaps the analysis stage should know about (off-record broker color, a term we bid blind on, a relationship factor not logged).
9. Produce the bid record. State facts and their source. Do not analyze.

## Output
Write to: 01_signal/output/record-[deal]-[date].md

Format:
```
# Bid Record: [Deal Name]
Outcome: [Won / Lost / Withdrew-late]   Resolved: [Date]
Asset type: [from taxonomy]   Deal-size band: [from taxonomy]
Process type: [from taxonomy]   Seller type: [from taxonomy]
Broker/intermediary: [from taxonomy]   Market/submarket: [from taxonomy]

## How It Reached Us
[Broker/intermediary or off-market path. Process type.]

## Our Bid
[Thesis, price, structure, financing, certainty/timing terms. From the deal record.]

## Clearing Price & Our Gap
[Winning bid and terms. Our gap in price AND in terms. Source: broker / public record.]

## Broker's Stated Reason
[As told to us, verbatim or close. A logged fact, not yet assessed.]

## Process Path
[Where we gained/lost ground, if known: first round, best-and-final, last look.]

## Gaps
[What is not in the record that analysis should know about: off-record color,
 a term bid blind, an unlogged relationship factor.]
```

## Done Looks Like
A factual, source-grounded record of the process — our bid, the clearing price, and our gap, tagged by the taxonomy — that the analysis stage can work from without re-querying the deal system. No explanation of why — just what happened.

## Common Failure Modes
- **Reconstructing from memory.** The deal record and market data are the source. A bid history assembled from impression is exactly the unreliable input that would corrupt the analysis and then the store. Pull it; do not recall it.
- **Conflating stated and actual reasons.** "The broker said we were just outbid" is a logged fact. Whether price was the real reason is an analysis question. Keep them separate at this stage.
- **Inventing a clearing price.** If the winning bid is not knowable, say so in Gaps — do not estimate a number and let it harden into the record.
- **Analyzing early.** The job is assembly. An early "why" shapes the record and undermines the comparability the whole workspace depends on.

## Layer Annotation
L2 stage contract. The deal record, broker debrief, and clearing price are L4 (this run). The store is read here for context (its L3-like role). The deal taxonomy from _config/ is L3.
