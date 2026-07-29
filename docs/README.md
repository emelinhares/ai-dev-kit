# Documentation

This is the durable, human-facing knowledge base. Start here; use
[`.ai/`](../.ai/README.md) for compact agent operating memory.

## Official homes

| Topic | Official home | What belongs there |
| --- | --- | --- |
| Product truth | [`product/`](product/README.md) | Users, problem, outcome, scope, capabilities, success |
| Current engineering truth | [`engineering/`](engineering/README.md) | Architecture, boundaries, data flow, constraints, quality and delivery model |
| Historical decisions | [`decisions/`](decisions/README.md) | Why a material choice was made, its status, and consequences |
| Operations | [`runbooks/`](runbooks/README.md) | Safe procedures, verification, rollback, escalation, and ownership |
| Agent working memory | [`.ai/project/`](../.ai/project/) | Current task state, assumptions, health, terms, and concise evidence |

Indexes may summarize a link in one sentence but must not copy the linked
document's substantive content.

## Documentation governance

Before adding a document:

1. Identify its audience and question.
2. Find the official home above and update an existing page when it owns the
   topic.
3. Link across categories rather than copying text.
4. Name an accountable role/group and a review trigger for operational or
   fast-changing truth.

Use these lifecycles:

- **Product and architecture documents state current truth.** Update them when
  behavior or boundaries change; history comes from version control and ADRs.
- **ADRs record historical decisions.** Once accepted, do not rewrite their
  context or decision to match the present. Mark them superseded and link the
  replacement.
- **Runbooks are operational procedures.** Verify them after meaningful system
  change or an execution reveals drift. Unknown steps are explicit gaps.
- **Research logs hold concise decision evidence.** They do not replace the
  durable decision or architecture document.
- **Project memory routes current work.** It links to durable truth and avoids a
  second narrative.

Every page should be as small as its question allows. Remove stale content,
redirect a retired page when inbound links matter, and fix indexes in the same
change. Do not preserve generated transcripts, raw research dumps, credentials,
private keys, tokens, production data, or personal data.

## Quality checklist

- One official home and an index link
- Current claims verified against observable behavior
- Facts, assumptions, and decisions distinguished
- Terms aligned with the repository glossary
- Owner and review trigger present when useful
- Relative links valid
- No sensitive material
