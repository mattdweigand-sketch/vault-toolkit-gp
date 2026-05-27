# Stage 01: Signal

## Purpose
Capture the verified signal that may require attention.

## Inputs
- Platform-verified operating data or portfolio dashboard.
- Asset report, if available.
- `_config/intervention-standards.md`.

## Process
1. Record the source of each signal.
2. Classify the signal: plan variance, liquidity, covenant, leasing, expense, customer, operator, valuation, or other.
3. Note whether it trips a threshold or is judgment-based.
4. Flag missing source support.

## Output
Write `01_signal/output/signal-[asset]-[period].md`.

## Done Looks Like
The diagnosis stage has a verified signal and knows where each fact came from.
