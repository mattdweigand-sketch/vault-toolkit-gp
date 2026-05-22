# Stage 01: Signal

## Purpose
Assemble the factual engagement record for an LP whose engagement has resolved. Pull the timeline and facts from the CRM into a structured record the analysis stage can reason over — without yet explaining anything. Facts in; the why comes later.

## Inputs
- **The trigger**: an LP has committed or passed. Name the LP, the fund, and the outcome.
- **CRM engagement data**: the touchpoint timeline, meetings, materials shared, who was involved on both sides, questions and objections logged, and the outcome with its date.
- **_store/** (for context): any prior record for this LP, and the records for similar-segment LPs, so this record is assembled with awareness of what is already known.
- **_config/segment-taxonomy.md**: to tag the LP's segment and check-size band.

## Process
1. Confirm the trigger: which LP, which fund, committed or passed, and the date.
2. Pull the engagement timeline from the CRM: first contact through resolution. Meetings, calls, materials sent, data-room access, the people involved.
3. Record the objections, questions, and concerns the LP raised, as they were logged — not as you remember them.
4. Record the outcome precisely: committed (amount, terms, any conditions) or passed (and the stated reason, if one was given — kept distinct from the *actual* reason, which analysis will probe).
5. Tag the LP's segment and check-size band per the taxonomy.
6. Note what the CRM does not capture — gaps the analysis stage should be aware of (an off-record conversation, a relationship factor not logged).
7. Produce the engagement record. State facts and their source. Do not analyze.

## Output
Write to: 01_signal/output/record-[lp-name]-[date].md

Format:
```
# Engagement Record: [LP Name]
Fund: [Name]   Outcome: [Committed / Passed]   Resolved: [Date]
Segment: [from taxonomy]   Check-size band: [from taxonomy]

## Timeline
[First contact → resolution. Touchpoints, meetings, materials, people,
 each from the CRM with dates.]

## Objections / Questions Raised
[As logged in the CRM. The LP's stated concerns, verbatim or close.]

## Outcome
[Committed: amount, terms, conditions. / Passed: stated reason if given.]

## Gaps
[What is not in the CRM that analysis should know about.]
```

## Done Looks Like
A factual, source-grounded record of the engagement, tagged by segment, that the analysis stage can work from without re-querying the CRM. No explanation of why — just what happened.

## Common Failure Modes
- **Reconstructing from memory.** The CRM is the source. A timeline assembled from impression is exactly the unreliable input that would corrupt the analysis and then the store. Pull it; do not recall it.
- **Conflating stated and actual reasons.** "They said it was timing" is a logged fact. Whether timing was the real reason is an analysis question. Keep them separate at this stage.
- **Analyzing early.** The job is assembly. An early "why" shapes the record and undermines the comparability the whole workspace depends on.

## Layer Annotation
L2 stage contract. The CRM engagement data is L4 (this run). The store is read here for context (its L3-like role). The segment taxonomy from _config/ is L3.
