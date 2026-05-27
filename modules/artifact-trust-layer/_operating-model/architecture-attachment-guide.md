# Architecture Attachment Guide

The Artifact Trust Layer attaches to existing architectures. It does not replace them.

## `messy-input-intake`

Use when source material arrives as scattered files, emails, notes, exports, screenshots, or prior artifacts.

Reference:

- `modules/artifact-trust-layer/README.md`
- `modules/artifact-trust-layer/_prompts/build-source-packet.md`

Copy when needed:

- `modules/artifact-trust-layer/_templates/source-packet.md` to `_templates/artifact-trust/source-packet.md`

Add outputs:

- `01_capture/output/source-packet-draft-[name]-[date].md`
- `04_handoff/output/artifact-trust-handoff-[name]-[date].md`

## `evidence-review`

Use when the team needs to know what the source set supports before drafting, deciding, or responding.

Reference:

- `modules/artifact-trust-layer/README.md`
- `modules/artifact-trust-layer/_config/artifact-boundary.md`
- `modules/artifact-trust-layer/_config/review-severity.md`
- `modules/artifact-trust-layer/_prompts/build-source-packet.md`
- `modules/artifact-trust-layer/_prompts/create-claim-evidence-map.md`
- `modules/artifact-trust-layer/_prompts/hostile-review.md`

Copy when needed:

- `modules/artifact-trust-layer/_templates/source-packet.md` to `_templates/artifact-trust/source-packet.md`
- `modules/artifact-trust-layer/_templates/claim-evidence-map.md` to `_templates/artifact-trust/claim-evidence-map.md`
- `modules/artifact-trust-layer/_templates/artifact-review-report.md` to `_templates/artifact-trust/artifact-review-report.md`
- `modules/artifact-trust-layer/_templates/xlsx-control-map.md` to `_templates/artifact-trust/xlsx-control-map.md` when a workbook is in scope.

Add outputs:

- `01_inventory/output/source-packet-[name]-[date].md`
- `04_evidence_brief/output/claim-evidence-map-[name]-[date].md`
- `04_evidence_brief/output/artifact-review-report-[name]-[date].md` when a draft artifact exists.

## `decision-prep`

Use when the artifact supports a human or committee decision.

Reference:

- `modules/artifact-trust-layer/README.md`
- `modules/artifact-trust-layer/_config/artifact-boundary.md`
- `modules/artifact-trust-layer/_config/review-severity.md`
- `modules/artifact-trust-layer/_prompts/hostile-review.md`
- `modules/artifact-trust-layer/_prompts/stale-number-review.md`
- `modules/artifact-trust-layer/_prompts/formula-risk-review.md` when a workbook is in scope.
- `modules/artifact-trust-layer/_operating-model/human-approval.md`

Copy when needed:

- `modules/artifact-trust-layer/_templates/artifact-spec.md` to `_templates/artifact-trust/artifact-spec.md`
- `modules/artifact-trust-layer/_templates/claim-evidence-map.md` to `_templates/artifact-trust/claim-evidence-map.md`
- `modules/artifact-trust-layer/_templates/artifact-review-report.md` to `_templates/artifact-trust/artifact-review-report.md`
- `modules/artifact-trust-layer/_templates/human-approval-note.md` to `_templates/artifact-trust/human-approval-note.md`
- `modules/artifact-trust-layer/_templates/pptx-claim-map.md` to `_templates/artifact-trust/pptx-claim-map.md` for decks.
- `modules/artifact-trust-layer/_templates/xlsx-control-map.md` to `_templates/artifact-trust/xlsx-control-map.md` for workbooks.
- `modules/artifact-trust-layer/_templates/docx-claim-map.md` to `_templates/artifact-trust/docx-claim-map.md` for memos.

Add outputs:

- `01_decision_frame/output/artifact-spec-[name]-[date].md`
- `03_challenge/output/artifact-review-report-[name]-[date].md`
- `04_approval_packet/output/human-approval-note-[name]-[date].md`

## `stakeholder-response-prep`

Use when the artifact will explain verified facts to an investor, LP, board, executive, customer, partner, or employee.

Reference:

- `modules/artifact-trust-layer/README.md`
- `modules/artifact-trust-layer/_config/artifact-boundary.md`
- `modules/artifact-trust-layer/_config/review-severity.md`
- `modules/artifact-trust-layer/_prompts/create-claim-evidence-map.md`
- `modules/artifact-trust-layer/_prompts/hostile-review.md`
- `modules/artifact-trust-layer/_prompts/stale-number-review.md`
- `modules/artifact-trust-layer/_operating-model/human-approval.md`

Copy when needed:

- `modules/artifact-trust-layer/_templates/claim-evidence-map.md` to `_templates/artifact-trust/claim-evidence-map.md`
- `modules/artifact-trust-layer/_templates/artifact-review-report.md` to `_templates/artifact-trust/artifact-review-report.md`
- `modules/artifact-trust-layer/_templates/human-approval-note.md` to `_templates/artifact-trust/human-approval-note.md`
- `modules/artifact-trust-layer/_templates/docx-claim-map.md` to `_templates/artifact-trust/docx-claim-map.md` for narratives or memos.
- `modules/artifact-trust-layer/_templates/pptx-claim-map.md` to `_templates/artifact-trust/pptx-claim-map.md` for decks.

Add outputs:

- `01_verified_facts/output/claim-evidence-map-[name]-[date].md`
- `04_review_packet/output/artifact-review-report-[name]-[date].md`
- `04_review_packet/output/human-approval-note-[name]-[date].md`

## `institutional-memory-loop`

Use only after human validation.

Capture:

- Repeated unsupported claim patterns.
- Recurring stale source problems.
- Workbook control failures.
- Review issues that should become future guidance.

## Setup Rule

If a workflow produces or reviews decks, workbooks, memos, reports, IC materials, LP narratives, board materials, diligence artifacts, or one-off deliverables, ask whether to attach this module.

## Default Attachment Rule

Reference module files in place by default. Copy templates only when a workspace needs local fields, naming, owners, or review rules.

Copied templates go under `_templates/artifact-trust/`.

Use `_operating-model/workspace-output-conventions.md` for default output paths.

## Ready Check

An attached workspace is ready when:

- The selected architecture is unchanged.
- The module is referenced in workspace or stage context.
- Source packet output location is named when source review is in scope.
- Claim evidence map output location is named when an artifact is in scope.
- Artifact review report output location is named when a draft artifact exists.
- Human approval owner is named.
- Open confirmations are captured in `_config/before-you-trust-this.md`.
