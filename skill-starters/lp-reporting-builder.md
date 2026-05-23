# SKILL: LP Reporting Workspace Builder

## Description
Builds a customized LP reporting workspace by asking diagnostic questions about a fund's investor communications, then assembling a folder structure, stage contracts, and config files based on the answers.

## When to Use
When you produce investor-facing communications on a recurring cycle (quarterly letters, capital call and distribution notices, capital account statements) and want a structured, controlled process that keeps the numbers tied to source and the voice consistent.

## Process

### Phase 1: Diagnosis (ask before building)

Before creating any files, ask the user the following questions one at a time. Wait for each answer before proceeding.

**Question 1: What do you produce for investors?**
"What investor communications do you create on a recurring basis? Quarterly letters, capital call notices, distribution notices, capital account statements, annual reports? List everything you send LPs at least once a year."

**Question 2: How does a reporting cycle actually run?**
"Walk me through what happens between 'the quarter closed' and 'the letter is sent.' Where do the numbers come from, fund admin, your GL, asset reports? Who reconciles them? Who drafts? Who reviews? Describe your actual process, not the ideal one."

**Question 3: Where does review and compliance happen?**
"At which points do you stop and review before something reaches an LP? Is there a number-reconciliation check, a compliance or legal review, a manager sign-off? If review only happens at the end, that is useful to know."

**Question 4: What reference material stays the same across cycles?**
"What applies to every communication you send? Your investor voice, required disclosures and footers, forward-looking-statement language, format templates, per-fund specifics. List what exists and where it lives, even if it is only in someone's head right now."

**Question 5: What does 'done' look like for your most common report?**
"For the communication you send most often, describe the final output. Format, length, the disclosures it carries, how it reaches the LP (portal, email). What makes it ready to send?"

### Phase 2: Assembly

Based on the answers, build the workspace:

1. Create the folder structure. The default is three stages (data, draft, distribution) but match it to their described process. Add _config/ for reference material. If compliance/legal review is a distinct gated step, add 02a_compliance-review.

2. Write CLAUDE.md as the workspace entry point. Include:
   - What this workspace is (based on their description)
   - Current state (new workspace, no active cycle)
   - Structure map (listing all folders and their purpose)
   - How to use (step-by-step based on their cycle)

3. Write CONTEXT.md as the routing file. Include:
   - Stage map table (stage name, purpose, inputs, output location)
   - How stages connect, emphasizing that the data stage gates the others
   - Reference material list

4. Write a CONTEXT.md for each stage. Include:
   - Purpose (derived from their process description)
   - Inputs (what this stage needs, referencing specific files)
   - Process (steps, based on their description)
   - Output format (based on their "done" description and format patterns)
   - "Done looks like" (one sentence)

5. Create config file templates:
   - voice-and-tone.md, format-patterns.md, constraints.md (use the three-file architecture from Constraint 05)
   - If they mentioned per-fund or per-investor specifics: create placeholders for each

6. Populate constraints.md with the starter constraints, including the reporting-specific ones (every figure ties to source, forward-looking caution, required disclosures present) and ask the user to add their own and confirm with compliance.

### Phase 3: Orientation

After building, walk the user through:
- "Here is what I built and why each piece exists."
- "The data stage gates everything. No figure reaches a letter until it ties to source. This is what keeps a wrong number out of an investor's inbox."
- "The constraint file has starter rules including disclosure and forward-looking language. Read through them, confirm them with compliance, then add your own."
- "The first thing to populate is [most impactful config file based on their answers]."

## Important Notes
- Do not build anything before completing the diagnosis. The questions are the skill.
- The data stage is the highest-value stage. A reporting process that drafts before the numbers are verified is how a restated figure reaches an LP. Emphasize the reconciliation gate even if their current process is looser.
- Compliance is a real constraint surface here, not a style preference. Where the user is unsure about disclosure or performance language, tell them to confirm with compliance rather than guessing.
- If the user's process has fewer than 3 distinct steps, do not force more stages. Verify-then-send is valid if that is their actual workflow.
- Always annotate files with their ICM layer (L0–L4) so the user understands the architecture, not just the files.
- Load and name the constraints this workflow uses: 01 (AI Writing Patterns), 02 (Output Drift), 05 (Voice Architecture), plus the universal 06 and 09; pull 10 (Source Provenance) when more than one version of an export or asset report is in play.
