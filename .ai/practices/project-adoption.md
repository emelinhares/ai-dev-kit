# Adopting an Existing Project

Use this practice in `ADOPT_PROJECT` mode.

## 1. Intake and boundaries

Capture the product purpose, owner, users, desired outcome, known pain, allowed
environments, time/cost constraints, and access already available with the
[intake template](../templates/project-intake.md). Do not request credentials.

## 2. Observe before changing

Inspect repository structure, version control state, manifests, configuration
shape, entry points, tests, automation, deployment descriptors, and existing
docs. Treat docs as hypotheses to verify. Do not run unknown scripts or connect
to external/production systems merely to map them.

Create or refresh:

- the repository-owned [`glossary`](../project/glossary.md);
- the [project mapping](../templates/adoption/project-mapping.md);
- the [health report](../project/health-report.md);
- an [environment map](../templates/adoption/environment-map.md); and
- an [access map](../templates/adoption/access-map.md).

Record facts with evidence, interpretations as assumptions, and unknowns as
gaps. Prefer role/group identifiers over personal data.

## 3. Access safely

Start with observation access. Request the minimum level, scope, and duration
needed using the [access request template](../templates/adoption/access-request.md).
Development, limited-operation, release, and admin are separate grants. Never
record the issued credential.

## 4. Establish operability

Identify how maintainers safely validate, release, observe, rollback, restore,
and escalate. Create or update the human runbook using the
[operational runbook template](../templates/adoption/operational-runbook.md).
Unknown production procedures are a health risk, not an invitation to test them.

## 5. Reconcile and hand off

Resolve contradictions among code, configuration, observable behavior, docs,
and owner input. Put durable current truth in `docs/`, working status in
`.ai/project/`, and historical choices in ADRs. Propose prioritized next actions
with evidence, risk, and owner-visible impact.
