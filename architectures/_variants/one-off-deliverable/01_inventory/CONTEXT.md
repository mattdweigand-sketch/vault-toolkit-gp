# Stage 01: Inventory

## Purpose
Make the source set inspectable before anything is drafted. Inventory every file, rank it by relevance and authority, summarize the ones that matter, and log duplicates, conflicts, and missing context. This is the provenance pass of Constraint 10. Its single most important rule is the boundary it shares with Constraint 09: **classify and flag; never reconcile or compute.** Surface that two figures disagree. Do not decide which is right.

This stage ends by stopping. It does not roll into drafting. It hands a reviewed-ready inventory back to a human.

## Inputs
- **00_sources/**: The raw source set, copied in. Read from here; never modify it.
- **_config/deliverable-spec.md**: What the deliverable is and who reads it — referenced only to judge which sources are relevant, not to start drafting.
- **_config/source-hierarchy.md**: Any authority ranking already known going in (e.g., "the fund admin export is the book of record"). The pass fills in the rest.
- **A document register, where one exists**: If the source set arrived through a platform that tracks versions and owners, that register is the authoritative inventory. Read it and flag what looks stale; do not rebuild it from scratch (Constraint 10).

## Process
1. If the originals are not yet in `00_sources/`, copy them in. Copy, never move; flag, never delete. The originals are the provenance anchor every later citation points back to.
2. Run exact-duplicate detection deterministically first (a checksum or file comparison). Reserve the model for the harder case: near-duplicates and version families where content overlaps but files are not identical (`model_v1`, `model_v2`, `model_final`).
3. Inventory every file. Assign each a short source ID (`S01`, `S02`, …). Record type, date, owner, relevance (high/med/low), authority (authoritative/supporting/background/superseded), current-or-stale with a stated reason, and a note for human review.
4. Rank authority. Force the ladder — authoritative (the book of record), supporting (adds context), background (relevant, not load-bearing), superseded (kept for history, never cited as current). Drafting will cite up the ladder, never down.
5. Summarize each high- and medium-relevance source into `01_inventory/output/summaries/` — one file per source, what it contains and what it is trustworthy for.
6. Log duplicates and version families: which version appears current and why. Nothing deleted.
7. Log conflicts: where two sources disagree on a number, date, or decision. Quote both sides. Note which looks more authoritative and whether resolution needs a human. Never pick a winner silently.
8. List missing context: claims with no supporting source, references to documents not present, numbers with no stated basis.
9. Honor `sensitive` flags from `_config/source-hierarchy.md`: note a sensitive source's existence and structure only; never copy or quote its contents.
10. Stop. Hand back for review. Do not draft.

## Output
Write to: 01_inventory/output/

Four artifacts plus the summaries:
```
source_inventory.md   One row per file: ID, name, type, date, owner,
                      relevance, authority, current-or-stale (with reason),
                      and a note for human review.

duplicate_log.md      Exact duplicates (from hashing), near-duplicates, and
                      version families. Which version appears current, and why.
                      Nothing deleted — flagged only.

conflict_log.md       Where two sources disagree. Both sides quoted. Which looks
                      more authoritative, and whether resolution needs a human.

missing_context.md    Claims with no supporting source. References to documents
                      not present. Numbers with no stated basis.

summaries/            One summary per high/medium-relevance source (S0x.md).
```

## Done Looks Like
Every file in `00_sources/` carries a source ID, a relevance rank, and an authority level with a stated reason. Duplicates and version families are identified. Conflicts and gaps are logged, not resolved. A reviewer can open `source_inventory.md` and tell, for any fact the deliverable will rest on, which source is authoritative for it. The stage has stopped and handed back. **No draft exists yet.**

## Common Failure Modes
- **Drafting from the pile.** The whole point is that the source set is inspected before a sentence is written. If this stage produces prose instead of an inventory, it has failed.
- **Silently resolving a conflict.** Two sources disagreeing is information, not noise. Log both sides and flag it. The cheapest error to catch is the one the model was about to hide.
- **Blending across versions.** A figure from `v2` and a figure from `final` do not belong in the same sentence. If the model cannot tell which version a number came from, that is a flag, not a guess.
- **Recomputing a figure.** The inventory establishes which source is authoritative for a number. It does not recompute the number. Tie-out is deterministic work (Constraint 09).
- **Rebuilding a register the platform already keeps.** If a document-management system tracks versions and owners, trust it and layer judgment on top; do not have the model re-derive what the system of record already knows.

## Layer Annotation
L2 stage contract. The copied sources in 00_sources/ and everything written to output/ are L4 (this deliverable). The deliverable spec and source hierarchy from _config/ are L3, referenced here to judge relevance and seed the authority ladder.
