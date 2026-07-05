# Trust Boundaries — Diagrams

Companion diagrams to [Specification 009 — Trust Boundaries](../specification/009-trust-boundaries.md).

## 1. The four boundaries on the request path

```mermaid
flowchart LR
    U([User])
    L0[L0 Channel]
    L1[L1 Gateway<br/>AuthN · AuthZ · WAF · RL]
    L2[L2 Orchestrator]
    L3[L3 Prompt]
    L6[L6 Model Router]
    M[(Model Provider<br/>external or internal)]
    L7[L7 Tool Router]
    T[(Tool · MCP · Enterprise API)]
    L8[L8 Guardrails]
    L9[L9 Verification]

    U --> L0
    L0 --> L1
    L1 --> L2
    L2 --> L3 --> L6
    L6 --> M
    L2 --> L7 --> T
    L6 --> L8 --> L9
    L9 --> L1 --> L0 --> U

    %% Trust boundary markers
    classDef tb fill:#fef2f2,stroke:#dc2626,color:#7f1d1d,stroke-width:2px,stroke-dasharray:6 3
    TBA[/"TB-A · Edge Boundary<br/>untrusted → trusted"/]:::tb
    TBB[/"TB-B · Response Boundary<br/>internal → observable"/]:::tb
    TBC[/"TB-C · Model Boundary<br/>internal → provider"/]:::tb
    TBD[/"TB-D · Action Boundary<br/>reasoning → real world"/]:::tb

    L0 -. crosses .- TBA
    L9 -. crosses .- TBB
    L6 -. crosses .- TBC
    L7 -. crosses .- TBD
```

## 2. Threat mapping (OWASP LLM Top 10)

| Threat | Boundary | Control | Diagrammed at |
|--------|----------|---------|---------------|
| LLM01 Prompt Injection | TB-A / TB-C / TB-D | Input, prompt, tool-arg guardrails; structural prompt boundaries | L8 checkpoints |
| LLM02 Insecure Output Handling | TB-B | Output guardrails + response formatter + schema | L8/L9 → L1 |
| LLM04 Model DoS | TB-A / TB-C | Rate limit + timeouts | L1 · L6 |
| LLM05 Supply Chain | TP-2 · TB-C | Signed artefacts · approved providers | CI/CD · Model Registry |
| LLM06 Sensitive Info Disclosure | TB-B · TP-1 | PII policy · redaction · cache-key policy | L9 · L11 |
| LLM07 Insecure Plugin Design | TB-D | Tool registry · argument guardrails · impact class | L7 · L8 |
| LLM08 Excessive Agency | TB-D | Impact class · approval · audit | L7 · L14 |
| LLM09 Overreliance | TB-B | Verification verdict · human-review escalation | L9 |
| LLM10 Model Theft | TB-A · TB-C | AuthN on APIs · egress policy | L1 · L6 |

Full mapping table lives in [Specification 009 §9](../specification/009-trust-boundaries.md#9-threat-mapping-summary).

## 3. Data plane and delivery plane

```mermaid
flowchart TB
    subgraph Compute
        C1[L2 · L3 · L6 · L7 · L8 · L9]:::c
    end
    subgraph Data["TP-1 · Data Plane"]
        MEM[(Memory Stores)]:::d
        IDX[(Vector · BM25 · SQL · Graph)]:::d
        CACHE[(Cache Plane)]:::d
    end
    subgraph Delivery["TP-2 · Delivery Plane"]
        SRC[Source · PR]:::e
        CI[CI · Prompt tests · Eval]:::e
        AR[Signed Artefacts · SBOM]:::e
        CD[Canary · Blue/Green]:::e
    end

    Compute -- TLS · identity-scoped --- Data
    Delivery -- signed · gated --- Compute

    classDef c fill:#c7d2fe,stroke:#3730a3,color:#1e1b4b
    classDef d fill:#fecdd3,stroke:#9f1239,color:#4c0519
    classDef e fill:#ddd6fe,stroke:#5b21b6,color:#2e1065
```

## 4. Change log

- **0.1.0 (2026-07-05)** — Initial threat-mapped trust-boundary diagrams.
