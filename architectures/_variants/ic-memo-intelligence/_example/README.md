# Worked Example: A Running IC-Memo-Intelligence Loop

This folder is a fully instantiated copy of the ic-memo-intelligence workspace, populated for a
fictional firm so you can see what the loop looks like once it has been run a few times. The
reference architecture one level up (`../`) ships empty on purpose — you copy and fill it. This
example shows the filled result and, crucially, a store with more than one record, because the
whole point of the loop is what emerges across records.

## The fictional setup
**Ridgeline Capital Partners** is a value-add CRE GP (multifamily, industrial, and mixed-use) — the same firm
used in the deal-win-loss-learning and underwriting-backtest examples, here running the IC-decision
loop. The deal team captures a record each time a deal is decided at IC. The store below holds three
decisions; one of them (Cedar Crossing Apartments) is shown running through all three stages so you
can follow a single pass end to end.

> **A note on the shared deals.** Cedar Crossing and Maple Grove also appear in the
> underwriting-backtest example as *realized* deals. Here you see the same two deals years earlier,
> at the moment the IC *approved* them. Stonebridge was *declined*, so it never realized and never
> enters the backtest store — a clean illustration that the two loops capture different moments in a
> deal's life: this one at the decision, the backtest one at the exit.

## What to look at, in order
1. **`_config/`** — the filled reference files. Note that `ic-questions.md` is a fixed set answered
   the same way every time; that fixed set is what makes the three records comparable.
2. **A single pass (Cedar Crossing Apartments, approved-with-conditions):**
   - `01_record/output/record-cedar-crossing-2019-06-04.md` — the facts: what was recommended vs.
     decided, the conditions, concerns, dissent, and vote, transcribed from the memo and minutes. No
     reading yet.
   - `02_analysis/output/analysis-cedar-crossing-2019-06-04.md` — the proposed reading, with the
     committee's stated rationale held distinct from the inferred one and confidence marked.
   - `03_capture/output/captured-cedar-crossing-2019-06-04.md` — the capture log: what a human
     validated and which patterns moved.
3. **The store (`_store/`)** — the deliverable:
   - `records/` holds three records (two approvals-with-conditions and one decline, all value-add MF).
   - `patterns.md` is the payoff: the decision intelligence visible *across* the three records, which
     no single decision could show. Read this last — it is the thing the next memo author reads first.

## The lesson this example is meant to teach
A single IC decision tells you little. Three already reveal that this committee runs a hard leverage
line (~65% LTV; it declined Stonebridge at 72% on a compelling basis rather than stretch) and a
standing way of getting a value-add MF deal *through*: cap the leverage, condition a DSCR stress
test, and manage lease-up risk with a milestone rather than declining. A memo author who reads the
store pre-empts all of it — comes in at ≤65% LTV, builds in the DSCR stress and a lease-up milestone,
and addresses absorption head-on — instead of being sent back or declined.

It is also the trap the loop's load-bearing Question 5 (stated vs. inferred rationale) exists to
catch. Cedar Crossing's minutes say "approved on basis and sponsor track record." The inferred
reading is that the committee approved *despite* real doubts about the 12-month lease-up assumption,
which it offloaded into conditions. Capture the tidy minute version and the store quietly teaches
the firm the IC is more comfortable with aggressive lease-up than it actually is. The store is the
product; the per-decision records are its inputs.

Everything here is fictional and illustrative.
