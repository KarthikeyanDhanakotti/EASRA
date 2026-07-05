# Deployment Architecture

## Purpose

The **Deployment Architecture** describes *where each logical component runs* and *how it is scaled, isolated, and made resilient*. It maps the vendor-neutral logical model onto physical / cloud substrate patterns without picking a vendor.

## Audience

- Platform engineers and SREs designing the runtime substrate.
- Cloud architects producing per-cloud implementation guides.
- Reliability and DR reviewers.

## Scope

- Zonal, regional, and multi-region topology.
- Kubernetes / serverless / dedicated placement patterns per layer.
- Data-plane vs. control-plane separation.
- Traffic management (global LB, region failover, ingress).
- State placement (session, memory, cache, ledger, audit).
- Network segmentation (egress control, private endpoints).
- Multi-tenancy and blast-radius isolation.
- Disaster recovery and RPO / RTO commitments.

Out of scope: request execution flow (→ Runtime), monitoring (→ Operational), zero-trust controls (→ Security — but boundaries are shown here).

## Anchoring specifications

| Spec | Purpose |
|------|---------|
| [010 Non-Functional Requirements](../../specification/010-nfr.md) | Availability, DR, scale requirements. |
| [009 Trust Boundaries](../../specification/009-trust-boundaries.md) | Boundaries that constrain deployment topology. |

## Diagrams

| ID | Title | Status |
|----|-------|--------|
| D-D1 | Deployment Topology (single region) | Done — [`../../diagrams/deployment-topology.md`](../../diagrams/deployment-topology.md) |
| D-D2 | Multi-Region Active-Active Topology | Planned |
| D-D3 | Kubernetes Placement Map | Planned |
| D-D4 | State & Cache Placement | Planned |
| D-D5 | Disaster Recovery Topology | Planned |

## Change control

Any topology change that alters availability or DR commitments requires updating [010 NFRs](../../specification/010-nfr.md) and, if it moves a trust boundary, an ADR.
