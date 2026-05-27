# Stage 02: Draft

## Purpose
Write the deliverable from the reviewed inventory — grounded, cited, and honest about what it does not know. Every claim traces to a source ID. Inferences are labeled as inferences. Anything the inventory does not support is flagged, not smoothed over. This is the downstream half of inspectable output; the inventory is what makes it possible.

Do not start this stage until a human has reviewed `01_inventory/output/source_inventory.md`. A draft from an unreviewed inventory is the failure this workspace exists to prevent.

## Inputs
- **01_inventory/output/source_inventory.md**: The reviewed source-of-truth table. Cite by the IDs it assigns. Cite up the authority ladder, never down — a claim resting on a superseded file is a flag, not a sentence.
- **01_inventory/output/summaries/**: The per-source summaries. Draft from these and the originals they point to, not from the raw pile.
- **01_inventory/output/conflict_log.md** and **missing_context.md**: The known disagreements and gaps. The draft must surface these where they bear on a claim, not write around them.
- **_config/deliverable-spec.md**: What the deliverable is, who reads it, what it must accomplish, and any format/length constraints.
- **_references/** (selectively): House style, prior comparable deliverables, standing standards.

## Process
1. Read the deliverable spec. Confirm what the deliverable must do and for whom.
2. Read the reviewed inventory, the summaries, and the conflict and missing-context logs. Work from the authoritative version of each fact.
3. Draft the deliverable. For every factual claim, cite the source ID inline. For every judgment, label it as an inference and name what it rests on. Where a conflict from the log bears on a claim, present both sides rather than picking one.
4. Send numbers to the book of record. Figures come from the authoritative source the inventory names — cited, not recomputed in prose, never blended across versions (Constraint 09).
5. Flag, do not fill. Where the deliverable would benefit from a fact the inventory does not support, mark it `[⚠️ NOT SUPPORTED — verify before finalizing]` rather than supplying a plausible number.
6. Close with an Open Items list (everything flagged, every unresolved conflict, every gap that bears on the deliverable) and a Source Usage Map (which source IDs the deliverable actually used).

## Output
Write to: 02_draft/output/

The deliverable itself, in whatever form the spec calls for (memo, letter, brief, case), plus:
```
## Open Items
[Unsupported claims flagged in the draft. Unresolved conflicts from the
 conflict log that bear on the deliverable. Gaps the reader should know about
 before relying on this.]

## Source Usage Map
[Which source IDs the deliverable used, and for what. Makes the grounding
 auditable: a reader can trace any claim back to 00_sources/ via the inventory.]
```

## Done Looks Like
The deliverable does what the spec asked. Every factual claim carries a source ID; every judgment is labeled as one; every figure traces to the source the inventory marked authoritative. Conflicts that bear on the deliverable are surfaced, not resolved silently. The Open Items list names what still needs a human, and the Source Usage Map makes the grounding auditable.

## Common Failure Modes
- **Citing down the ladder.** A claim resting on a file the inventory marked superseded is a flag, not a sentence. Cite the authoritative version or surface that you cannot.
- **Smoothing over a flag.** An unsupported claim written fluently is more dangerous than one left blank. If the room does not support it, mark it; do not let confident prose hide the gap.
- **Recomputing a figure.** The deliverable narrates the numbers; it does not compute them. The model that owns the figure is the source of record (Constraint 09).
- **Burying a conflict.** If two sources disagreed and the conflict bears on a claim, the reader needs to see both, not the one the draft happened to pick.

## Layer Annotation
L2 stage contract. The reviewed inventory, summaries, and logs from 01_inventory/output/ are L4, as is the deliverable written here. The deliverable spec from _config/ is L3; anything pulled from _references/ is L3.
