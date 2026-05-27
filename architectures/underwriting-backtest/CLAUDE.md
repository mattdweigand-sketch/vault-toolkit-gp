# Underwriting Backtest Workspace

## What This Is
A workspace for learning, systematically, why the firm's realized deals beat or missed the underwriting they were bought on — and turning that into calibrated future underwriting. When a deal realizes (an exit, a sale, a full capital return), this workspace assembles the factual variance between the assumptions the deal was approved on and what actually happened, runs a consistent forensic on *why* each material assumption missed, and captures a structured record into an accumulating store. The store is the point: over many records it reveals the firm's systematic underwriting biases — where the exit-cap assumption runs optimistic, where rent-growth prints hot, where lease-up takes longer than the model ever assumes — and, just as important, how much of the realized return was the firm's own skill versus a market tailwind it did not create. Built for a deal team, head of acquisitions, or investment committee that wants its underwriting to compound — sharper assumptions mean better-priced deals, a more honest track record, and a fundraising story backed by evidence — instead of repeating the same forecasting errors one deal at a time.

This is not a portfolio-accounting system and it does not produce the returns of record — fund accounting and your deal model own those numbers. This workspace does the one thing they do not: it explains *why* the realized result diverged from the underwriting, separates skill from luck, and remembers.

## A Different Shape: the Learning Loop
This is the flagship specialized instance of the **learning-loop** shape. Other workspaces often flow forward to a decision or deliverable. This one loops: its output is deposited into the workspace's own memory (`_store/`) and read back to inform future runs and future investment judgment. Three properties make it different:
- **The flow is circular.** `01_reconcile` and `02_attribution` read from the store for context; `03_capture` writes back to it. The output's destination is the system's own future input.
- **The deliverable is the store, not the per-run record.** A single backtest is nearly worthless alone. The asset is the accumulating corpus and the calibration patterns that emerge across it.
- **It is retrospective.** It is triggered by an outcome that already happened, and it exists to digest that outcome, not to produce a forward deliverable.

If you need the same loop for bid strategy, LP objections, or portfolio post-mortems, use `firm-memory-loop` and swap the config and taxonomy.

## Deterministic Core
This loop has a **deterministic core**: `01_reconcile` is largely a numeric variance computation — underwritten value minus actual, per assumption — and the store rolls up into a quantitative calibration table. That arithmetic is not an AI task (Constraint 06); it is a data join over the approved model and fund accounting. AI's job begins at `02_attribution`, where the *why* is judgment. Keep that line bright: the model never invents or estimates an actual, and it never recomputes a return it can source.

## Current State
- This is a reference architecture. The store is empty. A fully worked, populated copy lives in `_example/` — read it to see what the loop looks like after a few runs.
- To use: copy the folder, populate _config with your canonical underwriting questions, assumption taxonomy, and store schema, then run the loop each time a deal realizes.

## Structure
```
underwriting-backtest/
  CLAUDE.md              # You are here.
  CONTEXT.md             # Workflow routing. How the loop closes.
  01_reconcile/
    CONTEXT.md           # Stage contract: assemble the variance record — approved assumptions vs. realized actuals, gaps computed.
    output/              # The factual variance record for one realized deal.
  02_attribution/
    CONTEXT.md           # Stage contract: forensic on why each material assumption missed; skill vs. luck.
    output/              # The structured attribution for one deal.
  03_capture/
    CONTEXT.md           # Stage contract: validate the attribution, write to the store, update the calibration patterns.
    output/              # Capture log: what was written and which patterns moved.
  _config/               # Underwriting questions, assumption taxonomy, store schema.
  _store/                # THE ASSET. Accumulating records + the rolled-up calibration patterns.
  _example/              # A fully worked, populated run (Ridgeline Capital): one pass end-to-end + a 3-record store.
```

## How to Use
1. Read CONTEXT.md to understand how the loop closes.
2. Populate _config/ with your canonical underwriting questions, your assumption taxonomy (asset type, strategy, vintage, the controlled list of assumption categories you underwrite on), and your store schema.
3. When a deal realizes — exited, sold, or fully returned — start in 01_reconcile. Assemble the variance record from the **approved IC model of record** and the realized actuals from fund accounting / the exit. Compute the gap per assumption and on the headline return.
4. Move to 02_attribution. Run the forensic against the canonical questions so this record is comparable to every other, classifying each material miss as forecasting error / execution / exogenous, and keeping the firm's *skill* distinct from market *luck*.
5. Move to 03_capture. The underwriter / head of acquisitions / IC validates the attribution — especially the skill-vs-luck split — then the record is written to the store and the calibration patterns are updated.
6. Read `_store/patterns.md` before the next underwrite, before setting a going-in or exit-cap assumption, or whenever you tune the firm's standard assumptions — that is the loop paying off.

## Key Decisions
- **The store is the deliverable.** Treat the per-deal backtest as an input to the asset, not the asset. Resist the urge to make any single write-up perfect; invest instead in making records comparable so the corpus is queryable as a calibration table.
- **Comparability over richness.** Every record answers the same canonical questions from _config, in the same structure, tagged by the same taxonomy and the same controlled list of assumption categories. A pile of beautifully written but non-comparable post-mortems cannot reveal a systematic bias. This is Constraint 04 (Session Consistency) as the core design principle.
- **The approved model and fund accounting are the source; the model never invents the numbers.** The underwritten assumptions come from the IC-approved model of record; the actuals come from fund accounting and the realized exit. The model assembles and analyzes; it does not recall a return from memory or estimate an actual it could source. See Constraint 09.
- **Pin which model version is "the underwriting."** Measure against the assumptions the deal was *approved* on at IC, not a later revised model. Backtesting against a model that was quietly updated mid-hold measures nothing — the target moved. Record the model version and date in every record (Constraint 10).
- **Skill vs. luck is the load-bearing defense.** The single most damaging thing this workspace can do is credit a market tailwind — cap-rate compression, a rate move, a sector run — to the firm's own underwriting skill. That inflates confidence and quietly miscalibrates every future model, teaching the firm it is a better underwriter than the evidence supports. Two defenses: the canonical questions force the skill and luck portions of the return apart, and the human validation gate at capture stops an unvalidated attribution from entering the store. This is the analog of the win/loss sibling's stated-vs-assessed-reason defense.
- **The variance is arithmetic; the why is judgment.** Reconcile computes; attribution explains. If the model is "estimating" an actual or recomputing an IRR it could pull, it has left its lane (Constraint 06).
- **A human validates the attribution before it is captured.** The attribution is the model's proposed explanation. Causal claims about why a deal hit or missed — and especially the skill-vs-luck split — are exactly the thing that, if wrong, poisons the store. The underwriter / head of acquisitions / IC confirms the attribution before it becomes institutional memory.
- **The store feeds future investment work.** `_store/patterns.md` is meant to retune the firm's underwriting standards, screening assumptions, diligence questions, and IC pressure tests. The calibration produces concrete assumption adjustments, not just loose guidance.
- **Treat the store as sensitive.** It documents the firm's own systematic underwriting errors and the honest skill-vs-luck read on its track record. That is candid internal intelligence; handle and store accordingly, and be deliberate about what leaves this workspace.

## Constraints That Apply
Built against the GP Operating Toolkit. Most relevant: **04 (Session Consistency)** — the load-bearing one here, **10 (Source Provenance)** — the model of record and the actuals are sourced data, **03 (Context Hygiene)**, **08 (Handoff Readiness)**, and the universal **06 (Layer Triage)** and **09 (Platform Boundary)**.

## Modules Used
- `modules/validated-memory-store/CONTRACT.md`
- `modules/handoff-brief/CONTRACT.md`

## Layer Annotations
- CLAUDE.md: L0 (always loaded, orientation)
- CONTEXT.md: L1 (workflow routing)
- Stage CONTEXT.md files: L2 (stage contracts)
- _config/ files: L3 (reference: questions, taxonomy, schema)
- _store/ files: L3/L4 hybrid — persistent memory read by future runs (L3-like) and written each run (L4-like). This dual role is the signature of the learning-loop shape.
- The approved-model / fund-accounting / realized-exit data and per-run stage outputs: L4 (working artifacts)
