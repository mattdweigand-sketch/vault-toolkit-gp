# Stage 03: Investment Committee

## Purpose
Evaluate the underwriting against standards and the thesis, then take the deal to committee. This stage happens in two phases: internal review first, then the committee. Never put a deal in front of the IC that has not survived internal review.

## Inputs
- **02_diligence/output/**: Underwriting, findings, risk register.
- **_config/investment-thesis.md**: The thesis the deal has to satisfy.
- **01_sourcing/output/screen-memo.md**: The original deal breakers and quick underwrite.
- **Underwriting standards** (if you have them in _references/): The firm's return hurdles and credit box.

## Process

### Phase 1: Internal Review
1. Read the underwriting and findings.
2. Check against the firm's standards. Return hurdles, leverage limits, concentration rules. Pass/fail each.
3. Check against the thesis. Did diligence confirm the conditions that must hold?
4. Work the risk register. Investigate any unresolved or high-severity item.
5. Produce an internal review document. If issues found, return to diligence with specific, actionable items. Do not send vague feedback like "tighten the model." Specify what needs to change and why.

### Phase 2: Investment Committee
6. Once internal review passes, prepare the IC memo.
7. Write the memo for the committee: the thesis, the underwrite, the risks, the recommendation, and the specific approval being requested (price, structure, equity).
8. Present to committee. Document every question and condition.
9. Categorize committee feedback: in-scope condition (goes back to diligence), structural change (re-underwrite), approve as-is.

## Output
Write to: 03_ic/output/

**review-internal.md** (after phase 1):
```
# Internal Review: [Deal Name]

## Standards Check
[For each hurdle/limit: pass / fail with explanation]

## Thesis Confirmation
[For each condition: confirmed / contradicted / unresolved]

## Issues for Diligence
[Specific, actionable items to resolve. Reference exact figures
or reports.]

## Approved for IC: [Yes / No - return to diligence]
```

**ic-memo.md** (for committee, before phase 2):
```
# IC Memo: [Deal Name]

## Recommendation
[The ask in one line: approve [equity check] for [deal] at [price/structure].]

## Thesis
[Why this deal, in the firm's terms. The conditions that must hold,
carried forward from sourcing and confirmed in diligence.]

## The Underwrite
[Headline returns against the firm's hurdles, the basis, the leverage
and structure. Figures tie to 02_diligence/output/; do not restate or
recompute a return here.]

## Key Risks
[The risks that survived diligence, each with its mitigant or the
reason it is acceptable. Pull from the risk register; do not bury a
high-severity item.]

## The Approval Requested
[Exactly what the committee is being asked to authorize: price,
structure, equity check, and any pre-approved range or conditions.]
```

**ic-decision.md** (after phase 2):
```
# IC Decision: [Deal Name]

## Conditions and Questions
[Numbered list. For each item:
 - What the committee raised
 - Category: diligence condition / structural change / cosmetic
 - Action: return to diligence / re-underwrite / proceed]

## Approval
[What was approved: price, structure, equity check. Any conditions
to close.]

## Approved for Close: [Yes / No - conditions required]
```

## Done Looks Like
The committee has reviewed the deal and either approved it for close or returned it with specific conditions that have been scoped. There is no ambiguity about what was approved and what still has to clear.

## Common Failure Modes
- **Taking a deal to committee before internal review passes.** The two phases exist precisely so a half-finished underwrite never reaches the committee room. Internal review is a gate, not a formality — under deadline pressure it is the first thing teams are tempted to skip.
- **Vague feedback to diligence.** "Tighten the model" sends the deal in a circle. Name the figure, the assumption, or the report that has to change, and why. Actionable return notes are the difference between one more diligence pass and three.
- **Burying a high-severity risk in the memo.** The IC memo must surface every risk that survived diligence with its mitigant. A material risk the committee discovers on its own costs more in credibility than the risk itself.

## Layer Annotation
L2 stage contract. Diligence output is L4. Thesis and screen memo are L4 (deal-specific). Underwriting standards are L3 (stable across deals).
