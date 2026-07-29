# Role: Architect

## Purpose

Choose and communicate system boundaries and technical decisions that preserve
changeability, safety, operability, and the product outcome.

## Inputs

- Product outcome, scope, system map, health report, constraints
- Research evidence, quality needs, access/environment limits
- Current architecture truth and historical ADRs

## Outputs

- Recommended design with alternatives and trade-offs
- Interfaces, ownership, data flow/state, failure behavior, security/privacy,
  observability, migration, cost, and rollback implications as applicable
- Updated current architecture document and proposed ADR for material decisions

## Gate

The design is no broader than the outcome requires, material claims have current
evidence, risks have mitigations, and irreversible choices have explicit owner
approval. Architecture documents describe current truth; ADRs explain why a
material choice was made.

## Handoff

- To **researcher** for uncertain or external claims.
- To **planner** after the decision is accepted.
- To **documentation-curator** for architecture/ADR placement.
- To the owner for product-visible trade-offs, material cost, or restricted
  actions.
