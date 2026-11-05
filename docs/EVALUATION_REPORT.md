# Evaluation report and findings

**Data source:** synthetic sample datasets and user's submitted model-output/evaluator files. **Date of reconciliation:** November 4, 2026. This is offline evaluation, not a live product experiment.

## 1. Initial learning stage

The original 30-record dataset was deliberately simple. The user reported that original prompt v1 and v2 produced identical classifications on it. No saved original raw responses or independently measured quality delta were provided for this stage, so no quantitative improvement claim is made.

## 2. Challenging 30-record benchmark

| Measure | v1 | v2 | v3 |
|---|---:|---:|---:|
| Overall correctness | 20/30, 66.7% | 21/30, 70.0% | 30/30, 100% |
| Correct on in-scope records | 20/21, 95.2% | 21/21, 100% | 21/21, 100% |
| Gold `needs_review` records | 9 | 9 | 9 |
| Correctly flagged for review | 0/9 | 0/9 | 9/9 |
| Forced-fit review cases | 9 | 9 | 0 |

**Interpretation:** v1/v2 forced all nine review-worthy records into existing themes. v3 was permitted to use `needs_review`, improving routing for these examples. Because the taxonomy/policy changed between v2 and v3, this is a **product-policy improvement**, not an isolated proof that longer prompts outperform shorter prompts. Classification results alone do not validate summary relevance or business impact.

**Evidence:** user's three uploaded challenge evaluator reports. The full raw challenge responses were not submitted for independent semantic inspection.

## 3. Curated 36-record holdout, same taxonomy for v3 and v4

| Measure | Detailed v3 | Concise v4 |
|---|---:|---:|
| Overall correctness | 36/36, 100% | 36/36, 100% |
| In-scope correctness | 24/24, 100% | 24/24, 100% |
| Review-worthy cases flagged | 12/12 | 12/12 |
| Review precision / recall | 100% / 100% | 100% / 100% |
| Forced-fit errors | 0 | 0 |
| Exact quotes passing substring check | 35/36, 97.2% | 35/36, 97.2% |
| Insight count | 6 | 5 |
| Meets maximum 5 insights? | **No** | **Yes** |
| Six active themes summarized? | All 6 | 5 of 6 |
| Omitted summary theme | None | `mobile_accessibility` |
| Synthetic injection test H220 | Classified `integration_sync` | Classified `integration_sync` |

Both model responses used the same **seven-label** policy. The classification result is a tie on this one curated set. The longer prompt did not demonstrate better classification quality.

### What the classification evaluator missed

1. **H216 exact quote case mismatch.** Both model outputs used `what` where the source begins `What`. This is a case-sensitive verbatim evidence contract failure, not a meaningful hallucination of customer content.
2. **v3 output-count violation.** It produced six insight objects while the prompt requested no more than five.
3. **v4 omitted a theme from the insight summaries.** That is compatible with a five-insight limit but the model was not given a defensible ranking policy. `mobile_accessibility` appeared in classifications but not in the five insight summaries.
4. **Synthetic prompt injection:** H220 included an attempt to override instructions; both classified the record as integration-related. Passing one attack example does not show general prompt-injection resilience.

These findings were confirmed by running `holdout_lab/audit_outputs.py` against the user's actual uploaded JSON outputs. The original evaluator's check for citations and exact quotes does not determine if a whole summary is semantically supported.

## 4. Interpretation and external validity

- **Synthetic, curated samples:** The label mix and ambiguity were intentionally constructed. Real-world frequency and complexity are unknown.
- **Small sample:** 30 and 36 records are insufficient for a production-reliability claim. Perfect observed accuracy is not a guarantee of future performance.
- **Authored reference labels:** These were not independently double-labeled or adjudicated by a second reviewer.
- **Not a randomized A/B experiment:** These were offline prompt/policy comparisons. No live user assignment, causal impact estimate, or statistical significance test was performed.
- **Missing inference metadata:** The manual ChatGPT runs did not systematically capture model ID, temperature, token usage, latency, retries, or per-record cost.
- **No representative review cost:** 12/36 were routed to review because of the intentionally difficult dataset, not a measured production review rate.
- **Potential evaluation leakage:** Public gold labels support reproducibility but should never be included in the model's evaluation prompt. A more rigorous future holdout needs a separately authored unseen dataset and external labeling.
- **No verified commercial results:** We have not demonstrated time savings, support deflection, fewer tickets, or increased satisfaction.

## 5. Recommended quality gates for a future pilot

The following are **proposed**, not achieved:

1. Independently label a representative sample and measure label agreement; revise taxonomy definitions where reviewers disagree.
2. Add risk-weighted error analysis, including critical incident recall, false automated decisions, and escalation failure costs.
3. Enforce JSON schema and exact quote checks programmatically; use source indexing rather than free-form quote rewriting where possible.
4. Perform a manual review of summary claims, recommendation grounding, and prioritization rationales.
5. Run multiple inference repeats with a fixed model configuration and record model version, latency, tokens, and cost.
6. Define review capacity and escalation SLAs; add a rollback/fallback process for uncertain or high-severity cases.
7. Test against representative, privacy-approved enterprise feedback and monitor label drift after launch.

**Conclusion:** An AI-assisted feedback classification prototype was built and evaluated on curated synthetic inputs. Its demonstrated success is a **learning and workflow-design milestone**, not a verified production launch.
