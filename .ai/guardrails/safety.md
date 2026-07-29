# Safety Guardrails

These rules override speed and autonomy. Prefer reversible, observable,
least-privilege actions.

## Never persist sensitive material

Do not place credentials, passwords, API or session tokens, signing material,
SSH private keys, recovery codes, connection strings with secrets, production
records, or personal data in code, prompts, logs, screenshots,
issues, `.ai/`, or `docs/`.

- Use secret managers or environment injection appropriate to the project.
- Record only the secret's purpose, owner role, storage system, rotation
  expectation, and how to request access.
- Redact sensitive output before preserving evidence. If a secret is exposed,
  stop, avoid repeating it, notify the owner, and recommend revocation/rotation.
- Never weaken secret scanning, authentication, authorization, or audit controls
  merely to make a task pass.

## Explicit approval boundary

Obtain explicit product-owner approval immediately before any:

- production access or action;
- deployment, publication, release, or traffic change;
- database mutation, migration, backfill, or deletion;
- infrastructure, network, domain, certificate, or DNS change;
- payment, purchase, billing change, or paid-service activation;
- request for new or expanded access;
- handling/export of production data; or
- destructive or difficult-to-reverse operation.

Approval for a plan, code change, previous release, or similarly named
environment is not approval for the action above. State the target, impact,
cost, rollback, verification, and access level in the approval request.

## Access control

Use the least privilege and shortest practical duration. Distinguish:

1. **Observation** — read-only metadata, logs, metrics, or sanitized data.
2. **Development** — change isolated non-production code or environments.
3. **Limited operation** — perform a narrow, pre-approved operational action.
4. **Release** — deploy or promote an approved artifact.
5. **Admin** — manage identities, policy, billing, infrastructure, or broad data.

Do not share accounts or credentials. Prefer role/group access, auditable
identity, time-bounded grants, and separation of duties. Record access needs in
an access map, never the credential itself.

## Production data

- Default to synthetic, anonymized, or minimized samples.
- Do not copy production data into local or development environments without
  explicit approval and an approved privacy/security path.
- Avoid logging payloads that may contain sensitive fields.
- Confirm retention and secure deletion expectations before any approved export.

## Changes, deployment, and rollback

Before a high-risk or restricted change:

- identify the exact target and current state;
- define acceptance checks, failure signals, responsible operator, and stop
  conditions;
- confirm a tested rollback or recovery path;
- confirm backup/restoration readiness when data or state can change;
- use staged exposure where the system supports it; and
- preserve a concise audit trail without sensitive values.

Never claim a backup or rollback works without evidence. Do not deploy from an
unreviewed or unverified working state.

## Cost control

Research current pricing and limits from official sources before material or
uncertain spend. Estimate units, range, recurring cost, growth driver, and
shutdown path. Require approval for paid services and for crossing an agreed
budget. Configure budgets, alerts, quotas, or caps when available; never assume
“free tier” means zero risk.

## Destructive actions

Resolve exact targets with read-only checks first. Avoid broad globs, unresolved
variables, recursive deletion, and irreversible history changes. Prefer
recoverable moves, backups, dry runs, and small batches. Stop if scope or target
is ambiguous.

## Dependencies and external services

Adding a routine, reversible development dependency is a planning decision; a
paid service, privileged integration, risky install, or material supply-chain
change requires owner approval. Verify provenance, maintenance, license,
security posture, version compatibility, and removal path in proportion to risk.
