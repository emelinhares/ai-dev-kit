# Adaptive Subagent Orchestration

Subagents are optional. Use them only when work is independently executable,
specialized, or benefits from an independent challenge. Coordination overhead
must be lower than the expected gain.

Good candidates include independent repository areas, focused official-source
research, security/access review, test design, or release-readiness review. Do
not delegate tightly coupled edits, trivial searches, the same scan to multiple
agents, or decisions that require one continuously shared context.

## Coordinator contract

The coordinator:

- remains the single product-owner voice;
- defines a bounded task, inputs, allowed actions, expected output, evidence,
  and stop/approval conditions;
- gives agents the existing map and relevant context so they do not repeat
  broad scans;
- prevents overlapping writes unless intentional;
- integrates and verifies results rather than forwarding raw transcripts; and
- owns the final recommendation and project-memory update.

Use as few agents as the task needs. Parallelize only independent work. Handoffs
should contain outcome, evidence references, changed files, risks, uncertainty,
and next gate—not long dialogue or tool output.

An agent may not inherit approval to perform production, deploy, mutation,
infrastructure/DNS, payment, access, or paid-service actions. Those actions
remain behind the explicit owner approval boundary.
