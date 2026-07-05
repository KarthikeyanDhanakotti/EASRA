# EASRA on Microsoft Azure

Vendor-specific mapping of the EASRA architecture to Microsoft Azure services. This guide realises every EASRA layer and component ([Spec 012](../../specification/012-component-catalogue.md)) on Azure without changing the architecture.

| Field | Value |
|-------|-------|
| Status | Draft |
| Target EASRA version | v0.1.0 |
| Last updated | 2026-07-05 |

## 1. Layer mapping

| Layer | Capability | Azure services | Notes |
|-------|------------|----------------|-------|
| **L0** Channels & UX | C0 | Azure Front Door, Azure App Service, Azure Static Web Apps, Azure Communication Services | Channel adapter runs on Azure Container Apps or App Service. |
| **L1** Edge · Gateway · Identity | C1, C13 | Azure Front Door + WAF, **Azure API Management** (policy pipeline), **Microsoft Entra ID** (OIDC), Front Door rate-limit rules | APIM enforces rate limit, quota, auth, request validation, token-budget claim. |
| **L2** AI Orchestration | C2 | **Azure Container Apps** (agents), **Azure Durable Functions** (workflow), **Microsoft Agent Framework** / **Semantic Kernel** | Termination controller enforces max-steps/cost/time. |
| **L3** Prompt Intelligence | C3 | **Azure App Configuration** (registry), **Azure Key Vault** (secrets), **Prompty** / **Prompt flow (Azure ML)** | Prompt Registry candidate: App Config with feature flags + Key Vault refs. |
| **L4** Memory & Context | C4 | **Azure Cache for Redis** (working/short), **Azure Cosmos DB** (session/long/profile), **Azure AI Search** vector index (semantic), **Azure Database for PostgreSQL** with `pgvector` (episodic) | Memory Manager as a Container Apps microservice. |
| **L5** Knowledge & Retrieval | C5 | **Azure AI Search** (hybrid: vector + BM25), **Cosmos DB for Apache Gremlin** (graph), **Microsoft Fabric / OneLake** (structured), reranker via Azure ML online endpoint | Ingestion pipeline via Azure Data Factory + Azure Functions. |
| **L6** Models & Model Router | C6 | **Azure AI Foundry** (Model Catalog), **Azure OpenAI**, **Azure AI Speech**, **Azure AI Vision**, **Azure ML** online endpoints | Model Router as a Container Apps service with fallback logic. |
| **L7** Tooling & Actions | C7 | **APIM** (adapter), **Azure Logic Apps** (workflow-style tools), **MCP servers on Azure Container Apps**, **Microsoft Graph** for M365 actions | Impact class implemented as APIM policy tags + HITL via Teams / Approval workflows. |
| **L8** Guardrails & Safety | C8 | **Azure AI Content Safety** (Prompt Shields, jailbreak, groundedness detection), **Azure AI Language** (PII), custom classifiers on ML endpoints | Input, prompt, tool-arg, and output guardrails all callable as ACS APIs. |
| **L9** Verification | C9 | **Azure AI Foundry evaluators**, **Presidio** for PII, custom checkers on Container Apps, **AI Content Safety** groundedness | Verification Engine coordinates checkers and emits `Verdict`. |
| **L10** Observability & Evaluation | C10 | **Azure Monitor** + **Log Analytics**, **Application Insights**, **Azure Managed Grafana**, **Azure OpenAI diagnostic logs**, **Azure AI Foundry tracing** | OTLP exporter → Log Analytics via OpenTelemetry Collector on AKS/CA. |
| **L11** Performance · Caching · Cost | C11 | **Azure Cache for Redis** (prompt, semantic, response), **Azure Cost Management**, custom Cost Ledger on Cosmos DB | Semantic cache = Redis with vector similarity + embedding lookup. |
| **L12** LLMOps & Delivery | C12 | **GitHub Actions** / **Azure DevOps**, **Azure Container Registry**, **Azure ML pipelines**, **App Config feature flags**, **Azure Deployment Environments** | Canary via Container Apps revisions or APIM weighted routing. |
| **L13** Security & Zero Trust | C13 | **Microsoft Entra ID** (workload identity), **Managed Identity**, **Key Vault**, **Microsoft Purview** (PII), **Defender for Cloud**, **Private Endpoints** everywhere | Every hop uses Managed Identity + Entra token; no shared secrets. |
| **L14** Governance, Risk, Compliance | C14 | **Microsoft Purview**, **Azure Policy**, **Azure AI Foundry governance**, **Azure Monitor Workbooks** | Policy engine as Azure Policy + APIM policies + custom Container App. |
| **L15** Business Outcomes & Value | C15 | **Microsoft Fabric** + **Power BI**, **Application Insights KPI workbook** | KPI Registry as Fabric semantic model. |

## 2. Trust boundary mapping ([Spec 009](../../specification/009-trust-boundaries.md))

| Boundary | Azure realisation |
|----------|-------------------|
| **TB-A** User → Gateway | Front Door (public) → APIM (private endpoint). WAF + DDoS L3/7 at Front Door. mTLS between FD and APIM. |
| **TB-B** Reasoning → Model | Container Apps → Azure OpenAI over Private Link only. Managed Identity + Entra token. |
| **TB-C** Reasoning → Tool | APIM tool adapter with per-tool policy; MCP servers on isolated Container Apps environment; NSG egress control. |
| **TB-D** System → Data | Cosmos / AI Search / Storage all Private Endpoint only; encryption with customer-managed keys in Key Vault; Purview classification. |

## 3. NFR mapping ([Spec 010](../../specification/010-nfr.md))

| NFR | Azure realisation |
|-----|-------------------|
| N1 Availability | Multi-AZ Container Apps, Cosmos DB multi-write, AOAI PTU with regional failover. |
| N2 Latency | Front Door geo-routing + regional AOAI, Redis in-region, prompt/semantic cache. |
| N3 Throughput | APIM tier scaling, Container Apps HPA/KEDA, AOAI PTU. |
| N4 Cost | Cost Management + Cost Ledger (Cosmos append-only). |
| N5 Safety | Content Safety + Prompt Shields + Presidio. |
| N12 CI/CD | GitHub Actions + Azure ML pipelines + ACR + Deployment Environments. |

## 4. Reference deployment topology

Aligned to [D-D1](../../diagrams/deployment-topology.md). Bicep/Terraform scaffolding lives in [`../../reference-implementation/`](../../reference-implementation/) (planned).

## 5. Known gaps

- **Workflow Engine (`K-L2-WF`)** — Durable Functions covers the pattern but lacks native prompt/eval integration; considered a documented gap until an ADR selects a canonical binding.
- **Continuous Evaluator (`K-L10-EVAL`)** — Azure AI Foundry evaluators cover the majority of C10.6 but do not yet cover custom business-rule verifiers without additional code on Container Apps.

## 6. Capability Maturity Statement (Azure v0.1 target)

The Azure reference targets **M ≥ 3** for every subcapability implemented and **M0** (with justification) for those it does not. Full statement to accompany [reference-implementation/](../../reference-implementation/) release.

## 7. References

- [Azure AI Foundry documentation](https://learn.microsoft.com/azure/ai-foundry/)
- [Azure OpenAI Service documentation](https://learn.microsoft.com/azure/ai-services/openai/)
- [Azure API Management policies](https://learn.microsoft.com/azure/api-management/api-management-policies)
- [Microsoft Purview](https://learn.microsoft.com/purview/)
- [Microsoft Agent Framework](https://learn.microsoft.com/agent-framework/)
