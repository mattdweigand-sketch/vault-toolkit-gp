# IC Memo Intelligence Workspace

## What This Is
A workspace for turning the firm's investment-committee decisions into compounding institutional memory. Every time a deal goes to IC and a decision is rendered — approved, approved with conditions, declined, or tabled — this workspace assembles the factual decision record from the memo and the committee's deliberation, runs a consistent forensic on *what the committee actually weighed and decided*, and captures a structured record into an accumulating store. The store is the point: over many records it reveals the conditions the committee imposes again and again, its revealed risk appetite by segment (the leverage ceiling it will not cross, the markets it keeps passing on), the precedents a new deal can be measured against ("we declined a near-identical deal in 2023, here is why"), and the concerns it raises most. This is the judgment that today lives in a few senior partners' heads and walks out the door when they leave. Built for an IC chair, a deal team, or a head of acquisitions that wants the firm's decision-making to compound — so the next memo pre-empts the committee's standing conditions, cites precedent instead of relitigating it, and reflects what the IC actually cares about — instead of relearning the committee's mind one deal at a time.

This is not a memo-authoring tool and it does not run the IC gate — the `deal-pipeline` workspace writes the memo and moves the deal through committee, and `one-off-deliverable` can produce a one-off memo. This workspace does the one thing they do not: it remembers what the committee decided and why, *across* deals, and reads it back.

## A Different Shape: the Learning Loop
This is the third instance in the toolkit of the **learning-loop** shape — a sibling of `deal-win-loss-learning` (why we win or lose competitive bids) and `underwriting-backtest` (why realized deals beat or missed their underwriting), pointed this time at the firm's own committee judgment. The other workspaces are linear — a request or a deal or a reporting cycle flows through stages and the output leaves. This one is a **loop**. Its output does not leave; it is deposited into the workspace's own memory (`_store/`) and read back to inform future runs and other workspaces. Three properties make it different:
- **The flow is circular.** `01_record` and `02_analysis` read from the store for context; `03_capture` writes back to it. The output's destination is the system's own future input.
- **The deliverable is the store, not the per-run record.** A single decision write-up is nearly worthless alone. The asset is the accumulating corpus and the decision precedent and revealed preferences that emerge across it.
- **It is retrospective.** It is triggered by a decision that has already been made, and it exists to digest that decision, not to produce a forward deliverable.

If you have used `deal-win-loss-learning` or `underwriting-backtest`, this is the same loop with the config swapped: the bid table (or the assumption table) becomes the decision record, and the broker's "why you lost" becomes the committee's "why we approved / conditioned / declined." (Same shape, swap the config and the taxonomy.)

## One Thing That Differs From the Backtest Sibling
`underwriting-backtest` has a **deterministic numeric core** — `01_reconcile` computes underwritten-minus-actual variance, and the store rolls up into a quantitative calibration table. This loop has no such arithmetic. It is **qualitative end to end, like the win/loss sibling**: the decision record is conditions, concerns, dissents, and rationale, and the patterns roll up by *tallying controlled tags* ("the IC conditioned a DSCR stress test on 70% of value-add multifamily approvals"), not by computing a model. There is no actual to estimate and no return to recompute. Keep that in mind: the value here is in capturing the committee's reasoning faithfully and tagging it consistently, not in any calculation.

## Current State
- This is a reference architecture. The store is empty. A fully worked, populated copy lives in `_example/` — read it to see what the loop looks like after a few runs.
- To use: copy the folder, populate _config with your canonical IC questions, decision taxonomy, and store schema, then run the loop each time a deal is decided at IC.

## Structure
```
ic-memo-intelligence/
  CLAUDE.md              # You are here.
  CONTEXT.md             # Workflow routing. How the loop closes.
  01_record/
    CONTEXT.md           # Stage contract: assemble the factual decision record from the memo + IC minutes.
    output/              # The factual decision record for one deal.
  02_analysis/
    CONTEXT.md           # Stage contract: forensic on what the committee weighed, against the canonical questions.
    output/              # The structured analysis for one decision.
  03_capture/
    CONTEXT.md           # Stage contract: validate the analysis, write to the store, update the patterns.
    output/              # Capture log: what was written and which patterns moved.
  _config/               # IC questions, decision taxonomy, store schema.
  _store/                # THE ASSET. Accumulating records + the rolled-up decision intelligence.
  _example/              # A fully worked, populated run (Ridgeline Capital): one pass end-to-end + a 3-record store.
```

## How to Use
1. Read CONTEXT.md to understand how the loop closes.
2. Populate _config/ with your canonical IC questions, your decision taxonomy (asset type, deal-size band, market, strategy, decision lane, the controlled list of condition categories and concern categories, decisive factor), and your store schema.
3. When a deal is decided at IC — approved, approved with conditions, declined, or tabled — start in 01_record. Assemble the decision record from the **IC memo** and the **committee's minutes/notes**: recommendation, decision lane, conditions imposed, dissents, concerns raised, the vote.
4. Move to 02_analysis. Run the forensic against the canonical questions so this record is comparable to every other, keeping the committee's *stated* reasoning distinct from your *inferred* reasoning, and reading the store to flag whether this decision confirms, extends, or departs from precedent.
5. Move to 03_capture. The IC chair / deal lead validates the analysis — especially the stated-vs-inferred rationale — then the record is written to the store and the patterns are updated.
6. Read `_store/patterns.md` before the next memo goes to committee, or whenever you want to know the IC's standing conditions, revealed risk appetite, or precedent in a segment — that is the loop paying off.

## Key Decisions
- **The store is the deliverable.** Treat the per-decision record as an input to the asset, not the asset. Resist the urge to make any single write-up perfect; invest instead in making records comparable so the corpus is queryable as a body of decision precedent.
- **Comparability over richness.** Every record answers the same canonical questions from _config, in the same structure, tagged by the same taxonomy and the same controlled condition and concern categories. A pile of beautifully written but non-comparable minutes cannot reveal that the committee always conditions on the same thing. This is Constraint 04 (Session Consistency) as the core design principle.
- **The memo and the minutes are the source; the model never invents the decision.** The recommendation comes from the memo; the decision, conditions, dissents, and concerns come from the official IC minutes/notes. The model assembles and analyzes; it does not recall a decision from memory or paraphrase a condition the committee did not actually impose. See Constraint 09.
- **Capture at decision time, before outcomes are known.** Record the committee's judgment as it was made, not after the deal has played out. Capturing contemporaneously is itself a defense against hindsight — it stops a later good or bad outcome from rewriting how confident or how worried the room actually was (Constraint 10: pin what the committee said, when).
- **Stated vs. inferred rationale is the load-bearing defense.** The single most damaging thing this workspace can do is record a tidy, coherent rationale the committee never actually articulated — manufacturing a precedent that did not exist and quietly teaching the firm its IC is more consistent than it is. Two defenses: the canonical questions force the committee's *stated* reasons apart from the analyst's *inferred* reading, and the human validation gate at capture stops an unvalidated rationale from entering the store. This is the analog of the win/loss sibling's stated-vs-assessed-reason defense.
- **A human validates the analysis before it is captured.** The analysis is the model's proposed reading of what the committee weighed. Claims about *why* the IC decided as it did are exactly the thing that, if wrong, poisons the store. The IC chair / deal lead confirms the analysis — especially the inferred rationale and the precedent read — before it becomes institutional memory.
- **The store feeds other workspaces.** `_store/patterns.md` is meant to be read by `deal-pipeline`'s IC stage — so the next memo pre-empts the committee's standing conditions and cites precedent — and by `deal-screening`, so a deal the IC has reliably declined in a segment does not get advanced again. The loop pays off outside itself.
- **Treat the store as sensitive.** It documents the firm's own decision patterns, its revealed risk appetite, and candid reads on what the committee really weighed and where members dissented. That is confidential internal intelligence; handle and store accordingly, and be deliberate about what leaves this workspace.

## Constraints That Apply
Built against the GP Operating Toolkit. Most relevant: **04 (Session Consistency)** — the load-bearing one here, **10 (Source Provenance)** — the memo, minutes, and the decision itself are sourced data, **03 (Context Hygiene)**, **08 (Handoff Readiness)**, and the universal **06 (Layer Triage)** and **09 (Platform Boundary)**.

## Layer Annotations
- CLAUDE.md: L0 (always loaded, orientation)
- CONTEXT.md: L1 (workflow routing)
- Stage CONTEXT.md files: L2 (stage contracts)
- _config/ files: L3 (reference: questions, taxonomy, schema)
- _store/ files: L3/L4 hybrid — persistent memory read by future runs (L3-like) and written each run (L4-like). This dual role is the signature of the learning-loop shape.
- The memo / IC minutes / decision data and per-run stage outputs: L4 (working artifacts)
