# Stage 01: Sourcing

## Purpose
Understand what the deal actually is, not just what the broker is selling. Produce an investment thesis and a screen memo that the diligence stage can work from. This stage is the foundation of the whole deal. Time invested here saves multiples in diligence and protects you from chasing a deal that never penciled.

## Inputs
- **_config/deal-brief.md**: The original opportunity. Offering memo, teaser, broker email.
- **_config/deal-terms.md**: Asking price, structure, key dates.
- **Market data, rent rolls, comps**: Paste figures or notes here.
- **_references/** (selectively): Prior deals on similar assets, underwriting standards.

## Process
1. Read the offering memo and deal terms.
2. Identify the seller's pitch (what the OM says) and form your own view (what the asset and market actually support).
3. List what you know, what you assume, and what you need to find out. This three-column analysis is the backbone of sourcing.
4. Build a back-of-envelope underwrite. Going-in cap rate, stabilized yield, basis per unit or per square foot against comps. Does the story hold before you spend a dollar on diligence?
5. Identify the two or three things that would break the deal. If any are likely true, stop here.
6. Synthesize into a screen memo.
7. Draft the investment thesis: what you are buying, why it wins, the business plan, the return target, and the conditions that have to hold.
8. Get a go/no-go decision before committing diligence spend.

## Output
Write to: 01_sourcing/output/

Two files:

**screen-memo.md:**
```
# Screen Memo: [Deal Name]

## The Pitch
[What the seller/broker is presenting, in their framing.]

## Our View
[Your assessment. What the asset and market actually support.]

## Quick Underwrite
[Going-in cap, stabilized yield, basis vs. comps, target return.
Rough numbers. Enough to decide whether to spend diligence dollars.]

## Deal Breakers
[The two or three things that would kill this deal. Be specific.
If any are likely true, this is a no-go.]

## Recommendation
[Go / no-go on diligence, with the reason in one line.]
```

**investment-thesis.md:**
```
# Investment Thesis: [Deal Name]

## What We Are Buying
[Asset, location, size, current state.]

## Why It Wins
[The thesis in plain terms. Mispriced basis, value-add business plan,
market tailwind, off-market access. What is the edge?]

## Business Plan
[What you will do with the asset. Lease-up, reposition, refinance,
hold-and-distribute. Timeline and major milestones.]

## Return Target
[Target IRR, equity multiple, hold period. The math the thesis rests on.]

## Conditions That Must Hold
[The assumptions the thesis depends on. If one breaks in diligence,
the thesis changes. Make these explicit.]
```

Also copy the investment thesis to _config/investment-thesis.md so all subsequent stages can reference it.

## Done Looks Like
The deal has a go decision. The investment thesis captures not just the seller's pitch but your own underwrite and the conditions the deal depends on. Diligence can start without ambiguity about what "win" means on this deal.

## Layer Annotation
L2 stage contract. Deal brief and terms from _config/ are L3. Market data and comps pasted in are L4. Underwriting standards from _references/ are L3.
