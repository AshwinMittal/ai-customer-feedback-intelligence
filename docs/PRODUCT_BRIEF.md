# Product Brief: AI Customer Feedback Intelligence

## Persona
Senior PM at an imaginary B2B support SaaS company who receives feedback from users, customer success, and support.

## Job to be done
When I receive mixed feedback from different channels, help me group recurring pain points and trace recommendations to real statements so I can prioritize research and roadmap decisions without losing nuance.

## Problem and proposed solution
Manually reviewing large volumes of feedback is time-consuming and inconsistent. Prototype a human-reviewed workflow that classifies messages into a fixed taxonomy and synthesizes evidence-backed insights.

## Scope, v1
- Analyze 30 **synthetic** comments across six predefined themes.
- Output one theme per comment and an exact evidence quote.
- Generate cited summaries and suggested product hypotheses.
- Compare outputs against manual labels and audit evidence references.

## Non-goals
- Real customer data; production integration; autonomous roadmap changes; sentiment-as-fact; automated ticket response; revenue impact claims; RAG/vector database.

## Success metrics (targets, not results)
- 100% record coverage.
- >=90% primary-theme accuracy on synthetic test set.
- 0 invented feedback IDs and 0 unsupported verbatim quotes.
- All proposed product opportunities reviewed by a human PM.

## Limitations
Small synthetic balanced dataset. Gold labels represent one reviewer. Results will not generalize to a real distribution. Human reviewers must assess summaries' meanings and any claimed causal conclusions.

## Risks / mitigations
- Hallucinations -> exact quotes and traceability checks.
- Prompt injection -> feedback data must never override task instructions.
- Model output variance -> record prompts, run dates, and versions; repeat runs.
- Confirmation bias -> fixed taxonomy, manual review and documented disagreements.
- Sensitive data -> synthetic inputs only.

## Open decisions for the student PM
1. Should multi-issue feedback receive more than one label?
2. Which errors are most harmful: missing severe issues or overclassifying them?
3. What review burden is acceptable before the workflow is worth adopting?
4. What human approval step must exist before roadmap action?
