# Checklist — Security Review

**Purpose.** Pre-production security review of an Enterprise AI system claiming EASRA conformance.

**When to use.** Before every production release. Whenever the model, prompt, tool, or policy set changes materially.

Every item cites the enforcing spec, capability, or component.

## Identity, authz, network ([Spec 009](../specification/009-trust-boundaries.md), [Spec 012 L1/L13](../specification/012-component-catalogue.md))

- [ ] Every hop authenticated via workload identity (`K-L13-IAM`); no shared secrets.
- [ ] Coarse authorisation at the edge (`K-L1-AZ`) + fine-grained at services (`K-L13-POL`).
- [ ] TB-A / TB-B / TB-C / TB-D all enforced with private endpoints or mesh mTLS.
- [ ] Rate limit + quota active per principal / tenant (`K-L1-RL`, `K-L1-QM`).

## Prompt-injection defence ([security-reference §1](../security-reference/README.md))

- [ ] Input guardrails on every request (`K-L8-IG`).
- [ ] Prompt guardrails before every model call (`K-L8-PG`).
- [ ] Indirect-injection scan on retrieved and tool-returned content (`K-L8-IPI`).
- [ ] Output guardrails before every response (`K-L8-OG`).
- [ ] Adversarial regression set exercised in CI.

## Tool safety ([Spec 011 §C7](../specification/011-capability-model.md))

- [ ] Every tool has an impact class (read / write / high-impact) recorded in the Tool Registry (`K-L7-TREG`).
- [ ] High-impact tools gated by `K-L7-IMP` with HITL.
- [ ] Tool-arg guardrails on every tool call (`K-L8-AG`).
- [ ] Per-tool rate limit + audit (`K-L7-TREG`, `K-L13-AUD`).

## Data protection ([Spec 011 §C13](../specification/011-capability-model.md))

- [ ] PII detected and minimised on ingress and egress (`K-L13-PII`).
- [ ] Residency policy enforced by `K-L9-POL`.
- [ ] Encryption in transit AND at rest with customer-managed keys (`K-L13-ENC`).
- [ ] Data lineage tracked (`K-L14-LIN`).

## Model integrity ([Spec 011 §C6](../specification/011-capability-model.md))

- [ ] Every model deployment signed and versioned in `K-L6-MRG`.
- [ ] Fallback path tested for every model (`K-L6-FB`).
- [ ] Model quota + rate-limit enforced.

## Verification signal ([Spec 011 §C9](../specification/011-capability-model.md))

- [ ] `K-L9-VE` runs on every response; verdict recorded.
- [ ] Confidence policy documented and reviewed (`K-L9-CS`).
- [ ] Escalation path (HITL) exists for `escalate` verdicts.
- [ ] Blocked responses generate audit events (`K-L13-AUD`).

## Standards mapping

- [ ] OWASP LLM Top 10 threats reviewed against [security-reference §1](../security-reference/README.md).
- [ ] MITRE ATLAS relevant techniques reviewed.
- [ ] NIST AI RMF Govern / Map / Measure / Manage entries covered.
- [ ] ISO/IEC 42001 AIMS controls entered (where certified).
- [ ] EU AI Act obligations reviewed (where High-Risk).

## Sign-off

- [ ] Security architect sign-off.
- [ ] Privacy / DPO sign-off (where PII in scope).
- [ ] Compliance sign-off (where regulated).
- [ ] Product owner sign-off.

## Related

- [Security Reference](../security-reference/README.md)
- [Spec 009 — Trust Boundaries](../specification/009-trust-boundaries.md)
- [Threat model template](../templates/threat-model.md)
