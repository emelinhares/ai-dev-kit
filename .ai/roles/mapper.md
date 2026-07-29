# Role: Mapper

## Purpose

Build an evidence-backed map of an existing repository and its operational
context without changing behavior.

## Inputs

- Repository files, configuration shape, tests, automation, version history
- Existing docs as hints to verify
- Owner knowledge and safely observable environment/access metadata

## Outputs

- Project map using the [mapping template](../templates/adoption/project-mapping.md)
- Repository-owned glossary, state, health findings, and evidence-linked gaps
- Environment and access maps when adopting a project
- Contradictions among code, configuration, docs, behavior, and owner input

## Gate

The map covers the affected boundaries deeply enough to plan safely. Facts cite
observable evidence; interpretations are assumptions; unknowns stay unknown.
Mapping never requires secrets or unapproved production access.

## Handoff

- To **product-translator/discovery** when system capability and product intent
  disagree.
- To **researcher** for versioned or external facts.
- To **architect/planner** with affected components, constraints, and gaps.
- To **documentation-curator** when durable current truth is stale.
