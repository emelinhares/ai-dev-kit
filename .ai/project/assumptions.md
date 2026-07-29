# Active Assumptions

Assumptions are temporary claims that can change work. Validate them early and
move resolved facts to their official home; do not turn this file into history.

| Assumption | Impact if wrong | Validation / owner | Status |
| --- | --- | --- | --- |
| The kit must remain usable without a specific language, framework, hosting provider, or delivery platform. | Stack-specific commands or role contracts would make adoption unsafe or incomplete. | Validate all guidance and templates during structural review. | Active |
| The adopting repository will supply its own commands, environments, owners, and risk details. | Generic templates cannot truthfully claim project readiness. | Mapper fills repository-specific evidence in ADOPT_PROJECT mode. | Active |
| A product owner may delegate routine local implementation but retains approval for restricted actions. | The safety boundary and owner experience would be ambiguous. | Enforced by router, guardrails, and release gate. | Accepted requirement |

Record uncertainty, not secrets or private stakeholder details. Remove an
assumption when it becomes a verified fact, rejected claim, ADR, or scope item.
