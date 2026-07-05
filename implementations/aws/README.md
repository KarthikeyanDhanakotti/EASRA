# EASRA on Amazon Web Services

Vendor-specific mapping of the EASRA architecture to AWS services. This guide realises every EASRA layer and component ([Spec 012](../../specification/012-component-catalogue.md)) on AWS without changing the architecture.

| Field | Value |
|-------|-------|
| Status | Draft |
| Target EASRA version | v0.1.0 |
| Last updated | 2026-07-05 |

## 1. Layer mapping

| Layer | Capability | AWS services | Notes |
|-------|------------|--------------|-------|
| **L0** Channels & UX | C0 | CloudFront, Amazon API Gateway (public), Amazon Connect | Channel adapter on ECS Fargate or Lambda. |
| **L1** Edge · Gateway · Identity | C1, C13 | CloudFront + AWS WAF, **Amazon API Gateway** (REST/HTTP), **Amazon Cognito** or IAM Identity Center, API Gateway usage plans | Rate limit + quota via API Gateway usage plans; auth via Cognito authoriser. |
| **L2** AI Orchestration | C2 | **AWS Fargate on ECS**, **AWS Step Functions** (workflow), **Amazon Bedrock Agents**, LangGraph on Fargate | Termination via Step Functions state limits. |
| **L3** Prompt Intelligence | C3 | **AWS AppConfig** (registry), **AWS Secrets Manager**, **Amazon SageMaker Pipelines** (prompt testing) | Prompt Registry as AppConfig hosted configuration. |
| **L4** Memory & Context | C4 | **ElastiCache for Redis** (working/short), **Amazon DynamoDB** (session/profile), **Amazon OpenSearch** (semantic), **Amazon Aurora PostgreSQL** with `pgvector` (episodic) | Memory Manager as ECS service. |
| **L5** Knowledge & Retrieval | C5 | **Amazon OpenSearch Service** (hybrid), **Amazon Neptune** (graph), **AWS Glue** + **Athena** (structured), Amazon Bedrock Reranker | Ingestion via Glue + Lambda + S3. |
| **L6** Models & Model Router | C6 | **Amazon Bedrock**, **Amazon SageMaker JumpStart**, **SageMaker endpoints** | Model Router as ECS service with Bedrock + SageMaker fallback. |
| **L7** Tooling & Actions | C7 | **API Gateway** (adapter), **AWS Step Functions** (workflow tools), MCP servers on Fargate | HITL via SES + Step Functions Wait-for-Callback. |
| **L8** Guardrails & Safety | C8 | **Amazon Bedrock Guardrails**, **Amazon Comprehend** (PII), custom classifiers on SageMaker | Prompt shielding via Bedrock Guardrails. |
| **L9** Verification | C9 | **Amazon Bedrock Evaluations**, **Amazon SageMaker Clarify**, custom checkers on Fargate | Verification Engine coordinates checkers. |
| **L10** Observability & Evaluation | C10 | **Amazon CloudWatch** (metrics, logs), **AWS X-Ray** (traces), **Amazon Managed Grafana**, **CloudWatch Application Signals** | OTLP → ADOT collector on EKS/ECS. |
| **L11** Performance · Caching · Cost | C11 | **ElastiCache for Redis**, **AWS Cost Explorer** + custom Cost Ledger on DynamoDB | |
| **L12** LLMOps & Delivery | C12 | **GitHub Actions** / **CodePipeline**, **Amazon ECR**, **SageMaker Pipelines**, **AWS AppConfig feature flags** | Canary via CodeDeploy or App Mesh. |
| **L13** Security & Zero Trust | C13 | **IAM** + **IAM Roles Anywhere**, **AWS Secrets Manager**, **KMS**, **Amazon Macie** (PII), **AWS Security Hub**, **PrivateLink** everywhere | Every workload uses IAM role; no long-lived credentials. |
| **L14** Governance, Risk, Compliance | C14 | **AWS Config**, **AWS Audit Manager**, **AWS Control Tower**, **AWS CloudTrail** | Policy engine as AWS Config rules + custom Fargate service. |
| **L15** Business Outcomes & Value | C15 | **Amazon QuickSight**, CloudWatch KPI dashboards | KPI Registry via QuickSight dataset. |

## 2. Trust boundary mapping ([Spec 009](../../specification/009-trust-boundaries.md))

| Boundary | AWS realisation |
|----------|-----------------|
| **TB-A** User → Gateway | CloudFront + WAF → API Gateway (private endpoint via VPC endpoint). |
| **TB-B** Reasoning → Model | Fargate → Bedrock via VPC endpoint (PrivateLink). IAM role per service. |
| **TB-C** Reasoning → Tool | API Gateway tool adapter; MCP servers on isolated Fargate cluster; security groups + NACLs. |
| **TB-D** System → Data | DynamoDB / OpenSearch / S3 via VPC endpoints; KMS customer-managed keys; Macie classification. |

## 3. NFR mapping ([Spec 010](../../specification/010-nfr.md))

| NFR | AWS realisation |
|-----|-----------------|
| N1 Availability | Multi-AZ Fargate, DynamoDB global tables, Bedrock cross-region inference. |
| N2 Latency | CloudFront geo-routing + regional Bedrock endpoints, Redis in-region. |
| N3 Throughput | API Gateway throttling, Fargate autoscaling, Bedrock provisioned throughput. |
| N4 Cost | Cost Explorer + Cost Ledger on DynamoDB. |
| N5 Safety | Bedrock Guardrails + Comprehend PII + Macie. |
| N12 CI/CD | GitHub Actions / CodePipeline + ECR + SageMaker Pipelines. |

## 4. Reference deployment topology

Aligned to [D-D1](../../diagrams/deployment-topology.md). CDK / Terraform scaffolding to live in [`../../reference-implementation/`](../../reference-implementation/) (planned).

## 5. Known gaps

- **Semantic cache (`K-L11-SC`)** — no native AWS semantic-cache primitive; implement on ElastiCache + `pgvector` or use Bedrock Prompt Caching where available.
- **Workflow Engine (`K-L2-WF`)** — Step Functions covers the pattern but lacks native prompt/eval integration.

## 6. References

- [Amazon Bedrock documentation](https://docs.aws.amazon.com/bedrock/)
- [Amazon Bedrock Guardrails](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html)
- [AWS Well-Architected Framework — Generative AI Lens](https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/)
