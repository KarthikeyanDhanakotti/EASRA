# EA-006 · Model Router

**Status:** Stub (v0.0.1) · **Sprint:** planned Sprint-03 · **Taxonomy:** `EA-`

> Placeholder page. The full Model Router specification will land in **Sprint-03**.

## Purpose

Define how EASRA chooses **which model, which endpoint, which region, and which fallback chain** for each request — the "cost-latency-quality-safety" decision point.

## Scope (draft)

- Routing policy schema (versioned, promotable via Control Plane)
- Routing signals (task class, sensitivity, tenant tier, budget, latency SLO, region residency)
- Fallback chains (primary → secondary → cached-degraded)
- Circuit breakers per model / per endpoint
- Router observability (`easra.route.decision`, `easra.route.reason`)
- A/B routing for evaluation and safe rollout
- Per-tenant overrides and blocked-model lists

## Design Goals (draft)

- G1 · Every routing decision is explainable — attribute-attached to the span, reproducible from the input.
- G2 · Policy changes flow through the Control Plane, not through code deploys.
- G3 · Router failure never blocks the request — always has a safe fallback (including "return cached with degraded flag").
- G4 · A/B routing is a first-class capability, not a hack.

## Related

- Lives inside [EA-002 · AI Gateway](EA-002-Enterprise-AI-Gateway.md) as Stage 5
- Consumes registries from [EA-004 · Control Plane](EA-004-Control-Plane.md)
- Related patterns (planned): PAT-008 Router
- Related decisions (planned): ADR-004 AI Gateway as sole ingress

## Changelog

- v0.0.1 · Sprint-02 · Stub created as part of the 15-view architecture map.
