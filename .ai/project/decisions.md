# Decision Index

This is a compact operational index, not a second decision archive. Material
historical rationale lives in [`docs/decisions/`](../../docs/decisions/README.md).

| Decision | Status | Current effect | Durable record |
| --- | --- | --- | --- |
| Separate operational memory from human documentation | Accepted | `.ai/` holds compact working context; `docs/` holds durable human truth | [ADR-0001](../../docs/decisions/0001-separate-operational-memory-from-human-docs.md) |
| Route work through NEW_PRODUCT or ADOPT_PROJECT | Accepted | Every task selects a mode before role/risk routing | [ADR-0002](../../docs/decisions/0002-use-two-explicit-operating-modes.md) |

Add a row when a decision changes active work. Add or supersede an ADR when the
choice is architecturally material; do not paste the rationale here.
