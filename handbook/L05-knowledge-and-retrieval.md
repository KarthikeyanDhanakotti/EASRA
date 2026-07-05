# L5 — Knowledge & Retrieval

| Field | Value |
|-------|-------|
| Layer | L5 |
| Depends on Specs | 004, 005, 006, 007 |
| Status | Skeleton |

## 1. Purpose

L5 retrieves grounding evidence from vector, keyword, structured, and graph indexes, with provenance and ACL preservation.

## 2. Responsibilities

- **In scope.** Retrieval Router, Vector DB, BM25, SQL, Graph, Reranker, Hybrid Search, Chunk store, Source Registry.
- **Out of scope.** Embedding model calls (L6), memory (L4), tool APIs (L7).

## 3. Design principles

**P2 Security** (source ACLs), **P4 Observability** (retrieval trace), **P3 Verification** (provenance for grounding).

## 4. Patterns

- Hybrid search (vector + BM25) with reranker.
- Provenance-preserving chunks (source ID, version, timestamp).
- Freshness tagging → cache invalidation.
- Query rewriting (HyDE, decomposition) as a router responsibility.

## 5. Anti-patterns

- Silent chunking without provenance.
- Returning chunks the caller may not read.
- Reranker on every query regardless of retrieval quality.

## 6. Failure modes

| Failure | Degraded mode |
|---------|---------------|
| Vector DB outage | Keyword-only fallback |
| Reranker outage | Return unreranked with metric |

## 7. Observability

Query, retrieval strategy (vector / BM25 / hybrid), per-index latency, result count, rerank latency, cache hit/miss.

## 8. Production checklist

- [ ] Every chunk carries provenance.
- [ ] Source-level ACLs enforced.
- [ ] Freshness policy driving invalidation.
- [ ] Retrieval quality measured continuously (L10).
