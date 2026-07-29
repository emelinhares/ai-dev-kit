# Task-Sensitive Testing and TDD

Testing must match the task and risk. TDD is a strong default for observable
behavior, not a ritual for every file.

| Task | Expected approach |
| --- | --- |
| New or changed business behavior | Write an acceptance example, then red → green → refactor at a stable seam |
| Bug fix | Reproduce with a failing test or deterministic check before the fix |
| Refactor | Establish characterization tests first; behavior should remain stable |
| Integration or external API | Test the owned contract; use sandbox/fakes where appropriate and a bounded integration check |
| Data migration | Test forward behavior, representative data, invariants, and rollback/recovery |
| Security-sensitive change | Add abuse/negative cases and independent review |
| UI/experience change | Combine behavior checks with focused human/visual/accessibility review |
| Documentation/configuration only | Validate structure, links, parsing, or a safe dry run; a synthetic failing test may add no value |
| Exploration/prototype | Time-box learning; do not misrepresent prototype evidence as production verification |

## Red–green–refactor

1. State the behavior and why the test would fail before the change.
2. Run the narrow check and confirm failure for the expected reason.
3. Make the smallest complete change that satisfies the behavior.
4. Run the narrow check, relevant neighboring checks, then broader validation in
   proportion to risk.
5. Refactor while keeping checks green.

If the proposed red test passes, determine whether behavior already exists, the
test is invalid, or the seam is wrong. Do not manufacture a failure.

The executor may update tests when tests are part of the intended behavior
change. For medium/high-risk work, an auditor should independently challenge
coverage and evidence. Never weaken a valid assertion merely to obtain green.
