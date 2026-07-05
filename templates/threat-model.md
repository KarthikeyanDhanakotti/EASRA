# Threat Model — <Workload Name>

Per-workload threat model referenced from the [EASRA Security Reference](../security-reference/README.md). Written in STRIDE + AI-specific extensions from OWASP LLM Top 10 and MITRE ATLAS.

| Field | Value |
|-------|-------|
| Workload ID | <e.g. W-SARAG, W-MAC, W-TOOL> |
| Target EASRA version | v0.1.0 |
| Author | <name, date> |
| Last reviewed | <YYYY-MM-DD> |

## 1. System description

*One paragraph: what the workload does, which capabilities it exercises (C0..C15), which components it uses (`K-L*-*`), and which trust boundaries it crosses.*

## 2. Data flow (in scope)

*Reference a diagram or embed a Mermaid sequence — clearly showing every trust boundary crossing.*

## 3. Assets

| Asset | Sensitivity | Location |
|-------|-------------|----------|
| e.g. user prompts | Confidential | `K-L1-GW` → agent memory |
| e.g. retrieved documents | Internal | `K-L5-*` |
| e.g. tool credentials | Secret | `K-L13-KV` |

## 4. Threats

For each threat: **ID · Name · STRIDE / OWASP mapping · Attack vector · Impact · Likelihood · Mitigations · Residual risk**.

| ID | Threat | Mapping | Vector | Impact | Likelihood | Mitigations (control IDs) | Residual |
|----|--------|---------|--------|--------|:---------:|---------------------------|----------|
| T-01 | Direct prompt injection | OWASP LLM01 | Malicious user prompt | Data exfiltration | Med | CTL-INJ-01 (`K-L8-PG`), CTL-AUD-01 | Low |
| T-02 | Indirect injection via retrieval | OWASP LLM01 | Poisoned document | Policy bypass | Med | CTL-INJ-02 (`K-L8-IPI`), source-signing | Low |
| T-03 | Excessive agency via tool | OWASP LLM08 | Model calls high-impact tool without gate | Financial loss | Low | CTL-IMP-01 (`K-L7-IMP`), HITL | Very low |
| T-04 | PII leak in response | OWASP LLM06 | Model regurgitates training data | Regulatory | Med | `K-L13-PII` + `K-L9-POL` + `K-L8-OG` | Low |
| T-05 | Model DoS / cost exhaustion | OWASP LLM04 | Adversarial prompt inflates tokens | Cost anomaly | Med | `K-L1-TBM` + `K-L1-RL` + `K-L11-LG` | Low |
| T-06 | Data exfiltration via tool | ATLAS | Tool used to read + write sensitive data | Data loss | Low | `K-L7-IMP` + `K-L8-AG` + `K-L13-AUD` | Very low |
| T-07 | Confused deputy in workflow | ATLAS | Agent impersonates a downstream service | Priv escalation | Low | Workload identity per hop (`K-L13-IAM`) | Very low |

## 5. Assumptions

- <e.g. "Users are authenticated via corporate SSO with MFA.">
- <e.g. "Retrieved documents originate only from `K-L5-SRC` entries.">

## 6. Out of scope

- <e.g. supply-chain attacks on the base image (covered elsewhere).>

## 7. Open questions

- <List>

## 8. Review

| Reviewer | Role | Date | Verdict |
|----------|------|------|---------|
|  |  |  |  |
