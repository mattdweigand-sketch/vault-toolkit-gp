# Stage 02: Synthesis

## Purpose
Form the thesis: the firm's defensible point of view on the question, built from the vetted research, with evidence and inference kept distinct and confidence marked. This is where data becomes a view the firm can act on.

## Inputs
- **01_research/output/research-pack-[market-or-sector]-[date].md**: The vetted, sourced inputs.
- **_config/research-standards.md**: What counts as supported, how to mark confidence, the never-do list.
- **_references/**: The prior thesis on this market, to compare against and to update rather than restart.

## Process
1. Read the research pack and the prior thesis. You are updating a view, not inventing one from scratch each cycle.
2. Form the core claim: the answer to the question, stated plainly. Where to play, or not, and the direction of conviction.
3. Lay out the support, separating two things explicitly:
   - **Evidence**: what the sourced data shows. Tagged to the pack.
   - **Inference**: the firm's read of what the evidence implies. Labeled as inference, with a confidence level.
   Conflating these is the cardinal error; keep them in separate, marked categories.
4. State what would have to be true for the thesis to hold, and the leading indicators to watch — so the thesis is falsifiable, not just assertive.
5. Build the risk case: the strongest argument against the thesis and what would break it.
6. Note where this thesis differs from the prior one and why the change.
7. Produce the synthesized thesis.

## Output
Write to: 02_synthesis/output/thesis-[market-or-sector]-[date].md

Format:
```
# Thesis (draft): [Market / Sector]
Research reference: 01_research/output/research-pack-[...]-[date].md

## The Claim
[The firm's point of view, stated plainly. The direction of conviction.]

## Evidence
[What the sourced data shows. Each point tagged to the research pack.]

## Inference
[The firm's read of what the evidence implies. Labeled as inference,
 each with a confidence level. Kept separate from evidence above.]

## What Would Have to Be True
[The conditions the thesis depends on, and the leading indicators to watch.]

## Risk Case
[The strongest argument against, and what would break the thesis.]

## Change vs. Prior Thesis
[What is different from the last view on this market, and why.]
```

## Done Looks Like
A thesis that commits to a view, shows its evidence and its inference separately with confidence marked, states what would have to be true, and argues its own risk case. A reader can see exactly where the conviction rests and what would change it.

## Common Failure Modes
- **Inference smuggled in as evidence.** "The market is undersupplied" (a read) stated like "vacancy is 4%" (a datum). Label every inference; this is the discipline the whole stage exists for.
- **A view with no falsification.** A thesis that cannot be wrong cannot guide. State what would have to be true and what would break it.
- **No risk case.** A thesis that does not argue against itself is advocacy, not analysis. The risk case is mandatory, not optional.

## Layer Annotation
L2 stage contract. The research pack is L4 (this thesis). Research standards from _config/ are L3. The prior thesis from _references/ is L3.
