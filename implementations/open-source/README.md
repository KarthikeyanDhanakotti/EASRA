# EASRA on Open-Source (Kubernetes + CNCF)

Vendor-neutral, open-source mapping of the EASRA architecture. This guide realises every EASRA layer and component ([Spec 012](../../specification/012-component-catalogue.md)) using open-source and CNCF projects, deployable on any Kubernetes cluster.

| Field | Value |
|-------|-------|
| Status | Draft |
| Target EASRA version | v0.1.0 |
| Last updated | 2026-07-05 |

## 1. Layer mapping

| Layer | Capability | Open-source components | Notes |
|-------|------------|------------------------|-------|
| **L0** Channels & UX | C0 | React / SvelteKit / Next.js; server-sent events; WebSocket | Channel adapter as a small Go / Node service in K8s. |
| **L1** Edge · Gateway · Identity | C1, C13 | **Envoy Gateway** or **Kong**, **Keycloak** (OIDC), **OPA** (edge authz), **istio-ratelimit** | Rate-limit via Envoy + Redis. |
| **L2** AI Orchestration | C2 | **LangGraph**, **Temporal**, **Prefect**, **CrewAI**, **AutoGen** | Workflow via Temporal; single-agent via LangGraph. |
| **L3** Prompt Intelligence | C3 | **Prompty**, **PromptLayer OSS**, **Git-based prompt registry** | Prompt Registry as a Git repo + K8s ConfigMap sync. |
| **L4** Memory & Context | C4 | **Redis** / **Dragonfly** (working/short), **PostgreSQL** (session/profile), **Weaviate** or **Qdrant** (semantic), **PostgreSQL + pgvector** (episodic) | Memory Manager as a Rust / Go service. |
| **L5** Knowledge & Retrieval | C5 | **OpenSearch** (BM25 + kNN), **Milvus** / **Qdrant** (vector), **Neo4j** or **Apache AGE** (graph), **DuckDB** / **Postgres** (structured), **Cohere OSS** or **bge-reranker** (reranker) | Ingestion via Airflow / Dagster. |
| **L6** Models & Model Router | C6 | **vLLM**, **TGI**, **Ollama**, **LiteLLM proxy** (routing), **NVIDIA Triton Inference Server** | Model Router = LiteLLM proxy in front of vLLM/TGI. |
| **L7** Tooling & Actions | C7 | **MCP** servers, **OpenAPI** adapters, **temporal-workflows** for tool orchestration | HITL via Slack bot or Backstage plugin. |
| **L8** Guardrails & Safety | C8 | **NVIDIA NeMo Guardrails**, **Guardrails AI**, **LLM Guard**, **Rebuff** (injection), **Presidio** (PII) | Layered: pre-context, pre-model, pre-tool, post-model. |
| **L9** Verification | C9 | **Ragas** (grounding, faithfulness), **DeepEval**, **UpTrain**, custom Python checkers | Verification Engine coordinates checkers. |
| **L10** Observability & Evaluation | C10 | **OpenTelemetry Collector**, **Prometheus**, **Grafana**, **Loki**, **Tempo**, **Jaeger**, **Langfuse** (agent/prompt traces) | Full OSS observability stack. |
| **L11** Performance · Caching · Cost | C11 | **Redis** (prompt/response), **GPTCache** (semantic), custom Cost Ledger on PostgreSQL | |
| **L12** LLMOps & Delivery | C12 | **GitHub Actions** / **GitLab CI**, **Argo CD**, **Argo Rollouts** (canary/blue-green), **Harbor** (registry), **OpenFeature** (flags) | GitOps flow with Argo. |
| **L13** Security & Zero Trust | C13 | **SPIFFE** / **SPIRE** (workload identity), **HashiCorp Vault** or **Infisical** (secrets), **cert-manager**, **Falco** (runtime security), **Kyverno** / **OPA Gatekeeper** (admission) | Zero-trust via SPIFFE + mTLS mesh. |
| **L14** Governance, Risk, Compliance | C14 | **OPA** (policy), **OpenLineage** + **Marquez** (lineage), **DataHub** (metadata) | Policy engine = OPA sidecars + central library. |
| **L15** Business Outcomes & Value | C15 | **Apache Superset**, **Metabase**, **Grafana** dashboards | KPI Registry as a Postgres schema. |

## 2. Trust boundary mapping ([Spec 009](../../specification/009-trust-boundaries.md))

| Boundary | Open-source realisation |
|----------|-------------------------|
| **TB-A** User → Gateway | Envoy Gateway with mTLS + Keycloak OIDC + OPA policy. |
| **TB-B** Reasoning → Model | Istio / Linkerd mTLS; SPIFFE identity between agent pod and model pod. |
| **TB-C** Reasoning → Tool | Envoy tool egress with per-tool policy; MCP servers in dedicated namespace; NetworkPolicy. |
| **TB-D** System → Data | PVC encryption via LUKS / CSI encryption; Vault-managed keys; OPA-enforced data-class labels. |

## 3. Reference deployment topology

Aligned to [D-D1](../../diagrams/deployment-topology.md). Helm charts + Kustomize overlays to live in [`../../reference-implementation/`](../../reference-implementation/) (planned).

## 4. Known gaps

- **Continuous evaluator (`K-L10-EVAL`)** — Langfuse + Ragas covers most of C10.6 but requires custom scheduling for on-trace evaluation.
- **Semantic cache (`K-L11-SC`)** — GPTCache is workable but not production-hardened; treat as v0.1 gap.

## 5. References

- [CNCF landscape](https://landscape.cncf.io/)
- [OpenTelemetry](https://opentelemetry.io/)
- [MCP specification](https://spec.modelcontextprotocol.io/)
- [NVIDIA NeMo Guardrails](https://github.com/NVIDIA/NeMo-Guardrails)
- [Langfuse](https://langfuse.com/)
