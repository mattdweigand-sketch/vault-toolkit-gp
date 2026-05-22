# LP Engagement Learning Workspace

## What This Is
A workspace for learning, systematically, why LPs commit or pass — and turning that into intelligence that sharpens the next raise. When an LP's engagement resolves (a commitment, or a decline), this workspace assembles the engagement record, runs a consistent forensic on what actually drove the outcome, and captures a structured record into an accumulating store. The store is the point: over many records it reveals which LP segments convert, which objections recur, where the firm's raise consistently stalls. Built for an IR, capital-raising, or partner team that wants its fundraising to compound instead of restarting every fund.

This is not a CRM and it does not track the pipeline — your CRM owns that. This workspace does the one thing the CRM does not: it explains *why*, and remembers.

## A Different Shape: the Learning Loop
The other workspaces in this toolkit are linear — a request or a deal or a reporting cycle flows through stages and the output leaves: a notice sent, a deal decided, a letter distributed. This workspace is a **loop**. Its output does not leave; it is deposited into the workspace's own memory (`_store/`) and read back to inform future runs and other workspaces. Three properties make it different:
- **The flow is circular.** `01_signal` and `02_analysis` read from the store for context; `03_capture` writes back to it. The output's destination is the system's own future input.
- **The deliverable is the store, not the per-run record.** A single LP write-up is nearly worthless alone. The asset is the accumulating corpus and the patterns that emerge across it.
- **It is retrospective.** It is triggered by an outcome that already happened, and it exists to digest that outcome, not to produce a forward deliverable.

If you have used the FAQ bank in lp-inquiries or the pass log in deal-screening, this is that write-back instinct made into the whole workflow.

## Current State
- This is a reference architecture. The store is empty.
- To use: copy the folder, populate _config with your debrief question set, segment taxonomy, and store schema, then run the loop each time an LP engagement resolves.

## Structure
```
lp-engagement-learning/
  CLAUDE.md              # You are here.
  CONTEXT.md             # Workflow routing. How the loop closes.
  01_signal/
    CONTEXT.md           # Stage contract: assemble the engagement record from the CRM.
    output/              # The factual engagement record for one LP.
  02_analysis/
    CONTEXT.md           # Stage contract: forensic on why, against the canonical questions.
    output/              # The structured analysis for one LP.
  03_capture/
    CONTEXT.md           # Stage contract: write to the store, update the patterns.
    output/              # Capture log: what was written and which patterns moved.
  _config/               # Debrief questions, segment taxonomy, store schema.
  _store/                # THE ASSET. Accumulating records + the rolled-up patterns.
```

## How to Use
1. Read CONTEXT.md to understand how the loop closes.
2. Populate _config/ with your canonical debrief questions, your LP segment taxonomy, and your store schema.
3. When an LP commits or passes, start in 01_signal. Assemble the engagement record from the CRM.
4. Move to 02_analysis. Run the forensic against the canonical questions so this record is comparable to every other.
5. Move to 03_capture. A human validates the "why," then the record is written to the store and the patterns are updated.
6. Read `_store/patterns.md` before the next raise, the next prospect, or whenever you prep an engagement — that is the loop paying off.

## Key Decisions
- **The store is the deliverable.** Treat the per-LP record as an input to the asset, not the asset. Resist the urge to make any single write-up perfect; invest instead in making records comparable so the corpus is queryable.
- **Comparability over richness.** Every record answers the same canonical questions from _config, in the same structure. A pile of beautifully written but non-comparable narratives cannot reveal a pattern. This is Constraint 04 (Session Consistency) as the core design principle.
- **The CRM is the source; the model never invents the record.** Touchpoints, timeline, materials, and the outcome come from the CRM. The model assembles and analyzes; it does not recall an interaction from memory. See Constraint 09.
- **A human validates the why before it is captured.** The analysis is the model's proposed explanation. Causal claims about why an LP committed or passed are exactly the thing that, if wrong, poisons the store. A person confirms the "why" before it becomes institutional memory.
- **The store feeds other workspaces.** `_store/patterns.md` is meant to be read by capital-raising prep and prospect work, not just by this workspace. The loop's value is realized when its intelligence shapes a future engagement.
- **Treat the store as sensitive.** Why an LP passed, an objection, a relationship dynamic — this is confidential internal intelligence. Handle and store it accordingly.

## Constraints That Apply
Built against the GP Operating Toolkit. Most relevant: **04 (Session Consistency)** — the load-bearing one here, **03 (Context Hygiene)**, **08 (Handoff Readiness)**, and the universal **06 (Layer Triage)** and **09 (Platform Boundary)**.

## Layer Annotations
- CLAUDE.md: L0 (always loaded, orientation)
- CONTEXT.md: L1 (workflow routing)
- Stage CONTEXT.md files: L2 (stage contracts)
- _config/ files: L3 (reference: questions, taxonomy, schema)
- _store/ files: L3/L4 hybrid — persistent memory read by future runs (L3-like) and written each run (L4-like). This dual role is the signature of the learning-loop shape.
- The CRM engagement data and per-run stage outputs: L4 (working artifacts)
