# Research Log

This log stores concise decision evidence under the
[research policy](../policies/research.md). It is not a bookmark list or raw
content archive.

## 2026-07-28 — Safety, access, recovery, secrets, and cost controls

**Question:** Which official principles should constrain the kit's general
access, secret, recovery, and material-cost policies?  
**Decision informed:** Safety guardrails and adoption/release templates  
**Relevant version:** Technology-agnostic kit; cited source versions below  
**Recheck trigger:** A cited source is superseded, the policy becomes
technology-specific, or 2027-07-28

### Conclusion

Keep access limited to the capability needed for the task; manage secrets
outside repositories/logs with controlled lifecycle; govern risk and recovery
explicitly; and make material technology cost changes observable against
budgets/forecasts. These sources support the kit's general controls but do not
certify an adopted project's implementation.

### Official evidence

| Source | Version/date | Smallest useful fact |
| --- | --- | --- |
| [NIST SP 800-53 Rev. 5](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) | Official page accessed 2026-07-28 | AC-6 limits access to what assigned tasks require; CP-9 covers protected backups and restoration testing. |
| [OWASP Secrets Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html) | Living official project guidance accessed 2026-07-28 | Secrets need controlled storage, authorization, auditing, rotation/revocation, and must not be logged in plaintext. |
| [NIST Cybersecurity Framework 2.0](https://www.nist.gov/publications/nist-cybersecurity-framework-csf-20) | Published 2024; accessed 2026-07-28 | Cybersecurity outcomes include governance and the full identify/protect/detect/respond/recover lifecycle; implementations remain risk-based. |
| [FinOps Framework: Architecting and Workload Placement](https://www.finops.org/framework/capabilities/architecting-workload-placement/) | Living official framework accessed 2026-07-28 | Material technology choices should expose cost/usage impact, forecast variance, and budget/guardrail adherence. |

### Alternatives and contradictions

Vendor-specific controls were considered but rejected for the base kit because
they would not apply across adopted projects; they remain required research at
the project decision. Omitting general controls was outside the owner-approved
scope and contradicted the official evidence above. No contradiction among the
cited sources was found for this scoped conclusion.

### Confidence and uncertainty

**Confidence:** High for the general principles; not evidence that any specific
system, backup, role, price, or provider implements them.  
**Remaining uncertainty:** Each adopted repository must research its applicable
laws, vendor interfaces, service pricing/limits, and version-specific recovery
mechanisms before a material decision.

Add future entries newest first with the [research template](../templates/research.md).
