# Kit

Kit helps a business apply AI to the work its platforms cannot own: messy inputs, source interpretation, decision prep, exception handling, stakeholder response prep, and institutional memory.

Your CRM, ticketing system, project tracker, finance platform, document system, approval workflow, dashboard, and audit trail stay the source of truth. Kit builds the judgment layer above them.

## Quick start

1. Open this folder in any AI coding agent that can read files and make edits.
2. Tell the agent: `Read AGENTS.md, then run setup.`
3. Setup captures the organization profile, picks the right architecture, asks a few diagnostic questions, and creates a workspace under `workspaces/`.

If your agent automatically reads repo instructions, `Run setup` is enough. A plain browser chat can still use the reference files, but it cannot run setup or create workspaces.

## The boundary

Use this rule before building anything:

> If a platform can own the record, workflow state, entitlement, calculation, or audit trail, do not make it a toolkit architecture. If the work depends on firm judgment, source interpretation, decision framing, or institutional memory, it belongs here.

In practice:

| Layer | Owns |
|---|---|
| Platforms | Facts, records, status, permissions, calculations, delivery, audit |
| Automation | Known rules, routing, checklists, templates, repeatable handoffs |
| Kit | Interpretation, judgment, exceptions, decision prep, response framing, memory |
| Humans | Approval, accountability, external sends, irreversible actions |

Every workspace should answer:

1. What platform owns the record?
2. What deterministic tool owns the math or rule?
3. What routing or template can be automated?
4. What judgment does AI add?
5. What human approves the output?

## The six architectures

| If the team needs to... | Use |
|---|---|
| Turn messy emails, calls, notes, screenshots, forms, or files into a clean brief | `messy-input-intake` |
| Figure out what a source set supports, conflicts with, or leaves unanswered | `evidence-review` |
| Prepare options, tradeoffs, risks, assumptions, and conditions for a human decision | `decision-prep` |
| Handle a case that does not fit the normal process | `exception-handling` |
| Prepare high-context communication from verified facts | `stakeholder-response-prep` |
| Capture validated lessons so future work improves | `institutional-memory-loop` |

## Reusable modules

Modules are optional patterns that attach to an architecture. They do not create new architecture families.

| If the workflow needs to... | Attach |
|---|---|
| Turn messy sources into trustworthy decks, workbooks, memos, diligence maps, IC materials, LP narratives, or one-off deliverables | `modules/artifact-trust-layer/` |

## What is in here

```text
AGENTS.md        canonical project instructions
CLAUDE.md        Claude Code compatibility wrapper
SETUP.md         setup and workspace-build engine
_shared-config/  organization profile, voice, setup progress, learnings
constraints/     principles for reliable AI work
architectures/   six architecture families and examples
modules/         reusable patterns that attach to architectures
skill-starters/  six builders, one per architecture
workspaces/      live workflows created during setup
```

## Examples

Each architecture has a small worked example under `architectures/_examples/`:

- `vendor-request-intake`
- `contract-renewal-evidence-review`
- `pricing-exception-decision-prep`
- `customer-escalation-exception`
- `service-issue-stakeholder-response`
- `lost-renewal-memory-loop`

## Useful references

Start with:

- `constraints/06-layer-triage.md`
- `constraints/09-platform-boundary.md`

Those two explain what belongs to AI and what belongs to platforms or deterministic automation.

## Finalize

When the organization is ready, say `finalize`. The agent moves toolkit methodology into `_kit/`, leaving the organization's live operating system at the root.

Built by Matt Weigand. Released under the [MIT License](LICENSE).
