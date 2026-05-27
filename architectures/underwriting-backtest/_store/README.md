# The Store

<!--
This folder is the workspace's memory and its actual deliverable. It is what
makes this a learning loop rather than a linear pipeline: stages 01 and 02 read
from here for context, and stage 03 writes back here. The output of the
workflow does not leave the building — it accumulates in this folder.

Contents:
- records/        One file per realized deal, written by 03_capture in the store
                  schema. Append-only history. Do not overwrite.
- patterns.md     The rolled-up, firm-level calibration: which assumptions run
                  optimistic or conservative and by roughly how much, in which
                  segments, plus the skill-vs-luck ledger on realized returns.
                  Updated on each capture. This is the payoff-grain output and
                  the file future underwriting standards, screening assumptions,
                  diligence questions, and IC pressure tests read.

How the value compounds:
- One record is nearly worthless. Ten begin to suggest. A hundred, tagged
  consistently by asset type, strategy, vintage, and assumption category, reveal
  systematic biases no single deal could.
- Read patterns.md before the next underwrite, before setting a going-in or
  exit-cap assumption, before tuning the firm's standard assumptions. That is the
  loop paying off — the calibration retunes the assumptions other workspaces run on.

Handling:
- This is sensitive intelligence: it documents the firm's own systematic
  underwriting errors and the candid skill-vs-luck read on its track record.
  Treat access and any export accordingly (see _config/store-schema.md). The
  calibration adjustments may flow to future investment work; the
  "how much of our track record is luck" read stays internal to the team and IC.

Starting state:
- records/ is empty and fills as deals realize and the loop runs.
- patterns.md ships as a hypotheses-only scaffold (0 records) so its shape is clear
  from day one. Seed a few falsifiable hypotheses if you like, but do not let anything
  in it retune underwriting until real records support it (a stated pattern needs 3+).
  See _example/_store/patterns.md for what it looks like after a few runs.
-->
