# TEST-DRIVEN DEVELOPMENT (SEGREGATION OF DUTIES)
Mandatory workflow to prevent AI confirmation bias:
1. PLAN: PLANNER defines business rules in `plan.md`.
2. RED: AUDITOR writes automated test. Must execute and confirm FAILURE (Exit > 0).
3. GREEN: EXECUTOR writes production code only. Must achieve PASS (Exit 0) against Auditor's test.
4. REFACTOR: EXECUTOR optimizes production code while keeping tests green.
*Abort if tests pass before production code is written.*
