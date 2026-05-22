# Stage 01: Research

## Purpose
Gather the market inputs and vet them before any synthesis. The output is a sourced research pack with each input ranked by provenance and known bias, so the thesis rests on vetted data rather than on whatever was loudest.

## Inputs
- **Research brief**: the market, sector, or strategy question this thesis addresses, and the decision it will inform. Provide this when you enter the stage.
- **Data-provider exports** (CoStar and others): rents, vacancy, absorption, cap rates, transaction volumes, supply pipeline.
- **Sell-side / broker research**: market reports and forecasts — useful, but with a known lean.
- **Economic and capital-markets data**: rates, employment, demographics, capital flows.
- **_config/source-map.md** and **_config/research-standards.md**: the firm's sources and how to vet them.

## Process
1. Define the question precisely. A thesis answers a specific question ("should we be buying industrial in the Southeast over the next 24 months?"), not "what is happening in real estate."
2. Gather the inputs the question needs from the mapped sources.
3. Run a provenance pass on the inputs (Constraint 10): inventory each source, rank it by reliability and recency, and flag its bias. Sell-side research arguing a market is hot is evidence to weigh, not a finding to adopt. Note where sources conflict.
4. Extract the relevant data points, each tagged to its source and as-of date. Never restate a figure without its source.
5. Identify what is missing — the data the question needs that the inputs do not cover.
6. Produce the research pack: vetted, sourced, ranked, with conflicts and gaps named.

## Output
Write to: 01_research/output/research-pack-[market-or-sector]-[date].md

Format:
```
# Research Pack: [Market / Sector] — [Question]
As-of: [date]

## The Question
[The specific question the thesis will answer.]

## Source Inventory
[Each source, what it provides, its reliability/recency, and its known bias.
 Ranked. See Constraint 10.]

## Data Points
[The relevant figures, each tagged to source and as-of date.]

## Conflicts
[Where sources disagree, both sides cited. Not resolved here — surfaced.]

## Gaps
[What the question needs that the inputs do not cover.]
```

## Done Looks Like
A research pack the synthesis stage can reason over without re-checking a source. Every data point is tagged, biases are flagged, conflicts are surfaced, and gaps are named.

## Common Failure Modes
- **Adopting sell-side conclusions as findings.** Broker research has a position. Capture its data and its argument as a sourced input with a noted lean, not as the thesis.
- **A figure with no source.** An untagged statistic is exactly what produces a confident, unfounded thesis. Tag it or drop it.
- **Researching the world instead of the question.** Without a precise question, research sprawls and synthesis has nothing to commit to. Pin the question first.

## Layer Annotation
L2 stage contract. The research inputs are L4 (this thesis). The source map and research standards from _config/ are L3 (stable reference).
