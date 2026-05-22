# Stage 04: Close

## Purpose
Execute the approved transaction and ensure asset management can run the business plan from day one. Close is not just wiring funds. It includes the closing checklist, funding confirmation, and the handoff to asset management. The goal is that the asset manager never has to ask "what did we actually buy and why?"

## Inputs
- **03_ic/output/**: Approved IC memo and conditions.
- **_config/investment-thesis.md**: For final verification that the deal as closing still matches the approved thesis.
- **_config/deal-terms.md**: For closing mechanics (key dates, escrow, prorations, conditions to close).

## Process
1. Clear every condition to close from the IC decision. Track each to resolution.
2. Compile the closing checklist. Title, escrow, loan documents, equity funding, insurance, prorations, estoppels.
3. Confirm funding. Equity called, debt drawn, purchase price wired, settlement statement reconciled.
4. Build the asset management handoff: the business plan, the model, key dates, lender covenants, and the first 90-day action list.
5. Package everything so the asset manager opening this six months from now understands the deal without calling the deal team.
6. Archive the deal workspace for future reference.

## Output
Write to: 04_close/output/

**closing-package/** (folder containing):
- Executed documents index
- closing-checklist.md
- am-handoff.md

**closing-checklist.md:**
```
# Closing Checklist: [Deal Name]

## Conditions to Close
[Each IC condition: cleared / outstanding, with date and owner.]

## Closing Items
[Title, escrow, loan docs, equity funding, insurance, prorations.
Status each.]

## Funding Confirmation
[Equity called, debt drawn, price wired, settlement statement
reconciled. Final closing date.]
```

**am-handoff.md:**
```
# Asset Management Handoff: [Deal Name]

## What We Bought
[Asset, basis, structure, capital stack. The deal in plain terms.]

## The Business Plan
[What we are doing with the asset and the return target it has to hit.
Written for the person operating it daily, not the person who closed it.]

## Key Dates and Covenants
[Lender covenants, reporting dates, lease expirations, refinance window,
hold-period milestones.]

## First 90 Days
[The action list the asset manager owns out of the gate.]
```

**deal-record.md:**
```
# Deal Record: [Deal Name]

Asset: [Name, location]
Closed: [Date]
Basis / Structure: [Price, equity, debt]
Key decisions: [Major calls made during the deal and why]
Lessons learned: [What would you do differently next time?]
Follow-up: [Open items, pending conditions, asset management commitments]
```

## Done Looks Like
The deal has funded, every condition is cleared, and asset management has the business plan, the model, and the first 90-day list. You have a deal record that captures the knowledge from this transaction for the next similar deal.

## Common Failure Modes
- **Funding without a handoff.** The wire is the close. The handoff is what makes the asset perform. Without it, asset management spends month one reverse-engineering the deal team's thinking.
- **Writing the handoff for the deal team instead of the operator.** Deal-team shorthand assumes context the asset manager does not have. Write for the operator.
- **Skipping the deal record.** This is for you and the firm, not a counterparty. It captures lessons and institutional memory. Without it, the next similar deal starts from scratch instead of building on what you learned.

> Cross-link: if this was a competitive process, its resolution (won, or — for a deal that did not close here — lost) is the trigger for the `deal-win-loss-learning` loop. The deal record's lessons-learned and the clearing price feed that workspace's `01_signal` stage.

## Layer Annotation
L2 stage contract. Approved IC output is L4. Thesis and deal terms from _config/ are L3.
