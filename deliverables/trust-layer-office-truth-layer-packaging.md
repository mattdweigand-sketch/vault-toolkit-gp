# Trust Layer Packaging Recommendation

## Read

The repo is already close to a productized methodology home for the Trust Layer. Its strongest idea is the platform boundary: platforms own records, deterministic tools own math, rules own routing, AI owns judgment, and humans approve outputs.

The named workflows map to four reusable Trust Layer shapes:

| Workflow | Shape | Trust Layer job |
|---|---|---|
| `diligence-evidence-map` | Source provenance | Inspect the room before the firm relies on it. |
| `one-off-deliverable` variant | Provenance-gated drafting | Inspect a messy source set, stop for review, then draft from cited sources. |
| `lp-narrative-and-issue-prep` | Platform-fact narrative | Explain verified facts without becoming the investor platform. |
| `ic-pressure-test` | Gated decision challenge | Stress-test assumptions, evidence, risks, and conditions before a human decision. |
| `underwriting-backtest` | Learning loop | Convert realized outcomes into validated calibration memory. |

## Evaluation

### Diligence Evidence Map

This should remain a core Trust Layer architecture. It is the cleanest expression of the Office Truth Layer pattern: inventory first, authority explicit, conflicts visible, questions as output.

What works:
- Clear stage sequence: inventory -> authority -> questions.
- Strong platform boundary: the data room stores documents; the model maps evidence.
- High reuse potential across diligence, IC prep, lender packages, LP issue prep, and one-off memos.

What to strengthen:
- Add a reusable `source-provenance` module that this architecture consumes, rather than keeping inventory logic only inside this workflow.
- Add a handoff brief output from `03_questions` so IC pressure test can consume it directly.

### One-Off Deliverable Variant

This deserves promotion, but not as a ninth core architecture. It should become a reusable module or "starter mode" under the provenance pattern.

What works:
- The human review gate after inventory is excellent.
- It has the right failure model: the risk is drafting from an uninspected pile.
- It generalizes beyond GP work: any serious deliverable from messy sources needs this.

What to change:
- Rename the pattern from `one-off-deliverable` to something productized, like `source-grounded-deliverable`.
- Keep it as a reusable module: `inventory -> review gate -> grounded draft`.
- Let active workflows import it when they need a source-backed artifact, instead of making setup route to it as a standalone workflow by default.

### LP Narrative And Issue Prep

This is strategically important but currently lighter than the others. It has the right boundary: Juniper Square or the investor platform owns records, figures, DDQ, portal, entitlements, and audit; the workspace owns explanation and posture.

What works:
- Correct ownership split between platform and AI.
- Good stage shape: facts -> narrative -> questions -> posture.
- Natural Trust Layer use case because investor trust depends on source-backed language, not more workflow software.

What to strengthen:
- Make `01_facts` a formal "verified fact pack" module with source IDs, entitlement notes, and forbidden claims.
- Add a response posture taxonomy: answer directly, answer with caveat, hold, escalate, route to platform, legal/compliance review.
- Add a memory handoff from recurring LP objections into `firm-memory-loop`.

### IC Pressure Test

This is a flagship Trust Layer architecture. It frames AI correctly: not the IC gate, not the model, not the memo author, but the challenge layer above governed inputs.

What works:
- Strong distinction between memo intake, challenge, conditions, and capture.
- Good reuse of prior patterns through `_store/`.
- Clean output target: IC-ready questions and approval conditions.

What to strengthen:
- Make evidence input explicit: consume `diligence-evidence-map` handoff briefs instead of rereading diligence materials.
- Define a standard `decision-condition` schema: issue, source, decision impact, owner, required evidence, deadline, condition language.
- Feed lessons from `underwriting-backtest` into pressure-test questions, so realized misses change future IC challenge.

### Underwriting Backtest

This is the most mature architecture. It is also the clearest example of Trust Layer as an institutional memory product, not a one-off prompt.

What works:
- The deterministic core is correctly separated from AI judgment.
- The store is the product.
- The skill-vs-luck guardrail is exactly the kind of candid internal truth the methodology should protect.
- The schema and taxonomy are much stronger than the other active workflows.

What to strengthen:
- Promote its store design into a reusable `validated-memory-store` module.
- Add a cross-workflow handoff: calibration findings should flow into diligence questions, IC pressure tests, and investment-box updates.
- Add an optional periodic review stage that reads the store and proposes changes to standards.

## Packaging Recommendation

Package the Office Truth Layer as reusable modules underneath the eight core architectures. The architectures stay as productized workflows. The modules become the portable methodology.

Recommended modules:

1. `source-provenance`
   - Used by: diligence evidence map, one-off deliverables, IC pressure test, LP narrative fact packs.
   - Outputs: source inventory, duplicate log, conflict log, missing context, authority ladder.

2. `verified-fact-pack`
   - Used by: LP narrative, IC pressure test, hold/sell/refi, portfolio intervention.
   - Outputs: verified facts, source IDs, platform owner, entitlement notes, forbidden claims.

3. `grounded-draft`
   - Used by: one-off deliverables, LP narrative, market thesis, IC memo support.
   - Outputs: draft with source citations, inference labels, open items, source usage map.

4. `decision-challenge`
   - Used by: IC pressure test, hold/sell/refi, investment-box updates.
   - Outputs: fragile assumptions, missing evidence, decision-impact ranking, approval conditions.

5. `response-posture`
   - Used by: LP narrative, investor issue prep, lender communications, sensitive portfolio updates.
   - Outputs: answer/hold/escalate posture, owner, approved language boundaries.

6. `validated-memory-store`
   - Used by: underwriting backtest, firm memory loop, IC precedent, LP objection learning.
   - Outputs: append-only records, taxonomy, validated causal claims, pattern updates.

7. `handoff-brief`
   - Used between every architecture.
   - Outputs: subject, origin, carried-forward conclusion, sourced figures, open items, flags.

## Product Structure

Keep the current top-level product:
- `architectures/` = productized workflows.
- `constraints/` = methodology rules.
- `skill-starters/` = setup interviews.
- `workspaces/` = instantiated client operating system.

Add:

```text
modules/
  source-provenance/
  verified-fact-pack/
  grounded-draft/
  decision-challenge/
  response-posture/
  validated-memory-store/
  handoff-brief/
```

Each module should include:
- `README.md`: what it does, when to use it, when not to use it.
- `CONTRACT.md`: inputs, process, outputs, done looks like, failure modes.
- `templates/`: output skeletons.
- `examples/`: one compact worked example.

Architectures should reference modules instead of duplicating their logic. Example: `diligence-evidence-map/01_inventory/CONTEXT.md` should say it implements `modules/source-provenance/CONTRACT.md` with diligence-specific fact classes.

## Immediate Edits Worth Making

1. Add `modules/source-provenance` first. It is already present in three places: diligence evidence map, one-off deliverable, and Constraint 10.
2. Promote one-off deliverable into a module-backed pattern, not a core route.
3. Add handoff brief outputs to `diligence-evidence-map`, `ic-pressure-test`, and `underwriting-backtest`.
4. Strengthen `lp-narrative-and-issue-prep` by giving `01_facts` the same rigor as provenance inventory.
5. Update `scripts/setup_state.py`: its `WORKFLOWS` list still reflects archived variants, so `doctor` reports false registry errors against the current eight-architecture target.

## Positioning

The Trust Layer should be packaged as:

> The layer above systems of record that makes firm judgment inspectable, source-backed, reusable, and safe to hand off.

Office Truth Layer patterns are the reusable components inside that:
- What is the source?
- Which version is authoritative?
- What does the evidence support?
- What is inference?
- What needs a human?
- What should be remembered next time?

That is the product. The workflows are the packaging.
