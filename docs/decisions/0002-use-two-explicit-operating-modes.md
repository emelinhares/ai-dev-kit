# ADR-0002: Use two explicit operating modes

**Status:** Accepted  
**Date:** 2026-07-28  
**Decision owners:** Product and workflow architecture  
**Related architecture:** [Current architecture](../engineering/architecture.md)

## Context

A new product needs problem discovery and boundary formation. An inherited
project first needs evidence-based mapping, health assessment, and safe access
understanding. Treating both situations as immediate planning risks solving an
unvalidated problem or changing an unknown system.

## Decision

Every task starts in `NEW_PRODUCT` or `ADOPT_PROJECT`. Both modes share task and
risk routing, safety, research, testing, documentation, and release gates.
`NEW_PRODUCT` begins from outcome discovery; `ADOPT_PROJECT` begins from intake
and observation, and always maintains a repository-owned glossary.

## Consequences

The initial workflow fits the available evidence without duplicating two full
processes. If project state is absent or unreliable, the conservative default is
`ADOPT_PROJECT`. A mode selects the starting posture; it does not grant access
or waive approvals.
