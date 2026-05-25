# Store Schema

<!--
ANNOTATION: The structure of a stored record and how the decision-intelligence
patterns roll up. The capture stage normalizes each validated analysis into this
shape before writing it to _store/records/. A consistent schema is what lets the
store be queried — "show every value-add MF deal we conditioned on a DSCR stress
test" — rather than read one file at a time.

This is L3 reference, loaded in stage 03.
-->

## Record Schema (one per IC decision)
[The fields every stored record carries. Keep them stable. Example:
- Deal name and taxonomy tags (asset type, deal-size band, market/submarket,
  strategy)
- Decision lane (approved / approved-with-conditions / declined / tabled) and
  decision date
- Recommended vs. decided (and any divergence)
- Conditions imposed, each tagged by condition category, with owner and deadline
- Concerns raised, each tagged by concern category
- Dissent (none / stated reservation / formal no-vote) and vote as minuted
- Decisive factor
- Stated vs. inferred rationale, with final confidence level
- Precedent relationship (sets / consistent-with / departs-from)
- Implied signal for future memos
- Validator and validation date
- Links to the source decision record and analysis files]

## Patterns File (_store/patterns.md)
[How firm-level decision intelligence is structured and maintained. Organize it
around what a future memo most needs to know. Each pattern entry should carry:
- The pattern statement (e.g., "The IC conditions a DSCR stress test on value-add
  multifamily approvals" or "The IC has declined every deal above 70% LTV since
  2023")
- The segment(s) it applies to (asset type, strategy, market, decision lane)
- The supporting records (count and references)
- Confidence, and the date last updated
- Any departing records and how the pattern was qualified

Organize patterns into the views a memo author actually wants:
- **Standing conditions** — what the committee reliably requires, by segment.
- **Revealed risk appetite** — the boundaries it will not cross (a leverage
  ceiling, a market it keeps passing on, a structure it requires).
- **Recurring concerns** — what it raises again and again, so a memo can
  pre-empt it.
- **Decision precedents** — notable approvals and declines a new similar deal
  should be measured against.

Rules:
- Append-only for records; patterns are revised in place but every revision is
  dated and notes what evidence drove it.
- A pattern needs a stated minimum of supporting records before it is treated as
  more than a hypothesis — set that threshold here (the example store uses 3+ for
  "stated," below that "emerging").
- A departing record revises the pattern; it does not get discarded to preserve
  the pattern. The committee changing its mind is exactly what the store exists to
  catch.
- A one-off bespoke condition is logged but does not become a standing condition
  until it recurs — do not read a single deal's quirk as the committee's policy.]

## Privacy / Handling
[Reminder: records document the firm's own decision patterns, its revealed risk
appetite, and candid reads on dissent and on what the committee really weighed.
State here who may access the store and any redaction rules for anything that
leaves this workspace. In particular, individual members' dissents and the
inferred (vs. stated) rationale are sensitive — the standing conditions and
risk-appetite boundaries may flow to deal-pipeline and deal-screening, but the
named-dissent detail and the "what really drove it" reads should stay internal to
the team and the IC.]
