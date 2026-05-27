# Stage 01: Position

## Purpose
Establish where the asset stands and surface the drivers for and against an exit — honestly, both sides — so the decision stage can make a real hold-vs-sell case rather than rationalize a foregone conclusion.

## Inputs
- **_config/asset-profile.md**: The asset, its original thesis, current business-plan status. Carried from asset-management where possible.
- **asset-management review** (if available): the latest business-plan-vs-actual analysis for this asset.
- **Model scenarios**: hold-vs-sell return scenarios from Argus or your model. Provided; not computed here (Constraint 09).
- **Broker BOV / value indications**: where available, the market's read on value.
- **Market and debt context**: the submarket window, the loan status (maturity, prepayment, assumability).

## Process
1. Summarize where the asset is against its original thesis and current business plan. What was achieved, what remains.
2. Lay out the value picture from the model scenarios and any BOV — as provided figures, sourced, not recomputed.
3. Surface the drivers *to sell*: business plan substantially complete, strong bid environment, a loan maturity, portfolio or fund-life considerations, a value peak.
4. Surface the drivers *to hold*: remaining upside in the plan, weak current market, tax or timing costs of selling, better risk-adjusted return in continuing.
5. Note the constraints that bound the decision: fund life and term, debt prepayment or maturity, partner/JV consent, tax considerations.
6. Produce the position assessment. Frame the decision; do not make it.

## Output
Write to: 01_position/output/position-assessment.md

Format:
```
# Position Assessment: [Asset]

## Standing vs. Plan
[Where the asset is against original thesis and current business plan.]

## Value Picture
[Model hold-vs-sell scenarios and BOV, as sourced figures. Note the model
 file/version and the BOV source. Not recomputed here.]

## Drivers to Sell
[The honest case for exiting now.]

## Drivers to Hold
[The honest case for continuing to hold.]

## Constraints
[Fund life, debt, consents, tax — what bounds the decision.]
```

## Done Looks Like
A balanced assessment that frames both sides of the hold/sell question with sourced figures and the binding constraints, ready for the decision stage to build the case. Neither side pre-judged.

## Common Failure Modes
- **Building only the sell case.** If position surfaces only reasons to sell, the decision is already made and the stage failed. The hold drivers must be as real as the sell drivers.
- **Recomputing the return.** The hold-vs-sell delta comes from the model. This stage presents it; it does not generate it (Constraint 09).
- **Ignoring the constraints.** A compelling sell case that runs into a prepayment penalty or a partner consent it cannot get is not a clean exit. Surface the constraints up front.

## Layer Annotation
L2 stage contract. The asset profile is L3 (also in _config/). The asset-management review, model scenarios, and BOV are L4 (this asset, this evaluation).
