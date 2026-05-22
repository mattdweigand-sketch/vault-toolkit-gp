# Workflow: LP Reporting

## Overview
Three-stage pipeline: Data → Draft → Distribution. Each stage has a defined contract, explicit inputs, and a clear output location. Human reviews between stages. The data stage gates the others: nothing gets written until the numbers are verified.

## Stage Map

| Stage | Purpose | Inputs | Output Location |
|---|---|---|---|
| 01_data | Gather and verify the numbers | Fund accounting export, asset reports, prior letter | 01_data/output/ |
| 02_draft | Write the letter or notice | Verified data pack, investor voice file, format patterns, constraints | 02_draft/output/ |
| 03_distribution | Finalize and distribute | Approved draft, format spec, distribution list | 03_distribution/output/ |

## How Stages Connect
- 01 → 02: The verified data pack becomes the source for drafting. The draft stage reads the data pack and the variance notes, NOT the raw accounting export. If the data stage did its job, the draft stage should never have to reconcile a number itself.
- 02 → 03: The approved draft becomes the distribution input. The distribution stage formats, applies the compliance pass, and prepares the letter for each investor. It does not rewrite the narrative. If distribution is doing heavy rewriting, the draft stage needs tighter constraints.

## Reference Material (in _config/)
- voice-and-tone.md: How the fund speaks to its LPs. Loaded in stage 02.
- format-patterns.md: Structure per report type (quarterly letter, capital call notice, distribution notice). Loaded in stage 02.
- constraints.md: The never-do list, including compliance and disclosure rules. Loaded in stages 02 and 03.

## When to Add Stages
Add a stage when you consistently find yourself doing a distinct type of work between two existing stages. If compliance or legal always reviews before distribution, add 02a_compliance-review or renumber. Do not add stages preemptively. Add them when the process demands it.

## AI vs. Platform: Where Each Step Lives

This is the workflow where the boundary is least negotiable. The numbers come from a governed source. AI writes the narrative around them. The rule: rely on your platform for the data and the record, use AI for the language and the judgment. See Constraint 09.

| Step in this workflow | Layer | Who owns it |
|---|---|---|
| Verified NAV, capital accounts, performance figures, the single source of truth, the audit trail | Platform / data foundation | Enterprise platform (Juniper Square and the fund admin underneath it) |
| The waterfall and allocation math of record | Deterministic | The platform's calculation engine |
| Drafting the letter narrative, explaining variances, summarizing portfolio activity, tailoring tone | AI | You, on top of governed data |
| Sign-off and compliance approval before anything reaches an LP | Human in the loop | Finance and compliance |

The trap on this workflow: asking AI to produce or "reconcile" a figure rather than to write about a figure the platform already verified. The data stage (01_data) exists to enforce exactly this. Every number in the letter traces to the platform source, never to the model.
