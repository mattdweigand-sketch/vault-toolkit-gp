# Store Schema — Ridgeline Capital Partners

Filled version for the worked example. The structure each stored record follows and how patterns
roll up. A consistent schema is what lets the store be queried rather than read one file at a time.

## Record Schema (one per resolved process)
Every stored record carries:
- Deal name and taxonomy tags (asset type, deal-size band, process type, seller type,
  broker/intermediary, market/submarket)
- Outcome (won / lost / withdrew-late) and date
- Our bid vs. clearing price, and the gap — in price and in terms
- Decisive dimension
- Canonical-question answers (the comparable core)
- Validated why, with final confidence level
- Stated vs. assessed reason (kept distinct — the broker spin-defense)
- Transferable lessons
- Validator and validation date
- Links to the source bid record and analysis files

## Patterns File (_store/patterns.md)
Each pattern entry carries:
- The pattern statement (e.g., "We win on certainty of close, not top price")
- The segment(s) it applies to (asset type, process type, broker, decisive dimension)
- The supporting records (count and references)
- Confidence, and the date last updated
- Any contradicting records and how the pattern was qualified

Rules:
- Records are append-only. Patterns are revised in place; every revision is dated and notes the
  evidence that drove it.
- A pattern is "stated" at **3+ supporting records**; below that it is "emerging."
- A contradicting record revises the pattern — it is not discarded to preserve the pattern.

## Privacy / Handling
Records contain sensitive competitive intelligence: our bid behavior, our gap to clearing price,
and our candid read on specific broker relationships. Access is limited to the acquisitions team.
What flows to deal-pipeline sourcing and bid strategy is the pattern-level lesson, not the named
detail — in particular, our assessed-vs-stated read on a named broker (e.g., that Pinnacle's
"you were light on price" feedback skews unreliable) stays internal to the team.
