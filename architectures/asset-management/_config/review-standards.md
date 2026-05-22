# Review Standards

<!--
ANNOTATION: What counts as "off plan," what triggers a watchlist flag, and the
materiality bars the review stage applies. Write these as testable thresholds,
not judgment calls, so the same variance gets flagged the same way every cycle
regardless of who runs the review. This is Constraint 04 (Session Consistency)
applied to analysis.

This is L3 reference, stable across cycles.
-->

## Materiality Thresholds
[What size of variance is worth flagging, by dimension. Examples:
- Occupancy: flag if more than [X] points behind plan
- NOI: flag if more than [X]% behind plan or budget
- Leasing pace: flag if more than [X] months behind schedule
- Expenses: flag if more than [X]% over budget
Set these so routine noise does not clutter the review and real drift does
not get buried.]

## Watchlist Criteria
[What puts an asset on the watchlist. Examples:
- Any structural (not timing) variance that threatens the business plan
- A covenant or debt-service concern (coordinate with the loan-covenant workspace)
- A material valuation risk
- Two consecutive periods behind plan on a key metric
For each, the recommended action template and the owner.]

## Variance Classification
[How to distinguish a timing variance (recoverable, expected to normalize) from
a structural one (the plan assumption was wrong). The review stage must label
which is which; this section defines the test.]

## Never-Do List
[Testable rules every review must pass. Examples:
- Never compute or restate a return, IRR, or valuation (Constraint 09).
- Never state an actual that does not tie to the data pack.
- Never put an asset on the watchlist without a cause and a recommended action.
- Never measure performance against last period when the standard is the plan.]
