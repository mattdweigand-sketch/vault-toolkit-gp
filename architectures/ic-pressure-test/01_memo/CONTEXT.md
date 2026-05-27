# Stage 01: Memo Intake

## Purpose
Normalize the pending IC packet into a clean memo brief: ask, thesis, model outputs of record, diligence evidence, open issues, and precedent context.

## Inputs
- IC memo or draft memo.
- Model outputs of record, not working scratch math.
- Diligence evidence and open issue list.
- `_config/ic-standards.md`.
- `_store/` and any IC precedent memory available.

## Process
1. Extract the ask, proposed decision, headline terms, thesis, risks, and requested committee action.
2. List the model outputs of record and source for each figure. Do not recompute.
3. Map evidence supporting each material claim.
4. Identify claims with weak, missing, or conflicting support.
5. Note prior precedent that appears relevant.

## Output
Write `01_memo/output/memo-brief-[deal]-[date].md` with ask, thesis, model outputs, evidence map, open issues, and precedent pointers.

## Done Looks Like
The challenge stage can evaluate the memo without rereading the full data room or rebuilding the model.
