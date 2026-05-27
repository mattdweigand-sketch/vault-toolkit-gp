# Workflow: Firm Memory Loop

## Overview
Three-stage loop: Signal -> Analysis -> Capture.

## Modules Used
- `modules/validated-memory-store/CONTRACT.md`
- `modules/handoff-brief/CONTRACT.md`

## Stage Map

| Stage | Purpose | Inputs | Output Location |
|---|---|---|---|
| 01_signal | Assemble factual outcome record | Trigger, source records, current store | 01_signal/output/ |
| 02_analysis | Explain why using canonical questions | Outcome record, questions, patterns | 02_analysis/output/ |
| 03_capture | Validate and write to store | Analysis, schema, taxonomy | 03_capture/output/ + _store/ |

## AI vs. Platform

| Step | Layer | Owner |
|---|---|---|
| Facts of record | Platform | Deal, investor, portfolio, or fund system |
| Simple counts and deterministic comparisons | Deterministic | Query / spreadsheet / platform export |
| Causal analysis and pattern synthesis | AI | Workflow owner |
| Validation of causal claim | Human | Accountable lead |
