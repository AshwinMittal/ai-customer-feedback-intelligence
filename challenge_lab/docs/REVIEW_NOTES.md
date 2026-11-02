# Challenge lab: Product manager review notes

## Baseline vs. change
| Run | Prompt | JSON valid? | Overall accuracy | Review recall | Forced-fit errors | Unsupported quotes | What changed? |
|---|---|---|---:|---:|---|---|---|
| 1 | v1 | | | | | | Six-category taxonomy, no review option |
| 2 | v2 | | | | | | Better guardrails but still six categories |
| 3 | v3 | | | | | | Adds an explicit review policy |

## Human review: five conclusions
For five *insights* (not only ticket classifications), write: insight summary, feedback_ids cited, whether source really supports the conclusion, and whether recommended next step is testable.

## Decisions and trade-offs
1. Why can forcing 100% categorization hurt customers?
2. What is the cost of sending too many records to a human reviewer?
3. Does a verbatim quote prove the overall summary? Why not?
4. What would change with multi-label classification?
5. What must be held constant to honestly say v3's *prompt alone* beat v2?

## Portfolio-ready writeup (fill with your *actual* run results)
- Problem and target persona:
- Product decision: add needs_review for ambiguous/out-of-taxonomy inputs.
- Baseline findings:
- After-change findings:
- Trade-offs / limits:
- Next experiments:

**Do not claim improvement, productivity savings, or customer value without actual run results.**
