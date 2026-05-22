# Stage 02: Diligence

## Purpose
Underwrite the deal in full and verify the thesis against real data. Work from the investment thesis, not from the offering memo. The sourcing stage already did the translation from "what the seller says" to "what we need to prove."

## Inputs
- **_config/investment-thesis.md**: The working specification. What you are buying, the business plan, the conditions that must hold.
- **01_sourcing/output/screen-memo.md**: The quick underwrite and identified deal breakers.
- **_references/** (selectively): Underwriting standards, market comps, prior deals on similar assets.
- **Data room and third-party reports**: Rent roll, trailing financials, leases, PCA, environmental, appraisal, title.

## Process
1. If the data room is unvetted, run a provenance pass first (Constraint 10). Inventory and rank every file by relevance and authority, flag exact and near-duplicates and version families, surface conflicts between sources, and list what is missing. Underwrite from the authoritative version of each document, not from the whole dump. The pass classifies and flags; it does not reconcile figures (Constraint 09).
2. Read the thesis and screen memo. Confirm the conditions that must hold and the deal breakers to test.
3. Plan diligence. List the workstreams (financial, physical, legal, market) and their dependencies.
4. Build the full underwrite. Replace the back-of-envelope model with a real one driven by the rent roll, leases, and verified expenses.
5. Verify each condition from the thesis against actual data. Confirmed, contradicted, or unresolved.
6. Run the deal breakers to ground. Each one is either cleared or it is not.
7. Maintain a risk register as findings come in.
8. Write output.

## Output
Write to: 02_diligence/output/

Two files: an underwriting model summary and a diligence summary. The model itself is built in
a spreadsheet or the platform's calculation engine, not by the model in prose. What you write
here is the **summary of** that underwrite, structured so IC can read it. The figures trace to
the model; AI summarizes, it does not compute. (See Constraint 09.)

```
# Underwriting Summary: [Deal Name]

## Basis and Assumptions
[Rent roll, in-place vs. market rents, expense assumptions, financing terms.
 Source each. State the as-of date.]

## Going-In and Stabilized
[Going-in NOI and cap rate. Stabilized NOI and the plan to get there.
 The figures come from the model; reference it.]

## Returns
[Levered IRR, equity multiple, hold period. Note the model file and version
 these come from. Do not recompute them here.]

## Sensitivities
[How returns move if the key variables miss: rent growth, exit cap, hold.
 The model runs these; summarize the result.]
```

Plus a diligence summary:

```
# Diligence Summary: [Deal Name]

## Workstreams Completed
[Financial, physical, legal, market. Status each: complete / partial / blocked.]

## Thesis Conditions
[For each condition in investment-thesis.md: confirmed / contradicted /
 unresolved. If contradicted, explain the impact on returns.]

## Underwriting vs. Screen
[How the full underwrite compares to the sourcing-stage numbers.
 Where reality diverged from the back-of-envelope, and why.]

## Risk Register
[Open risks, severity, mitigation or contingency. The items IC
 needs to weigh.]

## Retrade or Walk
[If findings change the price or kill the deal, say so here with
 the supporting numbers.]
```

## Done Looks Like
Every thesis condition has been tested against real data. The full underwrite is built and reconciled against the screen. The risk register is current. Ready for IC.

## Common Failure Modes
- **Underwriting to the offering memo instead of the thesis.** The OM is the seller's case. The thesis is what sourcing determined you need to prove. Underwrite the thesis.
- **Scope creep in diligence.** If you discover the deal needs a different business plan than scoped, that is a thesis change. Document it, escalate it, revise the thesis. Do not quietly re-underwrite to a new story without saying so.
- **Confirmation bias.** Diligence exists to break the thesis, not to justify the deal you already want to do. If a deal breaker is real, surface it loudly. The cheapest deal to walk from is the one you have not closed.

## Layer Annotation
L2 stage contract. Thesis and screen memo are L4 (deal-specific, though the thesis is also in _config/ for convenience). Underwriting standards and comps from _references/ are L3. Data room materials are L4.
