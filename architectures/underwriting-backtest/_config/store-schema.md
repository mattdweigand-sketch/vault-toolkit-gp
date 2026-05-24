# Store Schema

<!--
ANNOTATION: The structure of a stored record and how the calibration patterns roll
up. The capture stage normalizes each validated attribution into this shape before
writing it to _store/records/. A consistent schema is what lets the store be
queried and aggregated into a calibration table rather than just read one file at
a time.

This is L3 reference, loaded in stage 03.
-->

## Record Schema (one per realized deal)
[The fields every stored record carries. Keep them stable. Example:
- Deal name and taxonomy tags (asset type, deal-size band, market/submarket,
  strategy, hold-period band, vintage)
- Outcome (outperformed / in-line / underperformed) and realization date
- Model of record (version + IC-approval date) — what the backtest measured against
- Headline return: underwritten vs. realized IRR/MOIC, and the gap
- Material assumptions: underwritten vs. actual and the gap, per assumption category
- Decisive driver, and cause class (forecasting / execution / exogenous)
- Skill / luck attribution (skill-dominant / luck-dominant / mixed)
- Validated why, with final confidence level
- Calibration adjustment implied (assumption, segment, direction, rough magnitude)
- Validator and validation date
- Links to the source variance record and attribution files]

## Patterns File (_store/patterns.md)
[How firm-level calibration patterns are structured and maintained. Each pattern
entry should carry:
- The pattern statement (e.g., "Our exit-cap assumption runs ~40bps optimistic in
  secondary-market value-add")
- The segment(s) it applies to (asset type, strategy, market, vintage,
  assumption category)
- The direction and rough magnitude of the bias
- The supporting records (count and references)
- Confidence, and the date last updated
- Any contradicting records and how the pattern was qualified

Maintain a separate **skill-vs-luck ledger**: across the store, how much of
realized outperformance has been skill-dominant vs. luck-dominant, by segment.
This is the honest track-record read and the thing most worth protecting from
self-flattery.

Rules:
- Append-only for records; patterns are revised in place but every revision is
  dated and notes what evidence drove it.
- A pattern needs a stated minimum of supporting records before it is treated as
  more than a hypothesis — set that threshold here (the example store uses 3+ for
  "stated," below that "emerging").
- A contradicting record revises the pattern; it does not get discarded to
  preserve the pattern.
- A one-off miss is logged but does not move a pattern until it recurs — do not
  hard-code a single anomalous deal into the firm's standard assumptions.]

## Privacy / Handling
[Reminder: records document the firm's own systematic underwriting errors and the
candid skill-vs-luck read on its track record. State here who may access the store
and any redaction rules for anything that leaves this workspace. In particular,
the skill-vs-luck ledger is sensitive — the calibration adjustments may flow to
deal-screening and deal-pipeline, but the "how much of our track record is luck"
read should stay internal to the team and the IC.]
