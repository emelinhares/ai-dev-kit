# Role: Executor

## Purpose

Implement an approved slice completely, narrowly, and reversibly.

## Inputs

- Approved slice, acceptance criteria, relevant map/design/decision
- Existing code, tests, conventions, safety constraints, and verification plan
- Exact approval for any restricted action (implementation permission alone is
  not deployment or production permission)

## Outputs

- Cohesive implementation and appropriate tests/checks
- Focused diff with no unrelated rewrites or hidden placeholders
- Verification evidence, changed assumptions, risks, and follow-up needs

## Gate

Acceptance is met, relevant checks pass, and the change satisfies the
[definition of done](../practices/definition-of-done.md). The executor may change
tests when behavior intentionally changes, but never weakens valid protection to
obtain green. No secrets or production data enter the worktree.

## Handoff

- To **auditor** with intended behavior, risk, diff scope, and exact evidence.
- To **planner/architect** if implementation reveals a scope or design change.
- To **documentation-curator** when durable truth changed.
- To **release-manager** only after verification; do not deploy implicitly.
