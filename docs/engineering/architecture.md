# Architecture

**Status:** Current truth  
**Accountable role:** Architecture/engineering owner  
**Last reviewed:** 2026-07-28  
**Review trigger:** A new knowledge category, role, mode, gate, or execution
mechanism is introduced

## System shape

The kit is a document-driven control system around project work:

```text
Product owner
    ↕ plain-language outcomes and approvals
Coordinator
    → mode + task + risk router
    → role contracts and specialist work
    ↔ operational memory (.ai/project)
    → implementation and verification in the adopted repository
    → durable human truth (docs)
    → explicit release gate
```

The coordinator is the only product-owner voice. Roles are contracts, not
necessarily separate agents. A small task can move through several contracts in
one context; independent or specialized work may be delegated under a bounded
handoff.

## Boundaries

### Operational plane: `.ai/`

The canonical router selects `NEW_PRODUCT` or `ADOPT_PROJECT`, classifies
task/risk, and loads relevant role and policy files. `.ai/project/` carries
small, current, repository-specific state. Templates structure transient work.
Guardrails and policies define non-negotiable boundaries.

### Human knowledge plane: `docs/`

Product and engineering documents state current truth. ADRs preserve material
decision history. Runbooks define safe operations. Each topic has one official
home and is linked elsewhere.

### Adopted project plane

Source, tests, configurations, automation, environments, and external services
belong to the repository that consumes the kit. They are evidence, not
controlled by generic assumptions. The kit records their verified shape without
copying sensitive values.

## Control flow

1. Load current state, scope, and terms.
2. Select a mode.
3. Translate owner intent and map/discover uncertainty.
4. Research triggered claims from official/primary sources.
5. Make and record material design decisions.
6. Plan and implement coherent, testable slices.
7. Independently challenge behavior and risk in proportion to impact.
8. Curate durable knowledge into one official home.
9. Prepare a release; stop for immediate explicit approval at restricted
   actions.
10. Verify outcome and refresh health/state.

## Safety architecture

Restricted actions are capabilities behind an explicit human approval gate, not
ordinary delivery steps. Access levels are separate and least-privilege.
Backups, restoration evidence, rollback, stop conditions, and observation
protect stateful/high-risk changes. Repositories store references to secret
management and access processes, never secret values.

## Changeability

The system is modular by document contract: roles can evolve without changing
the memory boundary; practices can adapt by task type; adopted repositories add
technology-specific truth under their own current architecture/runbooks. The
dependency-light validator checks structure, JSON, and links without coupling
the kit to the adopted stack.

See [ADR-0001](../decisions/0001-separate-operational-memory-from-human-docs.md)
and [ADR-0002](../decisions/0002-use-two-explicit-operating-modes.md).
