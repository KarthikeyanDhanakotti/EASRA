# L15 — Business Outcomes & Value (cross-cutting)

| Field | Value |
|-------|-------|
| Layer | L15 |
| Depends on Specs | 004, 005, 010 |
| Status | Skeleton |

## 1. Purpose

L15 connects AI outputs to business outcomes: KPIs, value attribution, cost/benefit, adoption.

## 2. Responsibilities

- **In scope.** KPI definitions, value attribution, cost/benefit modelling, product-analytics linkage.
- **Out of scope.** Model quality metrics (L10), verification verdicts (L9), governance status (L14).

## 3. Design principles

**P9 Cost Awareness** (value alongside cost), **P10 Evolvability** (KPIs as extension points).

## 4. Patterns

- Every KPI has an owner, a definition, and a data lineage.
- Cost from L11 attributed to KPIs from L15.
- Value attribution model reviewed quarterly.

## 5. Anti-patterns

- KPIs without owners.
- Value attribution to individual model calls (usually meaningless).
- Adoption metrics without engagement quality.

## 6. Observability

KPI values, cost/value ratios, adoption and retention (where applicable), value attribution reports.

## 7. Production checklist

- [ ] Each KPI has an owner, a definition, a data source.
- [ ] Cost attributable end-to-end.
- [ ] Value review cadence in place.
