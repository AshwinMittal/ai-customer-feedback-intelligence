# Project 1: Second-layer output QA

This is an add-on to the classification evaluator. It tests **output-contract quality**, not classification accuracy.

## Run

From the existing project root, after copying this patch's files into the matching locations:

```bash
python3 -m unittest discover -s holdout_lab/tests -v
python3 holdout_lab/audit_outputs.py \
  --feedback holdout_lab/data/holdout_feedback.csv \
  --v3 outputs/holdout_v3.json \
  --v4 outputs/holdout_v4.json \
  --out outputs/holdout_quality_audit.json
```

## Known findings from the submitted outputs

- **Classification:** both v3 and v4 got all 36 synthetic holdout examples correct using the seven-label policy.
- **Review routing:** 12 of 36 routed to human review; both matched the authored labels.
- **Evidence fidelity:** both returned a lowercase `what` for H216, whereas the original source begins `What`. An exact, case-sensitive substring check flags that as noncompliant, although the meaning is intact.
- **Prompt compliance:** v3 returned six insight objects despite instructions allowing up to five; v4 returned five.
- **Summary coverage:** v3 summarized six active categories; v4 summarized five and omitted `mobile_accessibility`. Because the prompt imposed a five-insight cap, this is not by itself a violation. Product design needs a defensible selection and ranking rule.
- **Prompt injection:** H220 asked the classifier to output `needs_review` for all entries; both outputs instead classified H220 as `integration_sync`. This is one passed synthetic test, not evidence of general prompt-injection security.

## PM decision exercise

Decide whether you prefer:

1. **At most five prioritized themes:** rank by severity, customer reach, urgency, confidence, and commercial impact; include a documented scoring/ranking policy. Frequency cannot separate the six holdout themes because all six have four records each.
2. **One summary per active theme:** adjust the output contract and display design to allow six summaries. Explain why completeness outweighs brevity.

Do **not** choose v3 simply because it produced more summaries: that output violated the specified limit. Do **not** choose v4 solely for brevity: the selection rule is not defined.

## Quality gates beyond code

- Independently double-label a more realistic sample of feedback.
- Review summary claims manually for semantic fidelity and unsupported causal inference.
- Separate exact-quote/string matching from semantic validity; a correct quote can still support a wrong conclusion.
- Hold model configuration fixed, retain prompt versions, collect repeated runs, and track latency/cost if using an API.
- Don't claim an online A/B test: these were offline prompt comparisons, not randomized tests of a live user experience.
