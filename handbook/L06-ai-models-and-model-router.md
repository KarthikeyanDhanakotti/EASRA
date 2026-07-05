# L6 — AI Models & Model Router

| Field | Value |
|-------|-------|
| Layer | L6 |
| Depends on Specs | 004, 005, 006, 009 |
| Status | Skeleton |

## 1. Purpose

L6 selects and invokes the model best suited to the request across capability, cost, latency, availability, and policy.

## 2. Responsibilities

- **In scope.** Model Router, Provider adapters, Fallback, Cost accounting, Model Registry client.
- **Out of scope.** Prompt building (L3), guardrails (L8), verification (L9), tool execution (L7).

## 3. Design principles

**P1 Vendor Neutrality**, **P8 Failure Isolation** (fallback), **P9 Cost Awareness** (per-call cost accounting), **P2 Security** (TB-C enforcement).

## 4. Patterns

- Capability-based routing (chat / rerank / embed / classify / moderate).
- Cost / latency / availability-aware routing (extension point).
- Circuit breaker per provider; back-off; fallback model.
- Egress network policy allowing only approved model endpoints.

## 5. Anti-patterns

- Hard-coded provider SDK in upstream layers.
- Routing that ignores PII classification.
- Model calls without token/cost accounting.

## 6. Failure modes

| Failure | Degraded mode |
|---------|---------------|
| Primary provider down | Fallback model; emit metric |
| Rate limit | Route to alternate provider |
| Timeout | Structured error; caller decides |

## 7. Observability

Model ID, tokens (prompt / completion / cached), cost, latency, provider, fallback events, PII-routing decisions.

## 8. Security

Enforces **TB-C**. Secrets never in prompts. PII policy drives routing. Model registry (L14) is authoritative.

## 9. Production checklist

- [ ] Every call emits tokens + cost.
- [ ] Fallback tested via chaos.
- [ ] Egress policy limits providers.
- [ ] Model registry gates deployment.
