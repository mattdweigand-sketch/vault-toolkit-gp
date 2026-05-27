# Stage 03: Capture

## Purpose
Validate the proposed analysis, then commit the record to the store and update the rolled-up decision intelligence. This is where the loop closes — the per-run analysis becomes part of the workspace's memory. It is also the control gate: nothing enters the store as institutional memory without the IC chair / deal lead signing off on the rationale claims, and especially on the stated-vs-inferred split.

## Inputs
- **02_analysis/output/analysis-[deal]-[date].md**: The structured analysis with its stated-vs-inferred rationale, decisive factor, standing-vs-bespoke read, precedent test, and confidence flags.
- **_config/store-schema.md**: The structure a stored record must follow.
- **_config/decision-taxonomy.md**: To confirm the tags used for aggregation, including the controlled lists of condition and concern categories.
- **_store/**: The destination — records/ and patterns.md — and the current state of both.

## Process
1. Human validation first. The IC chair / deal lead reviews the proposed analysis, focusing on the claims the analysis flagged as low-confidence or precedent-departing — and especially the inferred rationale, anywhere it diverges from what the minutes actually attribute to the committee. Confirm, correct, or downgrade each rationale claim. This step is not optional — it is the reason the store stays trustworthy and a manufactured rationale does not become precedent.
2. Normalize the validated analysis into the store schema: the standard fields, the taxonomy tags, the decision lane, the conditions tagged by category, the concerns tagged by category, the dissent and vote, the decisive factor, the validated stated-vs-inferred rationale with its final confidence, and the implied signal for future memos.
3. Write the record to `_store/records/[deal]-[date].md`. Do not overwrite prior records; the store is append-only history.
4. Update `_store/patterns.md`: does this record strengthen a pattern (add to its evidence — a recurring condition, a risk-appetite boundary, a recurring concern), extend one (a new segment or strategy), or depart from one (the committee decided against its own precedent — revise or qualify the pattern)? Make the pattern change explicit and dated. A departure revises the pattern; it is not discarded to protect the existing story. Respect the minimum-support threshold before a pattern is treated as more than a hypothesis.
5. Note anything that should flow to another workspace now — a standing condition deal-pipeline's IC-memo template should pre-empt, a risk-appetite boundary deal-screening should screen against, a precedent worth surfacing on the next similar deal.
6. Record the capture in output.

## Output
Write to: 03_capture/output/captured-[deal]-[date].md

```
# Capture Log: [Deal Name]
Analysis reference: [filename]   Validated by: [name], [date]

## Stored
Record written to: _store/records/[deal]-[date].md
Validation: [rationale claims confirmed / corrected — note any changes, especially
 where an inferred rationale was reclassified, qualified against the minutes, or a
 confidence was downgraded]

## Patterns Updated
[Which pattern in _store/patterns.md changed and how:
 strengthened / extended / departed-and-revised. Dated.]

## Flag to Other Workspaces
[The concrete signal deal-pipeline / deal-screening should pick up now — a standing
 condition to pre-empt, a risk-appetite boundary, a precedent — or "none."]
```

## Done Looks Like
A validated record in the store, append-only, and a patterns file that reflects it — strengthened, extended, or honestly revised. The loop has closed: the next run will read this back. Any concrete decision signal is flagged to the workspaces that take deals to committee.

## Common Failure Modes
- **Skipping validation.** Capturing the model's unvalidated analysis — or a manufactured rationale — turns the store into a pile of confident guesses that then shape real memos. The human sign-off is the control that makes the whole workspace worth trusting.
- **Overwriting instead of appending.** The store is history. Revising a pattern is fine and expected; deleting a prior record erases the trail of how the committee's mind changed over time.
- **Protecting the pattern from the evidence.** When a record shows the committee departing from its own precedent, the pattern changes — not the record. Smoothing the departure away to keep a tidy story defeats the purpose of learning.
- **Hard-coding a one-off.** A single bespoke condition should not become "the committee's standing policy." Respect the minimum-support threshold; let a pattern earn its promotion.

## Layer Annotation
L2 stage contract. The analysis is L4 (this run). The schema and taxonomy from _config/ are L3. The store is written here — its L4-like role — completing the loop whose L3-like role is read by future runs. This dual read/write relationship to _store/ is the structural signature of the learning loop.
