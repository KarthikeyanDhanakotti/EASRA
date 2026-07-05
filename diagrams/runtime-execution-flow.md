# D-R1 · Master Runtime Execution Flow

The end-to-end execution flow of a single Enterprise AI request across the 16 EASRA layers, showing decision points, cache lookups, guardrail gates, model / tool calls, verification, and response streaming.

This is the **runtime companion** to the [High-Level Architecture (D-L1)](./high-level-architecture.md). Where D-L1 shows the layered structure, D-R1 shows the execution.

## Mermaid

```mermaid
flowchart TD
    %% Ingress
    U["User / Channel"]:::user --> CHAD["K-L0-CHAD<br/>Channel Adapter"]
    CHAD --> GW["K-L1-GW<br/>API Gateway"]
    GW --> AUTH["K-L1-AUTH<br/>Authenticate"]
    AUTH --> AZ["K-L1-AZ<br/>Coarse Authorize"]
    AZ --> RL["K-L1-RL<br/>Rate Limit / Quota"]
    RL --> RV["K-L1-RV<br/>Request Validate"]
    RV --> TBM["K-L1-TBM<br/>Token Budget"]

    %% Orchestration entry
    TBM --> ROUTER["K-L2-ROUTER<br/>AI Router"]
    ROUTER -->|"single"| SA["K-L2-SA<br/>Single-Agent Runtime"]
    ROUTER -->|"multi"| MA["K-L2-MA<br/>Multi-Agent Coordinator"]
    ROUTER -->|"workflow"| WF["K-L2-WF<br/>Workflow Engine"]

    %% Context build
    SA --> CB["K-L3-CB<br/>Context Builder"]
    MA --> CB
    WF --> CB
    CB --> MM["K-L4-MM<br/>Memory Manager"]
    CB --> RR["K-L5-RR<br/>Retrieval Router"]
    MM --> CB
    RR --> RRK["K-L5-RRK<br/>Reranker"]
    RRK --> CB

    %% Response cache
    CB --> RCACHE{"K-L11-RC<br/>Response cache?"}
    RCACHE -->|"hit"| OG_H["K-L8-OG<br/>Output Guardrails"]
    RCACHE -->|"miss"| PB["K-L3-PB<br/>Prompt Builder"]

    %% Guardrails input
    PB --> IG["K-L8-IG<br/>Input Guardrails"]
    IG -->|"block"| ERR["Error Envelope<br/>+ Audit"]
    IG -->|"allow"| PG["K-L8-PG<br/>Prompt Guardrails"]
    PG -->|"block"| ERR
    PG -->|"allow"| PCACHE{"K-L11-PC<br/>Prompt cache?"}

    %% Prompt & semantic cache
    PCACHE -->|"hit"| MODEL_OUT["Model Output<br/>(from cache)"]
    PCACHE -->|"miss"| SCACHE{"K-L11-SC<br/>Semantic cache?"}
    SCACHE -->|"hit"| MODEL_OUT
    SCACHE -->|"miss"| MR["K-L6-MR<br/>Model Router"]

    %% Model call
    MR --> FM["K-L6-FM / SM / VM / SPM<br/>Model"]
    FM -->|"ok"| MODEL_OUT
    FM -->|"fault / policy"| FB["K-L6-FB<br/>Fallback Router"]
    FB --> FM

    %% Tool decision
    MODEL_OUT --> NEEDS_TOOL{"Needs tool?"}
    NEEDS_TOOL -->|"no"| VE["K-L9-VE<br/>Verification Engine"]
    NEEDS_TOOL -->|"yes"| AG["K-L8-AG<br/>Tool-Arg Guardrails"]
    AG -->|"block"| ERR
    AG -->|"allow"| IMP{"K-L7-IMP<br/>Impact class?"}
    IMP -->|"read"| TR["K-L7-TR<br/>Tool Router"]
    IMP -->|"write"| TR
    IMP -->|"high-impact"| HITL["Human-in-the-loop<br/>gate"]
    HITL -->|"approved"| TR
    HITL -->|"denied"| ERR
    TR --> MCP["K-L7-MCP / ENT<br/>Tool Adapter"]
    MCP --> SA

    %% Verification
    VE --> GRD["K-L9-GRD Grounding"]
    VE --> CIT["K-L9-CIT Citation"]
    VE --> FCT["K-L9-FCT Factuality"]
    VE --> FMT["K-L9-FMT Format"]
    VE --> POL["K-L9-POL Policy"]
    VE --> BR["K-L9-BR Business Rule"]
    GRD --> CS["K-L9-CS<br/>Confidence Scorer"]
    CIT --> CS
    FCT --> CS
    FMT --> CS
    POL --> CS
    BR --> CS

    CS -->|"allow"| OG["K-L8-OG<br/>Output Guardrails"]
    CS -->|"escalate"| HITL2["Human review"]
    CS -->|"block"| ERR
    HITL2 -->|"approved"| OG
    HITL2 -->|"denied"| ERR

    OG -->|"block"| ERR
    OG -->|"allow"| STREAM["Stream response<br/>(SSE / WS)"]
    OG_H --> STREAM
    STREAM --> U

    %% Observability (cross-cutting)
    OTEL["K-L10-OTEL<br/>Traces / Metrics / Logs"]:::obs
    COST["K-L10-COST<br/>Cost Emitter"]:::obs
    EVAL["K-L10-EVAL<br/>Continuous Evaluator"]:::obs
    STREAM -.-> OTEL
    STREAM -.-> COST
    STREAM -.-> EVAL
    ERR -.-> OTEL
    ERR -.-> COST

    classDef user fill:#EAF3FF,stroke:#3B7DDD,color:#0B3D91,stroke-width:1px
    classDef obs fill:#FFF6E5,stroke:#B58900,color:#5A4600,stroke-width:1px
```

## Key decision points

| # | Decision | Enforced by | Outcomes |
|---|----------|-------------|----------|
| 1 | Response cache hit? | `K-L11-RC` | hit → skip to output guardrails; miss → prompt build. |
| 2 | Input / Prompt guardrails allow? | `K-L8-IG`, `K-L8-PG` | allow / block. |
| 3 | Prompt cache hit? | `K-L11-PC` | hit → skip model. |
| 4 | Semantic cache hit? | `K-L11-SC` | hit → skip model. |
| 5 | Model fault or policy breach? | `K-L6-MR` → `K-L6-FB` | retry via fallback. |
| 6 | Needs tool? | agent | branch to tool subpath. |
| 7 | Tool impact class? | `K-L7-IMP` | read / write / high-impact (→ HITL). |
| 8 | Verification verdict? | `K-L9-CS` | allow / escalate (→ HITL) / block. |
| 9 | Output guardrails allow? | `K-L8-OG` | allow / block. |

## Cross-cutting

- **Observability (L10)** — every node emits traces (W3C TraceContext), metrics, logs. Cost is emitted at every model and tool call.
- **Security (L13)** — every hop carries an identity; PII, secrets, and audit are enforced regardless of path.
- **Governance (L14)** — every model, prompt, and tool used must resolve to a registry-signed artefact.

## What this diagram intentionally omits

- Physical placement (→ [D-D1 Deployment Topology](./deployment-topology.md)).
- Trust boundaries (→ [D-S1 Trust Boundaries](./trust-boundaries.md)).
- Streaming internals (→ D-R6 Cache Lookup Sequence — planned).
- CI / CD (→ [D-O2 CI/CD Pipeline](./cicd-pipeline.md)).

## ASCII fallback (skeleton)

```
User → CHAD → GW → AUTH → AZ → RL → RV → TBM
      → ROUTER → { SA | MA | WF }
      → CB ← (MM, RR→RRK)
      → RCACHE? ─hit→ OG → Stream → User
                 └miss→ PB → IG → PG → PCACHE? → SCACHE? → MR → Model
                                                        ↑        │
                                                        FB ←─────┤ (on fault)
                                                                 ▼
                          Needs tool? ─yes→ AG → IMP{read/write/high} → TR → Tool → SA
                                        └no→ VE → { GRD, CIT, FCT, FMT, POL, BR } → CS
                                             CS→ { allow → OG → Stream ; escalate → HITL ; block → ERR }
Observability (L10), Security (L13), Governance (L14) apply to every step.
```

## Related

- [High-Level Architecture (D-L1)](./high-level-architecture.md)
- [Spec 007 — Data Flow](../specification/007-data-flow.md)
- [Spec 008 — Sequence Diagrams](../specification/008-sequence-diagrams.md)
- [Spec 011 — Capability Model](../specification/011-capability-model.md)
- [Spec 012 — Component Catalogue](../specification/012-component-catalogue.md)
