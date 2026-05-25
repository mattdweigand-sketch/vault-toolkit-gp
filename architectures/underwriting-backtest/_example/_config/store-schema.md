# Store Schema — Ridgeline Capital Partners

This file defines the structure the capture stage normalizes each validated attribution into before
writing to `_store/records/`, and how the calibration patterns roll up. Stable since v1.0 (2023-01).

## Record Schema (one per realized deal)
- Deal name and taxonomy tags (asset type, deal-size band, market, strategy, hold-period band,
  vintage)
- Outcome (outperformed / in-line / underperformed) and realization date
- Model of record (version + IC-approval date)
- Headline return: underwritten vs. realized IRR and equity multiple, and the gap
- Material assumptions: underwritten vs. actual and the gap, per assumption category
- Decisive driver, and cause class (forecasting / execution / exogenous)
- Skill / luck attribution (skill-dominant / luck-dominant / mixed)
- Validated why, with final confidence level
- Calibration adjustment implied (assumption, segment, direction, rough magnitude)
- Validator and validation date
- Links to the source variance record and attribution files

## Patterns File (`_store/patterns.md`)
Each pattern entry carries: the pattern statement; the segment(s); the direction and rough
magnitude of the bias; supporting records (count + references); confidence and date last updated;
any contradicting records and how the pattern was qualified.

A separate **skill-vs-luck ledger** tracks, across the store, how much of realized outperformance
has been skill-dominant vs. luck-dominant, by segment. This is the honest track-record read.

Rules:
- Records are append-only; patterns are revised in place, every revision dated with the evidence
  that drove it.
- A pattern is **stated** at 3+ supporting records; below that it is **emerging**.
- A contradicting record revises the pattern; it is not discarded to preserve it.
- A one-off miss is logged but does not move a pattern until it recurs.

## Privacy / Handling
The calibration adjustments (exit-cap, lease-up, etc.) may flow to deal-screening's
economics-assumptions and to deal-pipeline underwriting. The **skill-vs-luck ledger** — our candid
read on how much of the track record is market beta — stays internal to the deal team and the IC,
and does not leave this workspace.
