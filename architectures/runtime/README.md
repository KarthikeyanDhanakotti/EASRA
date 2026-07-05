# Runtime Architecture

## Purpose

The **Runtime Architecture** describes *how a request executes* across the logical structure — the step-by-step flow, the decision points, the concurrency, the caches consulted, the guardrails invoked, the models called, the tools invoked, and the verifications performed.

It does not describe physical placement (→ Deployment) or control loops (→ Operational).

## Audience

- Engineers implementing a feature, an agent, or a workflow.
- SREs debugging latency, cost, or correctness incidents.
- Evaluators authoring test cases and continuous evaluators.

## Scope

- Request lifecycle — from channel adapter to response chunk stream.
- Decision points — cache hit / miss, guardrail allow / block, impact-class gating, verification allow / escalate / block.
- Sequence diagrams for canonical scenarios.
- Data flows between layers.
- Concurrency (streaming, fan-out retrieval, parallel guardrails).

## Anchoring specifications

| Spec | Purpose |
|------|---------|
| [007 Data Flow](../../specification/007-data-flow.md) | Flows F1–F12 across the layers. |
| [008 Sequence Diagrams](../../specification/008-sequence-diagrams.md) | Sequences S1–S6 for canonical scenarios. |
| [006 Interface Specification](../../specification/006-interface-specification.md) | Interfaces exercised at runtime. |
| [010 Non-Functional Requirements](../../specification/010-nfr.md) | Latency, throughput, cost budgets that runtime must satisfy. |

## Diagrams

| ID | Title | Status |
|----|-------|--------|
| D-R1 | Master Runtime Execution Flow | Done — [`../../diagrams/runtime-execution-flow.md`](../../diagrams/runtime-execution-flow.md) |
| D-R2 | Single-Agent RAG Sequence | Done — [Spec 008 §S1](../../specification/008-sequence-diagrams.md) |
| D-R3 | Multi-Agent Coordination Sequence | Done — [Spec 008 §S2](../../specification/008-sequence-diagrams.md) |
| D-R4 | Tool-Use with Impact-Class Gating | Done — [Spec 008 §S3](../../specification/008-sequence-diagrams.md) |
| D-R5 | Guardrail + Verification Decision Flow | Planned |
| D-R6 | Cache Lookup Sequence (Prompt + Semantic + Response) | Planned |

## Change control

Adding a new canonical sequence requires a matching entry in [008 Sequence Diagrams](../../specification/008-sequence-diagrams.md). Adding a runtime decision point requires updating [007 Data Flow](../../specification/007-data-flow.md).
