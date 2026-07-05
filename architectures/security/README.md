# Security Architecture

## Purpose

The **Security Architecture** describes *trust boundaries, threats, and controls* across the logical, runtime, deployment, and operational views. It is the architectural surface on which security policy, zero-trust enforcement, and compliance obligations operate.

Per [Design Principle P2](../../specification/002-design-principles.md), security is *architectural, not add-on*.

## Audience

- Security architects, threat modellers, red-teamers.
- Compliance officers and auditors.
- Any reviewer applying NIST AI RMF, ISO/IEC 42001, EU AI Act, OWASP LLM Top 10, or MITRE ATLAS.

## Scope

- Trust boundaries and trust planes.
- Zero-trust identity for every hop.
- Least-privilege authorisation and policy enforcement points.
- Guardrails and injection defence surfaces (input, prompt, tool-arg, output, indirect).
- PII detection, minimisation, and residency.
- Secrets, keys, and encryption topology.
- High-impact action gating and audit.
- Standards mapping and compliance evidence.

## Anchoring specifications

| Spec | Purpose |
|------|---------|
| [009 Trust Boundaries](../../specification/009-trust-boundaries.md) | TB-A / TB-B / TB-C / TB-D + trust planes. |
| [005 Layer Definitions §L8, §L13, §L14](../../specification/005-layer-definitions.md) | Guardrails, Zero-Trust, Governance. |
| [002 Design Principles §P2, §P7](../../specification/002-design-principles.md) | Security- and human-in-the-loop-by-design. |

## Diagrams

| ID | Title | Status |
|----|-------|--------|
| D-S1 | Trust Boundaries & Trust Planes | Done — [`../../diagrams/trust-boundaries.md`](../../diagrams/trust-boundaries.md) |
| D-S2 | Zero-Trust Identity Flow | Planned |
| D-S3 | Prompt-Injection Defence-in-Depth (Direct + Indirect) | Planned |
| D-S4 | Data Classification & Residency Flow | Planned |
| D-S5 | High-Impact Action Gate & Audit Trail | Planned |

## Change control

Boundary changes require an ADR and a companion update to [009 Trust Boundaries](../../specification/009-trust-boundaries.md). New standards mappings are additive and land in [Spec 014 Standards Mapping — planned](../../specification/).
