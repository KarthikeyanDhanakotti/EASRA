# Specification 004 — Reference Architecture

| Field | Value |
|-------|-------|
| Specification | EASRA-SPEC-004 |
| Title | Reference Architecture |
| Version | 0.1.0 (Draft) |
| Status | Draft |
| Depends on | 001, 002, 003 |

---

## 1. Purpose

This specification defines the EASRA logical reference architecture: the sixteen layers, their ordering along the request path, the cross-cutting planes, and the extension points. Detailed layer responsibilities live in [Specification 005 — Layer Definitions](./005-layer-definitions.md); interface contracts live in [Specification 006 — Interface Specification](./006-interface-specification.md).

The reference architecture is **logical**. It says nothing about programming languages, deployment targets, or vendor products.

## 2. Layer Model

EASRA is a 16-layer architecture organised along the request path with three cross-cutting planes.

```
                                    REQUEST PATH  ─────────────────►
┌────────────────────────────────────────────────────────────────────────────┐
│  L0   Channels & User Experience                                           │
│  L1   Edge · Gateway · Identity                     Trust Boundary A       │
│  L2   AI Orchestration                                                     │
│  L3   Prompt Intelligence                                                  │
│  L4   Memory & Context                                                     │
│  L5   Knowledge & Retrieval                                                │
│  L6   AI Models & Model Router                     Trust Boundary C        │
│  L7   Tooling & Actions (MCP)                      Trust Boundary D        │
│  L8   Guardrails & Safety                          Trust Boundary B        │
│  L9   Verification                                                         │
│  L10  Observability & Evaluation                                           │
│  L11  Performance · Caching · Cost                                         │
│  L12  LLMOps & Delivery                                                    │
└────────────────────────────────────────────────────────────────────────────┘
    ┌──────────────────────────────────────────────────────────────────┐
    │  L13  Security & Zero Trust           (cross-cutting)            │
    │  L14  Governance · Risk · Compliance  (cross-cutting)            │
    │  L15  Business Outcomes & Value       (cross-cutting)            │
    └──────────────────────────────────────────────────────────────────┘
```

Layers L0–L12 sit on the request path in a defined order. Layers L13–L15 are cross-cutting: they attach to every layer at defined injection points. Trust boundaries are named in Spec 009.

## 3. Layer Summary

| # | Layer | One-line responsibility |
|---|-------|-------------------------|
| L0 | Channels & User Experience | Accept requests from user-facing surfaces; render responses. |
| L1 | Edge · Gateway · Identity | Terminate at the edge; authenticate, authorise, rate-limit, bot-protect; establish session. |
| L2 | AI Orchestration | Route the request to a single agent, a multi-agent coordinator, or a deterministic workflow. |
| L3 | Prompt Intelligence | Build context and assemble the prompt with grounded, safe, cost-aware inputs. |
| L4 | Memory & Context | Provide short-term, long-term, session, semantic memory, and user profile. |
| L5 | Knowledge & Retrieval | Retrieve grounding evidence from vector, keyword, structured, and graph indexes. |
| L6 | AI Models & Model Router | Select and invoke the model that best fits capability, cost, latency, availability, policy. |
| L7 | Tooling & Actions (MCP) | Expose tools to agents via MCP; enforce impact-class policy; execute actions. |
| L8 | Guardrails & Safety | Inspect and block unsafe inputs, prompts, tool arguments, and outputs. |
| L9 | Verification | Verify the candidate response against grounding, citation, factuality, format, policy, safety. |
| L10 | Observability & Evaluation | Emit traces, metrics, logs, token/cost, agent/tool traces; run continuous evaluation. |
| L11 | Performance · Caching · Cost | Prompt, semantic, embedding, memory, and response caches; cost accounting. |
| L12 | LLMOps & Delivery | CI/CD, prompt/model rollout, canary, blue/green, artefact registry. |
| L13 | Security & Zero Trust | Identity, secrets, encryption, PII, policy, audit — attaches to every layer. |
| L14 | Governance · Risk · Compliance | Policy engine, model registry, audit, compliance mapping. |
| L15 | Business Outcomes & Value | KPIs, value attribution, cost/benefit, product analytics. |

Full definitions are in [Specification 005](./005-layer-definitions.md).

## 4. High-Level Architecture (Canonical Diagram)

The canonical high-level diagram is maintained in [`diagrams/high-level-architecture.md`](../diagrams/high-level-architecture.md). A textual walkthrough is given here for the specification record.

**Request path — synchronous chat/agent request:**

1. **L0 Channel** receives the request from a user surface (web, mobile, API, chat).
2. **L1 Gateway** terminates TLS at the edge, applies WAF/bot protection, authenticates the caller, applies rate limits, establishes or resumes the session.
3. **L1 Session Manager** loads session state; **L1 Request Validator** enforces the request schema.
4. **L2 Orchestrator** decides between Single Agent, Multi-Agent Coordinator, or a deterministic workflow. In agentic modes, the **Planner / Workflow Engine** produces a plan.
5. **L3 Context Builder** gathers inputs from **L4 Memory Manager** and **L5 Knowledge Retrieval**.
6. **L11 Cache Manager** is consulted at each cache tier (prompt, semantic, embedding, memory, response) before expensive work.
7. **L3 Prompt Builder** assembles the prompt.
8. **L8 Input Guardrails** inspect user input and the assembled prompt.
9. **L6 Model Router** selects a model based on capability, cost, latency, availability, policy. The model produces a candidate response, possibly with tool calls.
10. If tool calls are present, **L7 Tool Router** resolves each call; **L8 Tool-Argument Guardrails** inspect arguments; the tool is executed (via MCP client → MCP server or enterprise API); the result returns.
11. Steps 7–10 repeat until the agent terminates.
12. **L8 Output Guardrails** inspect the candidate response.
13. **L9 Verification Engine** checks grounding, citation, factuality, format, policy, safety.
14. **L9 Response Formatter / Streaming Engine** produces the response to the client contract.
15. **L1** returns the response to **L0**.
16. **L10 Observability** has been emitting signals throughout: OpenTelemetry traces, metrics, logs, plus token usage, latency, cost, agent trace, prompt trace, tool trace, evaluation, alerts.

## 5. Cross-Cutting Planes

Three planes span every layer.

### 5.1 Security plane (L13)

`Zero Trust → Authentication → Authorisation → Secrets → Encryption → PII Detection → Policy Engine → Audit → Compliance`

Security is not a filter at the edge; it is a plane. Every layer has:

- An identity in scope (who is acting).
- An authorised action set (what may be done).
- A secret-access boundary (what credentials may be used).
- A PII classification for its inputs and outputs.
- A policy evaluation point.
- An audit emission.

### 5.2 Observability plane (L10)

Every layer emits, at minimum:

- OpenTelemetry trace spans with layer-specific attributes.
- Latency and error metrics.
- Structured logs with request/session/tenant correlation.
- AI-specific signals: token usage, cost, prompt trace, agent trace, tool trace, evaluation score, verification verdict.

Alerts are declarative and layer-owned.

### 5.3 Governance plane (L14)

Every layer participates in governance:

- Model registry (L6): what models are approved, for what data classes, under what policy.
- Prompt registry (L3): what prompts are approved, versioned.
- Tool registry (L7): what tools exist, their impact class, their approval policy.
- Policy engine (L14): allow/deny/require-approval verdicts on any action.
- Audit log: tamper-evident, retained per compliance requirements.

## 6. Extension Points

The architecture reserves the following extension points. Each is a *named seam* where new capabilities plug in without changing surrounding layers.

| Extension Point | Layer | Purpose |
|-----------------|-------|---------|
| Channel adapter | L0 | Add a new user surface (voice, embedded, IoT). |
| Auth provider | L1 | Add a new identity provider. |
| Rate-limit policy | L1 | Add per-tenant or per-agent limits. |
| Agent | L2 | Register a new agent with the coordinator. |
| Workflow | L2 | Register a new deterministic workflow. |
| Prompt template | L3 | Register a new template with the prompt registry. |
| Memory store | L4 | Add a new memory backend. |
| Retrieval index | L5 | Add a new retrieval backend. |
| Model provider | L6 | Register a new model with the router. |
| Routing policy | L6 | Add a new routing decision (cost-aware, latency-aware, capability-aware). |
| Tool | L7 | Register a new tool via MCP. |
| Guardrail | L8 | Add a new guardrail check. |
| Verifier | L9 | Add a new verification check. |
| Cache tier | L11 | Add a new cache. |
| Deployment strategy | L12 | Add canary, blue/green, feature-flag, shadow. |
| Policy | L14 | Add a new policy rule to the policy engine. |
| KPI | L15 | Add a new business KPI to value attribution. |

## 7. Reserved Extension Points (future specifications)

The following are named seams that will receive their own specification when they graduate from research (see [ROADMAP.md](../ROADMAP.md)):

- Multi-region deployment
- Disaster recovery
- Multi-model routing
- Cost-aware routing
- AI policy engine
- Agent marketplace
- Agent registry (federated)
- Skill registry (federated)
- Feature store
- Vector synchronisation
- Event bus
- Async workflows

These extension points are *reserved* — the current architecture does not close the door on them. Implementations may add them as internal capabilities and align with the eventual specification when it lands.

## 8. Deployment Topology (Logical)

The reference architecture assumes a logical topology of:

- **Edge tier** — CDN, WAF, global load balancer, API Gateway. (L1)
- **Compute tier** — Stateless containers for orchestration, prompt intelligence, model clients, tool clients, guardrails, verification. Autoscaled. (L2, L3, L6, L7, L8, L9)
- **Data plane** — Session store, memory stores (short/long/semantic/profile), cache plane, vector DB, feature store, event bus. (L4, L5, L11)
- **Model tier** — Model provider APIs and/or self-hosted inference (GPU/CPU/NPU). (L6)
- **Observability tier** — OTel collector, metric store, log store, evaluation store. (L10)
- **Delivery tier** — CI/CD pipeline, artefact registry, model registry, prompt registry. (L12)
- **Governance tier** — Policy engine, audit log, compliance dashboards. (L14)

See [`diagrams/deployment-topology.md`](../diagrams/deployment-topology.md) for the topology diagram.

## 9. Request Modes

EASRA recognises four canonical request modes; each is a sequence in [Specification 008](./008-sequence-diagrams.md):

| Mode | Sync/Async | Streaming | Tool Use | Multi-Agent |
|------|------------|-----------|----------|-------------|
| M1 Simple Chat | Sync | Optional | No | No |
| M2 RAG Query | Sync | Optional | No | No |
| M3 Single-Agent Tool Use | Sync | Optional | Yes | No |
| M4 Multi-Agent | Sync or Async | Optional | Yes | Yes |

Additional modes (batch, async workflow, event-driven) are reserved for future specifications.

## 10. Non-Functional Requirements

Non-functional requirements attach to layers, not to the system as a whole. See [Specification 010](./010-nfr.md) for latency, throughput, availability, safety, cost, and compliance targets by layer.

## 11. Change Log

- **0.1.0 (2026-07-05)** — Initial draft of the 16-layer reference architecture.

## 12. Next Specification

Continue to [Specification 005 — Layer Definitions](./005-layer-definitions.md).
