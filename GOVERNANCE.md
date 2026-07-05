# EASRA Governance

EASRA is an open, vendor-neutral reference architecture. Its long-term value depends on trustworthy, transparent governance. This document describes how EASRA is maintained today (v0.x) and how governance will evolve as adoption grows.

## Mission

To define, publish, and steward a vendor-neutral reference architecture for Enterprise AI systems that is:

- **Rigorous** — architecturally sound, evidence-based, and reviewable.
- **Neutral** — independent of any cloud, model, framework, or company.
- **Open** — developed in public under permissive licenses.
- **Durable** — versioned, backwards-compatible where possible, with an explicit deprecation process.

## Roles

### Founder / Lead Maintainer
- **Karthikeyan Dhanakotti** ([@KarthikeyanDhanakotti](https://github.com/KarthikeyanDhanakotti))
- Sets the initial vision, releases v0.x and v1.0.
- Has final decision authority until the Technical Steering Committee (TSC) is formed.

### Maintainers
- Merge pull requests and triage issues.
- Approve ADRs (two maintainer approvals required).
- Nominated by existing maintainers based on sustained, high-quality contributions.
- Listed in [`MAINTAINERS.md`](./MAINTAINERS.md) (added when the first non-founder maintainer joins).

### Domain Reviewers
- Subject-matter experts for specific layers (e.g., Security L13, Verification L9, Knowledge L5).
- Provide non-binding technical reviews on PRs in their domain.
- Recognised in the chapter they steward.

### Contributors
- Anyone who opens an issue, comments on a discussion, or submits a PR.
- Retain copyright to their contributions (licensed under the repo's dual license).

### Technical Steering Committee (TSC) — *future*
- Will be established when EASRA has ≥ 5 active maintainers from ≥ 3 unrelated organisations.
- Will replace the Lead Maintainer as final authority on spec versions.
- Composition, voting, and terms will be defined in an ADR at that time.

## Decision-making

| Decision type | Mechanism | Threshold |
|---------------|-----------|-----------|
| Typo / formatting / broken link | Single maintainer merge | 1 approval |
| Clarification of existing spec text | Single maintainer merge | 1 approval |
| New handbook chapter or example | Maintainer review | 1 approval + 1 domain reviewer if available |
| Change to layer boundary, interface, principle, or trust boundary | ADR + 14-day public comment | 2 maintainer approvals |
| New specification (011+) | ADR + 30-day public comment | Lead Maintainer (or TSC when formed) |
| Version release (v1.0, v1.1, v2.0) | Release PR + changelog | Lead Maintainer (or TSC when formed) |
| License change | ADR + 60-day public comment + unanimous maintainer approval | All maintainers |
| Governance change | Update to this document via ADR | Same as license change |

## Public comment periods

- Comment periods run on the pull request thread.
- Silence is not consent — a comment period may be extended if fewer than 3 substantive comments were received.
- Maintainers must publicly acknowledge and respond to substantive objections before merging.

## Versioning

EASRA follows a variant of semantic versioning tailored to a specification:

- **Major (X.0.0)** — Breaking changes: layer renumbering, interface contract changes, removal of principles.
- **Minor (X.Y.0)** — Additive changes: new specifications, new interfaces, new handbook chapters, clarifications with no semantic impact on existing implementations.
- **Patch (X.Y.Z)** — Editorial: typos, formatting, non-substantive rewording, new examples.

The specification version is tracked in [`CHANGELOG.md`](./CHANGELOG.md) and in the `Version` header of each spec file.

## Neutrality safeguards

- No maintainer may hold decision authority for a spec section that names or benefits their employer as *the* recommended implementation.
- All vendor-specific content must appear in dedicated "Cloud Implementation" subsections and must cover ≥ 2 vendors or open-source alternatives.
- Sponsorship (if any) is disclosed in `SPONSORS.md` and does not confer decision authority.

## Conflict resolution

1. Raise the issue on the PR or open a discussion in `GitHub Discussions`.
2. If unresolved in 7 days, escalate to the Lead Maintainer.
3. If unresolved in 14 days, the Lead Maintainer (or TSC) issues a written decision on the thread.
4. Decisions are logged in an ADR when they set precedent.

## Code of Conduct

EASRA follows the [Contributor Covenant v2.1](https://www.contributor-covenant.org/version/2/1/code_of_conduct/). Violations may be reported privately to the Lead Maintainer.

## Contact

- General: open an issue or discussion on GitHub.
- Governance / conduct concerns: contact the Lead Maintainer via GitHub.

## Amendments

This document is amended via the same ADR + public comment process described above. All amendments are recorded in the changelog.
