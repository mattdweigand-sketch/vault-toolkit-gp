# Workflow: Diligence Evidence Map

## Overview
Three-stage source-provenance workflow: Inventory -> Authority -> Questions. It turns a data room into a source-backed diligence question map, then produces a handoff brief for downstream IC or decision work.

## Modules Used
- `modules/source-provenance/CONTRACT.md`: shared method for inventory, duplicate log, conflict log, and missing context.
- `modules/artifact-review/CONTRACT.md`: skeptical review for the evidence map or handoff brief before downstream reliance.
- `modules/handoff-brief/CONTRACT.md`: shared output contract when diligence feeds IC pressure test or another workspace.

## Stage Map

| Stage | Purpose | Inputs | Output Location |
|---|---|---|---|
| 01_inventory | Identify and summarize the source set | `00_sources/`, source standards | 01_inventory/output/ |
| 02_authority | Rank authority and log conflicts | Inventory, source hierarchy | 02_authority/output/ |
| 03_questions | Map evidence to diligence questions and write downstream handoff brief | Authority map, diligence checklist | 03_questions/output/ |

## AI vs. Platform

| Step | Layer | Owner |
|---|---|---|
| Data room storage, permissions, document history | Platform | Deal platform / data room |
| Exact duplicate detection | Deterministic | File hash or document tool |
| Source ranking, conflict detection, question mapping | AI | Deal team on reviewed sources |
| Resolving conflicts and accepting evidence | Human | Diligence owner |

## Reference Material
- `_config/source-standards.md`
- `_config/diligence-questions.md`
- `_config/before-you-trust-this.md`
