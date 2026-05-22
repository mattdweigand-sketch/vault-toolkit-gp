# Stage 01: Data

## Purpose
Gather, organize, and verify the operating data for the review period. The output is a verified data pack the review stage can analyze from directly, without opening a property-system export. Every figure traces to its source.

## Inputs
- **Review brief**: What this cycle covers. Period, which assets or portfolio segments. Provide this when you enter the stage.
- **Property-system exports** (Yardi / MRI / RealPage): NOI, revenue, expenses, occupancy, leasing activity, delinquency, budget-vs-actual.
- **Rent roll**: Current tenancy, lease expirations, in-place vs. market rents.
- **Debt service / loan data** (if monitored here): debt service, reserves, covenant-relevant figures.
- **Prior-period data pack** (from a prior cycle): for continuity and trend.

## Process
1. Pull the operating data for the period. If more than one version of an export exists, confirm which is authoritative before pulling — never blend figures across versions (Constraint 10).
2. Identify the figures the review needs per asset: NOI, revenue and expense lines, occupancy, leasing activity, budget-vs-actual, delinquency.
3. Reconcile each figure to its source export. A figure that cannot be tied to a system export does not enter the pack.
4. Compute period-over-period and actual-vs-budget movements at the data level (these are arithmetic from the source, not modeled returns). Note anything that moved materially.
5. Flag any figure that is preliminary, estimated, or subject to a later true-up. The flag travels with it.
6. Produce the verified data pack.

## Output
Write to: 01_data/output/data-pack-[period].md

Format:
```
# Asset Data Pack: [Portfolio / Asset] [Period]

## Per-Asset Operating Figures
[Per asset: NOI, revenue, opex, occupancy, leasing activity, delinquency.
 Each with its source export and a tie-out note. As-of date.]

## Actual vs. Budget
[Per asset, the period actual against budget, at the line level.
 Arithmetic from source, not a modeled return.]

## Movements vs. Prior Period
[What changed materially since last period and the source figures behind it.]

## Flags
[Preliminary, estimated, or subject-to-true-up figures.]

## Reconciliation Status
[Tied to source: yes / no per asset. Nothing reaches the review stage
 marked "no."]
```

## Done Looks Like
A data pack where every operating figure ties to its system source and material movements are surfaced. If the analyst in stage 02 has to open a Yardi export to check a number, this stage did not finish its job.

## Common Failure Modes
- **Blending versions.** A revised export and an original with different occupancy figures must not be mixed. Confirm the authoritative version (Constraint 10).
- **Computing a return here.** This stage assembles operating actuals. IRR, equity multiple, and valuation are modeled elsewhere (Constraint 09). Do not produce them here.
- **Loading the whole portfolio when the review is one asset.** Pull only what this cycle's scope needs. A clean pack analyzes better than a comprehensive, noisy one.

## Layer Annotation
L2 stage contract. The property-system exports and rent roll loaded here are L4 (this cycle). The prior-period pack is L4. Business-plan targets live in _config/ and are L3 (loaded in stage 02, not here).
