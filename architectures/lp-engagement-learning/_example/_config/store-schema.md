# Store Schema

<!--
EXAMPLE: Filled for Meridian Fund III. Compare to the blank template in
../../_config/store-schema.md.
-->

## Record Schema (one per resolved engagement)
Every stored record carries, in this order:
- LP name; segment tags (type, check-size band, relationship origin, first-time/repeat, decision speed)
- Fund and outcome (committed/passed) and resolution date
- Canonical-question answers (the comparable core)
- Validated why, with final confidence level
- Stated reason vs. assessed reason
- Transferable lessons
- Validator and validation date
- Links to the source signal record and analysis files

## Patterns File (_store/patterns.md)
Each pattern entry carries:
- The pattern statement
- The segment(s) it applies to
- Supporting records (count and references)
- Confidence, and the date last updated
- Any contradicting records and how the pattern was qualified

Rules:
- Records are append-only. Patterns are revised in place, but every revision is dated and notes
  the evidence that drove it.
- A pattern needs at least **3 supporting records** before it is treated as more than a
  hypothesis. Below that it is logged as "emerging."
- A contradicting record revises the pattern; it is never discarded to preserve the pattern.

## Privacy / Handling
The store holds confidential intelligence about named LPs and why they acted. Access is limited to
the IR and capital-raising team. When a pattern flows to capital-raising prep, share the *pattern*
(segment-level), not the named-LP detail behind it, unless the named context is necessary and
cleared.
