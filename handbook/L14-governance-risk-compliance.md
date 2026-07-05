# L14 — Governance · Risk · Compliance (cross-cutting)

| Field | Value |
|-------|-------|
| Layer | L14 |
| Depends on Specs | 004, 005, 009 |
| Status | Skeleton |

## 1. Purpose

L14 owns the model registry, prompt registry, tool registry, policy engine, audit interface, and compliance mapping.

## 2. Responsibilities

- **In scope.** Model / Prompt / Tool Registries; Policy Engine; Audit; compliance mapping (NIST AI RMF, ISO/IEC 42001, EU AI Act, OWASP LLM Top 10, SOC 2, GDPR, HIPAA where applicable).
- **Out of scope.** Runtime enforcement (delegated to L8 / L9 / L7 / L13).

## 3. Design principles

**P10 Evolvability** (registries are extension points), **P7 Human-in-the-Loop** (approvals), **P2 Security** (policy as code).

## 4. Patterns

- Every model, prompt, tool, and policy is registered, versioned, approved.
- Policy engine evaluates action + context; returns allow / deny / require-approval + obligations.
- Compliance mapping tables generated from registries.

## 5. Anti-patterns

- Registries as spreadsheets, not APIs.
- Policies embedded in application code.
- Approvals over email without audit.

## 6. Observability

Registry changes, policy verdicts, compliance findings, approval throughput and latency.

## 7. Production checklist

- [ ] Every runtime artefact has a registry entry.
- [ ] Policy engine invoked at required points (L6, L7, L8, L9).
- [ ] Compliance dashboards up-to-date.
- [ ] Approval SLA measured.
