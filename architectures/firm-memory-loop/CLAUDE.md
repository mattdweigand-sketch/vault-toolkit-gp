# Firm Memory Loop Workspace

## What This Is
A generic learning-loop architecture for repeated GP judgment: deal win/loss, fundraising objection learning, IC precedent, portfolio post-mortems, or other post-event learning. It captures an outcome, analyzes why, validates the causal claim, and updates a store that informs the next run.

Use a specialized architecture when one exists, such as `underwriting-backtest`. Use this when the firm wants a new memory loop with the same shape.

## Modules Used
- `modules/validated-memory-store/CONTRACT.md`
- `modules/handoff-brief/CONTRACT.md`
