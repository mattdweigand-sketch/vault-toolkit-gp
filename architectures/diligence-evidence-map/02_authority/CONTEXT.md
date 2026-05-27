# Stage 02: Authority

## Purpose
Rank which sources are authoritative for each diligence fact class and flag conflicts.

## Inputs
- `01_inventory/output/source_inventory.md`.
- `_config/source-standards.md`.

## Process
1. Group sources by fact class: rent roll, financials, legal, environmental, capex, customer, market, or other.
2. Rank authority within each fact class.
3. Identify conflicts between sources.
4. Label each conflict as resolved by authority, unresolved, or needs human review.
5. Stop for review before question mapping if authority is unclear.

## Output
Write `02_authority/output/authority_map.md` and `conflict_log.md`.

## Done Looks Like
The team knows which source supports which fact class and where the room conflicts with itself.
