# Specification 012 — Component Catalogue

| Field | Value |
|-------|-------|
| Status | Draft |
| Version | 0.1.0 |
| Last updated | 2026-07-05 |
| Depends on | 004, 005, 006, 011 |
| Required by | all diagrams |

## 1. Purpose

The **Component Catalogue** is the frozen inventory of every named component in EASRA. It exists to eliminate two failure modes seen in prior reference architectures:

1. **Component drift** — diagrams and prose reference components that were never defined.
2. **Boundary erosion** — components migrate between layers without ceremony because there is no authoritative list.

Every diagram in [`../diagrams/`](../diagrams/) may reference **only** components that appear here. Every component here maps to exactly one layer and satisfies at least one subcapability in [011 Capability Model](./011-capability-model.md).

## 2. Component ID scheme

`K-<layer>-<short>` where:

- `layer` = `L0`..`L15` or `X` for cross-cutting substrate components.
- `short` = a stable, 2–5-character identifier.

Example: `K-L1-GW` = Layer 1, Gateway.

## 3. Status legend

| Status | Meaning |
|--------|---------|
| **Defined** | Responsibility, layer, capability listed here. |
| **Interfaced** | Additionally has a normative interface in [006 Interface Specification](./006-interface-specification.md). |
| **Referenced** | External to EASRA (e.g., a cloud primitive) but named for completeness. |
| **Planned** | Reserved name; definition due in a subsequent revision. |

## 4. Catalogue — by layer

### 4.1 L0 · Channels & UX

| ID | Name | Responsibility | Capability | Status |
|----|------|----------------|------------|--------|
| K-L0-CHAD | Channel Adapter | Terminate protocol (HTTP / WS / SSE / gRPC); normalise to `ClientRequest`. | C0.1 | Interfaced |
| K-L0-STRM | Streaming Client Engine | Consume server-sent chunks; render progressively. | C0.2 | Defined |
| K-L0-FBK | Feedback Collector | Capture thumbs / free-text / implicit feedback signals. | C0.3 | Defined |
| K-L0-ACC | Accessibility & Localisation | ARIA, RTL, locale, format. | C0.5 | Defined |

### 4.2 L1 · Edge Gateway & Identity

| ID | Name | Responsibility | Capability | Status |
|----|------|----------------|------------|--------|
| K-L1-CDN | CDN | Cache static assets; DDoS absorption. | C1.3 | Referenced |
| K-L1-WAF | Web Application Firewall | L7 threat filtering. | C13.1 | Referenced |
| K-L1-GLB | Global Load Balancer | Region-aware routing; health-based failover. | C1.3 | Referenced |
| K-L1-GW  | API Gateway | HTTPS termination; entry point of the policy pipeline. | C1.1 | Interfaced |
| K-L1-AUTH | Authenticator | OIDC / SSO / API-key / workload-identity verification. | C1.1 | Interfaced |
| K-L1-AZ  | Coarse Authorizer | Capability + tenant + scope checks at the edge. | C1.2 | Interfaced |
| K-L1-RL  | Rate Limiter | Per-principal / per-tenant / per-capability limits. | C1.3 | Interfaced |
| K-L1-QM  | Quota Manager | Long-horizon usage caps. | C1.3 | Defined |
| K-L1-SM  | Session Manager | Front-end to externalised session state. | C1.4 | Interfaced |
| K-L1-RV  | Request Validator | Schema and safety pre-condition validation. | C1.5 | Interfaced |
| K-L1-TBM | Token Budget Manager | Compute and enforce per-request token / cost budget. | C1.6 | Defined |

### 4.3 L2 · AI Orchestration

| ID | Name | Responsibility | Capability | Status |
|----|------|----------------|------------|--------|
| K-L2-ROUTER | AI Router | Route request to single-agent, multi-agent, or workflow path. | C2.1 | Interfaced |
| K-L2-SA | Single-Agent Runtime | Execute a stateless single-agent turn. | C2.3 | Interfaced |
| K-L2-MA | Multi-Agent Coordinator | Sequence and mediate multi-agent conversations. | C2.4 | Interfaced |
| K-L2-PLAN | Planner | Decompose task into steps. | C2.2 | Defined |
| K-L2-WF | Workflow Engine | Durable, resumable long-running workflows. | C2.2 | Planned |
| K-L2-TERM | Termination Controller | Enforce max-steps / max-cost / max-time. | C2.5 | Defined |

### 4.4 L3 · Prompt Intelligence

| ID | Name | Responsibility | Capability | Status |
|----|------|----------------|------------|--------|
| K-L3-CB | Context Builder | Assemble context from memory + retrieval + inputs. | C3.1 | Interfaced |
| K-L3-PB | Prompt Builder | Fill versioned template into a `PromptManifest`. | C3.2 | Interfaced |
| K-L3-PR | Prompt Registry | Version, sign, roll back templates. | C3.4 | Interfaced |
| K-L3-BUD | Prompt Budget Controller | Enforce token budget on the built prompt. | C3.3 | Defined |
| K-L3-TEST | Prompt Test Harness | Execute prompt tests against golden sets. | C3.5 | Defined |

### 4.5 L4 · Memory & Context

| ID | Name | Responsibility | Capability | Status |
|----|------|----------------|------------|--------|
| K-L4-MM | Memory Manager | Facade over all memory stores; policy and TTL enforcement. | C4.* | Interfaced |
| K-L4-WM | Working Memory | Scratchpad for a single reasoning step. | C4.1 | Defined |
| K-L4-ST | Short-Term Memory | Recent turns of a session. | C4.2 | Defined |
| K-L4-SS | Session Memory | Persistent session store (survives disconnect). | C4.3 | Defined |
| K-L4-LT | Long-Term Memory | Cross-session memory. | C4.4 | Defined |
| K-L4-SEM | Semantic Memory | Facts, concepts, embedded snippets. | C4.5 | Defined |
| K-L4-EP | Episodic Memory | Time-ordered event sequences. | C4.6 | Defined |
| K-L4-UP | User / Tenant Profile | Preferences, entitlements, personalisation. | C4.7 | Defined |

### 4.6 L5 · Knowledge & Retrieval

| ID | Name | Responsibility | Capability | Status |
|----|------|----------------|------------|--------|
| K-L5-RR | Retrieval Router | Fan-out to retrieval backends; merge. | C5.2 | Interfaced |
| K-L5-VDB | Vector DB | kNN retrieval over embeddings. | C5.2 | Defined |
| K-L5-BM25 | Keyword Index | BM25 lexical retrieval. | C5.2 | Defined |
| K-L5-SQL | Structured Store | SQL / semantic-layer retrieval. | C5.2 | Defined |
| K-L5-GR | Knowledge Graph | Graph-traversal retrieval. | C5.2 | Defined |
| K-L5-RRK | Reranker | Cross-encoder / LLM-based reranking. | C5.3 | Defined |
| K-L5-ING | Ingestion Pipeline | Chunk, embed, index sources. | C5.1 | Defined |
| K-L5-SRC | Source Registry | Provenance, licences, freshness policy. | C5.4, C5.5 | Defined |

### 4.7 L6 · Models & Model Router

| ID | Name | Responsibility | Capability | Status |
|----|------|----------------|------------|--------|
| K-L6-MR | Model Router | Route across capabilities, cost, latency, policy. | C6.1, C6.2 | Interfaced |
| K-L6-FM | Foundation Models | Large general-purpose models. | C6.1 | Defined |
| K-L6-SM | Small / Specialist Models | Classifiers, extractors, rerankers, embedders. | C6.1 | Defined |
| K-L6-VM | Vision Models | Image / video understanding. | C6.1 | Defined |
| K-L6-SPM | Speech Models | ASR / TTS. | C6.1 | Defined |
| K-L6-EM | Embedding Models | Text / multimodal embeddings. | C6.1 | Defined |
| K-L6-FB | Fallback Router | Redirect on primary failure / policy breach. | C6.3 | Defined |
| K-L6-MRG | Model Registry | Version, sign, gate models. | C6.4 | Interfaced |

### 4.8 L7 · Tooling & Actions

| ID | Name | Responsibility | Capability | Status |
|----|------|----------------|------------|--------|
| K-L7-TR | Tool Router | Select tool adapter for a `ToolInvocation`. | C7.1 | Interfaced |
| K-L7-MCP | MCP Bridge | Speak MCP to internal and external servers. | C7.1 | Interfaced |
| K-L7-ENT | Enterprise API Adapter | REST / GraphQL / SQL / SAP / Salesforce / Dynamics. | C7.1 | Defined |
| K-L7-IMP | Impact-Class Enforcer | Gate high-impact actions with HITL. | C7.2, C7.3 | Interfaced |
| K-L7-TREG | Tool Registry | Version, sign, gate tools. | C7.4 | Interfaced |

### 4.9 L8 · Guardrails & Safety

| ID | Name | Responsibility | Capability | Status |
|----|------|----------------|------------|--------|
| K-L8-IG | Input Guardrails | Pre-context content, PII, injection screening. | C8.1, C8.5, C8.6 | Interfaced |
| K-L8-PG | Prompt Guardrails | Pre-model structural and safety checks. | C8.2 | Interfaced |
| K-L8-AG | Tool-Argument Guardrails | Pre-tool argument validation and policy. | C8.3 | Interfaced |
| K-L8-OG | Output Guardrails | Post-model content and safety checks. | C8.4 | Interfaced |
| K-L8-IPI | Indirect Prompt-Injection Detector | Scan retrieved / tool-returned content. | C8.5 | Defined |

### 4.10 L9 · Verification

| ID | Name | Responsibility | Capability | Status |
|----|------|----------------|------------|--------|
| K-L9-VE | Verification Engine | Orchestrate all checkers; emit `Verdict`. | C9.* | Interfaced |
| K-L9-GRD | Grounding Checker | Claims ↔ retrieved chunks. | C9.1 | Defined |
| K-L9-CIT | Citation Checker | Citations ↔ Source Registry. | C9.2 | Defined |
| K-L9-FCT | Factuality Grader | Small verifier / grader-based factuality. | C9.3 | Defined |
| K-L9-FMT | Format Validator | Schema / JSON / policy format. | C9.4 | Defined |
| K-L9-POL | Policy Verifier | Data-class / jurisdictional / consent. | C9.5 | Defined |
| K-L9-BR | Business-Rule Verifier | Domain-specific invariants. | C9.6 | Defined |
| K-L9-CS | Confidence Scorer | Combine signals; produce action. | C9.7 | Defined |

### 4.11 L10 · Observability & Evaluation

| ID | Name | Responsibility | Capability | Status |
|----|------|----------------|------------|--------|
| K-L10-OTEL | OpenTelemetry Collector | Ingest traces / metrics / logs. | C10.1–3 | Interfaced |
| K-L10-AT | Agent Trace Emitter | Structured agent traces. | C10.4 | Defined |
| K-L10-PT | Prompt Trace Emitter | Prompt lineage per request. | C10.4 | Defined |
| K-L10-TT | Tool Trace Emitter | Tool invocation lineage. | C10.4 | Defined |
| K-L10-COST | Cost Emitter | Per-request cost record. | C10.5 | Interfaced |
| K-L10-EVAL | Continuous Evaluator | Scheduled and on-trace evaluations. | C10.6 | Defined |
| K-L10-ALRT | Alerting | SLO / safety / cost anomaly. | C10.7 | Defined |

### 4.12 L11 · Performance · Caching · Cost

| ID | Name | Responsibility | Capability | Status |
|----|------|----------------|------------|--------|
| K-L11-CM | Cache Manager | Coordinated invalidation and policy. | C11.* | Defined |
| K-L11-PC | Prompt Cache | Exact-match prompt cache. | C11.1 | Defined |
| K-L11-SC | Semantic Cache | Similarity-based response cache. | C11.2 | Defined |
| K-L11-EC | Embedding Cache | Embedded-text cache. | C11.3 | Defined |
| K-L11-MC | Memory Cache | Frequently accessed memory keys. | C11.4 | Defined |
| K-L11-RC | Response Cache | Full-response cache with policy fences. | C11.5 | Defined |
| K-L11-LG | Cost Ledger | Immutable per-request cost record. | C11.6 | Interfaced |

### 4.13 L12 · LLMOps & Delivery

| ID | Name | Responsibility | Capability | Status |
|----|------|----------------|------------|--------|
| K-L12-SCM | Source Control | Git-hosted artefacts (code / prompt / policy / eval). | C12.1 | Referenced |
| K-L12-CI | CI Pipeline | Lint, sec-scan, unit, prompt tests, evaluation. | C12.2 | Defined |
| K-L12-AR | Artefact Registry | Containers, prompts, models, policies. | C12.3 | Defined |
| K-L12-CD | CD Pipeline | Canary / blue-green / shadow / rollback. | C12.4, C12.5 | Defined |

### 4.14 L13 · Security & Zero Trust

| ID | Name | Responsibility | Capability | Status |
|----|------|----------------|------------|--------|
| K-L13-IAM | Identity Provider | OIDC / SSO / workload identity. | C13.1 | Referenced |
| K-L13-KV | Secrets Manager | Store, rotate, audit secrets. | C13.3 | Referenced |
| K-L13-ENC | Encryption Service | Envelope encryption; KMS / HSM. | C13.4 | Referenced |
| K-L13-PII | PII Detector | Detect, mask, redact PII. | C13.5 | Interfaced |
| K-L13-POL | Security Policy Engine | ABAC / RBAC / data-class enforcement. | C13.2 | Defined |
| K-L13-AUD | Audit Log | Append-only high-impact event log. | C13.6 | Defined |

### 4.15 L14 · Governance, Risk, Compliance

| ID | Name | Responsibility | Capability | Status |
|----|------|----------------|------------|--------|
| K-L14-GOV | Governance Policy Engine | Enforce enterprise / regulatory policy across layers. | C14.2 | Defined |
| K-L14-STD | Standards Mapper | NIST AI RMF / ISO 42001 / EU AI Act / OWASP / MITRE ATLAS. | C14.3 | Defined |
| K-L14-LIN | Lineage Tracker | Data lineage and consent tracking. | C14.4 | Defined |
| K-L14-IA | Impact Assessment Tool | Structured impact reviews and change control. | C14.5 | Defined |

### 4.16 L15 · Business Outcomes & Value

| ID | Name | Responsibility | Capability | Status |
|----|------|----------------|------------|--------|
| K-L15-KPI | KPI Registry | Named, versioned KPIs per use case. | C15.1 | Defined |
| K-L15-ATR | Value Attribution | Attribute value to prompt / model / tool / workflow. | C15.2 | Defined |
| K-L15-COST | Cost-to-Serve Model | Cost per interaction, per value unit. | C15.3 | Defined |
| K-L15-ADP | Adoption Analytics | Users, retention, satisfaction. | C15.4 | Defined |

### 4.17 Cross-cutting substrate

| ID | Name | Responsibility | Capability | Status |
|----|------|----------------|------------|--------|
| K-X-EBUS | Event Bus | Async substrate: Kafka / Event Grid / PubSub. | substrate | Planned |
| K-X-SCHED | Scheduler | Deferred and recurring work. | C12.1 | Defined |
| K-X-FF | Feature Flag Service | Runtime control of prompts / models / tools. | C12.4 | Defined |
| K-X-CFG | Configuration Service | Layered, signed, auditable config. | C13.3 | Defined |

## 5. Freezing rule

Additions, renames, or scope changes require an ADR (14-day comment period), a matching entry in [011 Capability Model](./011-capability-model.md), and a [`../CHANGELOG.md`](../CHANGELOG.md) note. Renames must publish a compatibility alias for one minor version.

## 6. Related

- [004 Reference Architecture](./004-reference-architecture.md)
- [005 Layer Definitions](./005-layer-definitions.md)
- [006 Interface Specification](./006-interface-specification.md)
- [011 Capability Model](./011-capability-model.md)
- [Diagram Catalogue](../diagrams/CATALOGUE.md)
