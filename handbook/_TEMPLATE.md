# Handbook Chapter Template

> Copy this file to `LNN-<slug>.md`, replace the placeholders, and open a PR. Skeleton chapters may be merged; each section should either have content or an explicit `TODO` referencing the tracking issue.

# LNN — Layer Name

| Field | Value |
|-------|-------|
| Layer | LNN |
| Depends on Specs | 001–010 |
| Status | Skeleton / Draft / Reviewed |
| Domain reviewer | *TBD* |

---

## 1. Purpose

*One paragraph on what this layer is responsible for.*

## 2. Problem statement

*What problem the layer solves and why it deserves its own layer.*

## 3. Why this layer exists

*Architectural justification. Reference the design principles from [Spec 002](../specification/002-design-principles.md).*

## 4. Responsibilities

- **In scope.** …
- **Out of scope.** …

## 5. Architecture

```mermaid
%% component diagram of this layer's internals
```

## 6. Components

### 6.1 …

## 7. Design principles

*Which of P1–P10 dominate here and why.*

## 8. Patterns

*Proven patterns with short descriptions.*

## 9. Anti-patterns

*What to avoid, with why.*

## 10. Design alternatives

*Options with trade-offs.*

## 11. Trade-offs

*Explicit choices and their justifications.*

## 12. Azure implementation

*Capabilities on Azure — never a single product presented as "the answer".*

## 13. AWS implementation

## 14. GCP implementation

## 15. Open-source implementation

## 16. Failure modes

| Failure | Degraded mode | Detection | Recovery |
|---------|---------------|-----------|----------|
| … | … | … | … |

## 17. Verification strategy

*How to test this layer (unit, contract, chaos, evaluation).*

## 18. Observability

*Required signals and dashboards; reference [Spec 006](../specification/006-interface-specification.md) telemetry contract.*

## 19. Performance

*Targets and how to measure them.*

## 20. Security

*Trust-boundary role and controls; reference [Spec 009](../specification/009-trust-boundaries.md).*

## 21. Production checklist

- [ ] …
- [ ] …
- [ ] …

## 22. References

- …
