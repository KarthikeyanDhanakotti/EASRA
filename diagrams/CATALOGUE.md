# EASRA Diagram Catalogue

The complete, versioned inventory of EASRA diagrams. Every diagram in the repository is listed here with an ID, view, audience, status, and file path. Any diagram not listed here is not part of EASRA.

Diagrams derive from the [Capability Model](../specification/011-capability-model.md) and reference only components in the [Component Catalogue](../specification/012-component-catalogue.md).

## ID scheme

`D-<view><n>` where `view` ∈ { `L`ogical, `R`untime, `D`eployment, `O`perational, `S`ecurity } and `n` is a stable integer.

## Status legend

| Status | Meaning |
|--------|---------|
| **Done** | Merged, renders correctly, matches the Component Catalogue. |
| **Draft** | Merged but not yet reviewed or has known caveats. |
| **Planned** | Reserved slot; expected content stated. |
| **Blocked** | Waiting on a listed prerequisite. |

## Logical view

| ID | Title | Audience | Status | Path / Note |
|----|-------|----------|--------|-------------|
| D-L1 | High-Level Architecture (16 layers) | Architect / Exec | Done | [`high-level-architecture.md`](./high-level-architecture.md) |
| D-L2 | Component Master Diagram | Architect / Engineer | Planned | All ~60 named components on one canvas, grouped by layer. |
| D-L3 | Memory Architecture (L4 zoom-in) | Engineer | Planned | Working / short / session / long / semantic / episodic / profile stores and their read/write paths. |
| D-L4 | Knowledge & Retrieval Architecture (L5 zoom-in) | Engineer | Planned | Ingestion + hybrid retrieval + reranker + source registry. |
| D-L5 | Guardrails & Verification Architecture (L8+L9 zoom-in) | Engineer / Security | Planned | Input / prompt / arg / output guardrails and the seven verification checkers. |

## Runtime view

| ID | Title | Audience | Status | Path / Note |
|----|-------|----------|--------|-------------|
| D-R1 | Master Runtime Execution Flow | Engineer / SRE | Done | [`runtime-execution-flow.md`](./runtime-execution-flow.md) |
| D-R2 | Single-Agent RAG Sequence | Engineer | Done | [Spec 008 §S1](../specification/008-sequence-diagrams.md) |
| D-R3 | Multi-Agent Coordination Sequence | Engineer | Done | [Spec 008 §S2](../specification/008-sequence-diagrams.md) |
| D-R4 | Tool-Use with Impact-Class Gating | Engineer / Security | Done | [Spec 008 §S3](../specification/008-sequence-diagrams.md) |
| D-R5 | Guardrail + Verification Decision Flow | Engineer / Evaluator | Planned | Every allow / block / escalate path across L8 and L9. |
| D-R6 | Cache Lookup Sequence | Engineer / SRE | Planned | Prompt cache → semantic cache → response cache lookup order and invalidation. |

## Deployment view

| ID | Title | Audience | Status | Path / Note |
|----|-------|----------|--------|-------------|
| D-D1 | Deployment Topology (single region) | Platform | Done | [`deployment-topology.md`](./deployment-topology.md) |
| D-D2 | Multi-Region Active-Active Topology | Platform / SRE | Planned | Global LB, regional planes, state replication, failover. |
| D-D3 | Kubernetes Placement Map | Platform | Planned | Namespaces per layer, HPA / KEDA policies, network policy. |
| D-D4 | State & Cache Placement | Platform / SRE | Planned | Where session, memory, cache, ledger, audit live. |
| D-D5 | Disaster Recovery Topology | SRE | Planned | RPO / RTO per state class; recovery flow. |

## Operational view

| ID | Title | Audience | Status | Path / Note |
|----|-------|----------|--------|-------------|
| D-O1 | Observability Plane | SRE / LLMOps | Done | [`observability-plane.md`](./observability-plane.md) |
| D-O2 | CI / CD Pipeline | LLMOps | Done | [`cicd-pipeline.md`](./cicd-pipeline.md) |
| D-O3 | Continuous Evaluation Loop | Evaluator / LLMOps | Planned | Production traces → evaluators → registries → rollout decisions. |
| D-O4 | Cost & Budget Enforcement Loop | SRE / FinOps | Planned | Per-request cost record → ledger → budget → gate. |
| D-O5 | Incident Response Runbook Overview | On-call | Planned | Signal → triage → mitigation → post-mortem loop. |

## Security view

| ID | Title | Audience | Status | Path / Note |
|----|-------|----------|--------|-------------|
| D-S1 | Trust Boundaries & Trust Planes | Security / Audit | Done | [`trust-boundaries.md`](./trust-boundaries.md) |
| D-S2 | Zero-Trust Identity Flow | Security | Planned | Identity propagation from user → gateway → agent → tool. |
| D-S3 | Prompt-Injection Defence-in-Depth | Security / Engineer | Planned | Direct and indirect injection surfaces and controls. |
| D-S4 | Data Classification & Residency Flow | Security / Compliance | Planned | Classification-aware routing across memory, retrieval, model. |
| D-S5 | High-Impact Action Gate & Audit Trail | Security / Audit | Planned | Impact-class check → HITL → audit → reconciliation. |

## Contributing a diagram

1. Confirm the components you will reference appear in the [Component Catalogue](../specification/012-component-catalogue.md).
2. Choose the correct view; a diagram belongs to exactly one.
3. Reserve an ID here as **Planned**.
4. Author the diagram in Mermaid (preferred) with an ASCII fallback.
5. **Mermaid rule:** never use empty-label dotted edges (`A -. .-> B` fails to parse on `github.com`). Use `A -.-> B` or `A -.->|"label"| B`.
6. Update the row to **Done** in the same PR.

## Change control

Adding a diagram row is additive. Removing or renaming an existing diagram requires a PR that also updates all cross-references and an [ADR](../adr/) if the change deletes content from a v0.1.0+ view.
