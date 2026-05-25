# The Store

<!--
This folder is the workspace's memory and its actual deliverable. It is what
makes this a learning loop rather than a linear pipeline: stages 01 and 02 read
from here for context, and stage 03 writes back here. The output of the
workflow does not leave the building — it accumulates in this folder.

Contents:
- records/        One file per IC decision, written by 03_capture in the store
                  schema. Append-only history. Do not overwrite.
- patterns.md     The rolled-up, firm-level decision intelligence: the conditions
                  the committee imposes again and again, its revealed risk
                  appetite by segment, its recurring concerns, and the precedents
                  a new deal is measured against. Updated on each capture. This is
                  the payoff-grain output and the file other workspaces
                  (deal-pipeline's IC stage, deal-screening) read.

How the value compounds:
- One record is nearly worthless. Ten begin to suggest. A hundred, tagged
  consistently by asset type, strategy, decision lane, and condition/concern
  category, reveal the committee's standing mind no single decision could — the
  judgment that otherwise lives only in a few partners' heads.
- Read patterns.md before the next memo goes to committee, before chasing a deal
  the IC may reject, or whenever you want to know the committee's standing
  conditions and precedent in a segment. That is the loop paying off — the memo
  pre-empts the conditions and cites the precedent instead of relitigating it.

Handling:
- This is sensitive intelligence: it documents the firm's own decision patterns,
  its revealed risk appetite, and candid reads on dissent and on what the
  committee really weighed. Treat access and any export accordingly (see
  _config/store-schema.md). The standing conditions and risk-appetite boundaries
  may flow to deal-pipeline and deal-screening; the named-dissent detail and the
  inferred-rationale reads stay internal to the team and the IC.

Starting state:
- records/ is empty and fills as deals are decided at IC and the loop runs.
- patterns.md ships as a hypotheses-only scaffold (0 records) so its shape is clear
  from day one. Seed a few falsifiable hypotheses if you like, but do not let anything
  in it shape a memo until real records support it (a stated pattern needs 3+).
  See _example/_store/patterns.md for what it looks like after a few runs.
-->
