# Duplicate Log: Maple Commons Hold/Sell Case

Exact duplicates, near-duplicates, and version families. Nothing deleted — flagged only.

## Exact duplicates
None. A checksum across the pile found no byte-identical files.

## Version families

### The financial model: S02 → S03
- **S02** `maple-commons-model-v3.xlsx` (modified ~2026-05-01)
- **S03** `maple-commons-model-FINAL.xlsx` (modified ~2026-05-15)

Same workbook structure, same asset, same tabs. Neither carries an internal version stamp, so
"which is current" had to be established by reading both: S03 is two weeks newer, its assumptions
tab references a February rent roll that v3 does not, and its scenario tab is more fully built
out. **S03 is current; S02 is superseded.**

They are not identical, and the difference matters: they use different exit-cap assumptions
(S02: 5.25%, S03: 5.50%), which flows through to different hold/sell values. That is not a
duplication issue to resolve here — it is a conflict, logged in `conflict_log.md`.

**Rule applied:** the draft cites S03 for forward math and never cites S02 as current. S02 is kept
for history. No figure is ever taken as "the model says" without specifying which model — the
exact failure (blending v3 and FINAL) this log exists to prevent.

## Near-duplicates
None beyond the model family above. The 2024 appraisal (S07) and the 2026 BOV (S04) both opine on
value but are different document types from different parties at different times; they are not
versions of each other and are ranked separately in the inventory.
