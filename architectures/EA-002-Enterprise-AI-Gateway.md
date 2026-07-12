# EA-002 · Enterprise AI Gateway

![EA-002 Enterprise AI Gateway](../diagrams/EA-002-Enterprise-AI-Gateway.png)

> **Version:** 0.1.0 (Sprint-02 kickoff)
> **Status:** First formal architecture. Refinements track in [../ROADMAP.md](../ROADMAP.md).
> **Companion to:** [EA-001 · Enterprise AI Systems Reference Architecture](EA-001-Enterprise-AI-Systems.md)
> **Source:** [SVG](../diagrams/EA-002-Enterprise-AI-Gateway.svg) · Draw.io (planned)

---

## Why the AI Gateway matters

The **AI Gateway is the API Gateway of Enterprise AI.** It is the single point where identity, safety, model routing, cost, and observability converge. Every AI call — from a copilot chat to a batch scoring job to an autonomous agent invoking a tool — flows through it.

Without a gateway, each application re-implements auth, redaction, quotas, routing, and telemetry. With a gateway, those concerns are enforced *in-path*, centrally versioned, and observable from a single vantage point.

EA-002 defines the reference design.

---

## Design Goals

1. **Single ingress for all AI traffic.** No app talks to a model, agent, or tool without traversing the gateway.
2. **Ordered, observable stages.** The request pipeline is explicit; every stage emits telemetry and is policy-gated.
3. **Vendor-neutral.** Stages describe *capabilities*, not products. OPA, Cedar, custom PDPs — all fit.
4. **Failure-aware.** Fallback chains, circuit breakers, and graceful degradation are first-class.
5. **Cost as a first-class metric.** Every request is token-accounted and cost-tagged to tenant/app/model/route.
6. **Verification-friendly.** Traces, cost, safety verdicts, and grounding signals are emitted on every hop.

---

## Architecture

The gateway is organized into **four zones** plus a **cross-cutting store layer**.

| Zone | Purpose |
|------|---------|
| **Callers** | Everything that consumes AI capabilities (apps, agents, batch jobs, notebooks, partners) |
| **Ingress edge** | Network-tier concerns: TLS, WAF, DDoS, correlation ID, canonicalization, multi-region failover |
| **Control path** | The gateway's request pipeline — 6 ordered stages plus response-side handling |
| **Egress** | Fan-out to Model, Agent/Orchestration, Knowledge, external APIs, and human review |
| **Cross-cutting stores** | Identity, Policy (PDP), Model Registry, Cost & Quota, Telemetry, Audit, Secrets |

### The 6-stage Control Path

```
1  AuthN / AuthZ           →  Who is calling, in which tenant, with which scope?
2  Quota & Rate Limit      →  Are they within their fairness / budget envelope?
3  Policy Enforcement      →  Does this request satisfy declarative rules?
4  Prompt Intelligence     →  Is the prompt safe, un-injected, PII-scrubbed?
5  Model Router            →  Which model handles it? Primary + fallback chain.
6  Cache & Dispatch        →  Serve from cache if possible; else stream to model.
```

Response path (after model returns) adds:
- **Output guardrails** — safety scan (toxicity, PII leakage, hallucination heuristics)
- **Grounding & citation** — attach citations for RAG responses
- **Cost attribution** — token accounting, cost tagging per tenant/app/model/route
- **Trace emit** — prompt, retrieval, tool, model, and cache spans emitted (OTel)
- **Feedback capture** — hook for explicit rating and implicit signals
- **Audit write** — immutable append to the audit log

---

## Stage Details

### 1. AuthN / AuthZ
- **Identity:** OIDC (users), SPIFFE/SPIRE (workloads), mTLS (partners), API keys (legacy)
- **Tenant isolation:** every request has a resolved `tenant_id`; no cross-tenant data or cache leakage
- **AuthZ model:** RBAC for coarse scopes (`chat.invoke`, `tool.execute`, `finetune.train`), ABAC for context (region, sensitivity)
- **Key management:** rotation, revocation, per-scope short-lived tokens

### 2. Quota & Rate Limit
- **Dimensions:** RPM (requests/min), TPM (tokens/min), USD/day, concurrent streams
- **Scopes:** tenant · app · user · model · route
- **Budget-awareness:** throttling *tightens* as monthly budget consumption approaches 100%
- **Priority queues:** guarantee latency SLOs for premium tenants

### 3. Policy Enforcement (PEP → PDP)
- **PEP** lives in the gateway; **PDP** is an external policy store (OPA, Cedar, custom)
- **Common policies:**
  - Data residency (`EU tenants → EU-region models only`)
  - Model allow-lists (`legal team → only reasoning models ≥ v3`)
  - Tool allow-lists (`external agents → cannot invoke `payments.transfer``)
  - Compliance gates (HIPAA/GDPR/EU AI Act tags flow with the request)
- **Versioned & auditable.** Every policy decision is logged with the policy version.

### 4. Prompt Intelligence
- **PII / secret redaction** before the prompt leaves the gateway (regex + classifier)
- **Injection defense** — detect direct + indirect prompt injection patterns
- **Jailbreak detection** — signature + LLM-as-classifier
- **Content classification** — topic, sensitivity, sentiment (used to route or block)

### 5. Model Router
- **Selection strategies:** cheapest-that-passes-quality-bar, latency-optimized, capability-required
- **Fallback chain:** primary → secondary → cached/degraded response
- **Region / residency routing** driven by tenant metadata
- **Version pinning + canary / A-B split** for controlled rollout
- **Router itself is stateless** and reads from the Model Registry

### 6. Cache & Dispatch
- **Exact prompt cache** for deterministic prompts (system + user hash → response)
- **Semantic cache** for near-duplicates (embedding similarity ≥ threshold)
- **Streaming multiplexer** so multiple identical concurrent requests share a single upstream stream
- **Retry / backoff** with jitter; circuit breaker on repeated 5xx / 429

---

## Cross-Cutting Stores

| Store | Purpose | Typical implementation |
|-------|---------|------------------------|
| **Identity Provider** | User + workload identity | Entra ID, Okta, Auth0 · SPIFFE/SPIRE |
| **Policy Store (PDP)** | Versioned declarative policies | OPA (Rego), AWS Cedar, custom |
| **Model Registry** | Model versions, SLAs, cost, capability tags | MLflow, custom, cloud-native registry |
| **Cost & Quota Store** | Budgets, counters, chargeback data | Redis/DynamoDB + warehouse |
| **Telemetry Pipeline** | Traces, metrics, logs | OpenTelemetry → any backend |
| **Audit Log** | Immutable, WORM, tamper-evident | Append-only object store, ledger DB |
| **Secrets Vault** | Model keys, tenant secrets | Key Vault, KMS, HSM |

---

## Interface Contract (v0.1)

The gateway exposes **one canonical AI-invocation surface**:

```
POST /v1/invoke
Headers:
  Authorization: Bearer <token>
  X-Tenant-Id: <tenant>
  X-Correlation-Id: <trace-id>       (optional, generated if absent)
  X-Route-Hint: <model-family|null>  (optional; router may override)
Body:
  {
    "task": "chat|embed|rerank|tool_call",
    "input": { ... },
    "policy_tags": ["hipaa", "eu-only"],   // optional
    "budget_ceiling_usd": 0.05             // optional per-request cap
  }
Response:
  {
    "output": { ... },
    "route": { "model": "gpt-5-mini", "version": "2026-05-01", "region": "eu-west" },
    "cost": { "tokens_in": 812, "tokens_out": 214, "usd": 0.0031 },
    "safety": { "input": "pass", "output": "pass", "citations_present": true },
    "trace_id": "…"
  }
```

Full OpenAPI spec ships in a follow-up sprint under [`../specification/`](../specification/).

---

## Observability Contract

Every request emits at minimum:

- **Spans:** `gateway.auth`, `gateway.quota`, `gateway.policy`, `gateway.prompt_intel`, `gateway.router`, `gateway.cache`, `gateway.model_call`, `gateway.output_guard`
- **Metrics:** `requests_total{tenant,app,model,route,status}`, `latency_ms_bucket{...}`, `tokens_total{direction,tenant,model}`, `usd_total{tenant,model}`
- **Events:** policy decisions (with policy version), safety verdicts, cache hits/misses, fallback triggers
- **Feedback hook:** `/v1/feedback` correlated by `trace_id`

Follows the OpenTelemetry semantic conventions for `gen_ai.*` where available.

---

## Failure Modes & Degradation

| Failure | Behavior |
|---------|----------|
| Primary model 5xx | Router falls back through chain; final fallback returns cached / templated response with `degraded: true` |
| Policy store unreachable | Fail-**closed** for high-sensitivity tenants; fail-**open** to last cached policy for low-sensitivity (configurable) |
| Quota exhausted | Return `429` with `Retry-After` and `budget_status` payload |
| Prompt intelligence classifier down | Fail-**closed** on injection defense; fail-**open** on classification metadata |
| Downstream network partition | Circuit-break; serve cached responses; emit high-severity alert |

---

## Related Patterns

Once the pattern catalog is populated, EA-002 will link to:

- **PAT-001 · AI Gateway** — the productized pattern derived from this architecture
- **PAT-003 · Verification** — how the gateway participates in the verification loop
- **PAT-004 · Prompt Intelligence** — deep-dive on stage 4

See [../patterns/README.md](../patterns/README.md).

---

## Reference Implementations (planned)

| Target | Location | Status |
|--------|----------|--------|
| Azure (APIM + Functions + Front Door + APIM AI Gateway policies) | `../implementations/azure/ai-gateway/` | ⏳ |
| AWS (API Gateway + Lambda + WAF + Bedrock Guardrails) | `../implementations/aws/ai-gateway/` | ⏳ |
| Kubernetes (Envoy + OPA + Redis + OTel Collector) | `../implementations/kubernetes/ai-gateway/` | ⏳ |

---

## Related Architectures

| ID | Title | Status |
|----|-------|--------|
| EA-001 | Enterprise AI Systems Reference Architecture | ✅ v0.0.1 |
| EA-002 | Enterprise AI Gateway | ✅ **v0.1.0 (this page)** |
| EA-003 | Runtime Plane | ⏳ Planned |
| EA-004 | Control Plane | ⏳ Planned |
| EA-005 | Knowledge Plane | ⏳ Planned |
| EA-006 | Verification Plane | ⏳ Planned |
| EA-007 | Guardrails Plane | ⏳ Planned |
| EA-008 | Observability Plane | ⏳ Planned |

---

## Changelog

- **2026-07-12** — v0.1.0 · First formal EA-002 published (SVG + PNG + spec). Companion to EA-001. Sprint-02 kickoff.
