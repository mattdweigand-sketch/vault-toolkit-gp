# Store Schema — Ridgeline Capital Partners

This file defines the structure the capture stage normalizes each validated analysis into before
writing to `_store/records/`, and how the decision-intelligence patterns roll up. Stable since v1.0 (2022-06).

## Record Schema (one per IC decision)
- Deal name and taxonomy tags (asset type, deal-size band, market, strategy)
- Decision lane (approved / approved-with-conditions / declined / tabled) and decision date
- Recommended vs. decided (and any divergence)
- Conditions imposed, each tagged by condition category, with owner and deadline
- Concerns raised, each tagged by concern category
- Dissent (none / stated reservation / formal no-vote) and vote as minuted
- Decisive factor
- Stated vs. inferred rationale, with final confidence level
- Precedent relationship (sets / consistent-with / departs-from)
- Implied signal for future memos
- Validator and validation date
- Links to the source record and analysis files

## Patterns File (_store/patterns.md)
Organized into the views a memo author wants: **Standing Conditions**, **Revealed Risk Appetite**,
**Recurring Concerns**, **Decision Precedents**, **Departures / Open Questions**. Each pattern carries
its statement, segment, supporting records (count + references), confidence, and last-updated date.

Rules:
- Records are append-only; patterns are revised in place with dated notes.
- A pattern is "stated" at 3+ supporting records, "emerging" below that. Set the threshold and hold it.
- A departing record revises the pattern; it is not discarded to preserve the pattern. The committee
  changing its mind is exactly what the store exists to catch.
- A one-off bespoke condition is logged but does not become a standing condition until it recurs.

## Privacy / Handling
Records document Ridgeline's own decision patterns, revealed risk appetite, and candid reads on
dissent. The standing conditions and risk-appetite boundaries flow to deal-pipeline and
deal-screening; the named-dissent detail and the inferred-rationale reads stay internal to the deal
team and the IC.
