# Office Truth Layer Modules

Modules are reusable Trust Layer contracts. They sit between `constraints/` and `architectures/`.

Use constraints for principles. Use modules for repeated work units. Use architectures for complete GP workflows.

## Modules

| Module | Use when |
|---|---|
| `source-provenance` | A source set must be inventoried, ranked, and checked before use. |
| `verified-fact-pack` | A narrative or decision needs only platform-verified facts. |
| `grounded-draft` | A serious artifact must be drafted from reviewed sources. |
| `artifact-review` | A draft, deck, workbook, memo, or handoff must be checked before it travels. |
| `decision-challenge` | A decision packet needs pressure testing before a human gate. |
| `response-posture` | Sensitive external-facing issues need answer, hold, route, or escalate posture. |
| `validated-memory-store` | Repeated judgment should become validated institutional memory. |
| `handoff-brief` | One workspace needs to feed another without re-deriving context. |

## How To Use

Builders should load only the modules named by the selected architecture. Do not copy every module into a workspace. Reference the module contract and copy only the output template the workspace needs.

When the repo is finalized, these paths move with the kit to `_kit/modules/`.
