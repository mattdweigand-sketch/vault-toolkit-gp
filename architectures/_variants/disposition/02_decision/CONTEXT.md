# Stage 02: Decision

## Purpose
Build the hold-vs-sell recommendation with a timing thesis, and take it through the investment committee. This is the fork: a hold exits the pipeline with a revisit trigger; a sell proceeds to market. The judgment heart of the workspace.

## Inputs
- **01_position/output/position-assessment.md**: The framed decision — both sides and the constraints.
- **_config/hold-sell-criteria.md**: The firm's framework for when to sell.
- **Model scenarios**: the hold-vs-sell return comparison, as provided figures.

## Process
1. Read the position assessment and the firm's hold/sell criteria.
2. Build the **hold case**: the return to continuing, the remaining upside, the risk of holding. Make it genuinely, not as a foil.
3. Build the **sell case**: the return to exiting now, the timing argument, the risk of waiting.
4. Construct the timing thesis. Disposition is as much *when* as *whether* — why now versus six months from now versus at plan completion. Ground it in the market window, the bid environment, and the constraints, not in a gut feel.
5. Form a recommendation against the criteria, with the decisive factors named. Where the model's delta is close, say so — a marginal return difference should not be dressed as conviction.
6. Prepare the IC materials. The committee decides; this stage gives them both cases and a recommendation.
7. Record the decision: hold (with the revisit trigger) or sell (with the timing thesis that carries into market).

## Output
Write to: 02_decision/output/

Two files — the case memo and the recorded decision:
```
# Hold/Sell Case: [Asset]
Position reference: 01_position/output/position-assessment.md

## Hold Case
[The real return and rationale for continuing to hold.]

## Sell Case
[The return and rationale for exiting now.]

## Timing Thesis
[Why now (or why a specified later trigger). The market and constraint
 logic behind the timing. Figures sourced to the model.]

## Recommendation
[Hold or sell, the decisive factors, and honest confidence given how
 close the model delta is.]
```
```
# IC Decision: [Asset]
Decision: [Hold / Sell]   Decided by: [committee], on [date]
If hold: revisit trigger — [date or condition].
If sell: timing thesis carried to market — [summary]. Conditions, if any.
```

## Done Looks Like
A decision the IC made on the strength of both cases, with a timing thesis if selling and a revisit trigger if holding. The recommendation's confidence is honest about how close the call was.

## Common Failure Modes
- **A hold case built to lose.** If the hold case is a token, the IC is not really deciding. Both cases must be argued in good faith.
- **Whether without when.** A sell decision with no timing thesis hands the market stage no strategy. Why now is part of the decision, not an afterthought.
- **Manufacturing conviction from a marginal delta.** When hold and sell returns are close, that is a real finding. Present it as close; do not inflate it to justify action.

## Layer Annotation
L2 stage contract. The position assessment is L4. Hold/sell criteria from _config/ are L3. Model scenarios are L4 (this evaluation).
