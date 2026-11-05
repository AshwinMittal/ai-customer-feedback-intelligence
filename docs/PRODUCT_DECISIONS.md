# PM product decisions and trade-offs

This file records what was observed, what was decided, and what remains only a design proposal.

## Decision 1: Start with a fixed taxonomy

**Choice:** Six stable product themes plus a seventh `needs_review` state (introduced in the upgraded challenge).

**Why:** Stable categories support trend analysis, consistent dashboarding, and reproducible offline evaluation. A dynamic free-form taxonomy would require human normalization before results could be compared over time.

**Trade-off:** New or overlapping topics may not fit. Mitigation: review queue and periodic human-approved taxonomy updates, potentially informed by clustering or exploratory LLM analysis.

**Status:** Implemented in prompt and evaluator logic for challenge/holdout. No operational triage service exists.

## Decision 2: Allow abstention instead of forced-fit classification

**Observed:** Without `needs_review`, v1/v2 forced all nine review-worthy challenge records into ordinary themes. On the same benchmark v3 flagged nine of nine. On the curated holdout both seven-label prompts flagged twelve of twelve.

**Choice:** Keep an explicit review state for ambiguous and out-of-scope feedback.

**Trade-off:** Human review costs time, and too much abstention may reduce useful automation. Set quality thresholds based on business risk instead of optimizing raw accuracy alone.

**Status:** Implemented in classification outputs; queue workflow is proposed only.

## Decision 3: Progressive disclosure with an exception channel

**User's decision:** Display **five prioritized insights with expandable access to the remaining themes**, so the default view stays concise without hiding the full evidence from users who need more detail.

**Instructor refinement:** The choice is sound but must not become a rigid limit that hides a critical sixth insight. Critical problems need persistent high-visibility alerts and separate escalation.

**Proposed design:**

- Top five cards ranked by documented impact, severity, urgency, affected users, and evidence quality.
- Expandable section with all remaining themes, counts and source record IDs.
- Distinct exception queue for `needs_review` cases with escalation rules.
- A critical-incident override outside or above the standard ranking.
- Each card includes supporting feedback IDs and an editable, explicitly provisional recommendation.

**Why frequency alone fails:** In the 36-record holdout, all six active themes had four records each. Nothing in frequency distinguishes a duplicate-contact integration defect from low-value notification clutter.

**Status:** Product UX decision and proposed design; **no actual dashboard was implemented**.

## Decision 4: Separate classification evaluation from output QA

**Observed:** Both holdout outputs classified 36/36 correctly, yet both failed one exact-string quote, v3 broke the max-five insight contract, and v4 excluded one active category from its five summaries.

**Choice:** Maintain separate checks for label correctness, human-review outcomes, source fidelity, insight coverage, and output schema. Require manual qualitative review of summary semantics.

**Status:** Deterministic output audit implemented and tested. Manual semantic audit still required; no claim that the model provides fully grounded insight synthesis.

## Decision 5: Stop optimizing the same benchmark

**Choice:** Do not tweak the prompt until it scores 100% again on already-seen records. Next improvements require more realistic, separately labeled inputs, repeated trials and consistent model parameters. Consider comparison to a rules-based or commercial feedback-analysis baseline before choosing an LLM.

**Status:** Current learning milestone closed; production validation outstanding.
