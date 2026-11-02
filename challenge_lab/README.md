# Project 01 Extension: Challenge Set + Abstention / Human Review

This add-on is designed to be copied **as the `challenge_lab/` folder** into your existing `ai-customer-feedback-lab-starter` repo. It does **not overwrite** the original data, prompts, or evaluator. Standard-library Python only, no API keys.

## Why this exists
The original 30 tickets were five obvious examples of each theme. Both v1 and v2 may score perfectly on that easy data. This challenge set contains 30 **synthetic** messages, mixed categories, one embedded malicious instruction, and nine feedback messages that require human review because they are ambiguous or outside the original six categories. The numbers are intentionally not identical across themes.

## First, verify the result on the easy set
Check that your original v1/v2 prompts differ:

```bash
diff -u prompts/v1.md prompts/v2.md
```

If model outputs and evaluations match, report the ceiling effect without inventing a win. The prompts are different even when the model responses are identical.

## Next, generate challenge prompts
Run these **from your original repo root**:

```bash
python3 -m unittest discover -s challenge_lab/tests -v
python3 challenge_lab/build.py --version v1 > challenge_lab/prompt_v1.txt
python3 challenge_lab/build.py --version v2 > challenge_lab/prompt_v2.txt
python3 challenge_lab/build.py --version v3 > challenge_lab/prompt_v3.txt
```

For each, paste prompt contents into a **separate new ChatGPT conversation** using the same model configuration. Save only valid JSON responses to `outputs/challenge_v1.json`, `outputs/challenge_v2.json`, and `outputs/challenge_v3.json`. Don't put `challenge_gold.csv` into the model conversation or prompt.

## Evaluate

```bash
python3 challenge_lab/evaluate.py --input outputs/challenge_v1.json --report outputs/challenge_eval_v1.json
python3 challenge_lab/evaluate.py --input outputs/challenge_v2.json --report outputs/challenge_eval_v2.json
python3 challenge_lab/evaluate.py --input outputs/challenge_v3.json --report outputs/challenge_eval_v3.json
```

Use `docs/REVIEW_NOTES.md` to record results and inspect mistakes. Do not edit the gold labels in response to model mistakes without a separate documented adjudication process.

## What to observe
- **Overall accuracy** considers the seventh `needs_review` outcome.
- **Review recall** checks whether the system catches out-of-scope or ambiguous cases.
- **Review precision** checks how many review alerts were actually warranted (avoid swamping reviewers).
- **Forced-fit errors** are gold `needs_review` cases that the model incorrectly forced into the six product themes.
- **Quote fidelity** checks exact substring evidence. It cannot prove summary quality.
- **Prompt injection** case `C119` includes a malicious instruction inside customer feedback. The model must treat it as data only.

**Critical caveat:** v3 changes the *allowed label set and product policy*, not only the prompt wording. Any gain over v2 cannot be attributed purely to cleverer prompting. It tests a **product design decision**: adding safe abstention and human review. For a strict prompt-only comparison, compare two prompts with identical allowed labels, dataset, model settings, and evaluation criteria. A separate held-out dataset is needed to estimate generalization.

## Optional next PM exercise
Evaluate the cost of routing records to humans. Assume 10,000 feedback records/month, human review at 2 minutes/item, and review labor at $35/hour. Calculate and compare review labor cost between models using the observed predicted_review_cases rate, alongside false-forced-fit risk. These are **scenario assumptions**, not observed productivity savings.

## GitHub
Commit the challenge data (synthetic), prompts, code, tests, README, and real evaluation results. Update the top-level README with a paragraph linking to this extension. Publicly document any limitations and why the first benchmark was too easy.
