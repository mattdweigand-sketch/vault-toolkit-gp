# GP AI Architecture Improvement Plan

## Decision

The architecture library should be smaller and sharper.

Use the 60/30/10 filter:
- 60% belongs in platforms, databases, calculation engines, and established software.
- 30% belongs in rules, routing, templates, and deterministic automation.
- 10% belongs in AI: judgment, synthesis, source interpretation, narrative, and memory.

That means the toolkit should not try to rebuild DDQs, investor records, capital activity,
dashboards, pipeline tracking, fund accounting, data extraction, or valuation engines. Juniper
Square, Dealpath, DealCloud, Chronograph, Canoe, iLevel-style tools, and similar platforms already
cover much of that layer.

The toolkit should own the layer above the platforms: how the firm thinks, decides, explains, and
learns.

## Architecture Rule

Add an architecture only when the work depends on firm-specific judgment or source interpretation
that platforms do not own.

Do not add an architecture when the work is primarily:
- System of record.
- Workflow state.
- Entitlement or permissioning.
- Calculation or reconciliation.
- Audit trail.
- Dashboarding.
- Standard document extraction.
- Platform-native execution.

Every architecture should answer five questions:
- What platform owns the record?
- What deterministic tool owns the math?
- What rules own routing?
- What judgment does AI add?
- What human approves the output?

## Highest-Leverage GP AI Areas

### 1. Investment Judgment

AI should make the investment decision sharper, not make the decision.

Best uses:
- Pressure-test IC memos.
- Map diligence evidence and unresolved questions.
- Challenge deal theses.
- Compare a proposed deal to IC precedent.
- Turn market research into investment-box changes.

Why this belongs here: platforms can store deal data and manage the pipeline, but they do not
capture the firm's internal judgment about why a risk matters, what would change the answer, or
how today's deal compares to prior committee decisions.

### 2. Portfolio Intervention

AI should turn portfolio signals into attention, diagnosis, and action.

Best uses:
- Explain business-plan variance.
- Separate timing issues from structural misses.
- Draft watchlist rationale.
- Produce an action plan with owner, deadline, and next evidence point.
- Frame hold / sell / refinance decisions.

Why this belongs here: portfolio systems can collect data and show variance. The judgment is why it
matters, whether it changes the plan, and what action should follow.

### 3. Investor Communication Judgment

AI should help explain verified facts, prepare for investor conversations, and handle sensitive
framing.

Best uses:
- Draft LP narrative around platform-verified numbers.
- Prepare likely LP questions before a meeting.
- Frame bad-news explanations.
- Capture recurring LP objections.
- Feed fundraising messaging with what the firm has learned.

Why this belongs here: Juniper Square and similar systems should own investor records, reporting,
DDQs, entitlements, portal delivery, and audit. AI adds judgment only around explanation, context,
and memory.

### 4. Source Control

AI should inspect the evidence before the firm relies on it.

Best uses:
- Data-room inventory.
- Source authority ranking.
- Duplicate, stale-version, and conflict logs.
- Diligence question map.
- Source-backed one-off deliverables.

Why this belongs here: platforms may store or extract documents. The AI value is spotting what the
source set does and does not support before the team drafts or decides.

### 5. Firm Memory

AI should make repeated judgment compound.

Best uses:
- Underwriting backtests.
- IC decision precedent.
- Deal win/loss learning.
- Fundraising objection learning.
- Portfolio post-mortems.

Why this belongs here: platforms hold records, but they rarely turn candid post-mortems into a
usable memory that changes the next underwrite, next IC discussion, next bid, or next LP meeting.

## Recommended Core Architectures

Build toward eight core architectures:

1. `ic-pressure-test`
   - Stage shape: memo intake -> risk challenge -> decision conditions -> precedent capture.
   - AI job: challenge assumptions, surface missing evidence, write IC-ready questions.
   - Platform boundary: deal system stores pipeline and documents; model of record owns math.

2. `diligence-evidence-map`
   - Stage shape: inventory -> authority ranking -> gap / conflict log -> diligence question map.
   - AI job: inspect sources, identify conflicts, map evidence to questions.
   - Platform boundary: data room stores documents; underwriting model owns calculations.

3. `underwriting-backtest`
   - Stage shape: reconcile -> attribution -> capture.
   - AI job: explain why assumptions missed, separate skill from luck, update calibration memory.
   - Platform boundary: approved model and fund accounting own actuals and variance math.

4. `portfolio-intervention`
   - Stage shape: signal -> diagnosis -> action plan -> follow-up.
   - AI job: explain variance, prioritize attention, draft action plan.
   - Platform boundary: portfolio-monitoring system owns actuals, dashboards, and valuations.

5. `hold-sell-refi`
   - Stage shape: position -> alternatives -> IC decision -> execution handoff.
   - AI job: frame alternatives, risks, timing, recommendation, and conditions.
   - Platform boundary: valuation model and fund data own return math and capital implications.

6. `market-thesis-to-investment-box`
   - Stage shape: research -> synthesis -> investment-box update -> downstream handoff.
   - AI job: synthesize evidence, distinguish fact from inference, propose sourcing changes.
   - Platform boundary: market data providers own data; deal platform owns pipeline.

7. `lp-narrative-and-issue-prep`
   - Stage shape: verified facts -> narrative -> likely questions -> approved response posture.
   - AI job: explain platform-verified facts, prepare sensitive language, capture recurring concerns.
   - Platform boundary: Juniper Square or the investor platform owns LP records, figures, DDQ, portal,
     entitlements, and audit.

8. `firm-memory-loop`
   - Stage shape: event signal -> analysis -> validated capture -> pattern update.
   - AI job: standardize post-mortems and make patterns readable before the next decision.
   - Platform boundary: source systems own the facts; humans validate causal claims.

## Implementation State

Done:
- `README.md` explains the 60/30/10 platform-boundary principle and the five high-leverage AI zones.
- `SETUP.md` routes setup through the platform-boundary filter before workflow selection.
- Source provenance is a first-class shape.
- The active top-level `architectures/` folder contains the trimmed core set.
- Matching active builders live in `skill-starters/`.
- Older lifecycle examples are archived under `architectures/_variants/` and
  `skill-starters/_variants/` for reference or migration.

Still worth doing later:
- Add worked `_example/` folders for the new architectures.
- Decide whether any archived variant deserves a simplified active replacement after real user
  demand proves it.

## Final Target

The library should land at 8 core architectures, with older lifecycle examples archived as
variants:

Core:
- `ic-pressure-test`
- `diligence-evidence-map`
- `underwriting-backtest`
- `portfolio-intervention`
- `hold-sell-refi`
- `market-thesis-to-investment-box`
- `lp-narrative-and-issue-prep`
- `firm-memory-loop`

Variants:
- Archived under `architectures/_variants/` and `skill-starters/_variants/`.
- Use only for reference or migration, not primary setup routing.

Do not exceed 10 core architectures. If a proposed workflow does not add a new judgment pattern,
make it a variant.
