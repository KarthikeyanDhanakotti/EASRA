# PAT-008 · Model Router

**Status:** Stub (v0.0.1) · **Sprint:** planned Sprint-03 · **Layer:** L2, L6 · **Taxonomy:** `PAT-`

> Placeholder page. The full Model Router pattern will land in **Sprint-03**.

## Context

Enterprises rarely run one model. They run a fleet — different sizes, providers, regions, tiers — with different cost, latency, quality, and residency profiles. Routing decisions can't live in application code.

## Solution (outline)

- Declarative, versioned **routing policy** stored in the Control Plane and consumed by the Gateway
- Router evaluates policy against `{task_class, sensitivity, tenant_tier, budget, region, latency_slo}` from Prompt Intelligence
- **Fallback chain** — primary → secondary → cached-degraded — with per-hop deadlines
- **Circuit breakers** per model/endpoint, per region
- A/B routing for evaluation and safe rollout of new models
- Every decision emitted as `easra.route.decision` + `easra.route.reason` on the span

## Interfaces (to be specified)

- Routing policy JSON schema (versioned)
- `GET /v1/router/decision/preview` — dry-run a route for a hypothetical input

## Controls

- Blocked-model list per tenant / per region
- Cost-cap short-circuits (over budget → route to cheaper model or fail-fast)
- Circuit-break threshold + cool-down

## KPIs

- Fallback rate
- Circuit-break events
- Per-tenant cost / quality / latency scorecards
- Router-decision consistency (reproducibility)

## Trade-offs

- Static routing = predictable but wastes budget
- Adaptive routing = efficient but harder to reason about — must remain explainable
- Multi-region routing helps residency but complicates cost accounting

## Anti-patterns

- Routing logic in application code
- Silent fallbacks with no observability
- Routing based on model name substring matching

## Related

- Realizes [EA-006 · Model Router](../architectures/EA-006-Model-Router.md)
- Lives inside [EA-002 · AI Gateway](../architectures/EA-002-Enterprise-AI-Gateway.md) Stage 5
- Related decisions (planned): ADR-004 AI Gateway as sole ingress

## Changelog

- v0.0.1 · Sprint-02 · Stub created as part of the pattern-catalog completion plan.
