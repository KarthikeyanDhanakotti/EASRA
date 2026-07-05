# Specification 007 — Data Flow

| Field | Value |
|-------|-------|
| Specification | EASRA-SPEC-007 |
| Title | Data Flow |
| Version | 0.1.0 (Draft) |
| Status | Draft |
| Depends on | 001–006 |

---

## 1. Purpose

This specification defines the canonical data flows through EASRA: request flow, response flow, cache flow, memory flow, retrieval flow, tool flow, guardrail flow, verification flow, telemetry flow, policy flow, and delivery flow. Each flow names the layers, interfaces, transformations, and invariants involved.

Data flows are *logical*. A concrete implementation may combine or split hops as long as the invariants hold.

## 2. Flow catalogue

| # | Flow | Purpose |
|---|------|---------|
| F1 | Request | Client input → validated, authenticated request in orchestration. |
| F2 | Response | Verified response → client. |
| F3 | Cache | Read/write across the cache plane. |
| F4 | Memory | Read/write across short-term / long-term / semantic / session / profile. |
| F5 | Retrieval | Query → grounded chunks with provenance. |
| F6 | Tool | Tool call → authorised, guardrailed, audited action. |
| F7 | Guardrail | Content → allow/warn/block verdict at four checkpoints. |
| F8 | Verification | Candidate response → structured verdict. |
| F9 | Telemetry | Layer signals → observability plane. |
| F10 | Policy | Action + context → allow/deny/require-approval. |
| F11 | Delivery | Change → tested, signed, gated, deployed artefact. |
| F12 | Audit | Security-relevant events → tamper-evident audit log. |

## 3. F1 — Request Flow

```
L0 Channel
  → IX.L0→L1 ClientRequest
L1 Gateway
  ├── TLS termination, WAF, bot protection
  ├── Authentication → Identity
  ├── Coarse authorisation
  ├── Rate limiting
  ├── Session Manager: load session (external store)
  └── Request Validator: schema + semantic checks
  → IX.L1→L2 ValidatedRequest
L2 AI Router
  → Single Agent | Multi-Agent Coordinator | Workflow Engine
```

**Transformations.**
- Credentials → Identity (verified, scoped).
- Raw input → structured input.
- Anonymous request → session-bound request.

**Invariants.**
- No unauthenticated request reaches L2 (except in documented anonymous modes).
- Session state is loaded from external store; compute stays stateless (P6).
- Every request has a correlation context.

## 4. F2 — Response Flow

```
L6 Model output → L8 Output Guardrails → L9 Verification
                                            │
                              pass          │           fail
                                ▼                         ▼
                       L9 Response Formatter    Escalation (policy):
                                │                 · human-review
                                │                 · block
                                │                 · log-only + degraded
                       L9 Streaming Engine
                                │
                        IX.L1→L0 ClientResponse
                                │
                              L0 Channel
```

**Transformations.**
- Model raw output → guardrailed candidate.
- Candidate → verified response with verdict attached.
- Verified response → client-shaped payload (JSON, markdown, SSE frames).

**Invariants.**
- Every emitted response carries a verdict (P3).
- Streaming responses have verdict-emitted-at-end semantics and interim safety checks.

## 5. F3 — Cache Flow

Five tiers, each with independent invalidation policy:

| Tier | Key | Value | Invalidation |
|------|-----|-------|--------------|
| Prompt cache | Hash of prompt manifest inputs | Assembled prompt | Template version bump. |
| Semantic cache | Embedding of query + identity scope | Prior response | Grounding freshness; policy version. |
| Embedding cache | Text hash + embedding model version | Embedding vector | Embedding model change. |
| Memory cache | Identity + memory key | Memory record | Write-through invalidation. |
| Response cache | Full request hash + identity scope | Full response | Policy version; explicit purge. |

```
Caller → IX.*→L11 CacheAccess {tier, key}
  hit: return value
  miss: caller executes, writes back
```

**Invariants.**
- Cache keys never contain PII in cleartext.
- Reads respect the caller's ACL scope.
- Semantic cache respects grounding freshness policy.

## 6. F4 — Memory Flow

```
L2/L3 → IX.L3↔L4 MemoryAccess (read)
        L4 Memory Manager
          → Short-term store   (recent turns)
          → Long-term store    (durable, identity-bound)
          → Session store      (working notes)
          → Semantic store     (vector recall)
          → Profile store      (structured preferences)
        ← Ranked records
```

**Writes** (e.g., agent commits a note): identical path, with PII classification enforced at write time.

**Invariants.**
- Every memory record has an owning identity.
- Reads never cross authorisation scope.
- PII in memory is classified and access-controlled.

## 7. F5 — Retrieval Flow

```
L3 Context Builder
  → IX.L3↔L5 RetrievalQuery
    L5 Retrieval Router
      ├── Vector index  (kNN over embeddings)
      ├── Keyword index (BM25)
      ├── Structured index (SQL / graph)
      └── Reranker
    ← Ranked chunks with provenance + ACL scope
  → L11 Embedding Cache (optional)
```

**Invariants.**
- Every chunk carries provenance (source ID, version, timestamp).
- Retrieval never returns content the caller may not read.
- Fallback path is defined per index outage.

## 8. F6 — Tool Flow

```
L2 Agent (via L6 model tool-call)
  → IX.L2→L7 ToolInvocation {tool, args, impactClass}
    L8 Tool-Argument Guardrails
    L14 Policy Engine (impactClass gate; approval if required)
    L7 Tool Router → MCP Client → MCP Server | Enterprise API
    L7 Audit logger → L13 audit log
  ← Tool result + side-effect record
L9 (result may be re-verified before use)
```

**Invariants.**
- Every tool call is authenticated as the caller.
- High-impact tool calls require approval (P7).
- Every side effect is audited (F12).

## 9. F7 — Guardrail Flow

Four checkpoints:

| Checkpoint | Where | Purpose |
|------------|-------|---------|
| Input | L1 → L2 boundary | Reject unsafe or malicious user input at ingress. |
| Prompt | L3 → L6 boundary | Enforce prompt structure, block injection, mark system boundaries. |
| Tool argument | L2 → L7 boundary | Block harmful, out-of-scope, or overly permissive arguments. |
| Output | L6 → L9 boundary | Enforce policy on model output before verification. |

```
Caller → IX.*→L8 GuardrailCheck
  L8 runs registered guardrails for the checkpoint
  Emits Verdict (pass | warn | fail) + reason
  On fail: caller short-circuits per policy (block, degrade, escalate)
```

**Invariants.**
- Fail-closed on integrity; fail-safe on availability (P2 tension resolution).
- Every block is auditable with a reason.

## 10. F8 — Verification Flow

```
Candidate response + grounding + policy set
  → IX.L2/L8→L9 VerificationRequest
    L9 Verification Engine
      ├── Grounding checker  (all claims traceable to grounding?)
      ├── Citation checker   (citations well-formed and non-fabricated?)
      ├── Factuality checker (matches trusted source?)
      ├── Format checker     (schema, length, banned patterns?)
      ├── Policy checker     (aligned with L14 policy set?)
      └── Safety checker     (residual harm signal after L8?)
    ← Verdict (pass | warn | fail per check)
```

**Escalation.** On `fail`, policy chooses `human-review`, `block`, or `log-only + degraded`.

**Invariants.**
- Every response emitted to the client carries a verdict.
- Verification cost is bounded per policy (P9).

## 11. F9 — Telemetry Flow

Every layer emits, at minimum:

- Trace spans (W3C TraceContext).
- Metrics (latency, error rate, throughput).
- Structured logs.
- AI-specific attributes: token counts, cost, model ID, guardrail decisions, verdicts, agent/tool trace.

```
Layer emitter → OTel SDK → OTel Collector (L10)
                              ├── Traces store
                              ├── Metrics store
                              ├── Logs store
                              └── Evaluation store
                            Alert manager → notification channels
```

**Invariants.**
- PII redacted before persistence.
- Sampling controlled centrally.
- Buffered delivery; drops are metric-visible.

## 12. F10 — Policy Flow

```
Actor (any layer) → IX.All→L13/L14 PolicyDecision {action, resource, context}
  L14 Policy Engine
    evaluates: data classification, tenant policy, role, impact class, jurisdiction
  ← { decision: allow | deny | require-approval, reasons[], obligations[] }
  Obligations may include: redaction, encryption, additional logging, cache exclusion.
```

**Invariants.**
- Decisions are audit-logged (F12).
- Deny reasons are structured and stable.
- Obligations are enforced by the caller (contractually) and monitored in L10.

## 13. F11 — Delivery Flow

```
PR (source control)
  → CI: static analysis + security scan + prompt tests + unit tests
  → Build: container image + model bundle
  → Registry: signed artefact
  → CD gates: evaluation regression check + policy check
  → Deployment strategy: canary → blue/green → prod
  → Rollback: SLO-breach auto-triggered
```

**Invariants.**
- Every deployed version is traceable to a commit and release note.
- Evaluation regression blocks promotion.
- Rollback is defined per SLO.

## 14. F12 — Audit Flow

```
Security-relevant event (auth, secret access, policy decision, side effect, escalation)
  → L13 Audit Emitter
    → Tamper-evident audit log (append-only, integrity-verified)
    → Retention per compliance requirement
    → Export to SIEM (optional)
```

**Invariants.**
- Audit records are immutable.
- Retention meets the strictest applicable compliance requirement.
- Access to audit records is itself audited.

## 15. Data classifications

Every payload traversing EASRA carries a classification:

| Class | Definition | Handling |
|-------|------------|----------|
| Public | No confidentiality requirement. | No special handling. |
| Internal | Restricted to authenticated users. | Standard encryption in transit and at rest. |
| Confidential | Restricted to authorised roles. | Field-level encryption where feasible; access-audited. |
| Restricted | Regulatory (PII, PHI, PCI). | Redaction/tokenisation; strict retention; audit. |
| Secret | Credentials, keys. | Never in prompts, memory, caches, or logs. |

## 16. Change Log

- **0.1.0 (2026-07-05)** — Initial draft. Twelve canonical flows defined.

## 17. Next Specification

Continue to [Specification 008 — Sequence Diagrams](./008-sequence-diagrams.md).
