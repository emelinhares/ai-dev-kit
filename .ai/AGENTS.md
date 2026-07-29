# AI Development Kit Router

This is the canonical operating entry point. `.ai/` is working memory for
agents; [`docs/`](../docs/README.md) is durable documentation for people.
Never copy the same truth into both.

## Start every task

1. Read [`project/state.json`](project/state.json),
   [`project/scope.md`](project/scope.md), and the relevant terms in
   [`project/glossary.md`](project/glossary.md).
2. Select the mode below. If the state is missing or unreliable, use
   `ADOPT_PROJECT`.
3. Classify the task and risk, then load only the routed role contracts and
   relevant policies.
4. Check [`guardrails/safety.md`](guardrails/safety.md) before any external,
   privileged, costly, destructive, or production-facing action.
5. At handoff, update changed project memory and durable documentation. Do not
   store secrets, credentials, private keys, tokens, production records, or
   personal data.

## Modes

### `NEW_PRODUCT`

Use when creating a product in an empty or intentionally new repository.

Typical route:
`product-translator → discovery → researcher? → architect → planner →
executor ↔ auditor → documentation-curator → release-manager`

Before implementation, establish the problem, owner-visible outcome, boundaries,
assumptions, and success evidence. Create the repository glossary even if no
product documentation exists.

### `ADOPT_PROJECT`

Use for an existing, inherited, unclear, or partially documented repository.

Typical route:
`product-translator → mapper → discovery? → researcher?/architect? → planner →
executor ↔ auditor → documentation-curator → release-manager?`

Follow [`practices/project-adoption.md`](practices/project-adoption.md). Treat
existing documentation as useful evidence, not sole truth. Verify it against
code, configuration, tests, observable environments, and owner input. Never
block initial mapping only because privileged access is unavailable; record the
gap and request the least privilege needed.

## Task routing

| Task signal | Lead role | Add when needed | Expected gate |
| --- | --- | --- | --- |
| Outcome is vague or phrased non-technically | [`product-translator`](roles/product-translator.md) | discovery | Owner confirms the plain-language outcome |
| Problem, users, or value is uncertain | [`discovery`](roles/discovery.md) | researcher | Evidence supports a bounded opportunity |
| Repository behavior or structure is unclear | [`mapper`](roles/mapper.md) | researcher | Map cites observed evidence and gaps |
| Work is understood but needs safe slicing | [`planner`](roles/planner.md) | architect, auditor | Plan has acceptance and verification |
| Cross-boundary, data, security, or costly choice | [`architect`](roles/architect.md) | researcher | Decision and rollback are explicit |
| Recent, uncertain, versioned, external-API, security, or cost claim | [`researcher`](roles/researcher.md) | architect | Official evidence and uncertainty logged |
| Approved change must be implemented | [`executor`](roles/executor.md) | auditor | Acceptance evidence is green |
| Behavior, risk, or release needs independent challenge | [`auditor`](roles/auditor.md) | researcher | Findings resolved or accepted |
| Durable knowledge changed | [`documentation-curator`](roles/documentation-curator.md) | mapper | One official home is current and linked |
| A change may be exposed to users or an environment | [`release-manager`](roles/release-manager.md) | auditor | Approval, rollback, and observation exist |

One agent may perform several roles sequentially on small, low-risk tasks, but
must honor each role's gate. Use a specialist or independent review when risk or
uncertainty warrants it.

## Risk routing

| Level | Examples | Required handling |
| --- | --- | --- |
| Low | Docs, reversible local refactor, isolated test | Lead role; proportional verification |
| Medium | User-visible behavior, dependency/config change, data model design | Plan plus auditor; research if trigger applies |
| High | Auth, privacy, security, material cost, migration, external integration | Architect, researcher, auditor, rollback plan, owner-visible approval |
| Restricted | Production action, deploy, database mutation, infrastructure/DNS, payments, new access, paid service | Explicit product-owner approval immediately before action; release-manager gate |

If risk rises during work, stop at the new gate. Approval to design or prepare is
not approval to execute a restricted action.

## Product-owner communication

- Maintain one coordinator as the product owner's voice and point of contact.
- Explain decisions as outcome, impact, risk, evidence, and next choice in plain
  language. Translate technical terms when they first matter.
- Ask only questions that materially change scope, safety, cost, or outcome.
- Offer a recommendation; do not make the owner orchestrate roles or agents.
- Concise machine-style payloads are acceptable only between cooperating agents
  when they improve reliability. Never force them on the product owner or use
  terseness to hide uncertainty.

## Shared operating rules

- Safety: [`guardrails/safety.md`](guardrails/safety.md)
- Research: [`policies/research.md`](policies/research.md)
- Context: [`practices/token_economy.md`](practices/token_economy.md)
- Testing: [`practices/tdd.md`](practices/tdd.md)
- Done: [`practices/definition-of-done.md`](practices/definition-of-done.md)
- Adoption: [`practices/project-adoption.md`](practices/project-adoption.md)
- Delegation: [`practices/subagent-orchestration.md`](practices/subagent-orchestration.md)

## Finish every task

Report the useful outcome, verification performed, remaining uncertainty, and
any decision or approval needed. Update [`project/state.json`](project/state.json)
last so it reflects the actual handoff rather than intent.
