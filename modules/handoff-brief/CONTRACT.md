# Handoff Brief Contract

## Purpose
Carry the minimum sourced conclusion, open items, and flags from one workspace to another.

## Inputs
- Upstream output.
- Source references.
- Open confirmations.
- Carried-forward finding, decision, or recommendation.

## Process
1. Name the subject, origin workspace, stage, and date.
2. State the carried-forward conclusion.
3. Include sourced figures or evidence IDs.
4. List open items the downstream must resolve.
5. Carry `[NEEDS CONFIRMATION]` flags forward.
6. Point back to source files instead of copying full context.

## Outputs
- `handoff_brief.md`

## Done Looks Like
A downstream workspace can start from the brief, understand what has already been settled, and see what still needs review.

## Common Failure Modes
- Re-summarizing the whole upstream workspace.
- Dropping open confirmations.
- Copying unsupported conclusions without source IDs.

## Layer Annotation
L2 module contract. Handoff briefs are L4 outputs that become L3-like reference for downstream work.
