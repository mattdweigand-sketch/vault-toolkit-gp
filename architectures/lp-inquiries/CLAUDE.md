# LP Inquiries Workspace

## What This Is
A workspace for handling inbound investor inquiries: the ad hoc questions and soft requests LPs send between formal events. "What is my current capital balance?" "Can you re-send my K-1?" "What is your view on the office exposure in Fund II?" "We are thinking about increasing our commitment — who do we talk to?" This architecture fits an investor relations, IR-finance, or fund finance team that fields a steady stream of LP questions and wants consistent, accurate, on-voice responses without each one becoming a fire drill.

This is not capital-event processing. Capital calls, distributions, transfers, and onboarding are platform-governed transactions handled in your fund-administration platform, not in an AI workspace (see Constraint 09). This workspace is for the inquiry traffic that arrives in between — informational, document, and light action requests.

## Current State
- This is a reference architecture. No active inquiry queue.
- To use: copy the folder, edit _config files to match your fund and your investor base.

## Structure
```
lp-inquiries/
  CLAUDE.md              # You are here.
  CONTEXT.md             # Workflow routing.
  01_intake/
    CONTEXT.md           # Stage contract: receive, classify, prioritize, route.
    output/              # Classified inquiry tickets, ready to resolve.
  02_resolve/
    CONTEXT.md           # Stage contract: gather governed data, draft, escalate.
    output/              # Drafted responses with escalation flags.
  03_respond/
    CONTEXT.md           # Stage contract: review, send, log, capture patterns.
    output/              # Sent responses and the inquiry log.
  _config/               # Response standards, investor context, FAQ bank.
  _templates/            # Reusable response templates.
```

## How to Use
1. Read CONTEXT.md for the full workflow.
2. Populate _config/ with your response standards, investor context, and FAQ bank.
3. A new inquiry enters through 01_intake. It gets classified, prioritized, and routed here.
4. The classified ticket moves to 02_resolve, where the answer is gathered from the platform of record and drafted, with anything beyond IR's authority flagged for escalation.
5. The draft moves to 03_respond for an accuracy-and-tone review, then it is sent, logged, and any reusable answer is captured back into the FAQ bank.

## Key Decisions
- **Classification is the first job, not answering.** The intake stage sorts each inquiry by type (informational / document request / action request / sensitive) before anyone drafts a word. A balance question and a "we are considering redeeming" message look similar in an inbox and could not be more different in stakes. Classifying first is what keeps the sensitive ones from being answered casually.
- **The platform is the source of every figure.** A capital-account balance, a performance number, a distribution amount — those come from the platform, not from the model. The model retrieves and phrases; it never computes or recalls a number from memory. See Constraint 09. This is the difference between an IR assistant and an IR liability.
- **Escalation is a designed step, not an exception.** Some inquiries are not IR's to answer: a redemption signal, a side-letter interpretation, a complaint, a request that touches legal or compliance. The resolve stage flags these explicitly and routes them, rather than improvising an answer that commits the firm to something.
- **The FAQ bank compounds.** Every answered inquiry that could recur gets captured. Over time the bank turns the same questions from research tasks into lookups, and keeps the firm's answers consistent across every person who responds. This is Constraint 04 (Session Consistency) made concrete.
- **_templates is separate from _config.** Templates are response structures (balance confirmation, document re-send, holding statement). Config is operating logic (what IR can answer vs. refer, the investor record, the FAQ bank). They change at different rates.

## Constraints That Apply
This workspace was built against the GP Operating Toolkit. The constraints most relevant here: **02 (Output Drift)**, **04 (Session Consistency)**, **05 (Voice Architecture)**, and the universal **06 (Layer Triage)** and **09 (Platform Boundary)**. Read them before customizing the stage contracts and _config.

## Layer Annotations
- CLAUDE.md: L0 (always loaded, orientation)
- CONTEXT.md: L1 (workflow routing)
- Stage CONTEXT.md files: L2 (stage contracts)
- _config/ files: L3 (reference material, response logic and investor record)
- _templates/ files: L3 (reference material, response structures)
- Incoming inquiries and stage outputs: L4 (working artifacts)
