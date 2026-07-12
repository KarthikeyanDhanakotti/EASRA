# EA-008 · Memory Plane

**Status:** Stub (v0.0.1) · **Sprint:** planned Sprint-03 · **Taxonomy:** `EA-`

> Placeholder page. The full Memory Plane specification will land in **Sprint-03**. Preview content lives inside [EA-003 · Runtime Plane](EA-003-Runtime-Plane.md) — this page will lift and expand it into a self-contained architecture.

## Purpose

Define how enterprise AI systems **remember** — across turns, sessions, users, agents, and organizations — with clear TTL, consent, and forget semantics.

## Scope (draft)

- **Working memory** (turn / step scratchpad)
- **Session memory** (user + conversation, TTL-bounded)
- **Long-term memory** (user preferences, learned facts, consent-gated)
- **Vector memory** (episodic embeddings, recency-decayed)
- **Shared / team memory** (cross-agent artifact store, RBAC per key namespace)
- **Task state** (durable workflow checkpoints)
- **Forget contract** — every tier implements `POST /forget?subject=X` returning 200 only after complete removal (rows, indices, embeddings, derived artifacts)
- Memory-quality metrics (hit rate, staleness, contradiction detection)

## Design Goals (draft)

- G1 · Every memory operation is observable, tier-labeled, and traceable to the request that wrote it.
- G2 · Forget is a strong guarantee, not a soft promise. Compliance-testable.
- G3 · Memory is scoped by identity, tenant, and purpose. Cross-scope reads require explicit policy grant.
- G4 · Memory quality is measured, not assumed — episodic memories have decay + confidence.

## Related

- Currently previewed inside [EA-003 · Runtime Plane](EA-003-Runtime-Plane.md)
- Registry governed by [EA-004 · Control Plane](EA-004-Control-Plane.md)
- Related patterns (planned): PAT-006 Memory
- Related decisions (planned): ADR-009 Forget contract

## Changelog

- v0.0.1 · Sprint-02 · Stub created as part of the 15-view architecture map.
