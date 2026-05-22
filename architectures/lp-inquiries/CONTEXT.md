# Workflow: LP Inquiries

## Overview
Three-stage queue: Intake → Resolve → Respond. Designed for the inbound investor questions that arrive between formal events. The stages separate three distinct modes of work: deciding what an inquiry actually is, finding and drafting the answer, and reviewing before it reaches the LP. Each inquiry passes through all three. A human reviews before anything is sent.

## Stage Map

| Stage | Purpose | Inputs | Output Location |
|---|---|---|---|
| 01_intake | Receive, classify, prioritize, route | LP email, portal message, call note, IR forward | 01_intake/output/ |
| 02_resolve | Gather governed data, draft the response, flag escalations | Classified ticket, FAQ bank, investor context, platform data | 02_resolve/output/ |
| 03_respond | Review for accuracy and tone, send, log, capture patterns | Drafted response, response standards | 03_respond/output/ |

## How Stages Connect
- 01 → 02: Intake produces a classified ticket — what type of inquiry, which investor, which fund, what it actually requires, and how urgent. Resolve picks that up and answers it. If resolve has to ask "what is this person actually asking and is it sensitive?", intake did not finish its job.
- 02 → 03: Resolve produces a drafted response plus any escalation flags. Respond reviews it against the standards, sends it, and logs it. If respond is rewriting the substance, resolve needs tighter standards or better source data.
- Escalation path: at any stage, an inquiry that is not IR's to answer (redemption signal, complaint, legal/compliance/side-letter question) is flagged and routed to the right owner. It does not get a casual answer. The workflow's job then is to acknowledge and hand off, not to resolve.

## Reference Material (in _config/)
- response-standards.md: Service-level expectations, the firm's response voice, and the line between what IR answers directly and what gets referred. Loaded in stages 02 and 03.
- investor-context.md: The recurring investor record — entities, contacts, sensitivities, history. Loaded in stages 01 and 02.
- faq-bank.md: Vetted answers to recurring questions. Loaded in stage 02 and added to in stage 03.

## Reference Material (in _templates/)
- Response structures for the most common inquiry types: balance confirmation, document re-send, performance question holding statement, escalation acknowledgment.

## When to Add Stages
Common additions:
- **02a_review** between resolve and respond: if responses that touch numbers require an independent second-set-of-eyes check before they go out, separate from the tone review in respond.
- **01a_authentication** within or before intake: if you must verify the requester's identity and authority before releasing any account information (a real control for balance and document requests).

Add a stage when you find yourself consistently doing that work informally. Do not add it preemptively.

## AI vs. Platform: Where Each Step Lives

The temptation here is to let the model answer a balance or performance question from context. Do not. The rule: rely on your platform for the data and the record, use AI for the language and the judgment. See Constraint 09.

| Step in this workflow | Layer | Who owns it |
|---|---|---|
| Capital accounts, balances, performance figures, distribution history, the investor record, the audit trail | Platform / data foundation | Enterprise platform (fund admin and the software underneath it) |
| Whether the requester is authorized to receive the information | Deterministic / control | Platform entitlements plus a human check |
| Classifying the inquiry, retrieving and phrasing the answer, drafting the response, flagging escalations | AI | You, on top of governed data |
| Anything that commits the firm — a redemption, a side-letter reading, a complaint resolution | Human in the loop | IR principal, compliance, or counsel |

The trap on this workflow: the model stating a figure it did not retrieve from the platform, or answering a sensitive inquiry that should have been escalated. AI classifies, retrieves, and drafts. The number comes from the platform, and a human owns anything that binds the firm.
