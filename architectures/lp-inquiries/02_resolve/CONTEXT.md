# Stage 02: Resolve

## Purpose
Answer the classified inquiry. Retrieve the governed data or the vetted answer, draft a response in the firm's voice, and flag anything that must be escalated rather than answered. The output is a response ready for review, with every figure tied to its platform source.

## Inputs
- **01_intake/output/inquiry-[investor]-[date].md**: The classified ticket. It defines the type, the real need, and any escalation flag.
- **_config/faq-bank.md**: Vetted answers to recurring questions. Check here first.
- **_config/investor-context.md**: Entity details and history relevant to the answer.
- **_config/response-standards.md**: The answer-vs-refer line and the LP-email register; its Voice section points to the firm's shared voice in `_shared-config/voice-and-tone.md` — read that for the firm voice.
- **Platform data**: The capital-account balance, performance figure, distribution record, or document — retrieved from the platform. This is the source of any number. Load only what this inquiry needs.

## Process
1. Read the ticket. If it is flagged sensitive, do not draft an answer. Draft an acknowledgment and route it to the named owner (see Output, escalation form). Stop there.
2. For non-sensitive inquiries, check the FAQ bank. If a vetted answer exists and fits, use it as the basis — do not reinvent an answer the firm has already settled.
3. Retrieve any figure or document from the platform of record. Never state a balance, performance number, or distribution amount from memory or inference. If the platform value is not available, say so in the draft and flag it for the responder, rather than estimating.
4. Draft the response in the firm's voice (the shared `_shared-config/voice-and-tone.md`, reached via response-standards.md) at the LP-email register. Answer the real need from the ticket, not just the literal question. Keep it accurate, complete, and on-tone.
5. Mark the source of every figure inline for the reviewer (e.g., "[balance per platform as of DATE]"). The responder confirms these; they are not sent to the LP as-is unless the standards say so.
6. Note anything the responder must verify before sending.

## Output
Write to: 02_resolve/output/response-[investor]-[date].md

For a standard inquiry:
```
# Drafted Response: [Investor] — [Inquiry]
Ticket reference: [filename from intake]
Type: [Informational / Document request / Action request]

## Draft
[The response, in the firm's voice, ready for review.]

## Source Trace
[Each figure or document referenced, and where it came from
 in the platform, with the as-of date. The reviewer confirms these.]

## For the Responder to Verify
[Anything to confirm before sending: requester authorization,
 a figure as-of date, an attached document.]
```

For a sensitive inquiry (escalation):
```
# Escalation: [Investor] — [Inquiry]
Ticket reference: [filename from intake]
Routed to: [IR principal / compliance / counsel]

## Why This Escalates
[What makes it sensitive and why it is not IR's to answer.]

## Drafted Acknowledgment to the LP
[A brief, non-committal acknowledgment confirming receipt and
 that the right person will follow up. Commits the firm to nothing.]
```

## Done Looks Like
A response the reviewer can check and send without re-researching it. Every figure traces to the platform. Sensitive inquiries carry an acknowledgment and a routing, not an answer.

## Common Failure Modes
- **Stating a number from memory.** The model will happily produce a plausible balance. A plausible balance is a wrong balance. Retrieve it or flag that you could not.
- **Answering a sensitive inquiry anyway.** If intake flagged it, respect the flag. An off-hand answer to a redemption or complaint can commit the firm to a position it did not intend.
- **Ignoring the FAQ bank.** Re-deriving an answer the firm has already vetted is how two LPs get two different answers to the same question. Check the bank first.

## Layer Annotation
L2 stage contract. The ticket and the retrieved platform data are L4 (this run). FAQ bank, investor context, and response standards from _config/ are L3 (stable reference).
