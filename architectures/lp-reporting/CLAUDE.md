# LP Reporting Workspace

## What This Is
A workspace for producing LP-facing communications (quarterly letters, capital account statements, capital call and distribution notices) from data through drafting through distribution. Built for a GP finance or IR team that reports to investors on a recurring cycle and needs a consistent investor voice without rebuilding the process every quarter.

## Current State
- This is a reference architecture. No active reporting cycle.
- To use this workspace: copy the folder, populate _config with your fund's voice, format, and compliance constraints, and start with stage 01.

## Structure
```
lp-reporting/
  CLAUDE.md              # You are here. Workspace map and entry point.
  CONTEXT.md             # Workflow routing. How stages connect.
  01_data/
    CONTEXT.md           # Stage contract: gather and verify the numbers.
    output/              # Verified data pack. Becomes input for 02_draft.
  02_draft/
    CONTEXT.md           # Stage contract: write the letter or notice.
    output/              # Drafts. Becomes input for 03_distribution.
  03_distribution/
    CONTEXT.md           # Stage contract: finalize, format, distribute.
    output/              # Investor-ready files.
  _config/               # Reference material. Investor voice, format, compliance constraints.
  _prompts/              # Reusable prompt fragments for common tasks.
```

## How to Use
1. Read CONTEXT.md to understand the full workflow.
2. Populate _config/ with your investor voice file, format patterns, and compliance constraints (see Constraint 05 in the GP Operating Toolkit).
3. Start in 01_data. Follow the stage contract. Drop output into 01_data/output/. If more than one version of a source export exists, confirm the authoritative one before pulling figures (Constraint 10).
4. Move to 02_draft. The stage contract tells you which files from 01_data/output/ to use.
5. Move to 03_distribution. Same pattern.
6. Human review happens between every stage. The numbers and the language both get read before they go to an LP.

## Key Decisions
- **Three stages, not five or seven.** Most reporting workflows have more detail than this, but three stages is the minimum viable decomposition. Gathering the numbers, writing the narrative, and distributing are distinct modes of work. Combining them produces worse output in all three, and mixing data assembly with drafting is how a wrong figure ends up in a letter to investors. You can add stages (e.g., 02a_compliance-review between draft and distribution) when your process earns the complexity.
- **_config is separate from stages.** Investor voice, compliance constraints, and format patterns are reference material (L3 in ICM terms). They are configured once and stay stable across cycles. Keeping them outside the numbered stages means updating your disclosure language does not require touching stage contracts.
- **Output directories are the handoff points.** Stage 01 writes the verified data pack to 01_data/output/. Stage 02 writes from there. This makes the data flow explicit and gives you a clear place to reconcile numbers before they reach the narrative.
- **No deal-underwriting in this architecture.** Investment analysis is a different workflow (see the deal-pipeline architecture). This workspace reports on what the fund already owns. Mixing underwriting with reporting clutters the data stage.

## Constraints That Apply
Built against the GP Operating Toolkit. Most relevant: **01 (AI Writing Patterns)** and **02 (Output Drift)** so the letter reads clean and stays consistent cycle to cycle, **05 (Voice Architecture)** so it sounds like the firm regardless of who runs the cycle, and the universal **06 (Layer Triage)** and **09 (Platform Boundary)** so the model narrates verified figures and never generates or adjusts an investor's numbers. Pull **10 (Source Provenance)** when more than one version of an export or asset report is in play.

## Layer Annotations
- CLAUDE.md: L0 (always loaded, ~800 tokens, orientation)
- CONTEXT.md: L1 (loaded on workspace entry, routing)
- Stage CONTEXT.md files: L2 (loaded per-task, stage contract)
- _config/ files: L3 (reference, loaded selectively per stage)
- Source data and stage outputs: L4 (working artifacts, loaded selectively)
