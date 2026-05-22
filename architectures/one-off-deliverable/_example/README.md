# Worked Example: A Finished One-Off-Deliverable Workspace

This folder is a fully instantiated copy of the one-off-deliverable workspace, populated for a
fictional fund so you can see what "done" looks like. The reference architecture one level up
(`../`) ships empty on purpose — you copy and fill it. This example shows the filled result for
one deliverable.

**The deliverable:** a hold/sell case for a single asset, for the investment committee.
**The fund:** Northpoint Real Estate Partners, Fund III.
**The asset:** Maple Commons, a 240-unit garden multifamily in Columbus, OH.
**The mess:** the source set arrived as a pile — two versions of the model that disagree on the
exit cap, a broker's opinion of value, a stale 2024 appraisal, an informal email thread, and a
rent roll the model references but that nobody included.
**Everything here is invented.** The numbers, the asset, and the firm do not exist. Use the
shape, not the content.

## Why this is the example to study

This architecture exists for one job: inspect a messy source set before drafting, so the
deliverable rests on the authoritative version of each fact instead of a confident blend. This
example is built to show that job doing real work. Read it in order:

1. **`00_sources/README.md`** — the manifest of the messy pile, as it arrived. In a real run
   these are the copied originals; here they are described, since the files are fictional.
2. **`01_inventory/output/source_inventory.md`** — every file given a source ID and ranked on
   the authority ladder. This is the single most important artifact in the workspace. The two
   model versions are not treated as equal; the 2024 appraisal is marked superseded.
3. **`01_inventory/output/duplicate_log.md`**, **`conflict_log.md`**, **`missing_context.md`** —
   the three logs. The conflict log is the one to read: the two model versions disagree on the
   exit cap, and the pass surfaces it instead of picking a winner.
4. **`01_inventory/output/summaries/`** — one summary per high/medium-relevance source.
5. **`02_draft/output/hold-sell-case-maple-commons-2026-q2.md`** — the deliverable, written only
   from the reviewed inventory. Every claim cites a source ID, the exit-cap conflict is surfaced
   rather than hidden, the figures defer to the model and fund admin, and it closes with an Open
   Items list and a Source Usage Map.

## What to look at in `_config/`

The two reference files, populated. This is what a customer's `_config` should look like after
onboarding: a real deliverable spec and a real source hierarchy with a named book of record.
Compare a customer's `_config` to these to judge whether onboarding actually filled them in.

## How to use it during onboarding

When you reach the "one stage run end to end" item on the Onboarding Complete checklist, compare
the customer's output to the matching file here. The tests this example is built to enforce:

- Does their `source_inventory.md` rank authority, or does it just list files? A flat list is not
  an inventory.
- When two of their sources disagree, does the conflict surface in `conflict_log.md` and again in
  the draft — or did the model quietly pick one?
- Does every figure in their draft trace to the source the inventory marked authoritative, or did
  the model blend across versions?
- Does the draft flag what the sources do not support (here: the missing rent roll), or does it
  write around the gap with a plausible number?

If the draft reads clean but the conflict and the gap are invisible, the workspace is not done.
This example is the target.
