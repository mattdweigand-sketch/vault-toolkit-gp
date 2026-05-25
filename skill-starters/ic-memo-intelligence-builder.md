# SKILL: IC Memo Intelligence Workspace Builder

## Description
Builds a customized learning-loop workspace by asking diagnostic questions about how a firm could capture and learn from its own investment-committee decisions — the conditions it imposes, the concerns it raises, its revealed risk appetite, and the precedents it sets — then assembling a folder structure, stage contracts, config files, and a store based on the answers.

## When to Use
When a firm wants its committee's decision-making to compound — to systematically capture what the IC decides and why, and turn that into institutional memory the next memo can use — rather than relearning the committee's mind one deal at a time and watching that judgment walk out the door when senior partners leave. A store of decision precedent means memos that pre-empt standing conditions, cite precedent instead of relitigating it, and reflect what the committee actually cares about. This is a learning loop, not a memo-authoring tool or a deal pipeline; it remembers what the committee decided and why, *across* deals. (deal-pipeline authors the memo and runs the IC gate; this workspace does not author anything.)

### Phase 1: Diagnosis (ask before building)

> **Firm facts are already captured.** Run Setup wrote the firm's name, asset classes, systems of record, team, and voice to `_shared-config/` (firm-profile.md and voice-and-tone.md). Read those first. Do NOT re-ask firm-level facts — confirm them if needed. Ask only the workflow-specific questions below. If `_shared-config/firm-profile.md` does not exist yet, the firm skipped orientation; capture the basics first, then continue.

Ask the following questions one at a time. Wait for each answer before proceeding.

**Question 1: How is a deal decided at IC, and what counts as the trigger?**
"What are your committee's decision lanes — approve, approve-with-conditions, decline, table — and what event triggers a capture: a formal vote, a memo sign-off, a tabled deal that comes back? This establishes the trigger and what each run digests. The loop fires at decision time, on purpose — capturing the committee's judgment before outcomes are known is what keeps hindsight from rewriting it."

**Question 2: Where does the memo live, and what is the authoritative record of the decision?**
"Where is the IC memo that was put to the committee, and what is the authoritative record of what the committee actually decided — minutes, a decision log, the IC chair's notes? This is the governed source; the model narrates the decision, it never invents a condition the committee did not impose or smooths a split vote into consensus."

**Question 3: What does your committee actually decide on?**
"What dimensions decide your IC outcomes — basis, leverage, market, sponsor, structure, execution risk? And what conditions does it tend to impose? This seeds both the canonical question bank and the controlled condition-category and concern-category tags, and keeps each record focused on the few things that actually moved the decision."

**Question 4: How do you tell what the committee *said* from what actually drove the decision?**
"When the minutes record a rationale — 'approved on the sponsor's track record' — how confident are you that is what really drove it, versus a tidier reason than the room actually gave? How honest is that distinction in your notes today? This sets the load-bearing stated-vs-inferred defense; recording a rationale the committee never articulated manufactures precedent that never existed."

**Question 5: Who owns the read on 'why the committee decided that,' and who validates it before capture?**
"Who internally owns the final read on why the IC decided as it did — the IC chair, the deal lead? This sets the human-validation gate. Rationale claims, and especially the inferred-vs-stated split, must be signed off before they enter the store."

**Question 6: What would you change if you knew exactly how your committee decides?**
"If, across 50 decisions, you knew exactly which conditions your IC always imposes, where its leverage or market lines are, and what it worries about most, what would change — how memos are written, which deals you advance, what you pre-empt? This defines the payoff and which workspaces consume the store (deal-pipeline's IC stage, deal-screening)."

### Phase 2: Assembly

Based on the answers, build the workspace:

1. Start from the template: copy the matching architecture (`architectures/ic-memo-intelligence/` before finalize, `_kit/architectures/ic-memo-intelligence/` after) as your starting point into `workspaces/<name>/` (the firm's live workspaces live there; rename <name> for the fund/vehicle/committee) — its CLAUDE.md, CONTEXT.md, stage CONTEXT.md contracts, _config/ files, _store/ (README + patterns.md scaffold), and worked `_example/` are drafts and a reference to customize against, not blank files to write from scratch (copy the folder contents, not any .DS_Store). Then adapt to their answers: three stages (record, analysis, capture), plus _config/ and the _store/ folder with records/ and patterns.md. The _store/ is the deliverable — make it visible.
2. Write CLAUDE.md: what this is, the learning-loop shape and how it differs from a linear pipeline (the output feeds back into the store), the boundary (it authors nothing — deal-pipeline authors the memo), the one way it differs from the backtest sibling (no deterministic core — it is qualitative end to end, like win/loss), current state, structure map, how to use. Call out the stated-vs-inferred rationale guardrail in Key Decisions.
3. Write CONTEXT.md: the stage map, how the loop closes (capture writes the store; record and analysis read it back), how the store feeds deal-pipeline's IC stage and deal-screening, and the AI-vs-Platform table (the memo and minutes own what was decided; the model proposes the reading and keeps stated vs. inferred distinct; a human validates it).
4. Customize each stage's CONTEXT.md from the template's contract — adjust the existing contract, do not write a new one from scratch.
5. Create config templates: ic-questions.md (the canonical set — the most important file, with the stated-vs-inferred question load-bearing), decision-taxonomy.md (controlled tags including the controlled condition-category and concern-category lists, decision lane, decisive factor, precedent relationship), store-schema.md (record shape with conditions/concerns tagged and the patterns roll-up organized as standing conditions / revealed risk appetite / recurring concerns / decision precedents, privacy handling). Populate from their answers.
6. Set up _store/: keep the README, an empty append-only records/ folder, and the hypotheses-only patterns.md scaffold (0 records). Seed a few falsifiable hypotheses about the committee's standing mind if useful, but mark them untested and do not let them shape a memo. See _store/README and _example/_store/patterns.md for the shape.
7. Flag what you could not confirm. Populate _config/before-you-trust-this.md: list every value you could not get directly from the firm — especially which document is the authoritative IC minutes of record and who may access the store's named-dissent detail — mark each `[NEEDS CONFIRMATION — <owner>]`, name who signs off, and never invent these silently. Use `[TBD]` for values simply awaiting real data. (Constraint 08.)
8. Demonstrate one stage end to end. If a deal has already been decided at IC, run the record stage on it and check the output against its "Done Looks Like" line. If none has been decided yet, point the client at the worked _example/ as the stand-in run, and mark the workspace "stands up now, activates on the first IC decision."

### Phase 3: Orientation

Walk the client through what they now have:
- "This is a **loop**, not a pipeline. The output never leaves — `03_capture` writes it into `_store/`, and the next decision's `01_record` and `02_analysis` read it back. The store is the deliverable, not any single record."
- "The **store is the asset.** One decision is nearly worthless; the corpus reveals the committee's standing conditions, its risk-appetite lines, and the precedents a new deal is measured against — the judgment that otherwise lives only in a few partners' heads."
- "**Comparability is everything.** Every record answers the same canonical IC questions in the same order and is tagged with the same controlled condition and concern categories. That is what lets the store surface 'the IC conditions a DSCR stress test on 70% of value-add MF approvals.'"
- "The **stated-vs-inferred rationale guardrail** is load-bearing. The most damaging thing this workspace can do is record a tidy rationale the committee never gave — manufacturing precedent. Keep what the minutes say apart from what you read as the real driver, and flag the split for the validator."
- "There is a **human validation gate** at capture. The IC chair / deal lead signs off on the rationale and the precedent read before anything becomes institutional memory."
- "The **payoff is outside this workspace.** `_store/patterns.md` feeds deal-pipeline's IC stage — the next memo pre-empts standing conditions and cites precedent — and deal-screening, so a deal the IC reliably declines in a segment is not advanced again."

## Important Notes
- Diagnose before building. The canonical IC questions, the controlled condition/concern categories, and who validates are the load-bearing answers; do not skip them to get to assembly.
- The canonical questions are the most important file — they are what make records comparable, and comparability is what lets the store reveal the committee's standing mind. Keep them stable and versioned.
- The condition-category and concern-category lists are controlled lists on purpose. "What does the IC always require, and what does it always worry about" is the highest-value pattern, and it needs a stable vocabulary, not free text.
- Capture at decision time, before outcomes are known — it is itself a defense against hindsight rewriting how confident or worried the room was.
- This does not replace deal-pipeline or the IC gate. deal-pipeline authors the memo and moves the deal through committee; this workspace remembers the decision afterward. See Constraint 09.
- This is the qualitative twin of deal-win-loss-learning — there is no arithmetic here. If you find yourself computing rather than capturing and tagging, you have left the workflow's lane (Constraint 06).
- Load and name the constraints this workflow uses: **04 (Session Consistency)** — load-bearing, **10 (Source Provenance)** — the memo, minutes, and decision are sourced data, **03 (Context Hygiene)**, **08 (Handoff Readiness)**, and the universal **06 (Layer Triage)** and **09 (Platform Boundary)**.
- Annotate the ICM layer of each file you build (CLAUDE.md L0, CONTEXT.md L1, stage contracts L2, _config/ L3, _store/ L3/L4 hybrid — read by future runs and written each run, the signature of the learning-loop shape).
