# L13 — Security & Zero Trust (cross-cutting)

| Field | Value |
|-------|-------|
| Layer | L13 |
| Depends on Specs | 002 (P2), 004, 009 |
| Status | Skeleton |

## 1. Purpose

L13 provides identity, secrets, encryption, PII detection, policy, and audit — as a *plane* attached to every layer.

## 2. Responsibilities

- **In scope.** Identity provider integration, Secrets manager, KMS, PII detector, Policy engine client, Audit log, Compliance controls.
- **Out of scope.** Guardrails (L8 consumes L13 capabilities).

## 3. Design principles

**P2 Security by Design**. Every trust boundary in [Spec 009](../specification/009-trust-boundaries.md) has named controls owned or provided by L13.

## 4. Patterns

- Zero trust: authenticate every request between layers.
- Short-lived signed service tokens; no long-lived credentials in compute.
- KMS-backed encryption of state at rest.
- Field-level tokenisation for Restricted-class data.
- Tamper-evident audit log with integrity verification.

## 5. Anti-patterns

- Long-lived, broadly scoped service credentials.
- Custom crypto.
- Audit logs mutable by application code.

## 6. Observability

Authn / authz events, secret access, PII detection events, policy decisions, audit-log integrity metrics.

## 7. Production checklist

- [ ] Every trust boundary has enforced controls.
- [ ] Secret rotation tested.
- [ ] Audit log integrity verified continuously.
- [ ] Incident response playbook current and drilled.
