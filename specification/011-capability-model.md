# Specification 011 — Capability Model

| Field | Value |
|-------|-------|
| Status | Draft |
| Version | 0.1.0 |
| Last updated | 2026-07-05 |
| Depends on | 001, 002, 004 |
| Required by | 012, all handbook chapters, all diagrams |

## 1. Purpose

The **Capability Model** freezes *what* an Enterprise AI system must do, before any layer, component, interface, sequence, or diagram in EASRA describes *how*. It is the vocabulary from which every other EASRA artefact is derived.

Where design principles ([Spec 002](./002-design-principles.md)) constrain *how we build*, this model constrains *what we must be able to do*. Every future addition to EASRA — new layers, new components, new interfaces, new diagrams — must map to a capability enumerated here. Adding, removing, or re-scoping a capability requires an [ADR](../adr/README.md) with a 14-day public comment period.

## 2. Why capability-first

Reference architectures that start from diagrams accumulate incidental complexity: diagrams contradict prose, components appear that were never defined, layer boundaries erode without ceremony. EASRA takes the mature-framework path instead:

1. **Freeze capabilities** (this document).
2. **Freeze components** ([Spec 012 — Component Catalogue](./012-component-catalogue.md)).
3. **Freeze interfaces** ([Spec 006 — Interface Specification](./006-interface-specification.md)).
4. **Freeze data and control flows** ([Spec 007 — Data Flow](./007-data-flow.md), [Spec 008 — Sequence Diagrams](./008-sequence-diagrams.md)).
5. **Only then** publish diagrams as views over that frozen model ([Diagram Catalogue](../diagrams/CATALOGUE.md)).

## 3. Capability domains

There are **16 capability domains**, one per EASRA layer. Each is stated as *verb + object* with an explicit scope.

| ID   | Capability domain              | Scope (what it enables)                                                                                     | Maps to layer |
|------|--------------------------------|-------------------------------------------------------------------------------------------------------------|---------------|
| C0   | Interact with Users            | Multi-channel input, output, and streaming across web, mobile, chat, voice, API, SDK.                       | L0 |
| C1   | Govern Ingress                 | Authenticated, authorised, rate-limited, session-scoped, validated, budget-capped requests only.            | L1 |
| C2   | Orchestrate Reasoning          | Route, plan, and coordinate single- and multi-agent execution over a workflow.                              | L2 |
| C3   | Engineer Prompts               | Build context, assemble prompts, enforce token budgets, version templates.                                  | L3 |
| C4   | Manage Memory                  | Working, short-term, session, long-term, semantic, episodic, and profile memory.                            | L4 |
| C5   | Retrieve Knowledge             | Hybrid retrieval over vector, keyword, structured, and graph; reranking; freshness; provenance.             | L5 |
| C6   | Serve Models                   | Route across small, large, vision, speech, and embedding models with fallback and cost control.             | L6 |
| C7   | Execute Tools & Actions        | Invoke enterprise APIs and MCP servers under impact-class controls with full audit.                         | L7 |
| C8   | Enforce Safety & Guardrails    | Input, prompt, tool-arg, and output guardrails; injection detection; PII and content controls.              | L8 |
| C9   | Verify Outputs                 | Grounding, citation, factuality, format, policy, business-rule, and confidence verification.                | L9 |
| C10  | Observe & Evaluate             | Traces, metrics, logs, agent/prompt/tool traces, cost telemetry, continuous evaluation, alerting.           | L10 |
| C11  | Optimise Performance & Cost    | Multi-tier caching, cost ledger, budget enforcement, response optimisation.                                 | L11 |
| C12  | Deliver Safely (LLMOps)        | CI, prompt tests, evaluations, canary / blue-green / shadow, rollback.                                      | L12 |
| C13  | Secure the System              | Zero-trust identity, least-privilege authorisation, secrets, encryption, PII controls, audit.               | L13 |
| C14  | Govern Risk & Compliance       | Model / prompt / tool registries, policy engine, standards mapping (NIST AI RMF, ISO 42001, EU AI Act).     | L14 |
| C15  | Deliver Business Value         | KPIs, value attribution, cost/benefit, adoption analytics.                                                  | L15 |

The identity mapping is deliberate: **each capability maps to exactly one layer**. A future capability that does not fit any layer either forces a layer-model change (via ADR) or is rejected as out-of-scope for EASRA.

## 4. Subcapabilities (normative)

Each capability domain expands into subcapabilities. These are the smallest atoms EASRA describes and reference.

### 4.1 C0 — Interact with Users
- **C0.1** Accept multi-channel input (web, mobile, chat, voice, API, SDK).
- **C0.2** Stream and finalise responses (SSE, WebSocket, batch).
- **C0.3** Capture explicit and implicit feedback.
- **C0.4** Manage session continuity across turns.
- **C0.5** Support accessible, localisable presentation.

### 4.2 C1 — Govern Ingress
- **C1.1** Authenticate principals (OIDC / SSO / API-key / workload identity).
- **C1.2** Authorise coarse-grained access at the edge.
- **C1.3** Enforce rate limits and quotas (per principal, per tenant, per capability).
- **C1.4** Externalise session state.
- **C1.5** Validate request structure and safety pre-conditions.
- **C1.6** Enforce token and cost budget per request.

### 4.3 C2 — Orchestrate Reasoning
- **C2.1** Route incoming requests to the appropriate reasoning path.
- **C2.2** Plan multi-step execution (planner / workflow engine).
- **C2.3** Execute single-agent tasks.
- **C2.4** Coordinate multi-agent workflows with turn control.
- **C2.5** Enforce reasoning termination (max steps, max cost, max time).

### 4.4 C3 — Engineer Prompts
- **C3.1** Build task-specific context from memory, retrieval, and inputs.
- **C3.2** Assemble prompts from versioned templates.
- **C3.3** Manage token budgets and truncation.
- **C3.4** Register, version, and roll back prompt templates.
- **C3.5** Test prompts against golden sets.

### 4.5 C4 — Manage Memory
- **C4.1** Working memory for a single reasoning step.
- **C4.2** Short-term memory across turns of a session.
- **C4.3** Session memory that survives disconnects.
- **C4.4** Long-term memory across sessions.
- **C4.5** Semantic memory (facts, concepts, embeddings).
- **C4.6** Episodic memory (event sequences).
- **C4.7** Profile memory (user- or tenant-scoped preferences).

### 4.6 C5 — Retrieve Knowledge
- **C5.1** Ingest, chunk, and embed source content.
- **C5.2** Retrieve via vector, keyword (BM25), structured (SQL), and graph.
- **C5.3** Rerank retrieved candidates.
- **C5.4** Enforce freshness and source-of-truth policies.
- **C5.5** Attach provenance and licences to retrieved chunks.

### 4.7 C6 — Serve Models
- **C6.1** Route across small, large, vision, speech, and embedding models.
- **C6.2** Apply capability, cost, latency, and policy filters.
- **C6.3** Fail over to fallback models under fault or budget breach.
- **C6.4** Version, sign, and audit model deployments (Model Registry).
- **C6.5** Enforce per-model quotas and rate limits.

### 4.8 C7 — Execute Tools & Actions
- **C7.1** Invoke tools via MCP or enterprise API adapters.
- **C7.2** Classify tools by impact (read / write / high-impact).
- **C7.3** Gate high-impact actions with human-in-the-loop.
- **C7.4** Version, sign, and audit tools (Tool Registry).
- **C7.5** Enforce per-tool quotas and rate limits.

### 4.9 C8 — Enforce Safety & Guardrails
- **C8.1** Input guardrails (before context building).
- **C8.2** Prompt guardrails (before model call).
- **C8.3** Tool-argument guardrails (before tool call).
- **C8.4** Output guardrails (before verification).
- **C8.5** Prompt-injection detection (direct and indirect).
- **C8.6** PII, secrets, and content-moderation checks.

### 4.10 C9 — Verify Outputs
- **C9.1** Grounding verification against retrieved sources.
- **C9.2** Citation resolution against the source registry.
- **C9.3** Factuality checks via graders and small verifiers.
- **C9.4** Format and schema validation.
- **C9.5** Policy verification (data-classification, jurisdictional, consent).
- **C9.6** Business-rule validation.
- **C9.7** Confidence scoring and escalation.

### 4.11 C10 — Observe & Evaluate
- **C10.1** Distributed traces (W3C TraceContext) across every layer.
- **C10.2** Metrics per layer (latency, throughput, error, saturation, cost).
- **C10.3** Structured, correlated logs.
- **C10.4** Agent, prompt, and tool traces.
- **C10.5** Cost telemetry per request, per model, per tool.
- **C10.6** Continuous evaluation on production traces.
- **C10.7** Alerting on SLOs, safety incidents, cost anomalies.

### 4.12 C11 — Optimise Performance & Cost
- **C11.1** Prompt cache.
- **C11.2** Semantic cache.
- **C11.3** Embedding cache.
- **C11.4** Memory cache.
- **C11.5** Response cache.
- **C11.6** Cost ledger and budget enforcement.

### 4.13 C12 — Deliver Safely (LLMOps)
- **C12.1** Source-controlled prompts, policies, evaluators.
- **C12.2** CI with lint, security scan, prompt tests, evaluation gate.
- **C12.3** Artefact registry (containers, prompts, models, policies).
- **C12.4** Canary, blue-green, shadow, and traffic-shifted rollouts.
- **C12.5** Automated rollback on eval regression.

### 4.14 C13 — Secure the System
- **C13.1** Zero-trust identity for every hop.
- **C13.2** Least-privilege authorisation.
- **C13.3** Secrets management and rotation.
- **C13.4** Encryption in transit and at rest.
- **C13.5** PII detection, minimisation, and residency.
- **C13.6** Audit for every high-impact event.

### 4.15 C14 — Govern Risk & Compliance
- **C14.1** Model, prompt, and tool registries as governance artefacts.
- **C14.2** Policy engine driven by capability and data classification.
- **C14.3** Standards mapping (NIST AI RMF, ISO/IEC 42001, EU AI Act, OWASP LLM Top 10, MITRE ATLAS).
- **C14.4** Data lineage and consent tracking.
- **C14.5** Impact assessments and change control.

### 4.16 C15 — Deliver Business Value
- **C15.1** Define KPIs per use case.
- **C15.2** Attribute value to model, prompt, tool, or workflow.
- **C15.3** Track cost-to-serve and cost-to-value.
- **C15.4** Measure adoption and retention.
- **C15.5** Feed learnings back to prompt, model, and workflow evolution.

## 5. Capability maturity model

Every subcapability is assessed independently on a five-level scale. Maturity is orthogonal to presence: a capability may be *present* but at *low maturity*.

| Level | Name | Description |
|-------|------|-------------|
| M0 | Absent | Not implemented; no substitute in place. |
| M1 | Ad hoc | Implemented per team; no shared abstraction; not observable. |
| M2 | Defined | Shared abstraction; tested in one environment; partially observable. |
| M3 | Managed | Standard interface; tested and observed in production; on-call ownership. |
| M4 | Optimised | SLOs, budget enforcement, continuous evaluation, and automated response. |

EASRA v1.0 targets **M3 or higher for every capability** in the reference implementation. Adopters may publish a **Capability Maturity Statement** (planned artefact) declaring their per-capability maturity.

## 6. Capability → other-artefact mapping

| Capability artefact | Mapped by | Location |
|---------------------|-----------|----------|
| Layer definition    | 1-to-1    | [005 §L*](./005-layer-definitions.md) |
| Components          | many-to-many | [012 Component Catalogue](./012-component-catalogue.md) |
| Interfaces          | many-to-many | [006 Interface Specification](./006-interface-specification.md) |
| Data flows          | many-to-many | [007 Data Flow](./007-data-flow.md) |
| Sequences           | many-to-many | [008 Sequence Diagrams](./008-sequence-diagrams.md) |
| Diagrams            | many-to-many | [Diagram Catalogue](../diagrams/CATALOGUE.md) |
| Handbook chapters   | 1-to-1    | [handbook/L*.md](../handbook/) |

## 7. Freezing rule

The set of **capability domains** and their **scope statements** in this document is frozen for v0.1.0. Adding, removing, renaming, or re-scoping a domain requires:

1. An ADR under [`adr/`](../adr/README.md) with a 14-day comment period.
2. An accompanying update to [012 Component Catalogue](./012-component-catalogue.md).
3. An entry in [`../CHANGELOG.md`](../CHANGELOG.md).

Sub-capabilities may be added or refined without an ADR if they do not change a domain's scope; changes are still tracked in the changelog.

## 8. Conformance

A system claims conformance to EASRA at capability level by:

- Publishing a Capability Maturity Statement covering all 16 domains.
- Declaring M ≥ 2 for every subcapability it implements, and M0 (with justification) for those it does not.
- Making the Statement machine-readable (schema published under [`reference-implementation/schemas/`](../reference-implementation/) — planned).

## 9. Related

- [001 Introduction](./001-introduction.md)
- [004 Reference Architecture](./004-reference-architecture.md)
- [005 Layer Definitions](./005-layer-definitions.md)
- [012 Component Catalogue](./012-component-catalogue.md)
- [Architectures README](../architectures/README.md)
- [Diagram Catalogue](../diagrams/CATALOGUE.md)
