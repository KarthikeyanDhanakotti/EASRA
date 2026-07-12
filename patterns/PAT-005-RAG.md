# PAT-005 · Retrieval-Augmented Generation (RAG)

**Status:** Stub (v0.0.1) · **Sprint:** planned Sprint-03 · **Layer:** L2, L4 · **Taxonomy:** `PAT-`

> Placeholder page. The full RAG pattern will land in **Sprint-03**.

## Context

Foundation models don't know your enterprise's private data. Fine-tuning is expensive, slow, and stale. Users expect **grounded answers with citations**.

## Problem

How do we let a model answer questions using enterprise-private knowledge, with **citations, freshness, ACL-respect, and observability**, without leaking data or blowing latency?

## Solution (outline)

1. **Ingest** documents through an ACL-aware pipeline into a chunked, embedded store.
2. **Retrieve** with query rewrite → hybrid (vector + BM25) → rerank.
3. **Ground** the model call with `{system_prompt, retrieved_context, user_query}` and enforce citation format.
4. **Verify** that the response only asserts what the retrieved context supports; block or annotate unsupported claims.
5. **Observe** retrieval quality (hit-rate, MRR, groundedness) as a first-class KPI.

## Interfaces (to be specified)

- `POST /v1/knowledge/retrieve` — retriever contract
- Citation schema in the model response envelope

## Controls

- ACL-aware retrieval (never surface chunks the caller cannot see)
- PII redaction at ingest and at retrieval
- Freshness SLA per corpus

## KPIs

- Groundedness (%)
- Retrieval MRR
- Citation coverage
- Retrieval p95 latency
- Corpus staleness

## Trade-offs

- Cost of embedding + rerank vs. answer quality
- Freshness lag vs. index-rebuild cost
- Recall vs. precision (tunable per task class)

## Anti-patterns

- Ingesting without an ACL contract
- Serving stale embeddings after source deletion
- Passing raw retrieved text without a citation contract

## Related

- Realizes capabilities in [EA-005 · Knowledge Plane](../architectures/EA-005-Knowledge-Plane.md)
- Verified via [EA-010 · Verification Plane](../architectures/EA-010-Verification-Plane.md)
- Pairs with [PAT-003 · Verification](PAT-003-Verification.md)

## Changelog

- v0.0.1 · Sprint-02 · Stub created as part of the pattern-catalog completion plan.
