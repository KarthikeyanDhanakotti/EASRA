# Specification 008 — Sequence Diagrams

| Field | Value |
|-------|-------|
| Specification | EASRA-SPEC-008 |
| Title | Sequence Diagrams |
| Version | 0.1.0 (Draft) |
| Status | Draft |
| Depends on | 001–007 |

---

## 1. Purpose

This specification captures the canonical request sequences through EASRA. Each sequence shows the layers, interfaces, cache interactions, guardrail checkpoints, verification, and observability. The diagrams are the reference for what a spec-conformant system does in each mode.

Six canonical sequences are defined; additional sequences (batch, async workflow, event-driven, disaster recovery) are reserved for future specifications.

| # | Sequence | Mode | Streaming | Tool use | Multi-agent |
|---|----------|------|-----------|----------|-------------|
| S1 | Simple Chat | Sync | Optional | No | No |
| S2 | Cached Chat | Sync | Optional | No | No |
| S3 | RAG Query | Sync | Optional | No | No |
| S4 | Single-Agent Tool Use | Sync | Optional | Yes | No |
| S5 | Multi-Agent | Sync | Optional | Yes | Yes |
| S6 | Verification Failure & Escalation | Sync | – | Any | Any |

Diagrams below use Mermaid `sequenceDiagram`. Where a step is optional, it is annotated `[optional]`.

---

## 2. S1 — Simple Chat

Purpose: single-turn generation with no retrieval and no tools.

```mermaid
sequenceDiagram
    autonumber
    actor U as User
    participant L0 as L0 Channel
    participant L1 as L1 Gateway/Identity
    participant L2 as L2 Orchestrator
    participant L3 as L3 Prompt Intelligence
    participant L4 as L4 Memory
    participant L11 as L11 Cache Plane
    participant L8 as L8 Guardrails
    participant L6 as L6 Model Router
    participant L9 as L9 Verification
    participant L10 as L10 Observability

    U->>L0: user input
    L0->>L1: ClientRequest
    L1->>L1: AuthN + AuthZ + Rate limit + Session load
    L1->>L2: ValidatedRequest
    L2->>L3: ContextRequest
    L3->>L4: MemoryAccess (short-term)
    L4-->>L3: recent turns
    L3->>L11: Prompt Cache lookup
    alt Cache miss
        L3->>L3: build prompt
        L3->>L11: write prompt cache
    end
    L3->>L8: GuardrailCheck (input, prompt)
    L8-->>L3: pass
    L3->>L6: ModelRequest
    L6->>L6: Route → invoke provider
    L6-->>L3: ModelResponse (tokens, cost)
    L3->>L8: GuardrailCheck (output)
    L8-->>L3: pass
    L3->>L9: VerificationRequest
    L9-->>L3: Verdict (pass)
    L3->>L2: candidate + verdict
    L2->>L1: ClientResponse
    L1->>L0: response
    L0->>U: rendered output
    par
        L1-->>L10: telemetry
        L2-->>L10: agent trace
        L6-->>L10: token+cost telemetry
        L8-->>L10: guardrail telemetry
        L9-->>L10: verdict telemetry
    end
```

**Observability signals.** Trace ID, prompt trace, model ID, token counts, cost, all guardrail verdicts, verification verdict, end-to-end latency.

---

## 3. S2 — Cached Chat (semantic cache hit)

Purpose: exploit L11 semantic cache to serve a prior response.

```mermaid
sequenceDiagram
    autonumber
    actor U as User
    participant L0 as L0
    participant L1 as L1
    participant L2 as L2
    participant L3 as L3
    participant L11 as L11 Cache
    participant L6 as L6 (Embedding only)
    participant L8 as L8
    participant L9 as L9
    participant L10 as L10

    U->>L0: input
    L0->>L1: ClientRequest
    L1->>L2: ValidatedRequest
    L2->>L3: ContextRequest
    L3->>L6: embed(query)
    L6-->>L3: embedding
    L3->>L11: Semantic Cache lookup (identity-scoped)
    L11-->>L3: hit (prior response, verdict, grounding refs)
    L3->>L8: Guardrail (output)  [replay policy]
    L8-->>L3: pass
    L3->>L9: Verification (freshness + policy)
    L9-->>L3: pass
    L3->>L2: response
    L2->>L1: ClientResponse
    L1->>L0: response
    L0->>U: rendered
    L11-->>L10: cache-hit telemetry (saved cost, saved latency)
```

**Notes.** Cached responses still traverse L8 (with replay policy) and L9 (freshness + policy) — a cached response is not exempt from current policy.

---

## 4. S3 — RAG Query

Purpose: grounded answer with retrieval.

```mermaid
sequenceDiagram
    autonumber
    actor U as User
    participant L1 as L1
    participant L2 as L2
    participant L3 as L3
    participant L4 as L4 Memory
    participant L5 as L5 Retrieval
    participant L11 as L11 Cache
    participant L6 as L6 Model
    participant L8 as L8
    participant L9 as L9

    U->>L1: query
    L1->>L2: ValidatedRequest
    L2->>L3: ContextRequest (with retrieval hint)
    L3->>L4: MemoryAccess
    L3->>L11: Embedding Cache lookup
    alt Embedding miss
        L3->>L6: embed(query)
        L6-->>L3: embedding
        L3->>L11: write embedding
    end
    L3->>L5: RetrievalQuery (hybrid: vector + BM25)
    L5->>L5: index search + rerank
    L5-->>L3: chunks + provenance + ACL scope
    L3->>L3: build prompt with grounding
    L3->>L8: Guardrails (input, prompt)
    L3->>L6: ModelRequest
    L6-->>L3: response
    L3->>L8: Guardrail (output)
    L3->>L9: Verification (grounding + citation + factuality)
    L9-->>L3: pass
    L3->>L2: grounded response + citations + verdict
    L2->>L1: ClientResponse
```

**Verification focus.** L9 asserts (a) every claim maps to a chunk in `grounding`, (b) every citation resolves to a valid source, (c) no fabricated citations. On any failure the escalation path in S6 applies.

---

## 5. S4 — Single-Agent Tool Use

Purpose: agent plans, calls one or more tools via MCP, produces a grounded response.

```mermaid
sequenceDiagram
    autonumber
    participant L2 as L2 Agent
    participant L3 as L3 Prompt
    participant L6 as L6 Model
    participant L7 as L7 Tool Router
    participant L8 as L8 Guardrails
    participant L14 as L14 Policy Engine
    participant MCP as MCP Server
    participant L9 as L9 Verification

    L2->>L3: ContextRequest (with tool schemas)
    L3->>L6: ModelRequest
    L6-->>L3: response { toolCalls: [t1(args)] }
    L3->>L2: propagate tool call
    L2->>L8: GuardrailCheck (tool-arg)
    L8-->>L2: pass
    L2->>L14: PolicyDecision (impactClass, args, context)
    alt high-impact
        L14-->>L2: require-approval
        L2->>L2: pause; request approval (H-i-T-L)
        L2->>L14: approval evidence
        L14-->>L2: allow
    else read/write within policy
        L14-->>L2: allow
    end
    L2->>L7: ToolInvocation
    L7->>MCP: invoke
    MCP-->>L7: result + side-effect record
    L7-->>L2: ToolResult
    L2->>L3: extend context with tool result
    L3->>L6: ModelRequest (with result)
    L6-->>L3: final response
    L3->>L8: Guardrail (output)
    L3->>L9: Verification
    L9-->>L3: verdict
```

**Notes.** The loop `model → tool → model` may repeat until termination (bounded by L2 step count and wall-clock). Every tool call is audited (F12).

---

## 6. S5 — Multi-Agent

Purpose: coordinator dispatches sub-agents in parallel; merges results.

```mermaid
sequenceDiagram
    autonumber
    participant Coord as L2 Coordinator
    participant Plan as L2 Planner
    participant A1 as Sub-Agent A
    participant A2 as Sub-Agent B
    participant A3 as Sub-Agent C
    participant L8 as L8
    participant L9 as L9

    Coord->>Plan: decompose(goal)
    Plan-->>Coord: plan {A: sub-goal1, B: sub-goal2, C: sub-goal3}
    par
        Coord->>A1: dispatch(sub-goal1)
        A1-->>Coord: partial1 (already L8-checked, L9-verified locally)
    and
        Coord->>A2: dispatch(sub-goal2)
        A2-->>Coord: partial2
    and
        Coord->>A3: dispatch(sub-goal3)
        A3-->>Coord: partial3
    end
    Coord->>Coord: merge(partial1, partial2, partial3)
    Coord->>L8: Guardrail (merged output)
    Coord->>L9: Verification (aggregate)
    L9-->>Coord: verdict
    Coord-->>Coord: response
```

**Bulkheads.** Sub-agent failure is isolated by the coordinator (P8). Partial success is allowed only if policy permits and the aggregate verdict passes.

---

## 7. S6 — Verification Failure & Escalation

Purpose: response fails verification; escalation path invoked.

```mermaid
sequenceDiagram
    autonumber
    participant L3 as L3
    participant L9 as L9
    participant L14 as L14 Policy
    participant HITL as Human Reviewer
    participant L1 as L1
    participant L10 as L10 Observability

    L3->>L9: VerificationRequest
    L9-->>L3: verdict {overall: fail, checks: [grounding: fail]}
    L3->>L14: escalation decision
    alt policy: human-review
        L14-->>L3: require human-review
        L3->>HITL: notify + attach evidence
        HITL-->>L3: approve | reject | edit
        alt approved
            L3->>L1: ClientResponse (annotated: human-reviewed)
        else rejected
            L3->>L1: safe fallback response
        end
    else policy: block
        L14-->>L3: block
        L3->>L1: policy-blocked response
    else policy: log-only + degraded
        L14-->>L3: allow (log-only)
        L3->>L1: response with verdict warning
    end
    L9-->>L10: verdict + escalation telemetry
    L3-->>L10: audit event
```

**Notes.** The escalation policy is defined per data class, tenant, and impact context. All escalations emit audit events (F12).

---

## 8. Cross-cutting: telemetry on every hop

All sequences above emit telemetry at every hop. The observability layer (L10) is deliberately omitted from most arrows for readability; conformance requires it on every request path.

```mermaid
sequenceDiagram
    participant Any as Any Layer
    participant OTel as OTel Collector
    participant M as Metrics
    participant T as Traces
    participant L as Logs
    participant E as Evaluation
    participant A as Alerts

    Any-->>OTel: span + metric + log + AI attrs
    OTel-->>T: trace store
    OTel-->>M: metric store
    OTel-->>L: log store
    OTel-->>E: sampled requests → continuous eval
    E-->>A: regression detected → alert
```

---

## 9. Rendering notes

- Mermaid renders natively on GitHub. Copy-paste any block into any Mermaid-capable tool for adaptation.
- The `diagrams/` folder holds source (`.mmd`) and rendered exports (`.svg`, `.png`) for use in slides and papers.
- When adapting a diagram, keep layer names, interface names, and checkpoint names unchanged — that is the spec.

## 10. Change Log

- **0.1.0 (2026-07-05)** — Initial draft. Six canonical sequences defined.

## 11. Next Specification

Continue to [Specification 009 — Trust Boundaries](./009-trust-boundaries.md).
