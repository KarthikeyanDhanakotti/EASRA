# EA-001 · Enterprise AI Systems Reference Architecture

![EA-001 v1.0 Enterprise AI Systems Reference Architecture](../diagrams/EA-001-Enterprise-AI-Systems-Reference-Architecture-v1.png)

> **Version:** 1.0 (Sprint-02) · supersedes v0.0.1 Sprint-01 draft
> **Status:** Canonical. Unified Fluent-style iconography, four labeled bands, Governance pillar, high-resolution SVG.
> **Source files:**
> - v1.0 (current): [SVG](../diagrams/EA-001-Enterprise-AI-Systems-Reference-Architecture-v1.svg) · [PNG](../diagrams/EA-001-Enterprise-AI-Systems-Reference-Architecture-v1.png)
> - v0.0.1 (Sprint-01 archive draft): [SVG](../diagrams/EA-001-Enterprise-AI-Systems-Reference-Architecture.svg) · [PNG](../diagrams/EA-001-Enterprise-AI-Systems-Reference-Architecture.png)

---

## Purpose

**EA-001** is the flagship reference architecture of EASRA. It defines the target-state blueprint for an enterprise-grade AI platform — the planes, building blocks, contracts, and controls an organization needs to deliver AI capabilities safely, observably, and at cost.

It answers three questions for architects, platform teams, and CTO offices:

1. **What are the required capabilities** of an enterprise AI platform?
2. **How do those capabilities compose** into a coherent, governed system?
3. **Where do concerns live** — safety, evaluation, cost, identity — so nothing falls through the cracks?

EA-001 is **vendor-neutral**. It names *capabilities*, not products. Product-specific mappings will live in an `examples/` folder in Sprint-02.

---

## The Seven Planes

EA-001 organizes an enterprise AI platform into **six request-path planes** and **one cross-cutting plane**.

| # | Plane                              | One-line responsibility                                                     |
|--:|------------------------------------|-----------------------------------------------------------------------------|
| 1 | **Experience**                     | User- and app-facing surfaces (chat, copilots, APIs, embedded UX)           |
| 2 | **AI Gateway**                     | Single policy-enforcing ingress: auth, routing, quotas, redaction, telemetry|
| 3 | **Agent / Orchestration**          | Planner, executor, tools/MCP, memory, multi-agent workflows                 |
| 4 | **Model**                          | Hosted & self-hosted models, registry, versioning, fine-tuning              |
| 5 | **Knowledge & Data**               | Corpora, embeddings, retrievers, vector/feature stores, data contracts      |
| 6 | **Evaluation & Telemetry**         | Tracing, offline & online eval, continuous monitoring, feedback capture     |
| 7 | **Safety, Governance & FinOps**    | Guardrails, policy, DLP, controls mapping, cost & quota governance          |

Planes **1 → 6** are the request path. Plane **7** cross-cuts every other plane.

---

## Components

### 1. Experience plane
- Web apps (chat, copilots), mobile, embedded UX
- Programmatic APIs and SDKs
- Notebooks / IDE integrations for developers and analysts
- External / partner agents and marketplace surfaces

### 2. AI Gateway plane
- **AuthN / AuthZ** — identity, API keys, tenant isolation
- **Model router** — chooses target model by cost, latency, capability, or policy
- **Quota & rate limits** — per tenant / app / user / model
- **Policy & redaction** — guardrail hooks, DLP, safety pre-/post-filters
- **Caching** — prompt cache, semantic response cache
- **Telemetry hook** — emits traces, cost, and eval signals to Plane 6

### 3. Agent / Orchestration plane
- Planner and executor (single- or multi-agent)
- Tool runtime + **MCP servers**
- Short-term and long-term memory
- Workflow / multi-agent orchestration primitives

### 4. Model plane
- Model registry with lifecycle state and metadata
- Versioning and canary/blue-green promotion
- Hosted endpoints, self-hosted / edge deployments
- Fine-tuning pipelines: **SFT**, **DPO**, **RFT**
- Embedding and reranker models

### 5. Knowledge & Data plane
- Corpora / source systems (docs, tickets, databases, streams)
- Chunk + embed pipeline
- **Vector store** for retrieval
- **Feature store** for structured features
- Retriever + reranker + query rewriter
- Data contracts and provenance

### 6. Evaluation & Telemetry plane
- Distributed **tracing** across prompt · retrieval · tool · model spans
- **Offline evaluation** with datasets, graders, regression gates
- **Online / continuous** monitoring with drift alerts
- Feedback capture (explicit and implicit)
- Dataset curation loop: traces → eval sets → fine-tune data
- Cost/quality metrics feed FinOps

### 7. Safety, Governance & FinOps plane *(cross-cutting)*
- Content safety, prompt-injection defense, PII / DLP
- Policy engine (declarative rules over prompts, tools, and outputs)
- Identity & RBAC, audit, controls mappings (NIST AI RMF, ISO/IEC 42001, EU AI Act)
- Cost & unit economics, quotas & budgets, chargeback/showback

---

## Design Principles

1. **Vendor-neutral by default.** Capabilities are named; products are examples.
2. **Single ingress for AI traffic.** All model, agent, and tool calls flow through the AI Gateway.
3. **Composable planes with clear contracts.** Each plane can be evolved independently.
4. **Verification-first.** Every request emits enough signal to be evaluated, replayed, and audited.
5. **Governance by construction.** Plane 7 is enforced *in-path*, not bolted on.
6. **Reversible decisions.** Model, retriever, and gateway policy choices are configuration, not code.
7. **Cost is a first-class metric.** Cost and quality are graded together, not in isolation.

---

## Data Flow

Informal end-to-end request path:

```
User / App (Plane 1)
        │
        ▼
  AI Gateway (Plane 2)  ── authN, quota, policy, redact, route
        │
        ├──► Agent / Orchestration (Plane 3)
        │            │
        │            ├──► Tools · MCP servers
        │            └──► Knowledge & Data (Plane 5)  ── retrieve · rerank
        │
        └──► Model (Plane 4)  ── generate · embed · rerank

Every hop  ──► Evaluation & Telemetry (Plane 6)   [traces, cost, eval]
Every hop  ◄── Safety, Governance & FinOps (Plane 7)  [policy, guardrails]
```

Sprint-02 will publish a formal sequence-level flow diagram alongside the redesigned EA-001.

---

## Interfaces (Sprint-02)

Formal interface contracts between planes will land in Sprint-02:

- Gateway ↔ Model plane (routing & fallback contract)
- Gateway ↔ Safety plane (policy decision point / policy enforcement point)
- Orchestration ↔ Tools/MCP (tool discovery, invocation, error model)
- Telemetry contract (span schema, cost fields, eval outcomes)

---

## Known Limitations of the Sprint-01 Draft

This diagram is a **first draft**. For the official EASRA v1.0 release it will be redesigned with:

- Consistent typography and aligned spacing
- Unified Fluent-style iconography
- Higher-resolution SVG (canonical) with sharper PNG export
- Clearer visual separation between **Control Plane**, **Runtime Plane**, **Data Plane**, and **Governance pillars**
- Presentation-grade version suitable for the README, docs site, conference slides, and the EASRA whitepaper

Track progress in [`../ROADMAP.md`](../ROADMAP.md) → Sprint-02.

---

## Related Architectures

| ID     | Title                                | Status     |
|--------|--------------------------------------|------------|
| EA-001 | Enterprise AI Systems Reference Architecture | ✅ Sprint-01 draft (this page) |
| EA-002 | AI Gateway                           | ⏭️ Sprint-02 |
| EA-003 | Runtime Plane                        | ⏳ Planned  |
| EA-004 | Control Plane                        | ⏳ Planned  |
| EA-005 | Evaluation & Telemetry Plane         | ⏳ Planned  |
| EA-006 | Safety, Governance & FinOps Plane    | ⏳ Planned  |

---

## Changelog

- **2026-07-12** — v0.0.1 · First-draft SVG + PNG committed as EA-001 placeholder (Sprint-01).
