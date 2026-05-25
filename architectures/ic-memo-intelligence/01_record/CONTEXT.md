# Stage 01: Record

## Purpose
Assemble the factual decision record for a deal that has been decided at IC. Pull the recommendation from the memo and the decision, conditions, dissents, concerns, and vote from the committee's minutes/notes, into a structured record the analysis stage can reason over. Facts in; the reading of what the committee weighed comes later. This stage invents nothing — it transcribes and structures what the memo recommended and what the committee actually decided.

## Inputs
- **The trigger**: a deal has been decided at IC. Name the deal, the decision lane (Approved / Approved-with-conditions / Declined / Tabled), and the decision date.
- **The IC memo** (the deal-pipeline workspace / deal system): the recommendation put to the committee — the ask, the proposed structure, the sponsor's case, the headline terms.
- **The IC minutes / notes**: what the committee actually decided — the conditions imposed and to whom, the concerns and risks raised, any dissent and on what grounds, and the vote. This is the authoritative record of the decision; the model must not paraphrase a condition the committee did not impose or smooth a split vote into consensus.
- **_store/patterns.md** and **_store/records/**: read for precedent context — has the committee decided a similar deal before, and what did it condition or worry about?

## Process
1. Read the memo, the minutes, and the canonical taxonomy in _config/decision-taxonomy.md.
2. Record the decision lane and date, and the headline of what was recommended vs. what was decided. Where the two diverge (the memo recommended approval, the committee declined; or approved but on heavy conditions), note it plainly — that divergence is signal.
3. Transcribe the **conditions** the committee imposed, each tagged to a controlled condition category, and note to whom each condition was assigned and any deadline.
4. Transcribe the **concerns/risks** the committee raised, each tagged to a controlled concern category. Capture the committee's own words where they are on the record; do not upgrade a passing question into a formal concern.
5. Record any **dissent**: who dissented, on what grounds, and whether it was a formal no-vote or a stated reservation. A split or grudging decision is not the same as a clean one — preserve the difference.
6. Record the **vote** as minuted (unanimous / split / who abstained), if the firm minutes votes.
7. Tag the deal with the taxonomy (asset type, deal-size band, market, strategy) so the record can aggregate.
8. Note the **gaps**: what is not in the memo or minutes that analysis should know about (a concern raised verbally but not minuted, a condition whose owner is unclear). Flag it; do not fill it.

## Output
Write to: 01_record/output/record-[deal]-[date].md

Format:
```
# Decision Record: [Deal Name]
Decision: [Approved / Approved-with-conditions / Declined / Tabled]   Decided: [date]
Asset type: [taxonomy]   Deal-size band: [taxonomy]   Strategy: [taxonomy]
Market/submarket: [taxonomy]

## Recommended vs. Decided
[What the memo recommended, what the committee decided, and any divergence between them.]

## Conditions Imposed
[Each condition | condition category | owner | deadline. Empty if none.]

## Concerns Raised
[Each concern | concern category | the committee's own words where on the record.]

## Dissent
[Who dissented, on what grounds, formal no-vote vs. stated reservation. "None" if clean.]

## Vote
[As minuted: unanimous / split / abstentions. "Not minuted" if the firm does not record it.]

## Gaps
[What is NOT in the memo/minutes that analysis should know about. Flag, do not fill.]
```

## Done Looks Like
A factual decision record: the lane and date, what was recommended vs. decided, every condition tagged and assigned, every concern tagged and quoted where on the record, dissent and vote preserved as minuted, the deal tagged with the taxonomy, and gaps flagged — ready for analysis to read what the committee weighed without having to reconstruct what it decided.

## Common Failure Modes
- **Smoothing a split decision into consensus.** A grudging, heavily conditioned approval recorded as a clean yes loses the most important signal in the room. Preserve dissent and conditions exactly.
- **Inventing or upgrading a condition or concern.** Recording a condition the committee did not impose, or promoting an offhand question into a formal concern, manufactures precedent. Transcribe what is on the record.
- **Paraphrasing away the committee's own words.** Where the minutes capture how a member framed a concern, keep it — the analysis and the store are richer for the committee's actual language than for a tidy summary.
- **Filling a gap with a guess.** If the owner of a condition or the basis of a dissent is not minuted, flag it as a gap; do not infer it.

## Layer Annotation
L2 stage contract. The memo, the IC minutes, and the decision are L4 (this run). The decision taxonomy from _config/ is L3. The store is read here for precedent context (its L3-like role).
