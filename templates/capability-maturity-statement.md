# Capability Maturity Statement — <Adopter Name>

Adopters use this template to declare their per-capability maturity against the [EASRA Capability Model](../specification/011-capability-model.md). A published statement is a prerequisite for claiming EASRA conformance.

| Field | Value |
|-------|-------|
| Adopter | <TODO: organisation / team> |
| System name | <TODO: system / product> |
| Target EASRA version | v0.1.0 |
| Statement version | 0.1 |
| Assessment date | <YYYY-MM-DD> |
| Owner | <name, role> |

## Maturity scale ([Spec 011 §5](../specification/011-capability-model.md))

**M0** Absent · **M1** Ad hoc · **M2** Defined · **M3** Managed · **M4** Optimised

## Capability domains

| Capability | Current | Target | Owner | Evidence |
|------------|--------:|-------:|-------|----------|
| C0 Interact with Users |  |  |  |  |
| C1 Govern Ingress |  |  |  |  |
| C2 Orchestrate Reasoning |  |  |  |  |
| C3 Engineer Prompts |  |  |  |  |
| C4 Manage Memory |  |  |  |  |
| C5 Retrieve Knowledge |  |  |  |  |
| C6 Serve Models |  |  |  |  |
| C7 Execute Tools & Actions |  |  |  |  |
| C8 Enforce Safety & Guardrails |  |  |  |  |
| C9 Verify Outputs |  |  |  |  |
| C10 Observe & Evaluate |  |  |  |  |
| C11 Optimise Performance & Cost |  |  |  |  |
| C12 Deliver Safely (LLMOps) |  |  |  |  |
| C13 Secure the System |  |  |  |  |
| C14 Govern Risk & Compliance |  |  |  |  |
| C15 Deliver Business Value |  |  |  |  |

## Subcapability detail (optional, but recommended)

For each subcapability at maturity < M3, list evidence and closure plan.

| Subcapability | Current | Evidence | Closure plan | ETA |
|---------------|--------:|----------|--------------|-----|
| e.g. C4.5 Semantic memory | M1 | ad-hoc Redis + embeddings; no shared abstraction | wrap under `K-L4-MM` facade; add OTel tracing | Q<n> |

## Trust boundary declaration ([Spec 009](../specification/009-trust-boundaries.md))

| Boundary | Enforced? | Mechanism |
|----------|:---------:|-----------|
| TB-A User → Gateway | ☐ / ☑ |  |
| TB-B Reasoning → Model | ☐ / ☑ |  |
| TB-C Reasoning → Tool | ☐ / ☑ |  |
| TB-D System → Data | ☐ / ☑ |  |

## NFR declaration ([Spec 010](../specification/010-nfr.md))

| NFR | Committed? | Measured target |
|-----|:----------:|-----------------|
| N1 Availability | ☐ / ☑ |  |
| N2 Latency | ☐ / ☑ |  |
| N3 Throughput | ☐ / ☑ |  |
| N4 Cost | ☐ / ☑ |  |
| N5 Safety | ☐ / ☑ |  |
| N6 Verification quality | ☐ / ☑ |  |

## Standards attestation

- NIST AI RMF: covered ☐ / partial ☐ / N/A ☐
- ISO/IEC 42001: covered ☐ / partial ☐ / N/A ☐
- EU AI Act (High-Risk): covered ☐ / partial ☐ / N/A ☐
- OWASP LLM Top 10: mitigations documented ☐

## Sign-off

- Architecture: __________________________
- Security: __________________________
- Compliance: __________________________
- Product: __________________________

---

Publication: this statement SHOULD be published in the adopter's own repository, alongside the source of truth for their EASRA implementation. Link it from your project README.
