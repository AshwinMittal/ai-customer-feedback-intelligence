# Limitations, risk register, and future work

## Observed limitations

| Limitation | Why it matters | Planned mitigation, not yet implemented |
|---|---|---|
| Curated synthetic inputs | Inflated performance versus real customer diversity is possible | Privacy-approved representative data and out-of-sample evaluation |
| Small benchmark sizes | Perfect observed scores provide weak evidence of reliability under drift | More examples, repeated runs, segment-level reporting |
| Author-produced reference labels | Reviewer bias and category ambiguity remain unmeasured | Independent double labeling, disagreement resolution |
| Manual model runs | No fixed parameters, exact reproducibility, API latency, or token accounting | API-based inference with version and usage logging |
| Exact quote check is string-only | A valid substring may be used to justify an unsupported conclusion | Separate semantic/factual human review and structured evidence verification |
| No real review operations | Operational burden and SLA are unknown | Review queue, reasons, assignments, escalation, audits |
| No deployed app | No user experience data or adoption measurement | Prototype and usability testing only after core reliability gates |
| No conventional-tool baseline | Cannot demonstrate relative value or cost advantage | Comparative pilot with manual and non-LLM/vendor baselines |
| No security approval for real data | Real enterprise comments can contain secrets and PII | Security, privacy, procurement and legal review, tenant protections |
| Incomplete adversarial testing | One prompt injection example cannot establish security | Structured threat model and larger adversarial tests |

## Proposed next-step order

1. **Close learning project:** commit evidence, documented decisions, limitations, and interview answers. This is the current scope.
2. **Improve offline evaluation:** add realistic, independently labeled and multi-label examples; capture manual semantic audit of insight summaries.
3. **Design pilot economics:** estimate review hours and compare against a conventional rules or commercial tool baseline.
4. **Introduce a controlled API harness:** log model IDs, prompt version, usage, latency, costs, retries, and valid JSON schema rates.
5. **Develop a functioning product UI:** prioritized insight cards, expandable themes, source evidence, review queue, and critical alert override.
6. **Enterprise pilot only after approvals:** implement real privacy/security controls and monitor for data/label drift.

## Decision on a `SKILL.md`

Not required for Project 1. Prompt versions and deterministic scripts already describe its repeatable workflow. A formal `SKILL.md` becomes useful once a coding agent is expected to operate a repeatable procedure with defined inputs, outputs, test checks, and permissions. When that happens, document an explicit instruction sequence instead of turning the skill into a vague statement of general AI proficiency.
