# Deployment Topology

Companion diagram to [Specification 004 §8](../specification/004-reference-architecture.md#8-deployment-topology-logical).

## 1. Logical deployment topology

```mermaid
flowchart TB
    subgraph Users["Enterprise Users"]
        U([Web · Mobile · API · Chat · Voice])
    end

    subgraph Edge["Edge Tier"]
        CDN[CDN · WAF · Bot]:::edge
        GLB[Global Load Balancer]:::edge
        GW[API Gateway]:::edge
    end

    subgraph Compute["Compute Tier  (stateless · autoscaled)"]
        direction LR
        ORCH[Orchestration]:::comp
        PROMPT[Prompt Intelligence]:::comp
        MODEL[Model Clients]:::comp
        TOOL[Tool Clients · MCP]:::comp
        GR[Guardrails]:::comp
        VER[Verification]:::comp
    end

    subgraph Data["Data Plane  (externalized state · TP-1)"]
        direction LR
        SESS[(Session Store)]:::data
        MEM[(Memory Stores<br/>short · long · session · semantic · profile)]:::data
        IDX[(Vector · BM25 · SQL · Graph)]:::data
        CACHE[(Cache Plane<br/>prompt · semantic · embedding · memory · response)]:::data
        FS[(Feature Store)]:::data
        EVT[(Event Bus)]:::data
    end

    subgraph Models["Model Tier"]
        direction LR
        FM[Foundation Model Providers<br/>SaaS APIs]:::mod
        HOST[Self-Hosted Inference<br/>GPU / NPU / CPU]:::mod
    end

    subgraph Obs["Observability Tier"]
        OTEL[OTel Collector]:::obs
        MET[Metric Store]:::obs
        LOG[Log Store]:::obs
        TRC[Trace Store]:::obs
        EVL[Evaluation Store]:::obs
    end

    subgraph Deliver["Delivery Tier  (TP-2)"]
        CI[CI Pipeline]:::del
        AR[Signed Artefact Registry]:::del
        PR[Prompt Registry]:::del
        MR[Model Registry]:::del
        TR[Tool Registry]:::del
        CD[CD Controller]:::del
    end

    subgraph Gov["Governance Tier"]
        POL[Policy Engine]:::gov
        AUD[Audit Log]:::gov
        CMP[Compliance Dashboards]:::gov
    end

    subgraph Infra["Infrastructure Substrate  (any cloud · on-prem · hybrid)"]
        K8S[Kubernetes]:::infra
        NET[VNet · Private Endpoints · Egress Policy]:::infra
        SEC[Secrets Manager · KMS · IdP]:::infra
        BLOB[Blob / Object Storage]:::infra
        AS[Autoscaling · Multi-Region · DR]:::infra
    end

    U --> CDN --> GLB --> GW
    GW --> Compute
    Compute --> Data
    Compute --> Models
    Compute --> Obs
    Deliver -.->|deploy| Compute
    Gov -.->|policies| Compute
    Compute --> Gov
    Infra --- Compute
    Infra --- Data
    Infra --- Models
    Infra --- Obs
    Infra --- Deliver
    Infra --- Gov

    classDef edge fill:#38bdf8,stroke:#0c4a6e,color:#ffffff
    classDef comp fill:#22d3ee,stroke:#155e75,color:#083344
    classDef data fill:#fbcfe8,stroke:#9d174d,color:#4a044e
    classDef mod fill:#facc15,stroke:#713f12,color:#111827
    classDef obs fill:#1f2937,stroke:#0f172a,color:#f8fafc
    classDef del fill:#c084fc,stroke:#581c87,color:#ffffff
    classDef gov fill:#374151,stroke:#0f172a,color:#f8fafc
    classDef infra fill:#e5e7eb,stroke:#374151,color:#111827
```

## 2. Tier responsibilities (summary)

| Tier | Owns | Scales |
|------|------|--------|
| Edge | Termination, WAF, LB, gateway | Global points-of-presence |
| Compute | L2, L3, L6, L7, L8, L9 runtimes | Horizontal (P6) |
| Data plane | L4, L5, L11 stores | Per-store class (kv, vector, sql, cache) |
| Model tier | Provider APIs + self-hosted inference | Provider quotas or GPU/NPU fleet |
| Observability | L10 collectors and stores | Cardinality-driven |
| Delivery | L12 pipelines and registries | Build farm |
| Governance | L14 policy, audit, compliance | Low-volume, high-durability |
| Infrastructure | Kubernetes, network, secrets, storage, autoscale | Cluster-wide |

## 3. Cloud-mapping recipe

The topology is deliberately vendor-neutral. Each tier has ≥ 2 implementations on each cloud (Azure, AWS, GCP) and open-source. The mapping tables live in the handbook chapters for each layer.

## 4. Change log

- **0.1.0 (2026-07-05)** — Initial logical deployment topology.
