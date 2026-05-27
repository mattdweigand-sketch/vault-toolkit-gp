# Artifact Review Contract

## Purpose
Assume the artifact may be pretty but wrong, then enumerate the issues that must be resolved or accepted before it travels.

## Inputs
- Draft artifact, deck, workbook, memo, decision packet, or handoff brief.
- Source packet, source inventory, verified fact pack, or evidence map.
- Artifact spec when one exists.
- Review owner and approval threshold.

## Process
1. Check material claims for source IDs, source dates, and owners.
2. Check numbers, charts, tables, workbook cells, and formulas for traceability.
3. Flag stale sources, mixed date ranges, hidden assumptions, unsupported claims, and source conflicts.
4. Mark consequential unsupported items as `needs_human` or `blocked`.
5. Assign severity: low, medium, or high.
6. Name the recommended owner for each issue.
7. Do not rewrite, beautify, or fix the artifact in the review pass.

## Outputs
- `artifact_review_report.md`
- Optional `artifact_review_report.json`

## Done Looks Like
Every review issue has an artifact location, severity, description, source IDs if relevant, owner, and whether human judgment is required. High-severity issues are either resolved or explicitly accepted before external sharing or downstream reliance.

## Common Failure Modes
- Rewriting the artifact instead of reviewing it.
- Treating missing evidence as a style issue.
- Letting polished language hide unsupported claims.
- Reviewing prose while ignoring charts, tables, formulas, and speaker notes.
- Passing along a handoff brief with unresolved confirmations stripped out.

## Layer Annotation
L2 module contract. Review reports are L4 outputs and approval gates.
