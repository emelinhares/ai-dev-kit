# SAFETY GUARDRAILS
Irreversible damage prevention:
1. NO MASS DELETION: Never execute `rm -rf` on root directories without explicit HUMAN_GRANT.
2. SECRETS: Never commit or log real passwords, tokens, or private keys.
3. DEPENDENCIES: Pause for human approval before installing new packages unless in AUTO mode.
