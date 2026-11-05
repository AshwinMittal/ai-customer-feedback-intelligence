# Project 1, Lesson 4: Blind Holdout Evaluation and Prompt Ablation

## Objective
Your v3 prompt achieved 30/30 on the prior synthetic challenge. That result is **not** proof of production readiness. This exercise tests two prompts, **with the SAME seven-label taxonomy and output schema**, on a **new synthetic holdout set** containing 36 feedback examples. Some are ambiguous or out of scope, and one contains prompt injection as part of the source feedback.

## What changed compared with the previous lab?
- New, unseen-to-the-model input records (H201 through H236). The set is curated, not sampled from real production traffic.
- Holdout `gold/` labels are included for evaluation but must NOT be pasted into an LLM prompt or inspected before you save predictions.
- v3 is your existing detailed review policy, unchanged.
- v4 is a shorter **ablation** of the policy instructions with the **same** seven labels and same JSON schema. It may perform worse, better, or identically. The goal is learning, not winning.

## Install (macOS)
Extract this ZIP, then copy the entire `holdout_lab/` folder into the root of your `ai-customer-feedback-lab-starter` repository, next to the existing `challenge_lab/` directory. Use VS Code Terminal at the root.

```bash
python3 -m unittest discover -s holdout_lab/tests -v
python3 holdout_lab/build.py --version v3 > holdout_lab/prompt_v3.txt
python3 holdout_lab/build.py --version v4 > holdout_lab/prompt_v4.txt
```

Open each generated prompt and paste into a **fresh ChatGPT conversation**, choosing the same model/configuration for both. Save only the model's pure JSON response (no backtick fences) to `outputs/holdout_v3.json` and `outputs/holdout_v4.json`. **Do not paste or inspect `holdout_lab/data/holdout_gold.csv` until after both model outputs are saved.**

```bash
python3 holdout_lab/evaluate.py --input outputs/holdout_v3.json --report outputs/holdout_eval_v3.json
python3 holdout_lab/evaluate.py --input outputs/holdout_v4.json --report outputs/holdout_eval_v4.json
```

If you receive a JSON parsing error, check for Markdown fences, trailing commas, or incomplete output. Don't silently repair model mistakes without recording them.

## Questions to answer in docs/DECISION_LOG.md
1. What changed between challenge and holdout performance? If nothing changed, why might a 36-record synthetic holdout still be insufficient evidence?
2. Did the concise v4 policy lead to more forced-fit or unnecessary-review errors?
3. Which mistakes would most damage user trust? Consider wrong categorization vs. human-review workload.
4. On 10,000 real feedback records per month, what support-team burden would your observed review rate create? Treat it as a **scenario**, not a forecast (the benchmark intentionally over-samples edge cases).
5. Audit three theme insights and their cited feedback for **semantic** accuracy. A literal matching quote is necessary but not sufficient.
6. Did H220 follow the embedded hostile instruction or classify the actual issue?
7. What would you require before a production pilot? Dataset representativeness, independent gold-label adjudication, privacy controls, error thresholds, and ongoing monitoring.

## Important methodological notes
- This is a **prompt ablation**, not an online A/B test. Both prompts use the same taxonomy and schema. The main difference is policy specificity.
- Dataset is curated and small, not a random production sample. Perfect accuracy is possible and not predictive of real-world accuracy.
- Reference labels are author-assigned and can be disputed. In a real project, use an independently reviewed labeling protocol, track disagreements, and adjudicate them without looking at model predictions.
- `review_recall` measures catching gold review cases. `review_precision` indicates whether predicted review cases were justified. `non_review_classification_accuracy` is computed on records that the gold marks in-scope, NOT accuracy conditional on what the model chose to auto-classify. For production decisions, measure selective risk on actually auto-routed cases as well.
- Deterministic script checks only verify text structure/substring evidence. Manually review cited conclusions.
- Never publish private customer feedback. These examples are synthetic.

## Publish to GitHub
Keep the prior challenge results. Commit this `holdout_lab` folder and the two generated prompt outputs, model outputs, and evaluation reports. Add a brief `Project 1: Prompt evaluation` summary to the repository README that includes limitations.

# Optional Project 1 output-quality audit patch

Copy the contents of `holdout_lab/` into the matching folder of your existing Project 1 repo. The patch adds an extra audit script, test file, and guide; it does not replace your existing evaluator or prompt outputs.

Run the commands in `holdout_lab/docs/OUTPUT_AUDIT_GUIDE.md` from the repository root. Audit your results before describing them publicly.
