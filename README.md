# AI Development Kit

A technology-agnostic operating system for building or adopting software with a
non-technical product owner and AI collaborators. It turns plain-language goals
into evidence-backed plans, safe implementation, maintained project memory, and
release-ready documentation without requiring the owner to manage technical
roles.

## Quick start

1. Copy the kit into the repository and point the AI collaborator to
   [`AGENTS.md`](AGENTS.md).
2. Choose `NEW_PRODUCT` for an intentionally new product or `ADOPT_PROJECT` for
   an existing, inherited, or uncertain repository.
3. Describe the desired outcome in ordinary language: who needs what, why it
   matters, and any deadline, budget, or safety concern.
4. Let the kit map or discover enough context. Review the short product summary,
   scope, risks, and recommended plan.
5. Approve decisions and restricted actions only when their target, impact,
   cost, verification, and rollback are clear.

No particular language, framework, cloud, test runner, or deployment tool is
assumed.

## Two operating modes

- **NEW_PRODUCT** establishes the problem, users, scope, success evidence,
  architecture, and delivery slices before implementation.
- **ADOPT_PROJECT** first maps observable truth, reconciles existing
  documentation, reports project health, and identifies the least access needed
  before proposing changes.

The canonical mode and task router lives in [`.ai/AGENTS.md`](.ai/AGENTS.md).

## How the owner interacts

The product owner has one coordinator and can stay at the level of outcomes and
trade-offs. A useful request can be as simple as:

> Customers abandon setup because they do not know what to do next. Help me
> reduce that confusion without changing billing.

The coordinator translates that into discovery questions, evidence, acceptance
criteria, delivery work, and plain-language decisions. It should ask only for
choices that materially affect scope, safety, cost, or outcome.

## Safety model

The kit defaults to least privilege, reversible changes, evidence, and explicit
uncertainty. Explicit owner approval is required immediately before production
actions, deployments, database mutations, infrastructure or DNS changes,
payments, new access, paid services, or other destructive/difficult-to-reverse
operations. Backups, rollback, stop conditions, and observation are required
where state or users can be affected.

Credentials, SSH private keys, tokens, production data, and unnecessary
personal data must never be stored in this repository. See
[the safety guardrails](.ai/guardrails/safety.md).

## Information architecture

- [`.ai/`](.ai/README.md) — compact operational memory, roles, policies,
  practices, state, and working templates.
- [`docs/`](docs/README.md) — durable human-facing product truth, engineering
  truth, historical decisions, and operational runbooks.

Each topic has one official home. Indexes and project memory link to that home
instead of restating it.

## Validate the kit

Run the dependency-free structural checker with a local Python 3 interpreter:

```text
python3 scripts/validate_kit.py
```

It checks required files, JSON validity, relative Markdown links, and common
sensitive-file names. It does not prove the adopted product is correct or safe;
project-specific tests and review remain necessary.
