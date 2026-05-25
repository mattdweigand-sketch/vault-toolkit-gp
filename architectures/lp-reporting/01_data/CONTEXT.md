# Stage 01: Data

## Purpose
Gather, organize, and verify the numbers for a reporting cycle. The output of this stage is a verified data pack that the draft stage can write from directly, without re-deriving any numbers.

## Inputs
- **Reporting brief**: What this cycle covers. Quarter, fund, report type. Provide this when you enter the stage.
- **Fund accounting export** (from your fund admin or GL): NAV, capital accounts, contributions, distributions, fees.
- **Asset-level reports** (optional): Property performance, occupancy, NOI, leasing activity, valuations.
- **Prior letter** (from _config/ or pasted): Last cycle's reported figures, for continuity and variance.

## Process
1. Pull all source data for the period. If more than one version of an export or asset report is present, confirm which is authoritative before pulling — never blend figures across versions (Constraint 10).
2. Identify the headline figures the report has to carry. Fund NAV, net IRR, DPI/TVPI, called and uncalled capital, distributions for the period.
3. Reconcile each headline figure to its source. A number that cannot be tied to the accounting export does not go in the pack.
4. Compute the variances against the prior period and note anything an LP will ask about. A valuation markdown, a distribution change, an occupancy drop.
5. Flag any figure that is preliminary, estimated, or subject to audit. Those carry a label all the way to the letter.
6. Produce the verified data pack in the output format below.

## Output
Write to: 01_data/output/data-pack.md

Format:
```
# Data Pack: [Fund] [Period]

## Headline Figures
[NAV, net IRR, DPI, TVPI, called/uncalled, period distributions.
 Each with its source and a tie-out note.]

## Asset-Level Detail
[Per asset or per portfolio segment: value, NOI, occupancy, key activity.]

## Variances vs. Prior Period
[What changed and why. The items an LP will notice and ask about.]

## Flags
[Preliminary, estimated, or unaudited figures. Anything that needs a
 disclosure label in the letter.]

## Reconciliation Status
[Tied to source: yes / no for each headline figure. Nothing reaches
 the draft stage marked "no."]
```

## Done Looks Like
A data pack where every headline figure is tied to source and every notable variance is explained. If the writer in stage 02 has to open the accounting export to check a number, this stage did not finish its job.

## Common Failure Modes
- **Blending figures across export versions.** When two versions of an export exist, pick the authoritative one and pull every figure from it. Mixing a NAV from one version with a distribution from another produces a pack that ties to nothing.
- **Letting a figure through without a tie-out.** A headline number with no source note is a number nobody can defend when an LP asks. Reconciliation status "no" never reaches the draft stage.
- **Dropping the flags.** Preliminary, estimated, and unaudited labels have to travel with the figure all the way to the letter. Stripping them here is how an unaudited mark reaches an investor with no caveat.

## Layer Annotation
This is an L2 stage contract. It loads only when working in this stage. The accounting export and asset reports loaded here are L4 (working artifacts specific to this cycle). The prior letter from _config/ is L3 (reference, stable across cycles).
