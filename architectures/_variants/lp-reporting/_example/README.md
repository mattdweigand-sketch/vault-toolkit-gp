# Worked Example: A Finished LP-Reporting Workspace

This folder is a fully instantiated copy of the lp-reporting workspace, populated for a
fictional fund so you can see what "done" looks like. The reference architecture one level
up (`../`) ships empty on purpose — you copy and fill it. This example shows the filled
result for one cycle.

**The fund:** Meridian Real Estate Partners, Fund II — a value-add multifamily fund.
**The cycle:** Q1 2026 quarterly letter.
**Everything here is invented.** The numbers, the assets, and the firm do not exist. Use the
shape, not the content.

## What to look at

- **`_config/`** — the three reference files, populated. This is what a customer's `_config`
  should look like after onboarding: real voice, real format rules, real constraints. Compare
  a customer's `_config` to these to judge whether onboarding actually filled them in.
- **`01_data/output/data-pack.md`** — the verified numbers, every figure sourced. The draft is
  written only from this.
- **`02_draft/output/draft-quarterly-letter-meridian-fund-ii-q1-2026.md`** — the letter written
  from the data pack, in the fund's voice, before the compliance and formatting pass.
- **`03_distribution/output/final-quarterly-letter-meridian-fund-ii-q1-2026.md`** — the same
  letter after the compliance pass and formatting, ready to send.

## How to use it during onboarding

When you reach step 5 of the Onboarding Complete checklist ("one stage run end to end"),
compare the customer's output to the matching file here. If their data pack has unsourced
figures, or their draft pulls a number that is not in their pack, or their final lacks the
disclosures their `constraints.md` requires, the workspace is not done. This example is the
target.
