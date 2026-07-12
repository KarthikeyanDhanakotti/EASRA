# PAT-001 · AI Gateway

> **Layer:** L2 Gateway
> **Status:** Draft — full v1 lands with EA-002 refinement
> **See also:** [EA-002 · Enterprise AI Gateway](../architectures/EA-002-Enterprise-AI-Gateway.md) *(the architecture that this pattern productizes)*

## Context

An organization has multiple applications, teams, or agents making AI calls (chat, embed, tool-call, batch). Each is currently re-implementing authentication, rate limiting, redaction, model selection, and telemetry — inconsistently.

## Problem

- **Duplicated concerns** in every app → security, cost, and safety gaps
- **No single choke-point** for policy → hard to enforce data residency, model allow-lists, DLP
- **No unified cost visibility** → nobody can answer "how much are we spending on AI, per tenant?"
- **No single observability plane** → traces are fragmented, incidents take hours to diagnose

## Solution

Introduce **one policy-enforcing gateway** that every AI call — internal or external — must traverse. Enforce identity, quota, policy, prompt safety, and model routing centrally. Emit telemetry, cost, and audit from a single vantage point.

Full architectural detail: [EA-002 · Enterprise AI Gateway](../architectures/EA-002-Enterprise-AI-Gateway.md).

### Minimal viable design

```
Caller ──► Gateway ──► [Auth → Quota → Policy → Prompt-Intel → Router → Cache] ──► Model
                                                                                     │
                                                                                     ▼
                                                                             Telemetry + Audit
```

## Interfaces

- **Ingress:** single canonical `POST /v1/invoke` surface (see EA-002 for schema)
- **Egress:** provider-agnostic model / agent / tool clients
- **Sidecars:** Policy Store (PDP), Identity Provider, Model Registry, Cost Store, Telemetry pipeline

## Controls

| Control | Where |
|---------|-------|
| Identity + tenant isolation | Stage 1 (Auth) |
| Quota / budget throttling | Stage 2 (Quota) |
| Data residency / allow-lists | Stage 3 (Policy) |
| PII redaction · injection defense | Stage 4 (Prompt Intelligence) |
| Cost attribution | Stage 6 (Cache & Dispatch) + response path |
| Output guardrails | Response path |
| Immutable audit | Cross-cutting |

## KPIs

- **Coverage:** % of AI calls routed through the gateway *(target: 100%)*
- **p95 gateway latency** (excluding upstream model) *(target: < 50 ms)*
- **Blocked-request rate** by policy / safety *(track by tenant)*
- **Cache hit rate** — exact + semantic
- **Cost per unit outcome** — USD per successful task
- **Time-to-detect incident** — target < 5 min via gateway telemetry

## Trade-offs

- Adds one network hop → mitigated by co-location and streaming
- Central choke-point → must be highly available (multi-region, active-active)
- Introduces new team/ownership → the AI Platform team

## Variants

- **Edge-embedded** — gateway logic packaged as an SDK for latency-critical clients
- **Sidecar** — gateway deployed as a per-workload sidecar (service mesh style)
- **Egress-only** — gateway only enforces model egress (lightweight adoption path)

## Anti-patterns

- **App-side "SDK-only" enforcement** — apps that opt-in to safety can opt-out; policy must be *in-path*.
- **Multiple gateways per tenant** — fragments telemetry and cost visibility.
- **Gateway as passive proxy** — without policy/prompt intelligence, it's just an API gateway with extra hops.

## Reference implementations *(planned)*

- Azure (APIM + Functions) — [../implementations/azure/ai-gateway/](../implementations/azure/ai-gateway/)
- AWS (API Gateway + Lambda + WAF) — [../implementations/aws/ai-gateway/](../implementations/aws/ai-gateway/)
- Kubernetes (Envoy + OPA + Redis) — [../implementations/kubernetes/ai-gateway/](../implementations/kubernetes/ai-gateway/)
