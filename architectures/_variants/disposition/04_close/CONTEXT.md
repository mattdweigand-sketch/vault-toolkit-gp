# Stage 04: Close

## Purpose
Evaluate the offers, select the buyer, execute the sale to close, and hand off the capital return and the investor narrative. The disposition does not end at the wire — it ends when the exit is cleanly reflected to LPs.

## Inputs
- **03_market/output/**: The launched process and the incoming offers.
- **_config/disposition-standards.md**: Selection and approval gates.
- **Final terms**: the selected PSA terms, the net-proceeds figure from the model/closing statement.

## Process
1. Evaluate the offers: price, certainty of close, buyer track record, contingencies, timeline. Build a clear comparison.
2. Recommend a buyer with rationale; the IC or the authorized approver selects. Price is not the only axis — certainty and speed often matter as much.
3. Manage the transaction to close: PSA, buyer diligence, conditions, the closing checklist. Track open items to resolution.
4. Confirm the net proceeds and the capital-return figures — from the closing statement and the platform, not computed here (Constraint 09).
5. Hand off the capital return to your fund administration (the platform and fund-admin team run the distribution mechanics) and the exit narrative to LP reporting (how the realization is communicated). Provide each what it needs.
6. Record the close.

## Output
Write to: 04_close/output/

```
# Disposition Close Record: [Asset]
Market reference: 03_market/output/

## Offer Evaluation & Selection
[The offer comparison and the selection rationale. Who approved, when.]

## Closing
[Close date, final price, the closing checklist status, resolved conditions.]

## Capital Return Handoff
[Net proceeds (sourced to the closing statement / platform). What fund
 operations needs for the distribution; what LP reporting needs for the
 realization narrative. The figures are the platform's; this is the handoff.]

## Outcome vs. Underwriting
[Realized result against the original acquisition thesis — a natural feed
 into the firm's learning. Qualitative; the realized return is the model's.]
```

## Done Looks Like
A closed sale, a recorded selection rationale, and clean handoffs: fund administration has what it needs to return capital, LP reporting has what it needs to communicate the realization. The exit is reflected to investors, not just executed.

## Common Failure Modes
- **Selecting on price alone.** The highest offer that does not close is worth less than a certain one. Weigh certainty and speed; document why the chosen offer won.
- **Computing the return or the distribution here.** Net proceeds and the realized return come from the closing statement, the model, and the platform. This stage hands them off; it does not produce them (Constraint 09).
- **No handoff to fund administration and LP reporting.** A close that is not handed off leaves the capital return and the investor communication to improvise. Package both before declaring done.

## Layer Annotation
L2 stage contract. The offers and final terms are L4. Disposition standards from _config/ are L3. The capital-return handoff connects to your fund-administration platform and the lp-reporting workspace.
