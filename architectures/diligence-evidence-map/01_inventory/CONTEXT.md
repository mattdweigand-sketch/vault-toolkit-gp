# Stage 01: Inventory

## Purpose
Create a source inventory of the diligence material.

This stage implements `modules/source-provenance/CONTRACT.md` with diligence-specific fact classes from `_config/source-standards.md`.

## Inputs
- Files copied into `00_sources/`.
- `_config/source-standards.md`.

## Process
1. Assign each source an ID.
2. Record title, date, source owner, document type, apparent version, and relevance.
3. Summarize high-relevance files briefly.
4. Log duplicates, stale versions, missing dates, and unreadable files.

## Output
Write `01_inventory/output/source_inventory.md`, `duplicate_log.md`, and `missing_context.md`.

## Done Looks Like
Every source has an ID and enough metadata for authority ranking.
