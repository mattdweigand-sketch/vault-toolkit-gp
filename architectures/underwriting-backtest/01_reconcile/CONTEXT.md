# Stage 01: Reconcile

## Purpose
Assemble the factual variance record for a deal that has realized. Pull the assumptions the deal was approved on from the IC model of record, pull the realized actuals from fund accounting and the exit, and compute the gap — per material assumption and on the headline return — into a structured record the attribution stage can reason over. Facts and arithmetic in; the why comes later.

## Inputs
- **The trigger**: a deal has realized. Name the deal, the outcome lane (Outperformed / In-line / Underperformed vs. underwriting, or Interim-checkpoint as a flagged sub-case), and the realization date.
- **The approved IC model of record** (the deal system / model repository): the assumptions the deal was *approved* on — going-in cap, rent/revenue growth, opex growth, lease-up/absorption, exit cap, hold period, leverage/cost of debt, capex/renovation budget, terminal value, underwritten IRR/MOIC. Record the model version and date so the backtest measures against a fixed target, not a moving one.
- **Realized actuals** (fund accounting / the exit): the actual NOI trajectory, realized rents, actual exit price and cap, actual hold, realized IRR/MOIC, actual capex. From the system of record, not from memory.
- **_store/** (for context): any prior record in the same asset type, market, strategy, or vintage, and records sharing a decisive driver, so this record is assembled with awareness of what the store already knows.
- **_config/assumption-taxonomy.md**: to tag the deal per the controlled vocabulary, including the controlled list of assumption categories.

## Process
1. Confirm the trigger: which deal, which outcome lane, the realization date, and the model version of record.
2. Identify the **material** assumptions — the few that actually moved the return. A backtest that reconciles forty line items teaches nothing; name the handful that mattered.
3. For each material assumption, pull the underwritten value and the realized actual, and compute the gap — magnitude and direction. State the source of each actual.
4. Reconcile the headline return: underwritten IRR/MOIC vs. realized, and the gap. This is the arithmetic spine the attribution stage explains.
5. Tag the deal per the taxonomy: asset type, deal-size band, market/submarket, strategy, hold-period band, vintage year, outcome lane.
6. Note where the variance concentrates if visible from the numbers alone (e.g., "almost all of the IRR beat sits in the exit cap, not operations") — without yet explaining *why*.
7. Note what the record does not capture — gaps the attribution stage should know about (an actual not yet final, a mid-hold event like a refinance, an assumption the model never isolated).
8. Produce the variance record. State numbers and their source. Do not attribute.

## Output
Write to: 01_reconcile/output/record-[deal]-[date].md

Format:
```
# Variance Record: [Deal Name]
Outcome: [Outperformed / In-line / Underperformed / Interim-checkpoint]   Realized: [Date]
Model of record: [version, date approved at IC]
Asset type: [from taxonomy]   Deal-size band: [from taxonomy]   Strategy: [from taxonomy]
Market/submarket: [from taxonomy]   Hold-period band: [from taxonomy]   Vintage: [from taxonomy]

## Headline Return
[Underwritten IRR/MOIC vs. realized, and the gap. Source of the realized figure.]

## Material Assumptions: Underwritten vs. Actual
[Each material assumption: underwritten value | actual | gap (magnitude + direction).
 Source of each actual. Only the assumptions that moved the return.]

## Where the Variance Concentrates
[From the numbers alone: which assumption(s) account for most of the gap.
 Observation, not explanation.]

## Gaps
[What is not in the record that attribution should know about: an actual not
 final, a mid-hold refinance, an assumption the model never isolated.]
```

## Done Looks Like
A factual, source-grounded variance record — underwritten vs. actual on the material assumptions and the headline return, with the gaps computed and tagged by the taxonomy — that the attribution stage can work from without re-querying the model or fund accounting. No explanation of why — just what was assumed, what happened, and the difference.

## Common Failure Modes
- **Recomputing or estimating actuals.** Fund accounting and the exit are the source. An IRR reconstructed from impression, or an actual the model "estimates" because the real figure is inconvenient to pull, is exactly the unreliable input that would corrupt the attribution and then the store. Pull it; do not recall or estimate it.
- **Measuring against the wrong model.** Backtesting against a model revised mid-hold measures nothing — the target moved. Use the assumptions the deal was *approved* on at IC, and record the version.
- **Reconciling everything.** The job is the handful of assumptions that moved the return, not every line in the model. Forty reconciled inputs bury the two that mattered.
- **Attributing early.** The job is assembly and arithmetic. An early "why" shapes the record and undermines the comparability the whole workspace depends on.

## Layer Annotation
L2 stage contract. The approved model, realized actuals, and computed variance are L4 (this run). The store is read here for context (its L3-like role). The assumption taxonomy from _config/ is L3.
