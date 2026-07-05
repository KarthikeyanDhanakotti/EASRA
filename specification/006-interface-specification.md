# Specification 006 — Interface Specification

| Field | Value |
|-------|-------|
| Specification | EASRA-SPEC-006 |
| Title | Interface Specification |
| Version | 0.1.0 (Draft) |
| Status | Draft |
| Depends on | 001, 002, 003, 004, 005 |

---

## 1. Purpose

This specification defines the contract at every EASRA layer boundary: the inputs, outputs, invariants, error taxonomy, and observability signals. Interfaces are the mechanism by which loose coupling (P5), vendor neutrality (P1), and evolvability (P10) are enforced.

Interfaces are described in a language-agnostic form. Reference implementations may use JSON Schema, OpenAPI, Protocol Buffers, or language-native types — provided they preserve the contract.

## 2. Contract elements

Each interface has:

- **Name** — canonical identifier `EASRA.IX.<from-layer>.<to-layer>.<purpose>`.
- **Direction** — request/response, event, or duplex.
- **Payload** — the structured data exchanged.
- **Invariants** — properties that must hold on payload and behaviour.
- **Errors** — the defined error taxonomy.
- **Observability** — signals the caller and callee must emit.

## 3. Common types

The following types are used across many interfaces.

### 3.1 CorrelationContext

```
CorrelationContext {
  requestId       : ULID
  sessionId       : ULID | null
  tenantId        : string | null
  userId          : opaque hash
  traceId         : W3C-TraceContext traceparent
  spanId          : W3C-TraceContext spanid
  causationId     : ULID | null
}
```

### 3.2 Identity

```
Identity {
  subjectId       : opaque hash
  subjectType     : "user" | "service" | "agent" | "system"
  authnMethod     : string
  authnTime       : timestamp
  scopes          : string[]
  tenantId        : string | null
}
```

### 3.3 PIIClassification

```
PIIClassification {
  containsPII     : boolean
  categories      : ("name" | "email" | "phone" | "govId" | "financial" | "health" | "other")[]
  handlingPolicy  : "redact" | "hash" | "encrypt" | "block" | "allow"
}
```

### 3.4 CostRecord

```
CostRecord {
  tokensPrompt      : int
  tokensCompletion  : int
  tokensCached      : int
  currency          : ISO-4217
  amount            : decimal
  provider          : string
  modelId           : string
  timestamp         : timestamp
  attribution       : { tenantId, userId, agentId, requestId }
}
```

### 3.5 Verdict

```
Verdict {
  overall         : "pass" | "warn" | "fail"
  checks          : Array<{ name, result: "pass"|"warn"|"fail", score?: float, reason?: string, evidence?: string[] }>
  escalation      : "none" | "human-review" | "block" | "log-only"
  producedBy      : string
  timestamp       : timestamp
}
```

### 3.6 ErrorEnvelope

```
ErrorEnvelope {
  code            : string      // stable machine-readable identifier
  title           : string      // human-readable
  layer           : "L0".."L15"
  category        : "validation" | "auth" | "policy" | "guardrail" | "verification"
                  | "timeout" | "unavailable" | "rate-limit" | "internal"
  retryable       : boolean
  retryAfterMs    : int | null
  correlation     : CorrelationContext
  details         : object | null
}
```

## 4. Interfaces (canonical set)

The following interfaces are defined by v0.1. Additional interfaces (multi-region, event bus, async workflow) are reserved.

### IX.L0→L1  ClientRequest

- **Direction.** Request/response.
- **Payload.**
  ```
  ClientRequest {
    correlation      : CorrelationContext
    channel          : { type, version }
    credentials      : opaque token | null
    input            : { text?, media?, structured? }
    hints            : { streaming?: bool, latencySLO?: ms, preferModel?: string }
  }
  ```
- **Response.** `ClientResponse { correlation, verdict, output, formatMeta, cost }` or `ErrorEnvelope`.
- **Invariants.** `correlation.requestId` is unique per request. `credentials` never leave L1.
- **Errors.** `auth.invalid`, `auth.expired`, `validation.schema`, `rate-limit.channel`, `unavailable.backend`.

### IX.L1→L2  ValidatedRequest

- **Direction.** Request/response.
- **Payload.**
  ```
  ValidatedRequest {
    correlation      : CorrelationContext
    identity         : Identity
    session          : { id, state, memoryRefs, policyContext }
    input            : structured
    hints            : same as ClientRequest.hints
  }
  ```
- **Invariants.** `identity` is verified. `session` is loaded from the external store.
- **Errors.** `auth.forbidden`, `policy.blocked`, `session.expired`.

### IX.L2→L3  ContextRequest

- **Direction.** Request/response.
- **Payload.**
  ```
  ContextRequest {
    correlation      : CorrelationContext
    identity         : Identity
    goal             : structured intent
    turnHistory      : Turn[]
    memoryQuery      : { types: MemoryType[], k: int }
    retrievalQuery   : { indexes: string[], k: int, filters?: object } | null
    tokenBudget      : int
  }
  ```
- **Response.** `PromptManifest` (below).
- **Invariants.** `tokenBudget` is honoured. Prompt is deterministic given inputs.

### IX.L3→L6  ModelRequest

- **Direction.** Request/response (streaming or non-streaming).
- **Payload.**
  ```
  ModelRequest {
    correlation      : CorrelationContext
    identity         : Identity
    prompt           : { messages | text, systemMessage, toolSchemas? }
    routingHints     : { capabilities: string[], costCeiling?, latencySLO?, preferModel? }
    piiClassification: PIIClassification
    tokenBudget      : { maxCompletion, stopSequences? }
  }
  ```
- **Response.**
  ```
  ModelResponse {
    correlation      : CorrelationContext
    output           : { text?, toolCalls?, structured? }
    tokens           : { prompt, completion, cached }
    cost             : CostRecord
    modelId          : string
    finishReason     : "stop" | "length" | "tool_calls" | "safety" | "error"
  }
  ```
- **Invariants.** `modelId`, `tokens`, `cost` are always present. PII policy enforced on routing.

### IX.L3↔L4  MemoryAccess

- **Direction.** Duplex (read/write).
- **Read payload.** `{ correlation, identity, types, query, k }` → `MemoryRecord[]`.
- **Write payload.** `{ correlation, identity, type, record }` → `{ id, version }`.
- **Invariants.** Records are identity-scoped. PII is classified at write.

### IX.L3↔L5  RetrievalQuery

- **Direction.** Duplex (query/results, plus index-management).
- **Query payload.**
  ```
  RetrievalQuery {
    correlation, identity, query, indexes, k, filters?, rerank?: bool
  }
  ```
- **Response.**
  ```
  RetrievalResults {
    chunks: Array<{ text, score, source: { id, version, url?, aclScope }, index }>
    latencyMs, rerankMs?
  }
  ```
- **Invariants.** Every chunk carries provenance and ACL scope. Scope is honoured by callers.

### IX.L2→L7  ToolInvocation

- **Direction.** Request/response.
- **Payload.**
  ```
  ToolInvocation {
    correlation, identity
    tool             : { id, version }
    arguments        : structured
    impactClass      : "read" | "write" | "high-impact"
    approval         : ApprovalContext | null
  }
  ```
- **Response.**
  ```
  ToolResult {
    correlation, output, latencyMs, cost?, sideEffectRecord?, verdict?
  }
  ```
- **Invariants.** `impactClass` matches the tool registry. High-impact invocations require `approval`.

### IX.L*→L8  GuardrailCheck

- **Direction.** Request/response (may be pipelined).
- **Payload.**
  ```
  GuardrailCheck {
    correlation, identity
    checkpoint       : "input" | "prompt" | "tool-arg" | "output"
    content          : structured
    policyContext    : object
  }
  ```
- **Response.** `Verdict` (see §3.5) with `overall ∈ {pass, warn, fail}`.
- **Invariants.** Guardrail failure at any checkpoint short-circuits downstream layers per policy.

### IX.L2/L8→L9  VerificationRequest

- **Direction.** Request/response.
- **Payload.**
  ```
  VerificationRequest {
    correlation, identity
    candidateResponse: structured
    grounding        : Chunk[] | null
    policySet        : PolicyRef[]
  }
  ```
- **Response.** `Verdict`.
- **Invariants.** Every response emitted to the client carries a verdict.

### IX.L2→L11  CacheAccess

- **Direction.** Duplex.
- **Payload.** `{ correlation, identity, tier, key, valueOnMiss? }` → `{ hit, value? }`.
- **Invariants.** Cache keys never contain PII in cleartext. Reads respect ACL scope.

### IX.All→L10  Telemetry

- **Direction.** Event (fire-and-forget with buffered delivery).
- **Payload.** OpenTelemetry-shaped span/metric/log with AI-specific attributes:
  - `easra.layer`, `easra.component`, `easra.model_id`, `easra.tokens.*`, `easra.cost.*`, `easra.guardrail.*`, `easra.verdict.*`, `easra.tool.id`, `easra.impact_class`, `easra.pii.classification`.
- **Invariants.** PII is redacted before export. Sampling is centrally controlled.

### IX.All→L13/L14  PolicyDecision

- **Direction.** Request/response.
- **Payload.** `{ correlation, identity, action, resource, context }` → `{ decision: "allow"|"deny"|"require-approval", reasons, obligations }`.
- **Invariants.** Deny reasons are audit-logged. Approvals produce an `ApprovalContext` reusable in `ToolInvocation`.

### IX.L12→All  Deployment

- **Direction.** Event / control.
- **Payload.** `{ artefactId, version, strategy, gates }`.
- **Invariants.** Every artefact is signed. Evaluation gates block promotion on regression.

## 5. Prompt manifest

```
PromptManifest {
  templateId       : string
  templateVersion  : semver
  inputs           : {
    system         : string
    userTurns      : Turn[]
    memory         : MemoryRecord[]
    retrieval      : Chunk[]
    toolSchemas    : ToolSchema[]
  }
  tokenCounts      : { system, user, memory, retrieval, tools, total }
  piiClassification: PIIClassification
  cacheKey         : opaque hash
}
```

## 6. Error taxonomy

Errors are classified by `category` (see `ErrorEnvelope`). Categories are stable across versions.

| Category | Meaning | Retryable |
|----------|---------|-----------|
| `validation` | Input failed schema or semantic validation. | No |
| `auth` | Authentication or authorisation failure. | No |
| `policy` | Blocked by policy engine (L14). | No |
| `guardrail` | Blocked by guardrail (L8). | No |
| `verification` | Response failed verification (L9). | Sometimes (with revised prompt) |
| `timeout` | Layer or dependency exceeded time bound. | Yes with backoff |
| `unavailable` | Dependency down (open circuit). | Yes with backoff |
| `rate-limit` | Rate or quota exceeded. | Yes with `retryAfterMs` |
| `internal` | Unclassified server error. | Yes with backoff |

## 7. Versioning

- Interfaces are versioned by the specification version they were introduced in.
- Additive changes (new optional fields, new response types) are minor.
- Removal, renaming, or changing the meaning of a field is major.
- Callers must ignore unknown fields (tolerant reader).
- Interfaces are stable within a major EASRA version.

## 8. Reference schemas

JSON Schema and OpenAPI definitions live in [`reference-implementation/schemas/`](../reference-implementation/) once populated.

## 9. Change Log

- **0.1.0 (2026-07-05)** — Initial draft. Twelve canonical interfaces defined.

## 10. Next Specification

Continue to [Specification 007 — Data Flow](./007-data-flow.md).
