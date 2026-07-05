# EASRA Security Reference

The **Security Reference** is EASRA's authoritative catalogue of threats, controls, standards mappings, and reviewer materials for Enterprise AI systems. It is the working companion to the [Security Architecture view](../architectures/security/) and applies across every layer, capability, and deployment view.

Per [Design Principle P2](../specification/002-design-principles.md), security is architectural — not add-on.

## Scope

- **Threats** — a curated catalogue mapping OWASP LLM Top 10 and MITRE ATLAS to EASRA layers.
- **Controls** — a curated catalogue mapping preventive, detective, and responsive controls to layers and to components in [Spec 012](../specification/012-component-catalogue.md).
- **Standards mappings** — how EASRA satisfies NIST AI RMF, ISO/IEC 42001, EU AI Act (Article 15 / High-Risk AI), OWASP LLM Top 10, MITRE ATLAS.
- **Threat models** — per canonical workload (single-agent RAG, multi-agent, tool-use with HITL).
- **Red-teaming playbook** — reproducible adversarial exercises against EASRA-conformant systems.
- **Incident response** — signal → triage → mitigation → post-mortem loop for AI-specific incidents (prompt injection, data exfiltration via tool, model policy bypass, PII regression).

## 1. Threats catalogue (excerpt)

| Threat ID | Name | Source | Primary EASRA layer(s) | Primary control |
|-----------|------|--------|------------------------|-----------------|
| T-LLM01 | Prompt Injection (direct) | OWASP LLM01 | L8 | `K-L8-IG` + `K-L8-PG` |
| T-LLM01i | Prompt Injection (indirect via retrieval) | OWASP LLM01 | L5, L8 | `K-L8-IPI` + retrieval provenance |
| T-LLM02 | Insecure Output Handling | OWASP LLM02 | L8, L9 | `K-L8-OG` + `K-L9-FMT` |
| T-LLM03 | Training Data Poisoning | OWASP LLM03 | L5, L12 | Source Registry + signed ingestion |
| T-LLM04 | Model DoS | OWASP LLM04 | L1, L6 | `K-L1-RL` + `K-L6-FB` |
| T-LLM05 | Supply Chain | OWASP LLM05 | L6, L12 | Model Registry signing, SBOM |
| T-LLM06 | Sensitive Info Disclosure | OWASP LLM06 | L8, L13 | PII detection + policy verifier |
| T-LLM07 | Insecure Plugin | OWASP LLM07 | L7 | `K-L7-IMP` + Tool Registry |
| T-LLM08 | Excessive Agency | OWASP LLM08 | L2, L7 | Termination controller + impact-class gate |
| T-LLM09 | Overreliance | OWASP LLM09 | L9, L15 | Confidence scorer + HITL escalation |
| T-LLM10 | Model Theft | OWASP LLM10 | L6, L13 | Signed registry + rate-limit + audit |
| T-ATLAS-Rec | Reconnaissance | MITRE ATLAS | L1, L7 | Rate limit + audit |
| T-ATLAS-Ext | Model Extraction | MITRE ATLAS | L6 | Watermarking + query limits |
| T-ATLAS-Evade | Evasion (jailbreak) | MITRE ATLAS | L8 | Content Safety + custom classifiers |

## 2. Controls catalogue (excerpt)

| Control ID | Name | Type | Component | Standards |
|------------|------|------|-----------|-----------|
| CTL-EDGE-01 | mTLS at every hop | Preventive | `K-L1-GW`, mesh | ISO 42001 A.7.4 |
| CTL-IDENT-01 | Workload identity per service | Preventive | `K-L13-IAM` | NIST AI RMF Govern |
| CTL-PII-01 | Pre-context PII detection | Preventive | `K-L13-PII`, `K-L8-IG` | EU AI Act Art. 10 |
| CTL-INJ-01 | Prompt-shield on every model call | Preventive | `K-L8-PG` | OWASP LLM01 |
| CTL-INJ-02 | Indirect-injection scan on retrieved content | Preventive | `K-L8-IPI` | OWASP LLM01 |
| CTL-IMP-01 | Impact-class HITL gate on high-impact tools | Preventive | `K-L7-IMP` | EU AI Act Art. 14 |
| CTL-VER-01 | Grounding + citation verification | Detective | `K-L9-GRD`, `K-L9-CIT` | NIST AI RMF Measure |
| CTL-COST-01 | Per-request budget enforcement | Preventive | `K-L1-TBM`, `K-L11-LG` | NIST AI RMF Manage |
| CTL-AUD-01 | Append-only audit on high-impact events | Detective | `K-L13-AUD` | ISO 42001 A.9.2 |
| CTL-EVAL-01 | Continuous evaluation on production traces | Detective | `K-L10-EVAL` | NIST AI RMF Manage |

## 3. Standards mappings

| Standard | Mapping status | Notes |
|----------|----------------|-------|
| [NIST AI RMF 1.0](https://www.nist.gov/itl/ai-risk-management-framework) | Draft | Govern / Map / Measure / Manage → EASRA layers and controls. |
| [ISO/IEC 42001](https://www.iso.org/standard/81230.html) | Planned | AIMS controls → EASRA layers. |
| [EU AI Act](https://artificialintelligenceact.eu/) | Planned | Article 9–15 obligations → EASRA layers, particularly for High-Risk. |
| [OWASP LLM Top 10 (2025)](https://owasp.org/www-project-top-10-for-large-language-model-applications/) | Draft | Full mapping in §1 above. |
| [MITRE ATLAS](https://atlas.mitre.org/) | Draft | Techniques → EASRA controls. |

Full standards-mapping specification will land as **Spec 014** (planned).

## 4. Threat models

Per-workload STRIDE-style threat models will land as separate documents:

- `THREAT-MODEL-SARAG.md` — single-agent RAG (planned).
- `THREAT-MODEL-MAC.md` — multi-agent coordination (planned).
- `THREAT-MODEL-TOOL.md` — tool-use with HITL (planned).

## 5. Red-teaming playbook

Reproducible adversarial exercises with reference prompts, datasets, and scoring criteria — to land under [`../reference-implementation/red-team/`](../reference-implementation/) (planned).

## 6. Incident response

AI-specific incident classes (prompt injection, indirect injection, data exfiltration via tool, model policy bypass, PII regression, cost anomaly) with signal → triage → mitigation → post-mortem workflows.

## Related

- [Spec 002 — Design Principles (§P2, §P7)](../specification/002-design-principles.md)
- [Spec 009 — Trust Boundaries](../specification/009-trust-boundaries.md)
- [Architectures / Security](../architectures/security/)
- [Spec 011 — Capability Model (§C8, §C13, §C14)](../specification/011-capability-model.md)
- [Spec 012 — Component Catalogue (L8, L13, L14)](../specification/012-component-catalogue.md)
