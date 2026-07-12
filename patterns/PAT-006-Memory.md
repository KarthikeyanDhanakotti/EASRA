# PAT-006 · Memory

**Status:** Stub (v0.0.1) · **Sprint:** planned Sprint-03 · **Layer:** L3 · **Taxonomy:** `PAT-`

> Placeholder page. The full Memory pattern will land in **Sprint-03**.

## Context

Agents and copilots feel qualitatively different when they *remember* — preferences, prior turns, prior tasks, prior decisions. But unbounded memory is a legal, security, and quality liability.

## Problem

How do we give an agent useful memory across turns, sessions, users, and teams, while preserving **consent, forget guarantees, tenant isolation, and quality**?

## Solution (outline)

- Four tiers with explicit TTL: **working · session · long-term · vector**
- Optional fifth: **shared / team memory** with RBAC per key namespace
- **Forget contract** — every tier implements `POST /forget?subject=X` returning 200 only after complete removal (rows, indices, embeddings, derived artifacts)
- Memory writes are labeled by purpose and require policy grant
- Memory reads emit `easra.memory.tier` + `easra.memory.op` on the span
- Recency decay + confidence for episodic vector memory
- Contradiction detection when a new fact conflicts with a stored one

## Interfaces (to be specified)

- `POST /v1/memory/{tier}/write`
- `GET /v1/memory/{tier}/read?scope=…`
- `POST /v1/memory/forget?subject=…`

## Controls

- Consent capture at write time; consent revocation triggers forget
- Tenant isolation enforced in the store, not just at the API
- Purpose-of-use tagging on every read

## KPIs

- Recall of relevant memories (utility)
- Forget-latency p95
- Contradiction rate
- Memory-write governance-violation rate

## Trade-offs

- More memory tiers → richer behavior, larger surface area
- Vector memory decay too slow → stale personalization; too fast → forgetful agent

## Anti-patterns

- Long-term memory without a forget contract
- Sharing memory across tenants "for convenience"
- Storing raw prompts without redaction

## Related

- Realizes capabilities in [EA-008 · Memory Plane](../architectures/EA-008-Memory-Plane.md)
- Runs inside [EA-003 · Runtime Plane](../architectures/EA-003-Runtime-Plane.md)
- Related decisions (planned): ADR-009 Forget contract

## Changelog

- v0.0.1 · Sprint-02 · Stub created as part of the pattern-catalog completion plan.
