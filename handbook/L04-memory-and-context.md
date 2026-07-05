# L4 — Memory & Context

| Field | Value |
|-------|-------|
| Layer | L4 |
| Depends on Specs | 004, 005, 006, 007 |
| Status | Skeleton |

## 1. Purpose

L4 provides short-term, long-term, session, semantic memory, and user profile — externalised, indexed, and access-controlled.

## 2. Responsibilities

- **In scope.** Memory Manager, backing stores per memory type, memory access-control.
- **Out of scope.** Knowledge retrieval over documents (L5), caches (L11).

## 3. Components

- **Memory Manager** — unified read/write API over five memory types.
- **Short-Term Store** — recent turns; bounded, fast, evicted on session end.
- **Long-Term Store** — durable, identity-bound, persistent across sessions.
- **Session Memory Store** — working notes / intermediate results for the active session.
- **Semantic Memory Store** — vectorised recall of prior conversations or facts.
- **User Profile Store** — structured, durable preferences and attributes.

## 4. Design principles

**P6 Externalised State**, **P2 Security** (identity-scoped access), **P9 Cost** (per-store cost model).

## 5. Patterns

- Write-through for short-term to session store.
- Summarisation into long-term when short-term evicts.
- PII classification at write, not at read.

## 6. Anti-patterns

- Memory pinned to compute instance (breaks P6).
- Un-scoped memory reads (returns records outside caller's authorisation).
- Free-text memory with no schema (silent quality decay).

## 7. Failure modes

| Failure | Degraded mode |
|---------|---------------|
| Long-term store outage | Session memory only + read-only fallback |
| Semantic store latency | Skip semantic; short-term only |

## 8. Observability

Memory type accessed, read/write counts, latency, PII classification hits, cross-scope access attempts (should be zero).

## 9. Production checklist

- [ ] Every record has an owning identity.
- [ ] Access-control tests in CI.
- [ ] Retention policy per memory type documented and enforced.
- [ ] Summarisation cost tracked in the cost ledger.
