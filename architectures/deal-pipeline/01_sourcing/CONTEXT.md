# Stage 01: Sourcing

## Purpose
Understand what the deal actually is, not just what the broker is selling, and produce the investment thesis the diligence stage works from. This stage is the foundation of the whole deal. Time invested here saves multiples in diligence and protects you from chasing a deal that never penciled.

**Where this stage starts depends on how the deal arrived.** If it came through the deal-screening workspace, the screen is already done — start from the handoff brief and go straight to the thesis. If it came in directly (off-market, relationship-sourced, never screened), run the screen here first, then build the thesis. Do not re-screen a deal screening already cleared; that work is the handoff's whole point.

## Inputs
- **_config/deal-brief.md**: The original opportunity. Offering memo, teaser, broker email. For a screened deal, this is the deal-screening handoff brief (snapshot, fit assessment, screen rationale, rough economics, open questions) carried in from that workspace.
- **_config/deal-terms.md**: Asking price, structure, key dates.
- **Market data, rent rolls, comps**: Paste figures or notes here.
- **_references/** (selectively): Prior deals on similar assets, underwriting standards.

## Process
1. Read the inputs. For a screened deal, read the handoff brief — the pitch-vs-view, the rough economics, and the screen rationale are already in it; treat it as the starting point, not a draft to redo. For an unscreened deal, read the offering memo and deal terms cold.
2. **Produce the screen memo.** It captures the pitch-vs-view, the quick underwrite, and the two or three deal-specific things that would kill *this* deal in diligence — the inputs the diligence and IC stages later test against. The work differs by entry path:
   - *Unscreened deal:* build it from scratch — seller's pitch vs. your own view, a back-of-envelope underwrite (going-in cap, stabilized yield, basis vs. comps), and the deal-breakers. If any breaker is likely true, stop here.
   - *Screened deal:* do **not** redo deal-screening's box-fit screen (asset type, market, size — already settled in the handoff). Seed the screen memo from the handoff's rough economics and rationale, then add the forward piece the handoff does not carry: the deal-specific risks diligence must test, and a confirmation that the quick underwrite still holds.
3. List what you know, what you assume, and what you need to find out. This three-column analysis is the backbone of the thesis.
4. Pressure-test the carried-over (or just-built) underwrite against your own read. Does the story hold before you spend a dollar on diligence?
5. Draft the investment thesis: what you are buying, why it wins, the business plan, the return target, and the conditions that have to hold.
6. Get a go/no-go decision before committing diligence spend.

## Output
Write to: 01_sourcing/output/

Two files, both produced every time. The **screen memo** is written from scratch for an unscreened deal and seeded from the deal-screening handoff for a screened one — either way it ends up in `output/screen-memo.md` with the quick underwrite and the deal-specific deal-breakers, because the diligence and IC stages read it from there. The **investment thesis** is the required deliverable the rest of the deal works from.

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

## Common Failure Modes
- **Paraphrasing the pitch as your own view.** "Our View" has to be an independent read of what the asset and market support, not a reworded OM. If the two sections say the same thing, you have not done the sourcing work.
- **Suppressing the deal breakers to keep the deal alive.** The whole point of this stage is to find the two or three things that kill the deal cheaply, before diligence spend. Burying them to justify a "go" is the most expensive mistake in the pipeline.
- **Anchoring the thesis to the asking price.** The quick underwrite tests whether the story pencils on its own; it should not reverse-engineer a return to fit the seller's number. If the deal only works at the asking price, that is a finding, not a thesis.
- **Re-screening a deal that came through deal-screening.** If the handoff brief is in hand, the box-fit screen is done — carry its pitch-vs-view, rough economics, and rationale forward rather than rebuilding them from the OM. Spend the freed time on the thesis and on the deal-specific risks diligence will test, not on re-deciding whether the deal fits the box (the handoff already settled that).

## Layer Annotation
L2 stage contract. Deal brief and terms from _config/ are L3. Market data and comps pasted in are L4. Underwriting standards from _references/ are L3.
