# Stage 02: Attribution

## Purpose
Explain why the deal realized as it did against its underwriting, answering the canonical questions in the standard structure so this record is comparable to every other in the store. Propose the "why" for each material variance — grounded in the record, tested against existing patterns, with the firm's *skill* held distinct from market *luck* — for a human to validate at capture.

## Inputs
- **01_reconcile/output/record-[deal]-[date].md**: The factual variance record.
- **_config/underwriting-questions.md**: The canonical question set. Answer all of them, in order. This is what makes the record comparable.
- **_store/patterns.md**: The current firm-level calibration, so this outcome can be read as confirming, extending, or contradicting what is already known.

## Process
1. Read the variance record and the canonical questions.
2. Answer each canonical question from the record. Where the record does not support an answer, say so — do not fill the gap with a guess. A consistent "unknown" is more useful to the store than a fabricated cause.
3. For each material miss, classify the cause: **forecasting error** (we got the assumption wrong), **execution difference** (we delivered above or below the plan), or **exogenous** (the market moved under us). Separate causal from incidental — an assumption can have missed *and* be incidental to a return driven by something else. Make the distinction explicit and flag your confidence.
4. **Separate the firm's skill from market luck, and say which you believe and why.** Of the headline return variance, how much is attributable to what the firm did — a right thesis, strong execution, a well-timed forecast — versus market movement it did not create (cap-rate compression, a rate environment, a sector run)? This split is the central defense against poisoning the store: credit a tailwind to skill and the store quietly teaches the firm it underwrites better than it does.
5. Mark each material miss **systematic or one-off**: is it consistent with a bias the store already shows, or specific to this deal? A systematic miss is the calibration signal; a one-off is noise to log but not yet act on.
6. Test against the store. Does this outcome fit an existing calibration pattern in patterns.md, extend it, or contradict it? A contradiction is valuable — surface it loudly, because it is how patterns get corrected.
7. State the implied calibration adjustment: concrete and transferable — "going-in exit-cap assumption in this segment should widen by ~X bps," "lease-up assumption should add ~N months for this product" — not "underwrite better." If underperformed, state what the firm would have needed to see at underwriting to get it right.
8. Mark every causal claim and the skill-vs-luck split with a confidence level, so the human validator knows where to focus.
9. Produce the structured attribution.

## Output
Write to: 02_attribution/output/analysis-[deal]-[date].md

Format:
```
# Underwriting Attribution: [Deal Name]
Record reference: [filename from reconcile]   Outcome: [Outperformed / In-line / Underperformed]

## Canonical Questions
[Each question from underwriting-questions.md, answered from the record.
 "Unknown" where unsupported. Same order every time.]

## Skill vs. Luck
[Of the headline return variance, the portion attributable to the firm (thesis,
 execution, forecast) vs. market movement it did not create, and why you believe
 the split you do. This is the calibration defense — do not collapse the two.]

## Why (proposed)
[Per material miss: forecasting error / execution / exogenous, causal vs.
 incidental made explicit, systematic vs. one-off, each marked with a confidence
 level.]

## Against the Store
[Does this confirm / extend / contradict an existing calibration pattern? If it
 contradicts, say so plainly.]

## Implied Calibration Adjustment
[Concrete, transferable: the assumption to widen/tighten, in which segment, by
 roughly how much. If underperformed: what we'd have needed to see to get it right.]

## For the Validator
[The causal claims and the skill-vs-luck split that most need a human check
 before capture, and why — especially anywhere a tailwind could be read as skill.]
```

## Done Looks Like
A structured attribution answering every canonical question, with the firm's skill held distinct from market luck, a proposed "why" whose causal claims are explicit, classified, and confidence-marked, tested against the store, ending in a concrete calibration adjustment, ready for a human to validate at capture.

## Common Failure Modes
- **Crediting market beta as skill.** A realized IRR that rode cap-rate compression, recorded as proof the thesis was right, is the single most damaging output here — it enters the store and inflates the firm's confidence in its own underwriting. Hold skill and luck apart, and flag the split for the validator.
- **Confident causation from thin evidence.** A plausible "why" stated with false certainty will enter the store and bend future assumptions. Mark confidence honestly; prefer "unknown" to invention.
- **Answering the questions inconsistently.** If the canonical questions are answered loosely or in a different shape each time, the records stop being comparable and the store stops revealing systematic bias. Hold the structure.
- **Burying a contradiction.** When an outcome breaks an existing calibration pattern, that is the most valuable thing in the attribution. Do not smooth it over to fit the story the store already tells.
- **Calibrating off a one-off.** A single deal's miss may be idiosyncratic. Mark systematic vs. one-off so a one-deal anomaly does not get hard-coded into the firm's standard assumptions.

## Layer Annotation
L2 stage contract. The variance record is L4 (this run). The canonical questions from _config/ are L3. The store patterns are read here for context (the store's L3-like role).
