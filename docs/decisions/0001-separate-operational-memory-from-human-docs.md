# ADR-0001: Separate operational memory from human documentation

**Status:** Accepted  
**Date:** 2026-07-28  
**Decision owners:** Product and documentation architecture  
**Related architecture:** [Current architecture](../engineering/architecture.md)

## Context

Agents need compact, frequently updated repository context, while people need
durable explanations with clear ownership. Mixing task state, prompts,
architecture, research, and procedures creates duplicate claims and makes
staleness hard to see.

## Decision

Use `.ai/` for the router, role/policy/practice contracts, reusable work
templates, and compact project memory. Use `docs/` for durable product truth,
current engineering truth, historical ADRs, and operational runbooks. Assign
each topic one official home; indexes and memory link rather than copy.

## Consequences

Agents must curate knowledge at handoff instead of preserving transcripts.
Current documents and working state can change at different rates without
competing as sources of truth. Contributors must decide a document's audience
and lifecycle before adding it.
