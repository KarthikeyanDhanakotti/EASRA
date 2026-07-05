# L11 — Performance · Caching · Cost

| Field | Value |
|-------|-------|
| Layer | L11 |
| Depends on Specs | 004, 005, 006, 007 |
| Status | Skeleton |

## 1. Purpose

L11 provides the cache plane (prompt, semantic, embedding, memory, response) and the cost ledger.

## 2. Responsibilities

- **In scope.** Cache Manager, per-tier caches, invalidation policy, cost accounting and attribution.
- **Out of scope.** Model routing (L6), autoscaling policy (infrastructure), business KPIs (L15).

## 3. Design principles

**P9 Cost Awareness**, **P6 Externalised State**, **P2 Security** (ACL-scoped caches).

## 4. Patterns

- Per-tier invalidation triggers (template version, embedding model version, grounding freshness).
- Semantic cache with identity-scoped keys.
- Write-through on memory-cache.
- Cost ledger with tenant / user / agent attribution.

## 5. Anti-patterns

- PII in cache keys.
- Shared cache across identities with different authorisation scopes.
- Stale grounding served by semantic cache.

## 6. Observability

Hit/miss per tier, saved cost, saved latency, cost per request, cache invalidation events.

## 7. Production checklist

- [ ] All keys reviewed for PII / ACL.
- [ ] Invalidation policy documented per tier.
- [ ] Cost ledger reconciles with provider bills.
