# Runbooks

Runbooks are verified operational procedures, not architecture narratives or
release histories.

Each runbook must state purpose, accountable role/group, applicable
environment/version, required access level, last verification/review trigger,
preconditions, exact safe procedure, expected results, stop conditions,
verification, rollback/recovery, escalation, and closeout.

Use the [operational runbook template](../../.ai/templates/adoption/operational-runbook.md).
Do not invent technology-specific commands: an adopted project records only
commands and actions verified for that project. Unknown production procedures
remain explicit health gaps until an authorized owner validates them.

Never include credentials, private keys, tokens, production records, private
endpoints, or personal data. Link to approved access and secret
management processes by name.

This kit currently has no production system, so it ships no executable
environment runbook. The root [validation instructions](../../README.md#validate-the-kit)
cover its local structural check.
