# Stage 03: Capture

## Purpose
Validate the proposed attribution, then commit the record to the store and update the rolled-up calibration patterns. This is where the loop closes — the per-run attribution becomes part of the workspace's memory. It is also the control gate: nothing enters the store as institutional memory without the underwriter / head of acquisitions / IC signing off on the causal claims, and especially on the skill-vs-luck split.

## Inputs
- **02_attribution/output/analysis-[deal]-[date].md**: The structured attribution with its skill-vs-luck split, proposed why, classifications, and confidence flags.
- **_config/store-schema.md**: The structure a stored record must follow.
- **_config/assumption-taxonomy.md**: To confirm the tags used for aggregation, including the controlled list of assumption categories.
- **_store/**: The destination — records/ and patterns.md — and the current state of both.

## Process
1. Human validation first. The underwriter / head of acquisitions / IC reviews the proposed attribution, focusing on the claims the analysis flagged as low-confidence or pattern-contradicting — and especially the skill-vs-luck split, anywhere a market tailwind could have been read as the firm's own skill. Confirm, correct, or downgrade each causal claim. This step is not optional — it is the reason the store stays trustworthy and a tailwind does not get banked as edge.
2. Normalize the validated attribution into the store schema: the standard fields, the taxonomy tags, the underwritten vs. actual on each material assumption and the gap, the decisive driver, the cause class, the validated why with its final confidence, the skill-vs-luck attribution, and the calibration adjustment.
3. Write the record to `_store/records/[deal]-[date].md`. Do not overwrite prior records; the store is append-only history.
4. Update `_store/patterns.md`: does this record strengthen a calibration pattern (add to its evidence), extend one (a new segment, strategy, or vintage), or contradict one (revise or qualify it)? Make the pattern change explicit and dated. A contradiction revises the pattern; it is not discarded to protect the existing story. Respect the minimum-support threshold before a pattern is treated as more than a hypothesis.
5. Note anything that should flow to future investment work now — a concrete assumption edit, a diligence question to add, a pressure-test prompt to strengthen, or a segment to underwrite more conservatively.
6. Record the capture in output.

## Output
Write to: 03_capture/output/captured-[deal]-[date].md

```
# Capture Log: [Deal Name]
Analysis reference: [filename]   Validated by: [name], [date]

## Stored
Record written to: _store/records/[deal]-[date].md
Validation: [causal claims confirmed / corrected — note any changes, especially
 where a market tailwind was reclassified from skill to luck or a confidence
 was downgraded]

## Patterns Updated
[Which calibration pattern in _store/patterns.md changed and how:
 strengthened / extended / contradicted-and-revised. Dated.]

## Flag to Other Workspaces
[The concrete assumption edit, diligence question, or pressure-test prompt the investment process should pick up now
 — assumption, segment, direction, rough magnitude — or "none."]
```

## Done Looks Like
A validated record in the store, append-only, and a patterns file that reflects it — strengthened, extended, or honestly revised. The loop has closed: the next run will read this back. Any concrete calibration signal is flagged to the workspaces that underwrite on those assumptions.

## Common Failure Modes
- **Skipping validation.** Capturing the model's unvalidated attribution — or a tailwind banked as skill — turns the store into a pile of confident guesses that then bend real underwriting. The human sign-off is the control that makes the whole workspace worth trusting.
- **Overwriting instead of appending.** The store is history. Revising a pattern is fine and expected; deleting a prior record erases the evidence trail and the ability to see how the firm's calibration changed.
- **Protecting the pattern from the evidence.** When a record contradicts an existing calibration pattern, the pattern changes — not the record. Smoothing the contradiction away to keep a tidy story defeats the purpose of learning.
- **Hard-coding a one-off.** A single anomalous deal should not rewrite the firm's standard assumption. Respect the minimum-support threshold; let a pattern earn its promotion.

## Layer Annotation
L2 stage contract. The attribution is L4 (this run). The schema and taxonomy from _config/ are L3. The store is written here — its L4-like role — completing the loop whose L3-like role is read by future runs. This dual read/write relationship to _store/ is the structural signature of the learning loop.
