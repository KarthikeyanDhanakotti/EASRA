# Observability Plane

Companion diagram to Layer L10 in [Specification 005](../specification/005-layer-definitions.md) and NFR N10 in [Specification 010](../specification/010-nfr.md).

## 1. The observability plane (L10)

```mermaid
flowchart LR
    subgraph Emitters["Every EASRA Layer (L0 – L9, L11)"]
        E1[L1 Gateway]:::emit
        E2[L2 Orchestrator]:::emit
        E3[L3 Prompt]:::emit
        E4[L4 Memory]:::emit
        E5[L5 Retrieval]:::emit
        E6[L6 Model]:::emit
        E7[L7 Tools]:::emit
        E8[L8 Guardrails]:::emit
        E9[L9 Verification]:::emit
        E11[L11 Cache]:::emit
    end

    subgraph Collector["OpenTelemetry Collector"]
        OTEL[Receivers · Processors<br/>PII redaction · Sampling · Batching]:::col
    end

    subgraph Backends["Storage & Analysis"]
        direction LR
        TRC[(Traces)]:::back
        MET[(Metrics)]:::back
        LOG[(Logs)]:::back
        EVL[(Evaluation Store)]:::back
        AUD[(Audit Log · L13)]:::back
    end

    subgraph Products["Observability Products"]
        direction LR
        DASH[Dashboards]:::prod
        ALT[Alert Manager]:::prod
        SLO[SLO Watch]:::prod
        CEV[Continuous Evaluation]:::prod
        COST[Cost & Value<br/>tenant · user · agent]:::prod
    end

    E1 & E2 & E3 & E4 & E5 & E6 & E7 & E8 & E9 & E11 --> OTEL
    OTEL --> TRC
    OTEL --> MET
    OTEL --> LOG
    OTEL --> EVL
    OTEL --> AUD
    TRC & MET & LOG & EVL --> DASH
    MET --> ALT
    MET --> SLO
    EVL --> CEV
    MET --> COST

    classDef emit fill:#22d3ee,stroke:#155e75,color:#083344
    classDef col fill:#1f2937,stroke:#0f172a,color:#f8fafc
    classDef back fill:#374151,stroke:#0f172a,color:#f8fafc
    classDef prod fill:#facc15,stroke:#713f12,color:#111827
```

## 2. Required signals per layer (summary)

| Layer | Required signals |
|-------|------------------|
| L1 | Auth outcome, latency, rate-limit hit, session load latency |
| L2 | Agent trace, plan step count, wall-clock, per-step latency and cost |
| L3 | Prompt trace (template, version, inputs), token counts, cache hit/miss |
| L4 | Memory type, read/write count, latency, PII classification |
| L5 | Query, retrieval strategy, index latency, result count, rerank latency |
| L6 | Model ID, tokens (prompt/completion/cached), cost, latency, provider, fallback events |
| L7 | Tool ID, arguments (redacted), result, latency, cost, impact class, approval outcome |
| L8 | Checkpoint, guardrail ID, decision, reason, latency |
| L9 | Verdict per check, grader latency, grader cost, escalation events |
| L11 | Hit/miss per tier, saved cost, saved latency, cost per request |

Full signal specification lives in [Specification 006 §IX.All→L10 Telemetry](../specification/006-interface-specification.md#ixall→l10--telemetry).

## 3. Change log

- **0.1.0 (2026-07-05)** — Initial observability plane diagram.
