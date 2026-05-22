# Store Schema

<!--
ANNOTATION: The structure of a stored record and how patterns roll up. The
capture stage normalizes each validated analysis into this shape before writing
it to _store/records/. A consistent schema is what lets the store be queried and
aggregated rather than just read one file at a time.

This is L3 reference, loaded in stage 03.
-->

## Record Schema (one per resolved engagement)
[The fields every stored record carries. Keep them stable. Example:
- LP name and segment tags (type, check-size band, relationship origin)
- Fund and outcome (committed/passed) and date
- Canonical-question answers (the comparable core)
- Validated why, with final confidence level
- Stated vs. assessed reason
- Transferable lessons
- Validator and validation date
- Links to the source record and analysis files]

## Patterns File (_store/patterns.md)
[How fund-level patterns are structured and maintained. Each pattern entry
should carry:
- The pattern statement (e.g., "Endowments stall on the GP commitment question")
- The segment(s) it applies to
- The supporting records (count and references)
- Confidence, and the date last updated
- Any contradicting records and how the pattern was qualified

Rules:
- Append-only for records; patterns are revised in place but every revision is
  dated and notes what evidence drove it.
- A pattern needs a stated minimum of supporting records before it is treated
  as more than a hypothesis — set that threshold here.
- A contradicting record revises the pattern; it does not get discarded to
  preserve the pattern.]

## Privacy / Handling
[Reminder: records contain confidential intelligence about named LPs and why
they acted. State here who may access the store and any redaction rules for
anything that leaves this workspace (e.g., what may flow to capital-raising prep
vs. what stays internal to IR).]
