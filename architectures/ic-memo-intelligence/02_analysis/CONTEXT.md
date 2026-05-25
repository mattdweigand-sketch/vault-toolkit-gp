# Stage 02: Analysis

## Purpose
Read what the committee actually weighed in deciding as it did, answering the canonical questions in the standard structure so this record is comparable to every other in the store. Propose the inferred rationale — grounded in the record, tested against precedent, with the committee's *stated* reasoning held distinct from the analyst's *inferred* reading — for a human to validate at capture.

## Inputs
- **01_record/output/record-[deal]-[date].md**: The factual decision record.
- **_config/ic-questions.md**: The canonical question set. Answer all of them, in order. This is what makes the record comparable.
- **_store/patterns.md** and **_store/records/**: The current decision intelligence, so this decision can be read as confirming, extending, or departing from precedent.

## Process
1. Read the decision record and the canonical questions.
2. Answer each canonical question from the record. Where the record does not support an answer, say so — do not fill the gap with a guess. A consistent "not on the record" is more useful to the store than an invented rationale.
3. **Separate the committee's stated reasoning from your inferred reading, and say which is which.** The stated reasons are what the minutes attribute to the committee. The inferred reading is your assessment of what actually drove the decision — often the same, sometimes not (a deal "approved on the sponsor's track record" may really have turned on the co-investor's presence). Keep the two in distinct fields. Collapsing them manufactures a precedent the committee never set.
4. Identify the **decisive factor**: the one thing that, had it been different, would most likely have flipped the decision. Mark it causal vs. incidental, and flag your confidence.
5. Read the **conditions** as a set: are they bespoke to this deal, or the committee's standing guardrails showing up again? A condition that recurs is the calibration signal; a one-off is logged but not yet a pattern.
6. Read the **concerns** the same way: which are this committee's recurring worries in this segment, and which are deal-specific?
7. Test against the store. Does this decision fit an existing pattern in patterns.md (a standing condition, a risk-appetite boundary, a precedent), extend it, or depart from it? A departure is valuable — surface it loudly, because it is how the committee's evolving mind gets captured. (E.g., the IC approved a leverage level it had declined twice before — that is a shift, not noise.)
8. State the **implied signal for future memos**: concrete and transferable — "pre-empt the DSCR-stress condition in the memo for this product," "this segment needs the exit-cap sensitivity the committee always asks for," "do not bring >65% LTV here without addressing the standing concern" — not "write a better memo."
9. Mark every rationale claim, the decisive-factor call, and the precedent read with a confidence level, so the human validator knows where to focus.
10. Produce the structured analysis.

## Output
Write to: 02_analysis/output/analysis-[deal]-[date].md

Format:
```
# IC Decision Analysis: [Deal Name]
Record reference: [filename from record]   Decision: [lane]

## Canonical Questions
[Each question from ic-questions.md, answered from the record.
 "Not on the record" where unsupported. Same order every time.]

## Stated vs. Inferred Rationale
[The committee's stated reasons (from the minutes) vs. your inferred reading of
 what actually drove the decision, in distinct fields, and why you read it as you
 do. This is the defense — do not collapse the two.]

## Decisive Factor
[The one thing that, if different, most likely flips the decision. Causal vs.
 incidental made explicit, confidence-marked.]

## Conditions & Concerns: Standing vs. Bespoke
[Which conditions/concerns are the committee's recurring guardrails (per the
 store) and which are deal-specific.]

## Against the Store
[Does this confirm / extend / depart from an existing pattern, precedent, or
 risk-appetite boundary? If it departs, say so plainly.]

## Implied Signal for Future Memos
[Concrete, transferable: what a future memo in this segment should pre-empt,
 address, or cite. Or "none."]

## For the Validator
[The rationale claims and the precedent read that most need a human check before
 capture, and why — especially anywhere the inferred rationale departs from the
 stated one.]
```

## Done Looks Like
A structured analysis answering every canonical question, with the committee's stated reasoning held distinct from the inferred reading, a decisive factor that is explicit and confidence-marked, conditions and concerns sorted into standing vs. bespoke, tested against the store, ending in a concrete signal for future memos, ready for a human to validate at capture.

## Common Failure Modes
- **Manufacturing a tidy rationale.** Writing a clean, coherent "why the committee approved" that the minutes do not support is the single most damaging output here — it enters the store as precedent that never existed. Hold stated and inferred apart, and flag the split for the validator.
- **Confident reading from thin minutes.** A plausible inferred rationale stated with false certainty will enter the store and shape future memos. Mark confidence honestly; prefer "not on the record" to invention.
- **Answering the questions inconsistently.** If the canonical questions are answered loosely or in a different shape each time, the records stop being comparable and the store stops revealing the committee's standing conditions and recurring concerns. Hold the structure.
- **Burying a departure.** When a decision breaks an existing pattern — the committee approved what it used to decline — that is the most valuable thing in the analysis. Do not smooth it over to fit the precedent the store already tells.
- **Treating a one-off as a pattern.** A single bespoke condition is not a standing guardrail. Mark standing vs. bespoke so a one-deal quirk does not get read as the committee's policy.

## Layer Annotation
L2 stage contract. The decision record is L4 (this run). The canonical questions from _config/ are L3. The store patterns are read here for context (the store's L3-like role).
