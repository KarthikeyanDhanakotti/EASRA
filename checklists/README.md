# EASRA Checklists

Concrete, opinionated, reviewable checklists that turn EASRA's specifications into on-the-ground gates. Each checklist is a first-class artefact — versioned, referenceable, and improvable by PR.

## Available checklists

| Checklist | Purpose | Audience |
|-----------|---------|----------|
| [Repository Quality](./repository-quality.md) | The bar every repository in the EASRA ecosystem must meet. | Repo maintainers |
| [Adoption Assessment](./adoption-assessment.md) | Self-scored assessment before committing to EASRA. | Architects, sponsors |
| [Security Review](./security-review.md) | Pre-production security review of an Enterprise AI system. | Security architects, reviewers |
| [Verification Readiness](./verification-readiness.md) | Verification-layer readiness gate. | Evaluators, LLMOps |
| [LLMOps Readiness](./llmops-readiness.md) | Delivery, evaluation, cost, and incident-response gate. | LLMOps, SRE |
| [Standard Deliverables Status](./standard-deliverables-status.md) | Living status of EASRA's 10 pillars. | Maintainers |

## How to use a checklist

1. Copy the raw markdown into a PR (or an issue) in the target repository.
2. Convert each item to a checkbox.
3. Mark items as **Pass / Fail / N/A** with a one-line justification.
4. Attach the completed checklist to the release / review / audit artefact.

## Contributing a new checklist

- Open an ADR under [`../adr/`](../adr/) proposing the checklist.
- Follow the format used by the existing checklists (Purpose, When to use, Items with rationale, Scoring).
- Every item MUST cite the spec / capability / component it enforces.
