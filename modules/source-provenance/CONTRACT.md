# Source Provenance Contract

## Purpose
Make a source set inspectable before any downstream stage relies on it.

## Inputs
- Raw sources or platform document register.
- Source hierarchy by fact class.
- Fact classes that matter to the workflow.
- Sensitive-source handling rules.

## Process
1. Assign every source a stable source ID.
2. Classify each source by type, owner, date, authority, relevance, and current/stale status.
3. Flag exact duplicates, near duplicates, and version families.
4. Surface conflicts in numbers, dates, decisions, claims, or terms.
5. List missing context: unsupported claims, absent referenced files, or facts with no source.
6. Stop for human review when authority is unclear.

## Outputs
- `source_inventory.md`
- `duplicate_log.md`
- `conflict_log.md`
- `missing_context.md`
- Optional `summaries/Sxx.md`

## Done Looks Like
Every source has an ID. Authority is ranked. Duplicates, conflicts, stale versions, and missing support are visible. Nothing has been deleted, reconciled, or recomputed by the model.

## Common Failure Modes
- Drafting before inventory.
- Treating all files as equally authoritative.
- Silently resolving conflicts.
- Blending facts across versions.
- Recomputing figures instead of pointing to the book of record.

## Layer Annotation
L2 module contract. Inventories and logs are L4 outputs that downstream stages treat as reviewed reference.
