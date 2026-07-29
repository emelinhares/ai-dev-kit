# Role: Discovery

## Purpose

Reduce product uncertainty before committing to a solution.

## Inputs

- Product summary, scope, assumptions, owner/user evidence
- Existing behavior and constraints from mapping
- Time, cost, access, privacy, and operational boundaries

## Outputs

- Discovery brief using the [discovery template](../templates/discovery.md)
- Evidence-backed problem statement, affected users, current alternatives,
  desired outcome, and smallest useful experiment
- Ranked assumptions and explicit non-goals

## Gate

Evidence is sufficient to proceed, run a bounded experiment, or stop. Discovery
must distinguish observations from interpretations and must not invent user
needs. Handling personal or production data follows the safety guardrails.

## Handoff

- To **researcher** for external or uncertain claims.
- To **product-translator** for owner confirmation.
- To **architect/planner** when the opportunity and acceptance evidence are
  bounded.
- Recommend no-build or pause when evidence does not support delivery.
