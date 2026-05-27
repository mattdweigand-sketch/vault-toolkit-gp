# Kit

Kit is a plain-file toolkit for building governed AI workflows around work that business platforms cannot own: messy input intake, source interpretation, decision prep, exception handling, stakeholder response prep, and institutional memory.

It keeps systems of record in charge. CRM, ticketing, finance, document, approval, dashboard, and audit systems still own facts, status, permissions, calculations, delivery, and audit trails. Kit helps teams structure the judgment layer above them.

## What It Is

Kit provides:

- Six reusable workflow architectures.
- Setup instructions for creating a live workspace.
- Guardrails for platform boundaries, source provenance, handoffs, and human review.
- An Artifact Trust Layer for source packets, evidence maps, review reports, workbook controls, and approval notes.

Kit is not an application, hosted service, database, agent runtime, or compliance system. It is a file-based operating model that an AI coding agent can read, copy, and customize.

## Quick Start

1. Clone the repo.
2. Open the folder in an AI coding agent that can read and edit files.
3. Tell the agent: `Read AGENTS.md, then run setup.`
4. Answer the setup questions one at a time.
5. Review the workspace created under `workspaces/`.

If your agent automatically reads repo instructions, `Run setup` is enough.

## The Boundary

Use this rule before building anything:

> If a platform can own the record, workflow state, entitlement, calculation, or audit trail, do not make it a Kit architecture. If the work depends on source interpretation, decision framing, exception judgment, stakeholder communication, or institutional memory, it belongs here.

Every workspace should answer:

1. What platform owns the record?
2. What deterministic tool owns the math or rule?
3. What routing or template can be automated?
4. What judgment does AI add?
5. What human approves the output?

## Architectures

| If the team needs to... | Use |
|---|---|
| Turn messy emails, calls, notes, screenshots, forms, or files into a clean brief | `messy-input-intake` |
| Figure out what a source set supports, conflicts with, or leaves unanswered | `evidence-review` |
| Prepare options, tradeoffs, risks, assumptions, and conditions for a human decision | `decision-prep` |
| Handle a case that does not fit the normal process | `exception-handling` |
| Prepare high-context communication from verified facts | `stakeholder-response-prep` |
| Capture validated lessons so future work improves | `institutional-memory-loop` |

## Artifact Trust Layer

The reusable module at `modules/artifact-trust-layer/` attaches to workflows that produce or review decks, workbooks, memos, reports, IC materials, LP narratives, board materials, diligence artifacts, or one-off deliverables.

It includes patterns for:

- Source packets.
- Artifact specs.
- Claim evidence maps.
- Hostile review reports.
- Workbook, deck, and document control maps.
- Human approval notes.

## Repo Map

```text
AGENTS.md        canonical project instructions
CLAUDE.md        Claude Code compatibility wrapper
SETUP.md         setup and workspace-build engine
_shared-config/  organization profile, voice, setup state, learnings
architectures/   six architecture families and examples
constraints/     principles for reliable AI work
docs/            public documentation
modules/         reusable patterns that attach to architectures
scripts/         setup-state helper
skill-starters/  six builders, one per architecture
workspaces/      generated local workflows
```

## Examples

Worked examples live under `architectures/_examples/`:

- `vendor-request-intake`
- `contract-renewal-evidence-review`
- `pricing-exception-decision-prep`
- `customer-escalation-exception`
- `service-issue-stakeholder-response`
- `lost-renewal-memory-loop`

## Safety Notes

- The repo does not upload data by itself.
- Any AI tool you use may send loaded context to its model provider.
- Do not put secrets, private customer data, production exports, or regulated data into public forks.
- Human review is required before external sends, irreversible actions, or stakeholder-facing output.

## Documentation

Start with:

- [Setup Guide](SETUP.md)
- [Public Docs](docs/index.md)
- [Artifact Trust Layer](modules/artifact-trust-layer/README.md)
- [Layer Triage](constraints/06-layer-triage.md)
- [Platform Boundary](constraints/09-platform-boundary.md)

## License

Released under the [MIT License](LICENSE).
