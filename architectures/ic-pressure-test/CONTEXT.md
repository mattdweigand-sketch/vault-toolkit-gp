# Workflow: IC Pressure Test

## Overview
Four-stage decision-support workflow: Memo Intake -> Challenge -> Conditions -> Capture. It improves a pending IC decision without becoming the IC gate.

## Modules Used
- `modules/verified-fact-pack/CONTRACT.md`: normalizes model outputs and evidence into usable facts.
- `modules/decision-challenge/CONTRACT.md`: pressure-tests fragile assumptions, missing evidence, and conditions.
- `modules/validated-memory-store/CONTRACT.md`: captures validated lessons after IC.
- `modules/handoff-brief/CONTRACT.md`: consumes diligence handoff briefs and emits downstream learning flags.

## Stage Map

| Stage | Purpose | Inputs | Output Location |
|---|---|---|---|
| 01_memo | Normalize the memo, ask, model outputs, and verified evidence base | IC memo, model outputs, diligence evidence or handoff brief, precedent store | 01_memo/output/ |
| 02_challenge | Stress-test the thesis, assumptions, evidence, and risks | Memo packet, IC standards, precedent | 02_challenge/output/ |
| 03_conditions | Convert unresolved issues into decision questions and conditions | Challenge pack, decision standards | 03_conditions/output/ |
| 04_capture | Capture validated learning and handoff flags for future use | Final IC outcome, pressure-test pack | 04_capture/output/ + _store/ |

## How Stages Connect
- 01 -> 02: The normalized memo packet becomes the challenge input. Challenge should not reassemble the memo or recompute the model.
- 02 -> 03: Challenge produces fragile assumptions and missing evidence. Conditions turns them into IC-ready questions, approval conditions, or reasons to pause.
- 03 -> 04: After IC, capture records which questions mattered and what changed so future pressure tests improve.

## AI vs. Platform

| Step | Layer | Owner |
|---|---|---|
| Deal workflow state, memo files, IC approval record | Platform | Dealpath, DealCloud, CRM, or deal system |
| Return math, valuation, debt sizing, sensitivities | Deterministic | Underwriting model of record |
| Thesis challenge, risk synthesis, missing-evidence map, IC questions | AI | Deal team on governed inputs |
| Approval, decline, table, or conditions | Human | Investment committee |

## Reference Material
- `_config/ic-standards.md`: What the committee expects before approval.
- `_config/pressure-test-questions.md`: Canonical challenge questions.
- `_config/before-you-trust-this.md`: Open confirmations.
- `_store/`: Prior pressure-test learnings and reusable IC challenge patterns.
