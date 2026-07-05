# EASRA Handbook

The **Handbook** turns the specification into an engineering guide. Where the specification says *what* the architecture is, the handbook says *how* to build, operate, and evolve each layer.

The handbook is organised by layer. Every chapter follows the same template so that architects and engineers know exactly where to look.

## Chapter template

Every chapter contains the following sections, in this order:

1. **Purpose** — one paragraph.
2. **Problem statement** — what problem this layer solves.
3. **Why this layer exists** — the architectural justification.
4. **Responsibilities** — what belongs (and what does not).
5. **Architecture** — internal architecture with component diagram.
6. **Components** — one subsection per named component.
7. **Design principles** — which of P1–P10 dominate here.
8. **Patterns** — proven design patterns.
9. **Anti-patterns** — what to avoid, with why.
10. **Design alternatives** — options with trade-offs.
11. **Trade-offs** — the explicit choices.
12. **Azure implementation** — capabilities on Azure (never products alone).
13. **AWS implementation** — capabilities on AWS.
14. **GCP implementation** — capabilities on GCP.
15. **Open-source implementation** — capabilities via OSS.
16. **Failure modes** — how it fails and what degraded mode looks like.
17. **Verification strategy** — how to test.
18. **Observability** — required signals and dashboards.
19. **Performance** — targets and how to measure.
20. **Security** — trust-boundary role and controls.
21. **Production checklist** — the actionable list.
22. **References** — standards, papers, prior art.

## Contents

| # | Chapter | Status |
|---|---------|--------|
| L00 | [Channels & User Experience](./L00-channels-and-user-experience.md) | Skeleton |
| L01 | [Edge · Gateway · Identity](./L01-edge-gateway-identity.md) | Skeleton |
| L02 | [AI Orchestration](./L02-ai-orchestration.md) | Skeleton |
| L03 | [Prompt Intelligence](./L03-prompt-intelligence.md) | Skeleton |
| L04 | [Memory & Context](./L04-memory-and-context.md) | Skeleton |
| L05 | [Knowledge & Retrieval](./L05-knowledge-and-retrieval.md) | Skeleton |
| L06 | [AI Models & Model Router](./L06-ai-models-and-model-router.md) | Skeleton |
| L07 | [Tooling & Actions (MCP)](./L07-tooling-and-actions.md) | Skeleton |
| L08 | [Guardrails & Safety](./L08-guardrails-and-safety.md) | Skeleton |
| L09 | [Verification](./L09-verification.md) | Skeleton |
| L10 | [Observability & Evaluation](./L10-observability-and-evaluation.md) | Skeleton |
| L11 | [Performance · Caching · Cost](./L11-performance-caching-cost.md) | Skeleton |
| L12 | [LLMOps & Delivery](./L12-llmops-and-delivery.md) | Skeleton |
| L13 | [Security & Zero Trust](./L13-security-and-zero-trust.md) | Skeleton |
| L14 | [Governance · Risk · Compliance](./L14-governance-risk-compliance.md) | Skeleton |
| L15 | [Business Outcomes & Value](./L15-business-outcomes-and-value.md) | Skeleton |

## Cross-cutting handbook chapters (planned)

- Cost Engineering
- Multi-Region & Disaster Recovery
- Responsible AI

## Contributing

Chapters are the highest-leverage contribution to EASRA. Pick a chapter, follow the template, and open a PR. See [`../CONTRIBUTING.md`](../CONTRIBUTING.md).
