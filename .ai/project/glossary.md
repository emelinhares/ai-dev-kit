# Project Glossary

This repository always maintains its own glossary. The mapper and documentation
curator reconcile terms against code, configuration, behavior, owner language,
and existing docs; no external glossary is sole truth.

| Term | Meaning in this repository |
| --- | --- |
| AI Development Kit | The technology-agnostic roles, policies, practices, memory, docs, and templates in this repository |
| Product owner | The person accountable for product outcome, material trade-offs, and restricted-action approval; technical expertise is not assumed |
| Coordinator | The single AI collaborator that speaks with the product owner, routes work, integrates specialists, and owns the handoff |
| Operational memory | Compact current working context in `.ai/`, including state, scope, terms, evidence, assumptions, and role/policy contracts |
| Human documentation | Durable product, engineering, decision, and runbook truth under `docs/` |
| Official home | The one canonical location for a topic; other files link to it rather than restate it |
| Document mudball | Duplicated, mixed-purpose, ownerless documentation whose claims drift or conflict |
| Current truth | The best verified description of how the product/system works now; architecture docs carry this |
| ADR | Architecture Decision Record: an immutable historical account of a material decision and its context, superseded by a new ADR rather than rewritten |
| Runbook | A human operational procedure with prerequisites, safe steps, verification, rollback, escalation, and ownership |
| NEW_PRODUCT | Router mode for an intentionally new product or clean-slate initiative |
| ADOPT_PROJECT | Router mode for an existing, inherited, unclear, or partially documented repository |
| Research trigger | Uncertainty, recency, versions, security/cost sensitivity, or external APIs that require official-source evidence before a decision |
| Observation access | Read-only access to approved metadata, logs, metrics, or sanitized data |
| Development access | Permission to change an isolated non-production workspace/environment |
| Limited-operation access | Permission for one narrow, pre-approved operational action |
| Release access | Permission to deploy or promote an approved artifact |
| Admin access | Broad identity, policy, billing, infrastructure, or data control |
| Restricted action | Production, deploy, database mutation, infrastructure/DNS, payment, new access, paid service, or destructive action requiring explicit approval |
| Acceptance evidence | A check, observation, or review showing the owner-visible outcome and relevant failure behavior |
| Health report | Evidence-based snapshot of maintainability, verification, security, delivery, operability, documentation, and known gaps |

## Repository map

| Path | Responsibility |
| --- | --- |
| `AGENTS.md` | Thin, discoverable pointer to the canonical router |
| `.ai/AGENTS.md` | Canonical mode, task, risk, and role router |
| `.ai/project/` | Repository-specific operational memory |
| `.ai/roles/` | Purpose, inputs, outputs, gates, and handoffs for each role |
| `.ai/guardrails/` | Mandatory safety boundaries |
| `.ai/policies/` | Decision policies such as research |
| `.ai/practices/` | Adaptive delivery practices |
| `.ai/templates/` | Reusable working and onboarding templates |
| `docs/product/` | Durable product truth |
| `docs/engineering/` | Durable current engineering/architecture truth |
| `docs/decisions/` | Historical ADRs |
| `docs/runbooks/` | Operational procedures |
| `scripts/` | Dependency-light kit validation |

When adopting this kit into another repository, replace repository-specific map
entries while preserving and extending the workflow vocabulary actually used.
