# Decision Challenge Contract

## Purpose
Expose the fragile assumptions, missing evidence, and decision conditions in a decision packet.

## Inputs
- Decision packet.
- Verified facts or evidence map.
- Decision standards.
- Prior patterns or precedent.

## Process
1. Identify the proposed decision and what would change it.
2. Rank issues by decision impact.
3. Separate missing evidence from acceptable uncertainty.
4. Convert blockers into pre-decision work.
5. Convert residual risks into approval conditions, disclosures, or monitoring items.

## Outputs
- `challenge.md`
- `fragile_assumptions.md`
- `missing_evidence.md`
- `decision_conditions.md`

## Done Looks Like
The human decision owner has a short list of what must be resolved, what can be conditioned, and what should be monitored.

## Common Failure Modes
- Rewriting the memo instead of challenging it.
- Treating every concern as equally important.
- Confusing a condition with a blocker.

## Layer Annotation
L2 module contract. Challenge outputs are L4 artifacts for a human gate.
