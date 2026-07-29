# Adaptive Context Management

Optimize for correct decisions per unit of context, not minimum words.

## Load progressively

1. Start with the router, project state, scope, relevant glossary terms, and
   task-specific files.
2. Search for symbols and evidence before opening large files.
3. Read adjacent code, tests, configuration, and history only when they can
   change the decision.
4. Ignore generated/vendor artifacts unless they are the subject of the task.
5. Reuse an existing repository map; rescan only stale or affected areas.

## Compress responsibly

- Keep summaries around decisions, constraints, evidence, file/symbol
  references, open risks, and next actions.
- Prefer focused diffs and complete implementations over broad rewrites.
- Preserve exact text only for interfaces, errors, requirements, or evidence
  whose wording matters.
- Replace long tool output with a short finding and a reproducible reference.
- Never omit uncertainty, safety constraints, or a failing check to save tokens.

## Communicate for the audience

Internal handoffs should be structured and concise: outcome, evidence, changed
artifacts, risks, and next gate. Product-owner updates should remain plain,
helpful, and sufficient for a decision. Technical silence is not a goal.

## Refresh and stop

Refresh context after a scope change, conflicting evidence, or long execution
phase. Stop investigating when acceptance can be evaluated and remaining
uncertainty is either immaterial, explicitly assumed, or gated by an owner
decision. Do not perform redundant scans “for completeness.”
