# Security Policy

## Supported Versions

Kit is a plain-file toolkit. The `main` branch is the supported version.

## Reporting a Vulnerability

Please report security concerns through GitHub's private vulnerability reporting if enabled for this repository. If that is not available, open an issue with minimal detail and avoid posting secrets, customer data, exploit payloads, or sensitive business context.

Useful reports include:

- Secrets or private data accidentally committed to the repo.
- Unsafe setup guidance that could cause users to expose sensitive data.
- Templates that encourage bypassing human approval.
- Scripts that write outside the project folder unexpectedly.

## Data Handling

This repo does not run a service or upload data by itself. Users should still assume that any AI coding agent may send the files it reads to its model provider.

Do not commit:

- API keys or tokens.
- Customer data.
- Private exports from systems of record.
- Regulated or confidential documents.
- Generated local workspaces containing real business data.

Human approval is required before external sends, irreversible actions, or stakeholder-facing output.
