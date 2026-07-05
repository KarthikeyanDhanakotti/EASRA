# EASRA on Google Cloud

Vendor-specific mapping of the EASRA architecture to Google Cloud services. This guide realises every EASRA layer and component ([Spec 012](../../specification/012-component-catalogue.md)) on GCP without changing the architecture.

| Field | Value |
|-------|-------|
| Status | Draft |
| Target EASRA version | v0.1.0 |
| Last updated | 2026-07-05 |

## 1. Layer mapping

| Layer | Capability | GCP services | Notes |
|-------|------------|--------------|-------|
| **L0** Channels & UX | C0 | Cloud CDN, Cloud Load Balancing, Dialogflow CX (voice/chat) | Channel adapter on Cloud Run. |
| **L1** Edge · Gateway · Identity | C1, C13 | **Cloud Armor** (WAF), **Apigee** or **API Gateway**, **Identity Platform** / **Cloud IAM** | Rate limit + quota via Apigee policies. |
| **L2** AI Orchestration | C2 | **Cloud Run**, **Cloud Workflows**, **Vertex AI Agent Builder**, LangGraph on Cloud Run | Termination via Cloud Workflows step limits. |
| **L3** Prompt Intelligence | C3 | **Secret Manager**, **Cloud Storage** (versioned prompts), **Vertex AI Prompt Optimizer** | Prompt Registry as GCS bucket with versioning + Secret Manager. |
| **L4** Memory & Context | C4 | **Memorystore for Redis** (working/short), **Firestore** (session/profile), **Vertex AI Vector Search** (semantic), **AlloyDB** with `pgvector` (episodic) | Memory Manager on Cloud Run. |
| **L5** Knowledge & Retrieval | C5 | **Vertex AI Search** (hybrid), **Spanner Graph** (graph), **BigQuery** (structured), reranker via Vertex AI | Ingestion via Dataflow + Cloud Functions. |
| **L6** Models & Model Router | C6 | **Vertex AI Model Garden**, **Gemini API**, third-party model partners on Vertex AI | Model Router on Cloud Run. |
| **L7** Tooling & Actions | C7 | **Apigee** (adapter), **Cloud Workflows** (tool orchestration), MCP servers on Cloud Run | HITL via Pub/Sub + email/Chat. |
| **L8** Guardrails & Safety | C8 | **Vertex AI Safety Filters**, **DLP API** (PII), custom classifiers on Vertex AI | |
| **L9** Verification | C9 | **Vertex AI Evaluation service**, custom checkers on Cloud Run | |
| **L10** Observability & Evaluation | C10 | **Cloud Trace**, **Cloud Logging**, **Cloud Monitoring**, **Managed Service for Prometheus**, **Vertex AI Model Monitoring** | OTLP → GMP or Cloud Trace agent. |
| **L11** Performance · Caching · Cost | C11 | **Memorystore for Redis**, **Billing Export to BigQuery** + custom Cost Ledger | |
| **L12** LLMOps & Delivery | C12 | **Cloud Build**, **Artifact Registry**, **Vertex AI Pipelines**, **App Config** via Firebase Remote Config | Canary via Cloud Run traffic splitting. |
| **L13** Security & Zero Trust | C13 | **Cloud IAM** + **Workload Identity**, **Secret Manager**, **Cloud KMS**, **DLP API**, **VPC Service Controls**, **Private Google Access** | Every hop uses Workload Identity token. |
| **L14** Governance, Risk, Compliance | C14 | **Cloud Asset Inventory**, **Access Transparency**, **Assured Workloads**, **Chronicle** | Policy engine as Organization Policies + custom Cloud Run service. |
| **L15** Business Outcomes & Value | C15 | **Looker**, **BigQuery** dashboards | KPI Registry via BigQuery. |

## 2. Trust boundary mapping ([Spec 009](../../specification/009-trust-boundaries.md))

| Boundary | GCP realisation |
|----------|-----------------|
| **TB-A** User → Gateway | Cloud CDN + Cloud Armor → Apigee (VPC-SC perimeter). |
| **TB-B** Reasoning → Model | Cloud Run → Vertex AI via Private Google Access + VPC-SC. |
| **TB-C** Reasoning → Tool | Apigee tool adapter; MCP servers in dedicated Cloud Run service with egress control. |
| **TB-D** System → Data | Firestore / Vertex AI Search / GCS behind VPC-SC; CMEK via Cloud KMS; DLP classification. |

## 3. NFR mapping ([Spec 010](../../specification/010-nfr.md))

| NFR | GCP realisation |
|-----|-----------------|
| N1 Availability | Multi-region Cloud Run, Firestore multi-region, Vertex AI regional endpoints. |
| N2 Latency | Global load balancer + regional Vertex AI + regional Redis. |
| N3 Throughput | Cloud Run autoscaling, Vertex AI provisioned throughput. |
| N4 Cost | Billing export to BigQuery + Cost Ledger table. |
| N5 Safety | Vertex AI safety filters + DLP + custom guardrails. |
| N12 CI/CD | Cloud Build + Artifact Registry + Vertex AI Pipelines. |

## 4. Known gaps

- **Response cache (`K-L11-RC`)** — no first-party AI response cache; implement on Memorystore.
- **Impact-class enforcer (`K-L7-IMP`)** — no native HITL primitive; assemble from Pub/Sub + Chat + Workflows.

## 5. References

- [Vertex AI documentation](https://cloud.google.com/vertex-ai/docs)
- [Vertex AI Agent Builder](https://cloud.google.com/products/agent-builder)
- [Google Cloud generative AI resources](https://cloud.google.com/ai/generative-ai)
