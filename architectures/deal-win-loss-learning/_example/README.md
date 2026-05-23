# Worked Example: A Running Deal-Win/Loss-Learning Loop

This folder is a fully instantiated copy of the deal-win-loss-learning workspace, populated for a
fictional firm so you can see what the loop looks like once it has been run a few times. The
reference architecture one level up (`../`) ships empty on purpose — you copy and fill it. This
example shows the filled result and, crucially, a store with more than one record, because the
whole point of the loop is what emerges across records.

## The fictional setup
**Ridgeline Capital Partners** is a value-add CRE GP (multifamily and industrial). The acquisitions
team runs the win/loss loop each time a competitive process resolves — won or lost. The store below
holds three resolved processes; one of them (Larkspur Apartments) is shown running through all
three stages so you can follow a single pass end to end.

## What to look at, in order
1. **`_config/`** — the filled reference files. Note that `win-loss-questions.md` is a fixed set
   answered the same way every time; that fixed set is what makes the three records comparable.
2. **A single pass (Larkspur Apartments, lost):**
   - `01_signal/output/record-larkspur-apartments-2026-05-08.md` — the facts: our bid, the
     clearing price, our gap, and the broker's *stated* reason logged but not yet assessed.
   - `02_analysis/output/analysis-larkspur-apartments-2026-05-08.md` — the proposed "why," with
     the broker's stated reason held distinct from the assessed real reason and confidence marked.
   - `03_capture/output/captured-larkspur-apartments-2026-05-08.md` — the capture log: what a human
     validated and which patterns moved.
3. **The store (`_store/`)** — the deliverable:
   - `records/` holds three records (one industrial deal won on certainty, two deals lost where the
     broker cited price).
   - `patterns.md` is the payoff: the patterns visible *across* the three records, which no single
     bid could show. Read this last — it is the thing the next bid reads first.

## The lesson this example is meant to teach
A single record is nearly worthless. Three already suggest a pattern: at Ridgeline, deals are won
and lost on **certainty of close**, not top price — and twice the broker's "you were light on
price" masked a certainty driver that the bid structure revealed. That is exactly the trap the
loop's load-bearing Question 5 (stated vs. assessed reason) exists to catch: capture the broker's
polite "you were outbid" as the real reason and the store quietly teaches the firm to overbid on
price when the actual fix is a cleaner certainty package. The store is the product; the per-deal
records are its inputs.

Everything here is fictional and illustrative.
