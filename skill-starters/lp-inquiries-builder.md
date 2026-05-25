# SKILL: LP Inquiries Workspace Builder

## Description
Builds a customized LP-inquiry-handling workspace by asking diagnostic questions about the inbound investor questions a firm fields between formal events, then assembling a folder structure, stage contracts, and config files based on the answers.

## When to Use
When an investor relations or IR-finance team handles a steady stream of ad hoc LP questions and soft requests and wants consistent, accurate, on-voice responses — with sensitive inquiries reliably escalated rather than answered casually.

## Process

### Phase 1: Diagnosis (ask before building)

> **Firm facts are already captured.** Run Setup wrote the firm's name, asset classes, systems of record, team, and voice to `_shared-config/` (firm-profile.md and voice-and-tone.md). Read those first. Do NOT re-ask firm-level facts — confirm them if needed. Ask only the workflow-specific questions below. If `_shared-config/firm-profile.md` does not exist yet, the firm skipped orientation; capture the basics first, then continue.

Ask the following questions one at a time. Wait for each answer before proceeding.

**Question 1: What do LPs ask you between formal events?**
"What kinds of questions and requests come in — balance checks, document re-sends, performance questions, commitment-increase interest, complaints? List the common ones."

**Question 2: How is an inquiry handled today?**
"Walk me through what happens when one arrives. Who sees it, how fast does it get a response, and what do they check before replying?"

**Question 3: Where is the line between what IR answers and what gets referred?**
"What can IR answer directly, and what must go to a principal, compliance, or counsel? Who owns each kind of referral?"

**Question 4: Where do answers with numbers come from?**
"When a response includes a balance or performance figure, where does that number come from? Is there a check that the requester is authorized to receive it?"

**Question 5: Do you keep a record or an FAQ?**
"Do you log answered inquiries, and do you have a set of vetted answers to the questions that recur?"

### Phase 2: Assembly

Based on the answers, build the workspace:

1. Start from the template: copy the matching architecture (`architectures/lp-inquiries/` before finalize, `_kit/architectures/lp-inquiries/` after) as your starting point into `workspaces/<name>/` (the firm's live workspaces live there; rename <name> for the deal/fund/cycle) — its CLAUDE.md, CONTEXT.md, stage CONTEXT.md contracts, _config/ files, and the four starter response templates in _templates/ are drafts to customize, not blank files to write from scratch (copy the folder contents, not any .DS_Store). Then adapt to their answers: three stages (intake, resolve, respond), plus _config/ and _templates/. If they verify requester identity, add an authentication step in or before intake.
2. Write CLAUDE.md: what this is (and that it is *not* capital-event processing — those are platform-governed transactions handled in the fund-administration platform, not an AI workspace; see Constraint 09), current state, structure map, how to use.
3. Write CONTEXT.md: the stage map, how stages connect, the escalation path, and the AI-vs-Platform table (the platform owns balances and the record; the model classifies, retrieves, and drafts; humans own anything that commits the firm).
4. Customize each stage's CONTEXT.md from the template's contract — adjust the existing contract, do not write a new one from scratch.
5. Create config templates: response-standards.md (service levels, voice, the answer-vs-refer line, never-do list), investor-context.md (the working investor record and routing map), faq-bank.md (the compounding vetted-answer store). Populate from their answers. The firm's core voice already lives in `_shared-config/voice-and-tone.md` (from Run Setup) — reference it, do not redefine it; capture only this workflow's register overlay (how its deliverable differs from the firm's standard voice).
6. Customize the four starter templates that ship in _templates/ (balance-confirmation, document-resend, performance-holding-statement, escalation-acknowledgment) to the firm's voice and escalation rules; add a template for any other inquiry type they handle repeatedly.
7. Flag what you could not confirm. Populate _config/before-you-trust-this.md: list every value you could not get directly from the firm — above all the answer-vs-refer line and the authorized-contact roster in investor-context.md (an unconfirmed roster blocks safe authentication) — mark each `[NEEDS CONFIRMATION — IR lead/compliance]`, name who signs off, and never invent these silently. Use `[TBD]` for values simply awaiting real data. (Constraint 08.)
8. Demonstrate one stage end to end. Run the intake stage against a real or sample inquiry and check the output against its "Done Looks Like" line. If there is no live inquiry yet, use a sample inquiry as the stand-in run, and mark the workspace "stands up now, activates on the first inbound inquiry."

### Phase 3: Orientation

After building, walk the user through:
- "Here is what I built and why each piece exists."
- "Classification comes first, before anyone drafts. A redemption signal that reads like a routine question is exactly the one this catches."
- "Every figure comes from the platform, never from the model's memory. A plausible balance is a wrong balance."
- "Escalation is a designed step. Sensitive inquiries get an acknowledgment and a routing, not an off-hand answer that commits the firm."
- "The FAQ bank compounds — the respond stage writes vetted answers back into it, so the same question stops being a research task and answers stay consistent across everyone who replies."

## Important Notes
- Do not build before completing the diagnosis. The questions are the skill.
- The answer-vs-refer line in response-standards.md is the highest-stakes config. Where the user is unsure, tell them to confirm with compliance rather than guess.
- This is inquiry traffic, not transactions. If they describe capital calls or distributions, those are platform-governed operations handled in the fund-administration platform, not a workspace to build (Constraint 09).
- Load and name the constraints this workflow uses: 02 (Output Drift), 04 (Session Consistency), 05 (Voice Architecture), plus the universal 06 and 09.
- Always annotate files with their ICM layer (L0–L4).
