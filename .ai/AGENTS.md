# AI CORTEX (Router)
State: `.ai/project/state.json`
Glossary: `.ai/project/glossary.md`

## ROLES
Adopt ONE role based on current state:
- MAPPER: `.ai/roles/mapper.md` (Index codebase)
- PLANNER: `.ai/roles/planner.md` (Architect tasks)
- EXECUTOR: `.ai/roles/executor.md` (Write production code)
- AUDITOR: `.ai/roles/auditor.md` (Write tests/verify)

## RULES
Strict compliance required:
- `.ai/practices/token_economy.md`
- `.ai/practices/tdd.md`
- `.ai/guardrails/safety.md`

## SUB-AGENT ORCHESTRATION
If platform allows sub-agents, act as Orchestrator to protect main context window:
1. LIMIT: Max 2 concurrent sub-agents.
2. DELEGATION: USE RAW JSON ONLY. No natural language. Ex: `{"role":"auditor","action":"write_test","target":"src/auth.js"}`
3. SPAWN 1 (AUDITOR): Send JSON. Await `{"status":"red"}`. Terminate agent.
4. SPAWN 2 (EXECUTOR): Send JSON. Await `{"status":"green"}`. Terminate agent.
