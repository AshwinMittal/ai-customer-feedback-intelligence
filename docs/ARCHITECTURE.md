# Architecture and design rationale

## System boundary

This is an offline, manually operated LLM workflow. Python reads a local CSV and constructs prompts; a person pastes a prompt into ChatGPT, saves its JSON reply, and runs local evaluation scripts. There is **no production API integration, database, model service, hosted UI, or automated review queue**.

```text
[Source: synthetic CSV] -> [Prompt builder] -> [ChatGPT, manually operated]
                                                     |
                                               [Saved JSON]
                                                     |
                +------------------------------------+----------------------------------+
                |                                                                       |
       [Deterministic label evaluator]                                       [Output-quality audit]
       - theme versus reference                                             - exact quote strings
       - missing/extra/duplicate IDs                                        - max insight count
       - review precision and recall                                        - covered/omitted themes
       - forced-fit errors                                                  - citation group checks
                |                                                                       |
                +------------------------------------+----------------------------------+
                                                     |
                                         [PM interpretation and decisions]
                                                     |
                                        [Proposed UX, NOT implemented]
                        Five prioritized cards, expandable full set, separate review workflow
```

## Why choose each component?

**Fixed categories:** Six business-defined themes allow trend comparisons, consistent reporting, and deterministic scoring. **Trade-off:** a new problem may not fit any category. The `needs_review` policy provides a safer way to handle uncertainty until a human updates the taxonomy.

**Source IDs and quotes:** These allow users to investigate evidence rather than trust unsupported summaries. **Trade-off:** checking that text is a verbatim substring does not prove a recommendation is semantically justified.

**Human review:** A system should abstain rather than force an unsuitable label. **Trade-off:** human review consumes time and introduces operational queues; review rates from a curated challenge are not forecasts for live traffic.

**Two independent evaluator layers:** Classification accuracy does not equal output fidelity or UX compliance. A separate output audit caught a violated five-insight limit even when classification was perfect.

**Manual model workflow:** Fastest learning path with no API charges and minimal setup. **Trade-off:** weaker control of model parameters, repeated runs, usage/cost measurement, and reproducibility than an API-driven pipeline.

## Proposed product design, not shipped

- Main view shows five insights prioritized by verified severity, breadth, urgency, customer impact, and evidence quality.
- Additional themes remain accessible through progressive disclosure.
- Critical risks override normal ranking and are surfaced visibly; they must never be hidden as the sixth card.
- Each insight includes source feedback IDs, summary, provisional recommendation, and confidence/evidence indicators.
- Ambiguous, sensitive, out-of-scope, and potentially critical reports enter a human triage workflow.

These UX elements are **recommendations** arising from the learning exercise. No dashboard or queue was built in Project 1.

## Next technical architecture (not part of Project 1)

Approved data source -> ingestion and PII controls -> API inference with structured JSON -> schema validation -> traceable evidence storage -> exception queue -> insight dashboard -> audit logging and monitoring. This could also employ established NLP/rules approaches as baselines before adopting an LLM.

RAG is not used in this project. All feedback is supplied directly in each prompt; there is no embedding model, index, retrieval stage, or vector database. That distinction is intentional, because a future RAG project will teach retrieval separately.
