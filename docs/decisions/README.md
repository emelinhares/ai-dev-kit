# Architecture Decision Records

ADRs preserve why material decisions were made. They are historical records,
not the source of current architecture truth.

## Index

- [ADR-0001: Separate operational memory from human documentation](0001-separate-operational-memory-from-human-docs.md)
- [ADR-0002: Use two explicit operating modes](0002-use-two-explicit-operating-modes.md)
- [ADR template](0000-template.md)

## Governance

Use an ADR for a material, cross-boundary, costly, security-relevant, or
difficult-to-reverse decision. Allocate the next number, copy the template, and
link official research evidence. Accepted ADRs keep their original context and
decision. If direction changes, add a new ADR, mark the old one `Superseded`,
and cross-link them.

Update [current architecture](../engineering/architecture.md) when an accepted
decision changes present truth. Keep the compact operational index in
[`.ai/project/decisions.md`](../../.ai/project/decisions.md).
