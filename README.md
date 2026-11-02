# AI Customer Feedback Intelligence | PM Portfolio Project 01

> Independent learning prototype for PM interviews using **synthetic data**. No proprietary customer information. No production, revenue, or efficiency claims.

## Business problem
An imaginary B2B support SaaS PM needs a repeatable, explainable way to group product feedback and identify actionable opportunities.

## What this repo demonstrates
- Product framing and MVP decisions
- LLM prompt design and version comparisons
- Human-labeled reference data (gold labels)
- Offline evaluation of classification and evidence fidelity
- Human review and explicit limitations

## Tools
Python 3.11+ (standard library only), ChatGPT (manual prompt run), VS Code (optional), Git/GitHub. No OpenAI API key or paid packages needed.

## Quick start

```bash
python --version
python -m unittest discover -s tests -v
python src/build_prompt.py --version v1 > generated_prompt_v1.txt
```

1. Open `generated_prompt_v1.txt` and paste its entire contents into **a new ChatGPT conversation**.
2. Copy the assistant's plain JSON response, without ``` fences, into `outputs/run_01.json`.
3. Evaluate using:

```bash
python src/evaluate.py --input outputs/run_01.json --report outputs/eval_01.json
```

4. Read the errors in the report. Compare against `data/gold_labels.csv` (do **not** paste the labels into the classification prompt).
5. Run `python src/build_prompt.py --version v2 > generated_prompt_v2.txt`, repeat in a new ChatGPT conversation, save `outputs/run_02.json`, evaluate and compare.
6. Read `docs/LEARNING_LOG.md` and document what changed, what the evaluation measured, and what it could **not** detect.

On macOS or Linux, use `python3` instead of `python` if needed.

## Repo guide
- `data/feedback.csv`: 30 synthetic customer comments.
- `data/gold_labels.csv`: manual reference classifications. Keep separate from model input.
- `data/TAXONOMY.md`: valid labels and scope.
- `prompts/v1.md`, `prompts/v2.md`: baseline and evidence-first prompt versions.
- `src/build_prompt.py`: construct a complete copy/paste prompt.
- `src/evaluate.py`: deterministic validation and scoring.
- `tests/`: basic evaluator tests.
- `docs/PRODUCT_BRIEF.md`: PM problem, scope, success measures, trade-offs.
- `docs/LEARNING_LOG.md`: decision and learning log.
- `docs/INTERVIEW_STORY.md`: honest portfolio story template.

## Evaluation caveat
An exact quote provides mechanical traceability, not proof that a recommendation is semantically supported. A balanced synthetic dataset is not a production test set. Human interpretation and a separate realism check are necessary.

## Next improvements (intentionally not implemented in v1)
- Additional independent reviewer labels and disagreement analysis.
- Multi-label classification and review queues.
- AI run repeatability and latency/cost measurement via an API.
- User-facing dashboard (Streamlit or simple HTML).
- Deployment and governance design for real customer data.

## GitHub publication
This repository is safe to publish because it contains synthetic examples. Do not push confidential employer/customer records, private API keys, `.env`, or real interview transcripts. See the companion workshop instructions in ChatGPT for `git` and `gh` commands.
