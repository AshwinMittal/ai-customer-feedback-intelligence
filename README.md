# AI Customer Feedback Intelligence

**Project 01 | Independent AI Product Management Portfolio | Synthetic data**

> **Status:** Learning prototype and offline evaluation completed. Not deployed, not tested on real customer data, and not production-ready. The proposed insights dashboard and operational review queue are product designs, not implemented software.

## The problem

Product teams receive feedback from support tickets, interviews, and customer-success channels but struggle to turn raw comments into consistently categorized, evidence-backed product insights. Manual analysis is time-consuming and can be inconsistent. A language model might help, but a persuasive summary does not guarantee a reliable classification or trustworthy evidence.

## The solution explored

An offline, human-in-the-loop feedback analysis prototype that:

1. Sends **synthetic** customer feedback through a manually operated LLM prompt workflow.
2. Classifies comments into six defined product themes, with an explicit `needs_review` option for ambiguous or out-of-scope feedback.
3. Requests source quotes and feedback IDs for traceability.
4. Compares outputs against authored reference labels, then audits evidence and insight-output contracts separately.
5. Recommends a **proposed** UX: show five prioritized insights, let users expand to additional themes, and maintain a distinct review/exception workflow.

## What I contributed and learned

As an independent portfolio exercise, I defined the problem and success criteria, compared prompt and policy options, executed the manual ChatGPT runs, evaluated outputs with Python, analyzed failure cases, and made a product design decision to balance usability with full theme access. The starter scripts and sample data were AI-assisted learning materials. This is an **independent prototype**, not a production AI program at a prior employer.

## Results at a glance

| Evaluation | Version | Correct classifications | Review recall | Other findings |
|---|---|---:|---:|---|
| Challenge, 30 synthetic records | v1 | 20/30 (66.7%) | 0/9 | Nine forced-fit review errors |
| Challenge, 30 synthetic records | v2 | 21/30 (70.0%) | 0/9 | Nine forced-fit review errors |
| Challenge, 30 synthetic records | v3 | 30/30 (100%) | 9/9 | Added explicit `needs_review` policy |
| Curated holdout, 36 synthetic records | v3 | 36/36 (100%) | 12/12 | 1 invalid exact quote; 6 insights exceeded limit of 5 |
| Curated holdout, 36 synthetic records | v4 | 36/36 (100%) | 12/12 | 1 invalid exact quote; 5 insights omitted one active theme |

**Key interpretation:** v3 on the challenge altered the allowed category policy as well as prompt text, so its improvement is **not evidence of prompt engineering alone**. On a separate curated holdout, v3 and v4 used the same seven-label taxonomy and achieved identical classification accuracy. Neither holdout run fully complied with every output requirement. The 36-item data set is synthetic, small, and author-labeled; no deployment-readiness or commercial-benefit claim follows from these numbers.

## Architecture

```text
Synthetic CSV feedback -> prompt builder -> manual ChatGPT run -> JSON result
                                                     |
                                 +-------------------+-------------------+
                                 |                                       |
                        Classification evaluator                  Output QA audit
                        (reference labels, IDs)                  (quotes, count, coverage)
                                 |                                       |
                                 +-------------------+-------------------+
                                                     |
                                   PM interpretation and decision log
                                                     |
                             Proposed insight UI + human review process
                             (designed, not implemented)
```

[Architecture and workflow](docs/ARCHITECTURE.md) | [Evaluation report](docs/EVALUATION_REPORT.md) | [Product decisions](docs/PRODUCT_DECISIONS.md) | [Case study](docs/CASE_STUDY.md) | [Interview Q&A](docs/INTERVIEW_QA.md) | [Limitations](docs/LIMITATIONS_AND_NEXT_STEPS.md) | [GitHub publication guide for macOS](docs/GIT_PUBLISHING_MAC.md)

## Repository map

```text
data/                 Original 30-record synthetic benchmark, reference labels, taxonomy
prompts/              Initial prompt versions
src/                  Initial prompt builder and evaluator
challenge_lab/        Difficult-case dataset, review category, prompt v3, evaluator
holdout_lab/          36-record holdout, concise prompt v4, audit script and tests
outputs/              User-generated model responses, evaluator reports and quality audit
tests/                Evaluator unit tests
docs/                 Product brief, decisions, evaluation, case study and interview prep
```

## Quick start on macOS

From this repository root:

```bash
python3 --version
python3 -m unittest discover -s tests -v
python3 -m unittest discover -s challenge_lab/tests -v
python3 -m unittest discover -s holdout_lab/tests -v

python3 holdout_lab/evaluate.py --input outputs/holdout_v3.json --report outputs/holdout_eval_v3.json
python3 holdout_lab/evaluate.py --input outputs/holdout_v4.json --report outputs/holdout_eval_v4.json

python3 holdout_lab/audit_outputs.py \
  --feedback holdout_lab/data/holdout_feedback.csv \
  --v3 outputs/holdout_v3.json \
  --v4 outputs/holdout_v4.json \
  --out outputs/holdout_quality_audit.json
```

The commands assume the holdout raw response files already exist in `outputs/`. If not, see `holdout_lab/README.md` to generate and save them. Running an evaluator does **not** call an LLM; it scores saved outputs. No API key or paid model access is needed for these tests.

## Privacy and reproducibility

All project data is synthetic. Reference labels were kept out of the submitted classification prompts, but are part of the public repo so evaluation can be reproduced. Do not upload real client data, credentials, private employer records, or model conversations containing confidential material.

Manual ChatGPT runs are **not fully reproducible** because the model configuration, response variability, latency, and token costs were not recorded via an API. Future work should capture those variables and use more representative, independently labeled feedback.

## What this project does not demonstrate

It does not demonstrate shipped AI products, production ML systems, a deployed feedback dashboard, real customer productivity savings, enterprise security approvals, live online A/B tests, or reliability under real-world data drift.

## Publishing

If you have already initialized Git and made the first commit, **do not reinitialize Git**. Follow [the macOS Git instructions](docs/GIT_PUBLISHING_MAC.md) to review, stage, commit, and push the new work.
