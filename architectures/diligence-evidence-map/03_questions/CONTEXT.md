# Stage 03: Questions

## Purpose
Map the reviewed evidence to the diligence questions that remain.

This stage also implements `modules/handoff-brief/CONTRACT.md` when the evidence map feeds IC pressure test, hold/sell/refi, or another downstream workspace. Before downstream reliance, run `modules/artifact-review/CONTRACT.md` against the question map and handoff brief.

## Inputs
- `02_authority/output/authority_map.md`.
- `02_authority/output/conflict_log.md`.
- `_config/diligence-questions.md`.

## Process
1. For each diligence question, cite supporting source IDs.
2. Mark questions as answered, partially answered, contradicted, or unsupported.
3. Convert unsupported or contradicted questions into owner-specific diligence requests.
4. Flag any issue that could change price, structure, approval, or walk-away.

## Output
Write `03_questions/output/diligence_question_map.md`.

When another workspace will consume the result, also write `03_questions/output/handoff_brief.md`.

When the output will feed a decision or external artifact, also write `03_questions/output/artifact_review_report.md`.

## Done Looks Like
The diligence lead has a source-backed list of what is known, what is unsupported, and what must be resolved.
