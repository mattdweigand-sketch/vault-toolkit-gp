# Worked Example: A Running Underwriting-Backtest Loop

This folder is a fully instantiated copy of the underwriting-backtest workspace, populated for a
fictional firm so you can see what the loop looks like once it has been run a few times. The
reference architecture one level up (`../`) ships empty on purpose — you copy and fill it. This
example shows the filled result and, crucially, a store with more than one record, because the
whole point of the loop is what emerges across records.

## The fictional setup
**Ridgeline Capital Partners** is a value-add CRE GP (multifamily, industrial, and mixed-use) — the same firm
used in the firm-memory-loop pattern, here running the specialized underwriting calibration loop. The deal team
runs the backtest each time a deal realizes. The store below holds three realized deals; one of
them (Cedar Crossing Apartments) is shown running through all three stages so you can follow a
single pass end to end.

## What to look at, in order
1. **`_config/`** — the filled reference files. Note that `underwriting-questions.md` is a fixed
   set answered the same way every time; that fixed set is what makes the three records comparable.
2. **A single pass (Cedar Crossing Apartments, outperformed):**
   - `01_reconcile/output/record-cedar-crossing-2024-09-12.md` — the facts: underwritten vs.
     actual on each material assumption and the headline return, with the variance computed. No
     explanation yet.
   - `02_attribution/output/analysis-cedar-crossing-2024-09-12.md` — the proposed "why," with the
     firm's skill held distinct from market luck and confidence marked.
   - `03_capture/output/captured-cedar-crossing-2024-09-12.md` — the capture log: what a human
     validated and which calibration patterns moved.
3. **The store (`_store/`)** — the deliverable:
   - `records/` holds three records (two multifamily deals and one industrial, all "outperformed"
     on IRR).
   - `patterns.md` is the payoff: the calibration visible *across* the three records, which no
     single backtest could show. Read this last — it is the thing the next underwrite reads first.

## The lesson this example is meant to teach
A single backtest is nearly worthless. Three already separate two very different stories that the
headline IRRs hide. Every deal "beat" its underwriting — but the beat was dominated by **exit-cap
compression Ridgeline did not underwrite and did not create**, while their **multifamily lease-up
assumptions ran 6–10 months optimistic on both multifamily deals** — an emerging pattern the store
flags but has not yet promoted to a stated bias. That is exactly the trap the loop's load-bearing
Question 5 (skill vs. luck) exists to catch: bank the cap-compression beat as proof the firm
underwrites brilliantly, and the store quietly teaches it to keep assuming a tailwind that may not
return — while the real, correctable bias (slow lease-up) goes unfixed. The store is the product;
the per-deal records are its inputs.

Everything here is fictional and illustrative.
