# Specification 002 — Design Principles

| Field | Value |
|-------|-------|
| Specification | EASRA-SPEC-002 |
| Title | Enterprise AI Design Principles |
| Version | 0.1.0 (Draft) |
| Status | Draft |
| Depends on | 001 |

---

## 1. Purpose

This specification defines the ten design principles that govern every layer of EASRA. The principles are the shared "why" behind every layer boundary, every interface contract, and every trust boundary. Any change to a layer, interface, or trust boundary must be justified against these principles.

Design principles are **normative**. A system that violates a principle without a documented, justified deviation is not EASRA-conformant.

## 2. The Ten Principles

| # | Principle | Category |
|---|-----------|----------|
| P1 | Vendor Neutrality | Structure |
| P2 | Security by Design | Safety |
| P3 | Verification by Design | Safety |
| P4 | Observability by Default | Operations |
| P5 | Loose Coupling | Structure |
| P6 | Externalized State | Structure |
| P7 | Human-in-the-Loop | Safety |
| P8 | Failure Isolation | Operations |
| P9 | Cost Awareness | Operations |
| P10 | Evolvability | Structure |

---

## P1 — Vendor Neutrality

**Statement.** The architecture is defined in logical terms. Every layer must map cleanly to at least two independent implementations drawn from Azure, AWS, GCP, or open-source stacks.

**Rationale.** Vendor lock-in is the single largest reversibility cost in Enterprise AI. Models, embedding services, vector databases, agent frameworks, and orchestrators are all changing rapidly. A reference architecture that hard-codes any of them will not survive a two-year horizon.

**Implications.**
- Specification and handbook text names *capabilities*, not products.
- Vendor mappings live in dedicated "Cloud Implementation" subsections.
- Interface contracts (Spec 006) are technology-agnostic — no proprietary types in signatures.

**Violations.**
- Naming a specific vendor in a layer definition (e.g., "the retrieval layer uses Azure AI Search").
- Interface contracts that require a proprietary payload format.

**Verification.** For every layer, at least two independent implementations must exist in the handbook.

---

## P2 — Security by Design

**Statement.** Zero-trust, least-privilege, prompt-injection resistance, and PII protection are architectural — not add-on — concerns. Security controls attach to named trust boundaries defined in Specification 009.

**Rationale.** Enterprise AI systems handle sensitive data, execute tools, and produce actions with real-world consequences. Post-hoc security is insufficient. The OWASP LLM Top 10 (prompt injection, insecure output handling, training data poisoning, model DoS, supply-chain, sensitive information disclosure, insecure plugin design, excessive agency, overreliance, model theft) enumerate failures that must be addressed at architectural boundaries.

**Implications.**
- Every trust boundary in Spec 009 has named security controls.
- The Guardrails layer (L8) is architecturally *before* tool execution — not after.
- Identity is verified at L1 and re-verified before any privileged action.
- Secrets never traverse the model layer.

**Violations.**
- Security controls implemented only inside the model prompt.
- Tools executed without identity re-verification.
- PII entering L4 (memory) or L11 (cache) without classification.

**Verification.** The threat model in Spec 009 lists every OWASP LLM Top 10 threat mapped to a named control at a named boundary.

---

## P3 — Verification by Design

**Statement.** Every AI output is *verifiable* against a stated property. Verification is a first-class layer (L9), distinct from evaluation.

**Rationale.** Evaluation measures *the model* on a benchmark dataset; verification measures *this response* against constraints (grounding, citation, factuality, policy, format, safety). Evaluation happens offline; verification happens on the response path. Enterprise AI without verification is a system that cannot say *why* it accepted a given output.

**Implications.**
- L9 is on the response path, not a batch process.
- Verification failures produce structured verdicts, not silent pass-throughs.
- The response schema includes verification results.
- Escalation is a defined path when verification fails.

**Violations.**
- Treating evaluation datasets as verification.
- Silently retrying on verification failure without escalation.
- Producing responses that cannot be traced to grounding evidence.

**Verification.** Every response emitted by a conformant system carries a verification verdict.

---

## P4 — Observability by Default

**Statement.** Every component emits traces, metrics, logs, token/cost accounting, and agent/tool traces without configuration. Observability is opt-out, not opt-in.

**Rationale.** Enterprise AI systems fail in ways classical systems do not: silent quality regressions, hallucinated grounding, tool-argument drift, prompt-injection leakage. These failures are invisible to CPU/memory/latency metrics. OpenTelemetry-shaped telemetry plus AI-specific signals (token usage, prompt trace, tool trace, evaluation score, verification verdict, cost per request) are required.

**Implications.**
- The observability layer (L10) is on the request path, not a background job.
- Every layer emits a defined signal set (Spec 006 §Observability).
- Cost telemetry is emitted alongside latency telemetry.
- Traces carry both technical and AI-specific span attributes.

**Violations.**
- A layer that cannot be traced end-to-end.
- Cost tracked only in monthly bills, not per request.
- Model calls without token counts.

**Verification.** For every canonical sequence in Spec 008, the observability signals must be enumerable.

---

## P5 — Loose Coupling

**Statement.** Layers communicate only through published interfaces (Spec 006). No layer depends on another layer's internals, and no layer may cross more than one adjacent boundary without going through it.

**Rationale.** Tight coupling makes upgrades cost O(n²). Enterprise AI moves fast — new models, new tools, new agents — and the architecture must absorb that change locally. Loose coupling is what makes vendor neutrality (P1) achievable in practice.

**Implications.**
- Interfaces are versioned; internals are not.
- A layer may be replaced without changing its neighbours.
- Cross-cutting concerns (security, observability) attach via defined injection points, not direct calls.

**Violations.**
- A prompt-builder that reads directly from a vector-DB SDK.
- An orchestrator that hard-codes a model provider's SDK.
- Guardrails that inspect internal state of the model router.

**Verification.** Replace any single layer's implementation with a mock; the neighbouring layers must be unchanged.

---

## P6 — Externalized State

**Statement.** All state — memory, sessions, caches, feature stores, vector indexes — lives *outside* compute. Compute (agents, orchestrators, model clients) is stateless and horizontally scalable.

**Rationale.** Stateful compute cannot scale horizontally, cannot fail over, cannot be restarted safely, and cannot be canary-deployed. Enterprise AI needs autoscaling under bursty demand and safe rolling updates; both require stateless compute.

**Implications.**
- Session Manager writes to an external session store.
- Memory Manager writes to short-term, long-term, semantic memory stores.
- Cache Manager writes to the cache plane (L11).
- No in-process caches beyond a request lifetime.

**Violations.**
- Session state pinned to a specific pod / instance.
- In-memory agent state that cannot be restored on restart.
- Prompt cache held inside the process only.

**Verification.** Any compute node can be killed at any time; the system continues, and the request either completes on another node or fails cleanly with a defined error.

---

## P7 — Human-in-the-Loop

**Statement.** Every autonomous action has a defined escalation path, override mechanism, and audit trail. High-impact actions require explicit human approval by policy.

**Rationale.** Agentic systems act. Actions have consequences (money moved, records changed, messages sent). The OWASP LLM Top 10 explicitly names *Excessive Agency* as a top risk. Human-in-the-loop is not a UI feature; it is an architectural property enforced by the tooling layer (L7), the guardrails layer (L8), and the governance layer (L14).

**Implications.**
- Tools are classified by impact (read / write / high-impact).
- High-impact tools require an approval step routed through a defined channel.
- Every autonomous action is logged with actor, reason, evidence, verification verdict.
- An override channel exists — humans can stop a running agent.

**Violations.**
- Autonomous write actions with no approval or audit.
- Agents that cannot be interrupted.
- Actions logged without evidence.

**Verification.** For every tool in the tool registry, its impact class and approval policy are declared.

---

## P8 — Failure Isolation

**Statement.** Failure in one layer degrades the system gracefully. No single layer can cascade a full outage. Every layer has a defined degraded mode.

**Rationale.** Enterprise AI depends on external services (model APIs, retrieval indexes, tool APIs) that fail independently and often. A rigid architecture that requires every layer to be healthy will have poor availability. Bulkheads, circuit breakers, timeouts, and defined fallback behaviours are architectural.

**Implications.**
- Every external call has a timeout and a circuit breaker.
- Model routing (L6) has fallback models.
- Retrieval (L5) has fallback (cached / static) modes.
- Guardrails (L8) fail *closed* on integrity checks and *safe* on availability failures.
- Verification (L9) has defined behaviour on evaluator outage.

**Violations.**
- A single model outage taking down the whole platform.
- Guardrail outage silently disabling guardrails.
- No timeout on any external call.

**Verification.** A layer-level chaos test (kill one layer) is part of the conformance suite.

---

## P9 — Cost Awareness

**Statement.** Token, compute, and storage cost are explicit design inputs. Cost is a first-class telemetry signal, an SLO, and a routing input.

**Rationale.** Enterprise AI cost is dominated by token usage and can be non-linear with request patterns. Systems built without cost awareness routinely exceed budgets by 5–10×. Cost must be observable per request, attributable per tenant/user/agent, and enforceable via routing and caching policies.

**Implications.**
- Every model call emits token counts and cost.
- Every request has an owning tenant / user / agent for cost attribution.
- Cost telemetry lives alongside latency telemetry in L10.
- The router (L6) may route to cheaper models for lower-value requests.
- Caches (L11) are a cost control, not just a latency control.

**Violations.**
- Model calls without token accounting.
- Cost surfaced only in monthly bills.
- Routing decisions that ignore cost.

**Verification.** For every canonical sequence in Spec 008, the expected cost is declarable.

---

## P10 — Evolvability

**Statement.** New models, tools, agents, channels, and cross-cutting policies can be added without redesigning the architecture. The number of layers, and the layer boundaries, are stable across minor versions.

**Rationale.** Enterprise AI evolves faster than any architecture can be redesigned. A reference architecture that requires a redraw every six months is not a reference. Evolvability is achieved through explicit extension points (routers, registries, policy engines) rather than open-ended flexibility.

**Implications.**
- New models plug into the Model Router (L6) via the model interface.
- New tools plug into the Tool Router (L7) via the MCP contract.
- New agents plug into the Multi-Agent Coordinator (L2) via the agent interface.
- New channels plug into L0 via the request contract.
- New policies plug into L14 via the policy interface.

**Violations.**
- Adding a model that requires changes to L2, L3, or L8.
- Adding a tool that requires a new interface.
- Adding a channel that changes the request contract.

**Verification.** For every extension point, adding a new implementation is a local change.

---

## 3. Principle Interactions

Principles reinforce each other; some tensions exist and are resolved explicitly:

| Tension | Resolution |
|---------|------------|
| P2 (Security) vs P8 (Failure Isolation) | Guardrails fail *closed* for integrity, *safe* for availability. Explicit per-control policy. |
| P4 (Observability) vs P2 (Security / PII) | Observability signals are PII-classified; sensitive fields are hashed or redacted at emission (L10 §PII). |
| P9 (Cost) vs P3 (Verification) | Verification cost is bounded by policy — not every response requires every check. |
| P10 (Evolvability) vs P5 (Loose Coupling) | Extension points are the *only* places evolution happens; internals stay coupled where beneficial. |
| P6 (Externalised State) vs P9 (Cost) | State stores are chosen for cost/latency tradeoffs; the *externalisation* is non-negotiable. |

## 4. Deviation Process

A system may deviate from a principle if:

1. The deviation is documented in `EASRA-CONFORMANCE.md`.
2. The rationale references a specific constraint (regulatory, latency, cost).
3. Compensating controls are named.
4. The deviation is time-boxed with a review date.

Undocumented deviations disqualify the system from EASRA conformance.

## 5. Change Log

- **0.1.0 (2026-07-05)** — Initial draft. Ten principles defined.

## 6. Next Specification

Continue to [Specification 003 — Terminology](./003-terminology.md).
