# The Store

<!--
This folder is the workspace's memory and its actual deliverable. It is what
makes this a learning loop rather than a linear pipeline: stages 01 and 02 read
from here for context, and stage 03 writes back here. The output of the
workflow does not leave the building — it accumulates in this folder.

Contents:
- records/        One file per resolved competitive process, written by
                  03_capture in the store schema. Append-only history. Do not
                  overwrite.
- patterns.md     The rolled-up, firm-level intelligence: which processes we win,
                  where our bids fall short, which dimension decides outcomes,
                  which brokers' feedback proves reliable. Updated on each
                  capture. This is the payoff-grain output and the file other
                  workspaces (deal-pipeline sourcing and bid strategy,
                  deal-screening prioritization) read.

How the value compounds:
- One record is nearly worthless. Ten begin to suggest. A hundred, tagged
  consistently by asset type, process type, broker, and decisive dimension,
  reveal patterns no single process could.
- Read patterns.md before the next bid, before chasing a process, before setting
  bid strategy. That is the loop paying off.

Handling:
- This is sensitive competitive intelligence: our bid behavior, our gap to
  clearing price, and our candid read on specific broker relationships. Treat
  access and any export accordingly (see _config/store-schema.md).

Starting state:
- Empty. records/ fills as competitive processes resolve and the loop runs;
  patterns.md begins as hypotheses and earns confidence as records accumulate.
-->
