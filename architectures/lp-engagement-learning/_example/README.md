# Worked Example: A Running LP-Engagement-Learning Loop

This folder is a fully instantiated copy of the lp-engagement-learning workspace, populated for a
fictional firm so you can see what the loop looks like once it has been run a few times. The
reference architecture one level up (`../`) ships empty on purpose — you copy and fill it. This
example shows the filled result and, crucially, a store with more than one record, because the
whole point of the loop is what emerges across records.

## The fictional setup
**Meridian Real Estate Partners** is raising **Fund III**, a value-add multifamily fund. The IR
team runs the engagement-learning loop each time an LP commits or passes. The store below holds
three resolved engagements; one of them (Cedarline Endowment) is shown running through all three
stages so you can follow a single pass end to end.

## What to look at, in order
1. **`_config/`** — the filled reference files. Note that `debrief-questions.md` is a fixed set
   answered the same way every time; that fixed set is what makes the three records comparable.
2. **A single pass (Cedarline Endowment, passed):**
   - `01_signal/output/record-cedarline-endowment-2026-05-10.md` — the facts, from the CRM.
   - `02_analysis/output/analysis-cedarline-endowment-2026-05-10.md` — the proposed "why,"
     with evidence and inference kept separate and confidence marked.
   - `03_capture/output/captured-cedarline-endowment-2026-05-10.md` — the capture log: what a
     human validated and which patterns moved.
3. **The store (`_store/`)** — the deliverable:
   - `records/` holds three records (one cold endowment that passed, one pension re-up that
     committed, one referred family office that committed).
   - `patterns.md` is the payoff: the patterns visible *across* the three records, which no
     single engagement could show. Read this last — it is the thing the next raise reads first.

## The lesson this example is meant to teach
A single record is nearly worthless. Three already suggest a pattern: at Meridian, warm/referred
LPs are converting while cold-sourced institutions stall on the GP-commitment and fee questions,
and reaching the real decision-maker early tracks with commitment. That is intelligence the CRM
does not produce and a single debrief could not reveal. The store is the product; the per-LP
records are its inputs.

Everything here is fictional and illustrative.
