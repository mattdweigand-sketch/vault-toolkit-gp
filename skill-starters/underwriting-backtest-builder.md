# SKILL: Underwriting Backtest Workspace Builder

## Description
Builds a customized learning-loop workspace by asking diagnostic questions about how a firm could capture and learn from why its realized deals beat or missed the underwriting they were bought on, then assembling a folder structure, stage contracts, config files, and a store based on the answers.

## When to Use
When a firm wants its underwriting to compound — to systematically check, deal by deal, whether the assumptions it underwrote on held up, and turn that into calibrated future models — rather than repeating the same forecasting errors one deal at a time. Sharper assumptions mean better-priced deals, a more honest track record, and a fundraising story backed by evidence. This is a learning loop, not a portfolio-accounting system or a deal pipeline; it explains *why* a realized result diverged from the underwriting, separates skill from luck, and remembers.

## Process

### Phase 1: Diagnosis (ask before building)

> **Firm facts are already captured.** Run Setup wrote the firm's name, asset classes, systems of record, team, and voice to `_shared-config/` (firm-profile.md and voice-and-tone.md). Read those first. Do NOT re-ask firm-level facts — confirm them if needed. Ask only the workflow-specific questions below. If `_shared-config/firm-profile.md` does not exist yet, the firm skipped orientation; capture the basics first, then continue.

> **Learnings compound.** Before asking diagnostic questions, read `_shared-config/learnings.md`, but only `## General` and `## underwriting-backtest`. Apply reusable rules. Ignore task history.

Ask the following questions one at a time. Wait for each answer before proceeding.

**Question 1: How do you learn a deal has realized, and what triggers a backtest?**
"What counts as a realization worth backtesting — a full exit/sale, a capital return, or also interim checkpoints like the end of a business-plan year or a refinance? This establishes the trigger and what each run digests."

**Question 2: Where does the approved model of record and the realized actuals live?**
"Where is the underwriting the deal was *approved* on at IC — and which version is authoritative if the model was revised mid-hold? And where do the realized actuals come from — fund accounting, the exit closing, property-management reports? This is the governed source; the model must never invent or estimate a number it can pull, and the backtest must measure against the IC-approved model, not a moving target."

**Question 3: Which assumptions actually move your returns?**
"Which underwriting assumptions actually decide whether you beat or miss — going-in cap, rent/revenue growth, opex, lease-up/absorption, exit cap, hold, leverage, capex? This seeds both the canonical question bank and the controlled assumption-category tag, and it keeps each backtest focused on the handful that mattered rather than reconciling the whole model."

**Question 4: How do you tell your own skill from a market tailwind?**
"When a deal beats its underwriting, how do you currently judge how much was your edge — thesis, execution, forecast — versus market movement you did not create, like cap-rate compression or a sector run? How honest is that conversation today? This sets the load-bearing skill-vs-luck defense; banking a tailwind as skill is the single most damaging thing this store can do."

**Question 5: Who owns the attribution call, and who validates it before it's captured?**
"Who internally owns the final read on why a deal hit or missed — the underwriter, head of acquisitions, the IC? This sets the human-validation gate. Causal claims, and especially the skill-vs-luck split, must be signed off before they enter the store."

**Question 6: What would you change if you knew exactly where your underwriting is biased?**
"If, across 50 realized deals, you knew exactly which assumptions you systematically get wrong and by how much, what would you change — your standard exit-cap assumption, your lease-up timeline, which segments you underwrite more conservatively? This defines the payoff and which future investment work consumes the store: screening assumptions, diligence questions, underwriting standards, or IC pressure tests."

### Phase 2: Assembly

Based on the answers, build the workspace:

1. Start from the template: copy the matching architecture (`architectures/underwriting-backtest/` before finalize, `_kit/architectures/underwriting-backtest/` after) as your starting point into `workspaces/<name>/` (the firm's live workspaces live there; rename <name> for the deal/fund/cycle) — its CLAUDE.md, CONTEXT.md, stage CONTEXT.md contracts, _config/ files, _store/ (README + patterns.md scaffold), and worked `_example/` are drafts and a reference to customize against, not blank files to write from scratch (copy the folder contents, not any .DS_Store). Then adapt to their answers: three stages (reconcile, attribution, capture), plus _config/ and the _store/ folder with records/ and patterns.md. The _store/ is the deliverable — make it visible.
2. Write CLAUDE.md: what this is, the learning-loop shape and how it differs from a linear pipeline (the output feeds back into the store), the one way it differs from the win/loss sibling (a deterministic variance core — the arithmetic is not an AI task), current state, structure map, how to use. Call out the skill-vs-luck guardrail in Key Decisions.
3. Write CONTEXT.md: the stage map, how the loop closes (capture writes the store; reconcile and attribution read it back), how the store feeds future underwriting standards, screening assumptions, diligence questions, and IC pressure tests, and the AI-vs-Platform table (the approved model and fund accounting own what happened and the variance math; the model proposes the why and keeps skill vs. luck distinct; a human validates it).
4. Customize each stage's CONTEXT.md from the template's contract — adjust the existing contract, do not write a new one from scratch.
5. Create config templates: underwriting-questions.md (the canonical set — the most important file, with the skill-vs-luck question load-bearing), assumption-taxonomy.md (controlled tags including the controlled list of assumption categories, cause class, and skill/luck attribution), store-schema.md (record shape with underwritten-vs-actual and the gap per assumption, the calibration-patterns structure plus a skill-vs-luck ledger, privacy handling). Populate from their answers.
6. Set up _store/: keep the README, an empty append-only records/ folder, and the hypotheses-only patterns.md scaffold (0 records). Seed a few falsifiable calibration hypotheses if useful, but mark them untested and do not let them retune underwriting. See _store/README and _example/_store/patterns.md for the shape.
7. Flag what you could not confirm. Populate _config/before-you-trust-this.md: list every value you could not get directly from the firm — especially which model version is the underwriting of record — mark each `[NEEDS CONFIRMATION — <owner>]`, name who signs off, and never invent these silently. Use `[TBD]` for values simply awaiting real data. (Constraint 08.)
8. Demonstrate one stage end to end — but note this loop usually cannot run a live backtest at onboarding, because it needs a realized deal and a fund may have none yet. If a realized deal exists, run the reconcile stage on it against its "Done Looks Like" line. If none has realized, point the client at the worked _example/ as the stand-in run, and mark the workspace "stands up now, activates on the first realized exit." Do not treat the empty store as a failed build.

### Phase 3: Orientation

After building, walk the user through:
- "Here is what I built and why each piece exists."
- "This is a loop, not a pipeline. The deliverable is the store — a calibration table — not any single backtest. Resist perfecting one record; invest in making records comparable so the corpus reveals systematic bias."
- "Comparability is the whole game — every attribution answers the same canonical questions in the same shape and uses the same taxonomy tags, including the same controlled list of assumption categories (Constraint 04). Changing the questions breaks comparability with prior records."
- "There is a bright line between arithmetic and judgment: reconcile *computes* the variance from the approved model and fund accounting; attribution *explains* it. The model never invents or estimates an actual, and it never recomputes a return it can source (Constraint 06)."
- "Skill vs. luck is the load-bearing defense. A realized IRR that rode cap-rate compression, recorded as proof the thesis was right, quietly teaches the firm it underwrites better than it does. The skill-vs-luck question and the human validation gate are the defenses against banking market beta as edge."
- "A human — the underwriter / head of acquisitions / IC — validates the attribution before it is captured. A confident, wrong attribution in the store bends future assumptions."
- "Read patterns.md before the next underwrite — and feed its calibration adjustments to screening assumptions, diligence questions, underwriting standards, and IC pressure tests. That is the loop paying off."

## Important Notes
- Do not build before completing the diagnosis. The questions are the skill.
- The canonical underwriting questions are the highest-value config. Spend the most time here; a loose or shifting question set makes the store un-aggregatable. The skill-vs-luck question is load-bearing — do not drop it.
- The assumption-category list is a controlled list on purpose. The store's core job — "which assumptions do we systematically miss, and by how much" — requires a stable vocabulary of the assumptions the firm underwrites on.
- Pin the model of record. Backtesting against a model revised mid-hold measures nothing; record the IC-approved version and date in every run (Constraint 10).
- This is sensitive intelligence — it documents the firm's own systematic underwriting errors and the candid skill-vs-luck read on its track record. Address access and handling in store-schema.md; the skill-vs-luck ledger stays internal to the deal team and IC.
- It does not replace the model or fund accounting — it rides on them. The numbers are the platform's; this workspace adds the why, the skill-vs-luck split, and the memory. The loop is triggered by realized deals and pays back into the assumptions other workspaces underwrite on.
- Load and name the constraints this workflow uses: 04 (Session Consistency) — the load-bearing one, 10 (Source Provenance), 03 (Context Hygiene), 08 (Handoff Readiness), plus the universal 06 and 09.
- Load and name the modules this workflow uses: `validated-memory-store` and `handoff-brief`.
- Always annotate files with their ICM layer (L0–L4); note that _store/ is an L3/L4 hybrid — the signature of the learning-loop shape.
