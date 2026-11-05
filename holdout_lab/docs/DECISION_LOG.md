# Holdout evaluation and product decision log

## Hypothesis
Holding the label set fixed, does more detailed review-policy guidance reduce harmful forced-fit errors without overloading human reviewers?

## Setup
- Model and configuration:
- Date:
- v3 prompt source: `challenge_lab/prompts/v3.md`
- v4 prompt source: `holdout_lab/prompts/v4.md`
- Source data: 36 synthetic holdout feedback records
- Did you view gold labels before predictions? (should be no):

## Results
| Metric | v3 | v4 |
|---|---:|---:|
| Overall accuracy | | |
| Non-review classification accuracy | | |
| Review recall | | |
| Review precision | | |
| Forced-fit errors | | |
| Unnecessary reviews | | |
| Invalid quotes / citations | | |

## Error review (write at least three)
| ID | Gold | Prediction | Why it went wrong | Suggested mitigation |
|---|---|---|---|---|
| | | | | |

## Manual semantic audit of insights
- Insight 1:
- Insight 2:
- Insight 3:

## Business/PM implications
- Which errors are more costly?
- What review workload would you accept, and why?
- Should an automated routing feature be released now? What would you need to prove?
- What prompt or product change do you recommend next? Why?

## Interview story in 90 seconds
Problem → baseline → policy decision → how evaluated → findings → limitations → next validation step.
