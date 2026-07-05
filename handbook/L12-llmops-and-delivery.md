# L12 — LLMOps & Delivery

| Field | Value |
|-------|-------|
| Layer | L12 |
| Depends on Specs | 004, 005, 009 (TP-2) |
| Status | Skeleton |

## 1. Purpose

L12 owns CI/CD, prompt/model rollout, canary and blue/green deployments, artefact registry, and evaluation gates. It is the enforcement point for **TP-2 Delivery Plane**.

## 2. Responsibilities

- **In scope.** Source integration, CI pipeline, static analysis, security scanning, prompt tests, evaluation gate, container build, artefact registry, CD pipeline, deployment strategies, model registry, prompt registry.
- **Out of scope.** Runtime request path.

## 3. Design principles

**P5 Loose Coupling** (registries as extension points), **P8 Failure Isolation** (canary + rollback), **P2 Security** (signed artefacts, secretless pipelines).

## 4. Patterns

- Evaluation regression gate blocks promotion.
- SLO-triggered auto-rollback on canary.
- Signed artefacts with SLSA provenance.
- Feature-flagged agents, guardrails, verifiers.

## 5. Anti-patterns

- Prompts changed directly in production.
- Models deployed without registry entry.
- Long-lived credentials in the pipeline.

## 6. Observability

Build/test/deploy events, evaluation deltas, rollout progress, canary error / latency / cost / verdict deltas.

## 7. Production checklist

- [ ] No untested prompt or model reaches production.
- [ ] Every deployed version traceable to a commit.
- [ ] Rollback tested in a game day.
- [ ] SBOM generated per release.
