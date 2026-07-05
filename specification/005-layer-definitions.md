# Specification 005 — Layer Definitions

| Field | Value |
|-------|-------|
| Specification | EASRA-SPEC-005 |
| Title | Layer Definitions |
| Version | 0.1.0 (Draft) |
| Status | Draft |
| Depends on | 001, 002, 003, 004 |

---

## 1. Purpose

This specification gives the full definition of every EASRA layer: its purpose, responsibilities, components, inputs, outputs, invariants, failure modes, observability signals, and security posture. It is the authoritative reference for what belongs — and what does not belong — in each layer.

Each layer entry follows the same template:

- **Purpose** — one-sentence responsibility.
- **In scope** — what this layer owns.
- **Out of scope** — what belongs to another layer.
- **Components** — the named internal components.
- **Inputs / Outputs** — the layer's inputs and outputs (interface contracts are in Spec 006).
- **Invariants** — properties the layer must uphold.
- **Failure modes** — the failure classes and defined degraded behaviour.
- **Observability signals** — the minimum signals emitted.
- **Security posture** — trust boundary participation and controls.

---

## L0 — Channels & User Experience

**Purpose.** Accept requests from user-facing surfaces and render responses.

**In scope.** Web, mobile, chat, voice, API, embedded surfaces; UI-side session token handling; response rendering including streaming; user-facing error presentation.

**Out of scope.** Authentication (L1), business logic (L2+), any AI decisioning.

**Components.** Channel Adapter (per surface), Response Renderer, Streaming Client.

**Inputs.** User intent, credentials or session token.

**Outputs.** Structured request to L1.

**Invariants.**
- No AI model is called directly from L0.
- Session tokens are opaque to the channel.
- Requests carry a channel identifier and correlation ID.

**Failure modes.**
- Backend unavailable → cached / degraded UI response.
- Streaming interrupted → resumable or cleanly terminated.

**Observability signals.**
- Channel type, correlation ID, client-side latency, error rate.

**Security posture.** Outside all trust boundaries. Never handles secrets. Never sees PII in structured form.

---

## L1 — Edge · Gateway · Identity

**Purpose.** Terminate at the edge, authenticate, authorise, rate-limit, bot-protect, and establish or resume the session. This is the enforcement point for Trust Boundary A (Untrusted → Trusted).

**In scope.** CDN, WAF, global load balancer, API Gateway, Authentication, Authorisation (coarse-grained), Rate Limiter, Bot Protection, Session Manager, Request Validator.

**Out of scope.** Fine-grained authorisation on tool calls (L7 + L14); prompt-injection detection (L8); business logic (L2+).

**Components.** CDN, WAF, Load Balancer, API Gateway, Authentication, Rate Limiter, Bot Protection, Session Manager, Request Validator.

**Inputs.** Requests from L0.

**Outputs.** Validated, authenticated, session-bearing request to L2. Session state persisted externally.

**Invariants.**
- Every request past L1 has a verified identity or a documented anonymous mode.
- Session state is externalised (P6).
- Requests failing validation are rejected before reaching L2.

**Failure modes.**
- Identity provider outage → cached tokens honoured within TTL; new sessions refused.
- Rate-limit exceeded → structured 429 with retry-after.
- Session store outage → session-less fallback for read-only channels; write channels refused.

**Observability signals.**
- Auth outcome, auth latency, rate-limit hit/miss, session load latency, request size, validation errors.

**Security posture.** Enforces Trust Boundary A. Attaches identity to every request. Interacts with L13 for identity, secrets, and audit.

---

## L2 — AI Orchestration

**Purpose.** Route the request to a Single Agent, Multi-Agent Coordinator, or deterministic Workflow; own the plan and control flow.

**In scope.** AI Router, Single Agent, Multi-Agent Coordinator, Planner, Workflow Engine, Task decomposition and merging.

**Out of scope.** Prompt building (L3), retrieval (L5), model selection (L6), tool execution (L7), guardrails (L8), verification (L9).

**Components.** AI Router, Single Agent runtime, Multi-Agent Coordinator, Planner, Workflow Engine, Agent Registry client, Skill Registry client.

**Inputs.** Validated request + session from L1.

**Outputs.** A plan (implicit or explicit) executed via L3–L7 with results converging to L8/L9.

**Invariants.**
- The plan is bounded — a maximum step count and a wall-clock timeout are always set.
- Every autonomous action goes through L7 (never bypasses tooling).
- Every response is passed through L8/L9 before formatting.

**Failure modes.**
- Plan exceeds bound → terminate with structured error; escalate per policy.
- Sub-agent failure → coordinator applies bulkhead policy; degraded response if permitted.
- Loop detection → break the loop; emit alert.

**Observability signals.**
- Agent trace (plan steps, decisions), turn count, wall-clock, per-step latency, per-step cost, sub-agent outcomes.

**Security posture.** Runs under the caller identity (P7). Cannot escalate privilege. Every tool call carries the caller's identity into L7.

---

## L3 — Prompt Intelligence

**Purpose.** Build the context and assemble the prompt: grounded, safe, cost-aware, and versioned.

**In scope.** Context Builder, Prompt Builder, System Prompt manager, Prompt Registry client, prompt-template versioning.

**Out of scope.** Content retrieval (L5), memory retrieval (L4), guardrail application (L8), model selection (L6).

**Components.** Context Builder, Prompt Builder, Prompt Registry client, Prompt Cache client (via L11).

**Inputs.** Request, session, memory (from L4), retrieval results (from L5), system instructions.

**Outputs.** An assembled prompt with a manifest: which template, which version, which inputs, which token budget.

**Invariants.**
- The prompt is deterministic given its inputs (for cache correctness).
- The prompt manifest is recorded for every request (prompt trace).
- Token budget is enforced before submission.

**Failure modes.**
- Token budget exceeded → truncate lowest-priority context; emit metric.
- Prompt template missing → fail closed; emit alert.

**Observability signals.**
- Prompt trace (template, version, inputs, token counts), cache hit/miss, truncation events.

**Security posture.** Never mixes user input with system instructions without labelled boundaries. Applies PII policy to context inputs.

---

## L4 — Memory & Context

**Purpose.** Provide short-term, long-term, session, semantic memory, and user profile — externalised, indexed, and access-controlled.

**In scope.** Memory Manager, short-term store, long-term store, session store, semantic memory store, user profile store.

**Out of scope.** Knowledge retrieval over documents (L5), cache (L11).

**Components.** Memory Manager, backing stores per memory type, memory access-control policy client.

**Inputs.** Memory queries from L3 / L2.

**Outputs.** Ranked memory records with recency, relevance, and access-control metadata.

**Invariants.**
- Compute is stateless (P6); memory is external.
- Every memory record has an owning identity.
- PII in memory is classified and access-controlled.

**Failure modes.**
- Memory store outage → degraded mode: session memory only.
- Semantic memory latency exceeded → skip semantic; use short-term only.

**Observability signals.**
- Memory type accessed, read/write counts, latency, PII classification hits.

**Security posture.** Enforces identity-bound access. Never returns records outside the caller's authorisation scope.

---

## L5 — Knowledge & Retrieval

**Purpose.** Retrieve grounding evidence from vector, keyword, structured, and graph indexes.

**In scope.** Retrieval Router, Vector DB client, Keyword index client (BM25), Structured index client (SQL), Graph index client, Reranker, Hybrid Search.

**Out of scope.** Embedding computation (L6, embedding model), memory (L4), tool APIs (L7).

**Components.** Retrieval Router, Index Adapters, Reranker, Chunk store, Source registry.

**Inputs.** Queries from L3.

**Outputs.** Ranked chunks with source, score, and provenance.

**Invariants.**
- Every chunk carries provenance (source ID, version, timestamp).
- No unlabelled content reaches L3.
- Retrieval respects the caller's authorisation scope over sources.

**Failure modes.**
- Vector DB outage → keyword-only fallback.
- Reranker outage → return unreranked with metric.

**Observability signals.**
- Query, retrieval strategy, index latencies, result counts, reranker latency, cache hit/miss.

**Security posture.** Source-level ACLs. Retrieval never returns content the caller may not read.

---

## L6 — AI Models & Model Router

**Purpose.** Select and invoke the model that best fits capability, cost, latency, availability, and policy.

**In scope.** Model Router, Model Provider adapters, Fallback model selection, Cost accounting per call, Model Registry client.

**Out of scope.** Prompt building (L3), guardrails (L8), verification (L9), tool execution (L7).

**Components.** Model Router, Provider adapters (chat, completion, embedding, rerank, classify, moderate), Fallback policy, Model Registry client.

**Inputs.** Prompt + routing hints from L3.

**Outputs.** Model response (possibly with tool calls), token usage, latency, cost, model identity.

**Invariants.**
- The model used is recorded per call.
- Token usage is recorded per call.
- Cost is recorded per call.
- Fallback is deterministic under stated conditions.

**Failure modes.**
- Primary model outage → fallback; emit metric.
- Rate limit → back off + route to alternate provider.
- Timeout → structured error; caller decides retry vs escalate.

**Observability signals.**
- Model ID, prompt/completion tokens, cost, latency, provider, fallback events.

**Security posture.** Enforces Trust Boundary C (Reasoning → Model). Never sends secrets in prompts. PII is classified at L3; L6 enforces routing policy on classified content.

---

## L7 — Tooling & Actions (MCP)

**Purpose.** Expose tools to agents via MCP; enforce impact-class policy; execute actions.

**In scope.** Tool Router, MCP Client, MCP Server(s), Tool Registry, Impact-Class policy, Enterprise API adapters.

**Out of scope.** Model calls (L6), retrieval (L5), memory (L4), guardrails (L8), verification (L9).

**Components.** Tool Router, MCP Client, MCP Server catalog, Enterprise API adapters, Impact-Class enforcer, Tool audit logger.

**Inputs.** Tool calls from L2 (via the model in L6).

**Outputs.** Tool results, latency, cost, side-effect record.

**Invariants.**
- Every tool call is authenticated as the caller.
- Every tool call goes through L8 tool-argument guardrails.
- High-impact tool calls require an approval decision from L14 (P7).
- Every side-effect action is recorded to the audit log.

**Failure modes.**
- Tool unavailable → structured error; agent decides retry vs alternate tool.
- Tool timeout → cancel; emit alert.
- Approval timeout → fail closed.

**Observability signals.**
- Tool ID, arguments (redacted per PII policy), result, latency, cost, impact class, approval outcome.

**Security posture.** Enforces Trust Boundary D (Reasoning → Action). All actions are authorised, audited, and — for high-impact — approved.

---

## L8 — Guardrails & Safety

**Purpose.** Inspect and block unsafe inputs, prompts, tool arguments, and outputs.

**In scope.** Input Guardrails, Prompt Guardrails, Tool-Argument Guardrails, Output Guardrails, Prompt-injection detection, PII detection, Toxicity detection, Jailbreak detection, Format/schema enforcement.

**Out of scope.** Verification (L9), evaluation (L10), policy engine (L14 — L8 consumes L14 policies).

**Components.** Guardrail Runtime, Input/Prompt/Tool/Output guardrails, Policy client (to L14).

**Inputs.** Content at four checkpoints (input, prompt, tool argument, output).

**Outputs.** Allow / Warn / Block decision with reason.

**Invariants.**
- Guardrails fail closed on integrity checks (P2 § tension resolution).
- Every block decision produces an auditable reason.
- Guardrail results are available to L9 and L10.

**Failure modes.**
- Guardrail service outage → per-control policy: fail closed for integrity, degrade safely for availability.
- False positive → override channel through governance.

**Observability signals.**
- Checkpoint, guardrail ID, decision, reason, latency.

**Security posture.** Enforces Trust Boundary B (Reasoning ↔ Response). Prompt-injection resistant.

---

## L9 — Verification

**Purpose.** Verify the candidate response against grounding, citation, factuality, format, policy, safety — and emit a verdict.

**In scope.** Verification Engine, Grader plugins (rule, small-model, foundation-model), Grounding checker, Citation checker, Factuality checker, Format checker, Policy checker, Safety checker.

**Out of scope.** Guardrails (L8), evaluation (L10 — L9 is on the response path; L10 is offline / continuous).

**Components.** Verification Engine, Grader Registry, Verdict emitter, Escalation router.

**Inputs.** Candidate response + grounding evidence + policy set.

**Outputs.** Structured verdict (pass/warn/fail per check) + escalation decision.

**Invariants.**
- Every emitted response carries a verdict (P3).
- Failed verifications produce a structured escalation path.
- Verification cost is bounded per policy (P9).

**Failure modes.**
- Grader outage → policy decides: block, warn, or pass with degraded verdict.
- Verification timeout → treated as fail; escalate.

**Observability signals.**
- Verdict per check, grader latency, grader cost, escalation events.

**Security posture.** Consumes policy from L14. Emits audit records on any escalation.

---

## L10 — Observability & Evaluation

**Purpose.** Emit traces, metrics, logs, token/cost, agent/tool traces on the request path; run continuous evaluation on sampled traffic.

**In scope.** OpenTelemetry collector, Metric store, Log store, Evaluation store, Alert manager, Continuous-evaluation runner.

**Out of scope.** Verification (L9), guardrails (L8), CI/CD (L12).

**Components.** OTel collector, exporters, alert rules, continuous-evaluation runner, dashboards.

**Inputs.** Signals from every layer.

**Outputs.** Queryable telemetry; alerts; evaluation reports.

**Invariants.**
- Every request has an end-to-end trace.
- Every model call has token and cost telemetry.
- Every guardrail and verification decision is queryable.
- PII is redacted before persistence in observability stores.

**Failure modes.**
- Collector outage → local buffering; drop on overflow with metric.
- Alert storm → deduplication; escalation cap.

**Observability signals.**
- Meta-signals: collector health, buffer depth, drop rate.

**Security posture.** Enforces PII redaction. Audit-log-grade retention for security-relevant signals.

---

## L11 — Performance · Caching · Cost

**Purpose.** Provide prompt, semantic, embedding, memory, and response caches; account cost.

**In scope.** Cache Manager, per-tier caches, cache invalidation, cost accounting, cost attribution (tenant/user/agent), rate-shaping.

**Out of scope.** Model routing (L6), autoscaling policy (infrastructure), business KPIs (L15).

**Components.** Prompt Cache, Semantic Cache, Embedding Cache, Memory Cache, Response Cache, Cost Ledger.

**Inputs.** Cache lookups from L2, L3, L4, L5, L6, L9.

**Outputs.** Cache hit content or miss signal; cost ledger entries.

**Invariants.**
- Caches respect the caller's authorisation scope.
- Semantic cache respects grounding freshness policy.
- Cost is attributable to a tenant/user/agent for every request.

**Failure modes.**
- Cache outage → miss; upstream absorbs cost/latency.
- Semantic cache staleness → invalidation policy.

**Observability signals.**
- Hit/miss per tier, saved cost, saved latency, cost per request.

**Security posture.** Cache keys never leak identity or PII in cleartext.

---

## L12 — LLMOps & Delivery

**Purpose.** Own CI/CD, prompt/model rollout, canary, blue/green, artefact registry, prompt tests, evaluation gates.

**In scope.** Source-control integration, CI pipeline, Static analysis, Security scan, Prompt tests, Evaluation gate, Container build, Artefact registry, CD pipeline, Deployment strategies (canary, blue/green, shadow), Model registry, Prompt registry.

**Out of scope.** Runtime request path.

**Components.** CI/CD pipelines, registries, deployment controllers.

**Inputs.** Pull requests, model releases, prompt changes.

**Outputs.** Deployed versions of prompts, models, agents, tools, guardrails, verifiers.

**Invariants.**
- No untested prompt or model reaches production.
- Every deployed version is traceable to a commit and a release note.
- Rollback is automatic on defined SLO breaches.

**Failure modes.**
- Deployment failure → auto-rollback.
- Evaluation regression → block promotion.

**Observability signals.**
- Build/test/deploy events, evaluation deltas, rollout progress.

**Security posture.** Signed artefacts, secretless pipelines, supply-chain scanning.

---

## L13 — Security & Zero Trust (cross-cutting)

**Purpose.** Provide identity, secrets, encryption, PII detection, policy, audit — as a plane attached to every layer.

**In scope.** Identity provider integration, Secrets manager, KMS, PII detector, Policy engine client, Audit log, Compliance controls.

**Out of scope.** Guardrails (L8 — L8 consumes L13 capabilities).

**Invariants.**
- Every layer has an identity in scope.
- Every secret is centrally managed and rotated.
- Every action is auditable.
- Every trust boundary in Spec 009 is enforced.

**Observability signals.**
- Auth events, secret access, PII detections, policy decisions, audit records.

---

## L14 — Governance · Risk · Compliance (cross-cutting)

**Purpose.** Own the model registry, prompt registry, tool registry, policy engine, audit, and compliance mapping.

**In scope.** Model Registry, Prompt Registry, Tool Registry, Policy Engine, Audit, Compliance mapping (NIST AI RMF, ISO/IEC 42001, EU AI Act, OWASP LLM Top 10, SOC 2, GDPR, HIPAA as applicable).

**Out of scope.** Runtime enforcement (delegated to L8/L9/L7/L13).

**Invariants.**
- Every model, prompt, tool, and policy is registered, versioned, and approved.
- Policy decisions are logged.
- Compliance mappings are published.

**Observability signals.**
- Registry changes, policy verdicts, compliance findings.

---

## L15 — Business Outcomes & Value (cross-cutting)

**Purpose.** Attribute cost, measure business KPIs, connect AI outputs to business outcomes.

**In scope.** KPI definitions, value attribution, cost/benefit, product analytics linkage.

**Out of scope.** Model quality metrics (L10), verification verdicts (L9), governance status (L14).

**Invariants.**
- Every business KPI has an owner and a definition.
- Cost is attributable end-to-end.

**Observability signals.**
- KPI values, cost/value ratios, adoption/retention (where applicable).

---

## 2. Layer Interaction Matrix

The matrix below shows which layers a given layer is *permitted* to call directly. Empty cells indicate the call is forbidden (must route through an allowed layer).

| From\To | L0 | L1 | L2 | L3 | L4 | L5 | L6 | L7 | L8 | L9 | L10 | L11 |
|---------|----|----|----|----|----|----|----|----|----|----|-----|-----|
| L0 | – | ✓ |   |   |   |   |   |   |   |   | ✓* |   |
| L1 |   | – | ✓ |   |   |   |   |   |   |   | ✓* |   |
| L2 |   |   | – | ✓ |   |   |   |   | ✓ | ✓ | ✓* |   |
| L3 |   |   |   | – | ✓ | ✓ |   |   |   |   | ✓* | ✓ |
| L4 |   |   |   |   | – |   |   |   |   |   | ✓* | ✓ |
| L5 |   |   |   |   |   | – | ✓** |   |   |   | ✓* | ✓ |
| L6 |   |   |   |   |   |   | – | ✓ | ✓ |   | ✓* | ✓ |
| L7 |   |   |   |   |   |   |   | – | ✓ |   | ✓* |   |
| L8 |   |   |   |   |   |   |   |   | – |   | ✓* |   |
| L9 |   |   |   |   |   |   |   |   |   | – | ✓* | ✓ |

`✓*` = every layer emits to L10.
`✓**` = L5 may call L6 only for embedding-model calls.
L11 is a callable capability from many layers; it does not initiate calls.
L13, L14, L15 are cross-cutting and attach via defined injection points, not through direct calls.

## 3. Change Log

- **0.1.0 (2026-07-05)** — Initial draft. All 16 layers defined.

## 4. Next Specification

Continue to [Specification 006 — Interface Specification](./006-interface-specification.md).
