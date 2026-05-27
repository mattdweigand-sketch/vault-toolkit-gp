# Agentic OS Import Plan for GP Operating Toolkit

> Historical note: this plan predates the May 2026 architecture trim. It is kept as a completed
> implementation artifact, not as current setup routing. Current routing lives in `SETUP.md`.

## Decision

Use Agentic OS as a pattern source, not a code source.

The GP Operating Toolkit should stay a plain-file operating system for GP workflows. Do not import the Command Centre app, cron runtime, skill marketplace, or installer scripts. Import the small governance patterns that make the toolkit easier to operate, audit, and improve over time.

## Goals

1. Make context loading auditable.
2. Make setup and builder flows improve from user feedback.
3. Reduce routing drift between `architectures/`, `skill-starters/`, constraints, and `SETUP.md`.
4. Tighten onboarding so it feels like a short conversation, not a form.
5. Preserve the toolkit's current promise: no server, no database, no required Git, no scheduled runtime.

## Non-Goals

- Do not add a Next.js app.
- Do not add cron or background jobs.
- Do not add skill install/remove scripts.
- Do not create a plugin marketplace.
- Do not require Claude-specific hooks as a baseline.
- Do not turn `workspaces/` into a client-management layer. `_shared-config/` plus `workspaces/` is already the right GP shape.

## Phase 1: Add a Context Matrix

### Why

The toolkit already has ICM context layers. That explains when files load. What is missing is a per-workflow table that says exactly which files each builder should load, and at what depth.

Agentic OS solves this with a Context Matrix. This is the highest-value import.

### Add

Add a new section to `SETUP.md` after "A Note on Context Layers (ICM)":

```markdown
## Context Matrix

Each builder loads only the context named in this table. Load levels:
- `full` — read the whole file
- `summary` — use a short digest, not the full file
- `pointer` — know the file exists, load only if needed
- `writes` — this builder writes or updates the file
- `—` — do not load
```

Then add one row per workflow:

| Workflow | `_shared-config/firm-profile.md` | `_shared-config/voice-and-tone.md` | `_shared-config/learnings.md` | Constraints | Architecture | Builder |
|---|---|---|---|---|---|---|
| `deal-screening` | full | summary | `## deal-screening` | routed list | pointer | full |
| `deal-pipeline` | full | summary | `## deal-pipeline` | routed list | pointer | full |
| `asset-management` | full | summary | `## asset-management` | routed list | pointer | full |
| `disposition` | full | summary | `## disposition` | routed list | pointer | full |
| `lp-reporting` | full | full | `## lp-reporting` | routed list | pointer | full |
| `lp-inquiries` | full | full | `## lp-inquiries` | routed list | pointer | full |
| `deal-win-loss-learning` | full | summary | `## deal-win-loss-learning` | routed list | pointer | full |
| `underwriting-backtest` | full | summary | `## underwriting-backtest` | routed list | pointer | full |
| `ic-memo-intelligence` | full | summary | `## ic-memo-intelligence` | routed list | pointer | full |
| `market-thesis` | full | full | `## market-thesis` | routed list | pointer | full |
| `one-off-deliverable` | full | full when writing | `## one-off-deliverable` | routed list | pointer | full |

### Update

Update "The Onboarding Sequence" in `SETUP.md`:

- Before opening the builder, check the Context Matrix.
- Load only the files named in that row.
- Do not load all constraints, all architectures, or all `_shared-config`.
- If a builder needs extra context, it must say why before loading it.

### Acceptance Criteria

- A reader can tell what each builder loads without reading the whole repo.
- No builder instruction says "read everything."
- Constraint routing still controls which constraint files are loaded.
- Context Matrix and Constraint Routing do not conflict.

## Phase 2: Add a Per-Workflow Learnings Loop

### Why

The toolkit currently captures firm profile and setup progress, but not reusable learning from user corrections. Agentic OS compounds by writing feedback into per-skill sections. The GP version should write feedback into per-workflow sections.

### Add

Create `_shared-config/learnings.md`:

```markdown
# Learnings

Reusable corrections and preferences discovered while building or running GP workflows.

This is not a task log. Write only lessons that should change future behavior.

## General

## setup

## deal-screening

## deal-pipeline

## asset-management

## disposition

## lp-reporting

## lp-inquiries

## deal-win-loss-learning

## underwriting-backtest

## ic-memo-intelligence

## market-thesis

## one-off-deliverable
```

### Update

In `SETUP.md`, after "Verify", add:

```markdown
## After a Build

Ask: "Anything about this workflow setup that should be remembered for next time?"

If yes, write the reusable rule to `_shared-config/learnings.md` under the workflow section. If the lesson applies across workflows, write it under `## General`. Do not write task logs here.
```

In each `skill-starters/*-builder.md`, add:

```markdown
## Learnings

Before asking diagnostic questions, read `_shared-config/learnings.md`:
- `## General`
- `## <this-workflow>`

Apply only reusable rules. Ignore task history.
```

### Acceptance Criteria

- Every workflow has a learnings section.
- Builders read only `## General` plus their own section.
- User corrections have a durable place to land.
- The file stays rule-like, not diary-like.

## Phase 3: Tighten Onboarding UX

### Why

The setup flow already asks questions one at a time. Agentic OS adds sharper rules: cap questions, skip what was already answered, recommend instead of menuing.

### Update

In `SETUP.md`, revise "Firm Orientation" and "The Onboarding Sequence":

1. Ask one question at a time.
2. Skip a question if a prior answer already covered it.
3. Acknowledge skipped answers briefly.
4. Recommend the first workflow when the user's answer clearly maps to one.
5. Only show the full workflow menu if the user asks or the request is genuinely ambiguous.
6. Keep first-time setup to four firm-level questions plus one workflow-routing question.

### Add

Add this rule near the setup entry point:

```markdown
Do not make onboarding feel like a form. Ask the fewest questions that let you build a useful first workspace. If the user gives enough context in one answer, use it.
```

### Acceptance Criteria

- Setup never dumps the full diagnostic upfront.
- Setup does not re-ask facts already supplied.
- Setup recommends a workflow when the mapping is clear.
- The user still confirms before anything is built.

## Phase 4: Add Registry Reconciliation

### Why

The repo has several lists that must stay aligned:

- `architectures/`
- `skill-starters/`
- `constraints/`
- workflow routing table in `SETUP.md`
- README architecture list

Agentic OS has a reconciliation habit. Import that habit, not the scripts.

### Add

Add a "Registry Reconciliation" section to `SETUP.md`:

```markdown
## Registry Reconciliation

Before adding or modifying a workflow, compare:
- `architectures/<workflow>/`
- `skill-starters/<workflow>-builder.md`
- the Diagnose -> Route table
- the Constraint Routing table
- README workflow list

If a workflow exists on disk but is missing from the tables, add it silently and report what changed.

If a workflow is listed in the tables but missing on disk, stop and ask before removing it from docs.
```

### Optional Script

Later, add `scripts/check-registry.sh`:

- List architecture folders.
- List builder files.
- Grep workflow rows from `SETUP.md`.
- Report missing pairs.
- Do not modify files.

Keep the script optional. The repo should still work without shell access.

### Acceptance Criteria

- Adding a workflow has an explicit checklist.
- Missing architecture-builder pairs are easy to catch.
- Documentation drift has a named process.

## Phase 5: Clarify Multi-Firm / Multi-Workspace Boundaries

### Why

Agentic OS uses `clients/{slug}`. The GP toolkit should not copy that structure because its user is normally one firm building multiple workflows. But the principle is useful: shared methodology at root, firm context isolated, workflow context scoped.

### Update

In `README.md`, add a short "How the layers stay separate" section:

```markdown
- `_shared-config/` is firm-level truth.
- `workspaces/` is workflow-level operating context.
- `architectures/`, `constraints/`, and `skill-starters/` are toolkit methodology.
- After finalize, methodology moves to `_kit/`; firm work stays visible at root.
```

### Acceptance Criteria

- Users understand why this repo does not use `clients/`.
- Finalize reads as a clear separation move, not cleanup.
- The root stays firm-first after finalize.

## Phase 6: Optional Deterministic Checks

### Why

Agentic OS uses hooks for guarantees. The GP toolkit should not require hooks because it is tool-agnostic. But some deterministic checks can be offered as optional scripts.

### Add Later

Optional `scripts/verify-workspace.sh <workspace>`:

- Confirms `CLAUDE.md` exists.
- Confirms root `CONTEXT.md` exists.
- Confirms each stage has `CONTEXT.md`.
- Confirms `_config` required files are populated.
- Confirms `_example/` is labeled as sample data if present.
- Confirms workspace references `_shared-config/`.

### Acceptance Criteria

- The checklist remains in `SETUP.md` as the source of truth.
- The script only verifies. It does not build or rewrite.
- Users without shell access can still follow the manual checklist.

## Implementation Order

1. Add `_shared-config/learnings.md`.
2. Add Context Matrix to `SETUP.md`.
3. Add Learnings Loop instructions to `SETUP.md`.
4. Add Learnings section to all `skill-starters/*-builder.md`.
5. Tighten onboarding rules in `SETUP.md`.
6. Add Registry Reconciliation to `SETUP.md`.
7. Add layer-separation language to `README.md`.
8. Optionally add `scripts/check-registry.sh`.
9. Optionally add `scripts/verify-workspace.sh`.

## Files to Change

Historical note: the builder list below reflects the pre-trim architecture set. Current active
builders live at `skill-starters/*-builder.md`; archived lifecycle builders live under
`skill-starters/_variants/`.

Required:

- `SETUP.md`
- `README.md`
- `_shared-config/learnings.md`
- `skill-starters/_variants/deal-screening-builder.md`
- `skill-starters/_variants/deal-pipeline-builder.md`
- `skill-starters/_variants/asset-management-builder.md`
- `skill-starters/_variants/disposition-builder.md`
- `skill-starters/_variants/lp-reporting-builder.md`
- `skill-starters/_variants/lp-inquiries-builder.md`
- `skill-starters/_variants/deal-win-loss-learning-builder.md`
- `skill-starters/underwriting-backtest-builder.md`
- `skill-starters/_variants/ic-memo-intelligence-builder.md`
- `skill-starters/_variants/market-thesis-builder.md`
- `skill-starters/_variants/one-off-deliverable-builder.md`

Optional:

- `scripts/check-registry.sh`
- `scripts/verify-workspace.sh`

## Risks

### Risk: The Context Matrix duplicates Constraint Routing

Mitigation: Keep the matrix about load depth. Keep Constraint Routing about which constraint files apply.

### Risk: Learnings become task logs

Mitigation: Put a clear rule at the top of `_shared-config/learnings.md`: only reusable corrections, no task history.

### Risk: Setup becomes too procedural

Mitigation: Import the Agentic OS onboarding rule: recommend, ask one question, skip what is answered.

### Risk: Scripts make the toolkit feel less portable

Mitigation: Make scripts optional. The written checklist remains canonical.

## Definition of Done

The import is done when:

- `SETUP.md` includes a Context Matrix.
- `_shared-config/learnings.md` exists.
- Every builder reads `## General` plus its own workflow learnings.
- Setup has explicit one-question-at-a-time, skip-answered, recommend-first rules.
- Registry reconciliation is documented.
- README explains shared methodology vs firm context vs workflow context.
- No server, database, cron runtime, or Command Centre dependency has been added.

## Recommendation

Do Phases 1 through 4 now. They are small, local, and directly improve reliability.

Defer Phases 5 and 6 until after the first implementation pass. They are useful, but they are not blocking the core upgrade.
