# 2. Vendor-neutrality principle

- **Status:** Accepted
- **Date:** 2026-07-12
- **Deciders:** @KarthikeyanDhanakotti
- **Consulted:** External reviewer (Sprint-02)
- **Informed:** EASRA contributors

## Context and Problem Statement

EASRA describes an enterprise AI system. The temptation is to describe it in the language of whichever cloud, model provider, or framework is fashionable this quarter. That makes the document age faster than the industry it describes.

## Decision

**All canonical EASRA artifacts (EA-, RM-, PAT-, SPEC-, CHK-, ADR-) describe capabilities in vendor-neutral terms.** Cloud- and framework-specific realizations live only under `implementations/` (`IMPL-xxx`) and are explicitly labeled with the cloud, service, and version.

## Consequences

**Positive**
- The core standard survives across cloud shifts, model-provider shifts, and framework churn.
- Adopters can pick their stack and still map to EASRA without translation.
- Comparability across implementations becomes possible.

**Negative**
- Higher writing cost — must reason at the capability level, not the product level.
- Requires discipline to keep vendor names out of `EA-` / `PAT-` / `ADR-` pages.

## Follow-ups

- Add a lint rule for canonical artifacts that flags vendor product names.
- Every `IMPL-xxx` page must map back to a capability in the Capability Model.

## Related

- Reference Models: `reference-models/capability-model.md`
- Implementation policy: `implementations/README.md`
