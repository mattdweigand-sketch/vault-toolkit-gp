# Workspace Output Conventions

Use these default paths when attaching the Artifact Trust Layer to a workspace.

## Shared Rule

Generated outputs live under the stage that produces them. Use explicit filenames so downstream stages can cite them without guessing.

## Default Output Paths

| Output | Default Location |
|---|---|
| Source packet | `01_inventory/output/source-packet-[name]-[date].md` |
| Draft source packet | `01_capture/output/source-packet-draft-[name]-[date].md` |
| Claim evidence map | `04_evidence_brief/output/claim-evidence-map-[name]-[date].md` |
| Artifact spec | `01_decision_frame/output/artifact-spec-[name]-[date].md` or `02_message_frame/output/artifact-spec-[name]-[date].md` |
| Artifact review report | `03_challenge/output/artifact-review-report-[name]-[date].md` or `04_review_packet/output/artifact-review-report-[name]-[date].md` |
| Human approval note | `04_approval_packet/output/human-approval-note-[name]-[date].md` or `04_review_packet/output/human-approval-note-[name]-[date].md` |
| Workbook control map | `04_evidence_brief/output/xlsx-control-map-[name]-[date].md` or `03_challenge/output/xlsx-control-map-[name]-[date].md` |
| Artifact trust handoff | `04_handoff/output/artifact-trust-handoff-[name]-[date].md` |

## Architecture Defaults

### `evidence-review`

- Source packet: `01_inventory/output/source-packet-[name]-[date].md`
- Claim evidence map: `04_evidence_brief/output/claim-evidence-map-[name]-[date].md`
- Artifact review report: `04_evidence_brief/output/artifact-review-report-[name]-[date].md`

### `decision-prep`

- Artifact spec: `01_decision_frame/output/artifact-spec-[name]-[date].md`
- Artifact review report: `03_challenge/output/artifact-review-report-[name]-[date].md`
- Human approval note: `04_approval_packet/output/human-approval-note-[name]-[date].md`

### `stakeholder-response-prep`

- Claim evidence map: `01_verified_facts/output/claim-evidence-map-[name]-[date].md`
- Artifact review report: `04_review_packet/output/artifact-review-report-[name]-[date].md`
- Human approval note: `04_review_packet/output/human-approval-note-[name]-[date].md`

### `messy-input-intake`

- Draft source packet: `01_capture/output/source-packet-draft-[name]-[date].md`
- Artifact trust handoff: `04_handoff/output/artifact-trust-handoff-[name]-[date].md`
