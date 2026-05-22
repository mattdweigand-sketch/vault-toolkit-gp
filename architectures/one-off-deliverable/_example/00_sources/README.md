# 00_sources — The Pile, As It Arrived

In a real run, this folder holds the copied originals — the actual files, untouched. For this
worked example the files are fictional, so they are described here instead. This manifest is the
"before" picture: the messy source set the deal lead handed over, with no ranking and no sense of
which file is current. The inventory stage turns this list into
`01_inventory/output/source_inventory.md`.

What was in the folder (eight items, in the order they happened to be in):

1. `maple-commons-model-v3.xlsx` — a financial model. No internal version stamp.
2. `maple-commons-model-FINAL.xlsx` — another financial model, similar name, last-modified two
   weeks after v3.
3. `Northpoint_FundIII_FAexport_2026-03-31.pdf` — a fund-administration export: current basis,
   debt balance, NAV as of quarter-end.
4. `CBRE BOV - Maple Commons - May 2026.pdf` — a broker opinion of value.
5. `Maple Commons - AM report Q1 2026.docx` — the asset management quarterly report.
6. `RE_ Maple exit thoughts.eml` — an internal email thread about whether to sell.
7. `Maple Commons Appraisal 2024.pdf` — an MAI appraisal dated 2024.
8. (referenced, not present) `rent roll as of 2026-02` — the FINAL model cites a February rent
   roll in its assumptions tab, but no rent-roll file was in the folder.

The mess this represents, and what the inventory does about it:
- **Two models, no clear current one.** Similar names, no version stamp. → version family in the
  duplicate log; the pass reads both to find which is current and where they diverge.
- **The two models disagree on the exit cap.** → conflict log; surfaced, not averaged.
- **A broker's value view sits next to the firm's own.** → ranked background, not authoritative;
  a broker's BOV carries the broker's incentives.
- **A two-year-old appraisal.** → marked superseded; kept for history, never cited as current.
- **A referenced file that isn't here.** → missing-context log; the draft flags it rather than
  inventing a rent roll.
