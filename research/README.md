# EASRA Research

Forward-looking work that extends EASRA beyond v1.0. Research chapters are exploratory: they identify a problem, survey prior art, propose a direction, and (where possible) publish a prototype. Research is *not* specification — a research idea graduates to a numbered specification only after maturation and review.

## Themes

| # | Theme | One-line problem |
|---|-------|------------------|
| R1 | Enterprise AI Execution Compiler (EAEC) | Compile an agent plan to an optimised, verifiable execution graph. |
| R2 | Enterprise AI Verification Framework | Property-based verification for agent responses beyond grader ladders. |
| R3 | Constraint-based Agent Verification | Formal constraints on plans, tool sequences, and side effects. |
| R4 | Execution Graph Optimization | Reorder / parallelise / cache steps under latency and cost constraints. |
| R5 | Enterprise AI Benchmarks | Reproducible benchmarks for latency, cost, safety, and verification. |
| R6 | Cost-aware Multi-Model Routing | Routing policies that trade quality against token cost under SLOs. |
| R7 | Agent Marketplace Protocol | Federated agent discovery and invocation with governance. |
| R8 | Skill Registry Protocol | Federated skill discovery, versioning, and provenance. |
| R9 | Vector Synchronisation Protocol | Consistent updates across replicated vector indexes. |
| R10 | Async Workflow Substrate | Durable, event-driven agent execution across long time horizons. |

## Contents

Each theme gets its own file when substantive material exists. This directory currently ships only this index; contributions are welcome — see [`../CONTRIBUTING.md`](../CONTRIBUTING.md).

## From research to specification

Research graduates to a numbered specification when:

1. A prototype exists (open source) or a reproducible study is available.
2. The problem is described in EASRA terminology (Spec 003).
3. The proposed layer, interface, or extension point is explicit.
4. At least one external reviewer has published a critique.
5. A maintainer sponsors the graduation via ADR.

## Related

- [ROADMAP §Phase 6 — Research](../ROADMAP.md#phase-6--research-parallel-to-all-phases)
- [Specification 004 §7 — Reserved extension points](../specification/004-reference-architecture.md#7-reserved-extension-points-future-specifications)
