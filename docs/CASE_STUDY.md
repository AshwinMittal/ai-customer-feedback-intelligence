# Portfolio case study | AI Customer Feedback Intelligence

**Type:** Independent, offline AI PM learning prototype using synthetic feedback. **Role:** Product owner and evaluator in a guided, AI-assisted learning project. **Production deployment:** None.

## Opportunity

Teams using B2B support software receive feedback across support and customer-success channels. A product manager must identify recurring friction without discarding unusual, emerging, or high-risk customer issues. Naive forced-choice classification can produce neat dashboards while silently misrouting feedback that does not match existing labels.

## Hypothesis

A simple LLM-assisted classification workflow could produce evidence-linked feedback themes while using a human-review state to reduce forced-fit errors. The prototype should be assessed on label accuracy, review decisions, and source/output integrity, not just the persuasiveness of generated summaries.

## Scope

- Six business-defined categories and a seventh `needs_review` state.
- Manual prompts executed in ChatGPT, with JSON outputs saved locally.
- Python scripts for label scoring and output-quality auditing.
- Synthetic challenge and holdout datasets; authored reference labels.
- Proposed UX and operational policy, not an implemented dashboard.

## Iterations and evidence

| Stage | Observation | Product lesson |
|---|---|---|
| Original 30-example exercise | v1 and v2 yielded identical outcomes, as reported by the user | An easy benchmark cannot establish improvement |
| Difficult 30-example challenge | v1: 66.7%; v2: 70%; both forced nine review cases into ordinary themes | A model needs an abstention path when taxonomy is incomplete |
| New seven-label policy | v3: 30/30 and 9/9 review cases on challenge | Policy change improved this curated test, not proof of wording superiority |
| Separate curated 36-example holdout | Both v3 and v4: 36/36, with 12/12 review cases | Detailed prompting showed no classification advantage on this set |
| Independent output audit | Both 35/36 exact quotes; v3 exceeded five-insight limit; v4 omitted one theme | Reliability includes evidence fidelity, output constraints, and coverage |

## Product decision

Use progressive disclosure: show up to five prioritized, evidence-linked insights, with expandable access to all additional themes. Add a critical-risk escalation override and a distinct human-review workflow. Prioritization should use validated severity, urgency, business impact, affected-user reach, and evidence quality, **not raw comment frequency alone**. The dashboard and review queue remain proposed rather than shipped.

## What I would improve before a pilot

1. Independent human labeling and a representative, privacy-approved evaluation dataset.
2. More robust JSON/schema, source quotation, and semantic-grounding checks.
3. Risk-weighted escalation, actual review-capacity modeling, and fallback design.
4. Comparative baselines with manual analysts and conventional feedback-analysis products.
5. Logged model version, latency, tokens/cost, repeated runs, and monitoring.
6. Vendor security and privacy review before any real enterprise customer data.

## Outcome and honest limitations

The project produced a working offline prompt-and-evaluation workflow, a documented understanding of abstention and output quality, and a defensible product design recommendation. No customer time savings, revenue, production quality, live A/B experiments, deployed AI pipeline, RAG system, or production GenAI shipments were demonstrated.

## Takeaway for product leaders

> AI reliability is not only about choosing a model or refining prompts. The decision policy, evidence contract, review process, evaluation design, and business cost of mistakes determine whether the workflow is useful.

**Supporting material:** [Architecture](ARCHITECTURE.md), [Evaluation report](EVALUATION_REPORT.md), [Product decisions](PRODUCT_DECISIONS.md), [Interview Q&A](INTERVIEW_QA.md).
