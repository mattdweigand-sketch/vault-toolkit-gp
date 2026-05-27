# Contributing

Thanks for helping improve Kit.

## Good Contributions

Good changes make the toolkit clearer, safer, or easier to run:

- Better setup instructions.
- Clearer architecture contracts.
- More realistic examples.
- Stronger platform-boundary guidance.
- Better Artifact Trust Layer templates.
- Fixes to `scripts/setup_state.py`.

Avoid adding platform-native workflows. Kit should not become a CRM, ticketing system, approval system, calculation engine, or audit trail.

## Local Workflow

1. Create a branch.
2. Make a focused change.
3. Run:

```bash
python3 scripts/setup_state.py doctor --json
```

4. Confirm the README and changed Markdown files render cleanly.
5. Open a pull request with the problem, the change, and any remaining tradeoffs.

## Pull Request Checklist

- [ ] The change keeps systems of record authoritative.
- [ ] Generated local workspace data is not committed.
- [ ] Examples are fictional or safe to publish.
- [ ] New workflows map to one of the six architecture families, or explain why a new family is needed.
- [ ] Artifact-producing workflows name source, evidence, review, and human approval outputs.

## Style

Write plainly. Prefer concrete rules and examples over broad claims. Keep public docs useful to a first-time reader.
