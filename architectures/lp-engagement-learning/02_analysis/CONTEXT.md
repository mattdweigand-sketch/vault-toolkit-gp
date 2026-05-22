# Stage 02: Analysis

## Purpose
Explain why the engagement resolved as it did, answering the canonical debrief questions in the standard structure so this record is comparable to every other in the store. Propose the "why" — grounded in the record, tested against existing patterns — for a human to validate at capture.

## Inputs
- **01_signal/output/record-[lp-name]-[date].md**: The factual engagement record.
- **_config/debrief-questions.md**: The canonical question set. Answer all of them, in order. This is what makes the record comparable.
- **_store/patterns.md**: The current fund-level patterns, so this outcome can be read as confirming, extending, or contradicting what is already known.

## Process
1. Read the engagement record and the canonical questions.
2. Answer each canonical question from the record. Where the record does not support an answer, say so — do not fill the gap with a guess. A consistent "unknown" is more useful to the store than a fabricated cause.
3. Separate causal from incidental. The LP raised a fee objection AND passed — was the fee the reason, or the stated reason for a decision driven by something else? Make the distinction explicit and flag your confidence.
4. Test against the store. Does this outcome fit an existing pattern in patterns.md, extend it, or contradict it? A contradiction is valuable — surface it loudly, because it is how patterns get corrected.
5. Identify what the firm would do differently. Concrete and transferable: a material, a sequencing change, a person to involve earlier — not "engage better."
6. Mark every causal claim with a confidence level, so the human validator knows where to focus.
7. Produce the structured analysis.

## Output
Write to: 02_analysis/output/analysis-[lp-name]-[date].md

Format:
```
# Engagement Analysis: [LP Name]
Record reference: [filename from signal]   Outcome: [Committed / Passed]

## Canonical Questions
[Each question from debrief-questions.md, answered from the record.
 "Unknown" where unsupported. Same order every time.]

## Why (proposed)
[The proposed explanation for the outcome. Causal vs. incidental made
 explicit. Each causal claim marked with a confidence level.]

## Against the Store
[Does this confirm / extend / contradict an existing pattern? If it
 contradicts, say so plainly.]

## What We'd Do Differently
[Concrete, transferable lessons. Specific actions, not platitudes.]

## For the Validator
[The causal claims that most need a human check before capture, and why.]
```

## Done Looks Like
A structured analysis answering every canonical question, with a proposed "why" whose causal claims are explicit and confidence-marked, tested against the store, ready for a human to validate at capture.

## Common Failure Modes
- **Confident causation from thin evidence.** The single most damaging output here is a plausible "why" stated with false certainty, because it will enter the store and shape future decisions. Mark confidence honestly; prefer "unknown" to invention.
- **Answering the questions inconsistently.** If the canonical questions are answered loosely or in a different shape each time, the records stop being comparable and the store stops revealing patterns. Hold the structure.
- **Burying a contradiction.** When an outcome breaks an existing pattern, that is the most valuable thing in the analysis. Do not smooth it over to fit the story the store already tells.

## Layer Annotation
L2 stage contract. The engagement record is L4 (this run). The canonical questions from _config/ are L3. The store patterns are read here for context (the store's L3-like role).
