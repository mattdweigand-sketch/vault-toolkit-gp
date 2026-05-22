# The Store

<!--
This folder is the workspace's memory and its actual deliverable. It is what
makes this a learning loop rather than a linear pipeline: stages 01 and 02 read
from here for context, and stage 03 writes back here. The output of the
workflow does not leave the building — it accumulates in this folder.

Contents:
- records/        One file per resolved LP engagement, written by 03_capture
                  in the store schema. Append-only history. Do not overwrite.
- patterns.md     The rolled-up, fund-level intelligence: what converts, which
                  objections recur, where the raise stalls. Updated on each
                  capture. This is the payoff-grain output and the file other
                  workspaces (capital-raising prep, prospect work) read.

How the value compounds:
- One record is nearly worthless. Ten begin to suggest. A hundred, tagged
  consistently by segment, reveal patterns no single engagement could.
- Read patterns.md before a raise, before prepping a prospect, before a tough
  LP meeting. That is the loop paying off.

Handling:
- This is confidential internal intelligence about named LPs and why they
  acted. Treat access and any export accordingly (see _config/store-schema.md).

Starting state:
- Empty. records/ fills as engagements resolve and the loop runs; patterns.md
  begins as hypotheses and earns confidence as records accumulate.
-->
