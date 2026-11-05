# AI PM interview question bank: Project 1

Practice these in your own words. The examples below are defensible **independent learning-project answers**, not claims about production systems or past employer deployment.

## Q1. Why choose a fixed taxonomy rather than let the model discover its own categories?

**Strong 60-second answer**

> I chose a fixed taxonomy because the initial product goal was consistent routing and trend reporting, not exploratory topic discovery. A bounded set of categories makes it easier to compare feedback over time, define ownership, and evaluate accuracy against reference labels. The weakness is that new or ambiguous problems can be forced into the wrong category. That became visible in my challenge evaluation: both early prompts misrouted all nine cases that needed review. I addressed it through an explicit `needs_review` state. In a mature product I would combine fixed categories for production reporting with periodic exploratory theme discovery on the review queue, then let a PM approve taxonomy changes. That gives us consistency without becoming blind to emerging issues.

**Follow-up: Why not use embeddings and clustering?**

Clustering can help discover unanticipated themes, especially for large unlabeled datasets, but clusters need interpretation, may shift between runs, and may not map cleanly to operational ownership. It is an appropriate discovery tool, not a drop-in replacement for a maintained reporting taxonomy. Project 1 did **not** use embeddings or clustering; those are proposed future methods.

**Trade-off to articulate:** consistency and explainability versus adaptability and discovery.

## Q2. What does 90% classification accuracy tell you about readiness?

**Strong 60-second answer**

> It tells me that 90% of the evaluated items matched the reference labels on that specific dataset. It doesn't tell me whether the mistakes are acceptable, how representative the sample is, whether the reference labels are reliable, or whether the model is safe to rely on. For example, missing a critical security or outage complaint could be much worse than mislabeling a low-priority usability request. I would inspect a confusion matrix and risk-weighted errors, including recall for urgent cases; measure review precision and recall, evidence traceability, schema compliance, and human override rate; and evaluate across different customer segments and time periods. I would start with human review or shadow mode, not assume a single accuracy score proves production readiness.

**Project evidence:** On the 36-record synthetic holdout, classification was 100% for both prompts, yet the output audit found a case-sensitive quotation mismatch for H216 and v3 violated the maximum-insight limit. This demonstrated why classification quality and output quality must be assessed separately.

**Follow-up: How would you set an initial launch threshold?**

Work backward from error cost and workflow: define which errors are intolerable (e.g., critical issue missed), which can be routed to review, review capacity, and the minimum value needed. Collect representative pilot data and agree on thresholds with Product, Support, Security, and Compliance. Do not choose 95% or 99% arbitrarily without business context.

## Q3. What changes before using real enterprise customer data?

**Strong 60-second answer**

> I would move from a synthetic, manual learning prototype to a security-reviewed, permissioned service. First I'd classify the information and identify personally identifiable and confidential data, agree on permitted usage and retention, and review the chosen vendor's contractual and data-handling terms. I'd use least-privilege access, appropriate encryption, redaction or minimization, and auditable logs. I'd treat customer text as untrusted input to reduce prompt-injection risk, validate structured output rather than trusting generated text, and require human approval for uncertain or sensitive cases. Then I'd test against representative, properly authorized records, monitor quality, cost, latency, and drift, and roll out gradually with a rollback or manual fallback path.

**Additional layers to mention if asked:** data residency and cross-border transfers where relevant; whether provider inputs are used to train models; deletion rights and retention windows; incident response; tenant isolation; security review; capacity planning; safeguards against exposing unrelated customers' source records in insights.

**Important honesty:** No security controls, enterprise vendor approval, or production data pipeline was implemented in Project 1. These are requirements for a real deployment.

## Q4. How would you decide whether this beats conventional feedback-analysis tools?

**Strong 60-second answer**

> I would evaluate three realistic alternatives on the same privacy-approved sample: human analysts, an existing feedback-analysis product, and a proposed AI workflow. I would compare what matters to PMs and support leaders: time to surface an actionable issue, evidence quality, classification accuracy, critical-issue recall, usability, consistency, and review workload. Then I'd calculate full cost, not just LLM token charges: software licenses, integration and maintenance, inference, retries, hosting, security, and human exception handling. I'd use a blinded qualitative review of recommended insights, have PMs assess whether they would change roadmap decisions, and measure time savings in a controlled pilot. If a simpler conventional tool is cheaper and good enough, I'd recommend it instead.

**Useful formula**

```text
Total monthly cost = vendor or API charges
                   + infrastructure and logging
                   + implementation amortization
                   + human review hours * loaded hourly rate
                   + ongoing monitoring and maintenance

Net value = validated labor savings + validated business benefits
            - incremental total monthly cost
```

**Break-even thinking:** Do not count generated summaries as value by themselves. Measure whether they save research time or improve decisions without introducing unacceptable errors. Project 1 has **no measured dollar savings, customer adoption, or cost advantage**.

## Q5. Why did your v3 improvement not prove better prompt wording?

**Answer:** The move from v2 to v3 changed the set of allowed decisions by introducing `needs_review`; it changed policy and prompt instructions simultaneously. Therefore, the challenge improvement cannot be attributed to wording alone. On the same seven-label holdout, detailed v3 and concise v4 both scored 36/36. A cleaner future comparison would hold taxonomy, sample and model configuration constant, vary just one prompt element, run multiple repeats, and include qualitative output checks.

## Q6. What was the most important unexpected failure?

**Answer:** The first evaluator rewarded correct category labels but missed additional output requirements. A 100% classification score masked an exact-quote mismatch in both models and an over-limit number of insight objects in v3. A separate audit caught these failures and made the project more realistic.

## Q7. What would you do if 30% of requests needed human review?

**Answer:** First verify whether that rate represents real traffic; in this project, it does not, because the challenge was intentionally difficult and the holdout contained 12 review cases in 36 records. If real data showed a persistent 30% rate, estimate queue capacity, handling time and the cost of errors; segment review reasons; refine taxonomy only when supported; add targeted disambiguation; and selectively automate low-risk cases. High-risk cases may deserve review regardless of volume.

## Q8. Why didn't you use RAG?

**Answer:** This project's inputs were a small, directly supplied feedback dataset, so adding retrieval and a vector database would create complexity without solving a current input-size or evidence-discovery problem. RAG becomes useful when the system must retrieve relevant material from a much larger or changing knowledge base before generation. I planned to study it separately so I could measure retrieval quality independently from classification and output quality.

## Q9. How would you handle a prompt-injection attempt inside feedback?

**Answer:** Treat ticket/comment text as untrusted data and keep the task instructions separate. Validate output categories and IDs mechanically, avoid granting the model authority to execute instructions found in feedback, and test adversarial examples. One holdout record, H220, attempted an instruction override; both submitted outputs still categorized it as `integration_sync`. One passing synthetic case does not establish general defense against prompt injection.

## Q10. What exactly did you build versus propose?

**Answer:** I completed and exercised an offline feedback classification workflow using manual ChatGPT prompts, saved JSON outputs, Python evaluators, and tests; documented a product decision and evaluation findings. I **did not** deploy a web app, build an actual human review service, process real client data, measure production cost or latency, or launch the proposed insight cards. The UX and enterprise architecture are follow-on design recommendations.

## Interview story in 90 seconds

> I worked on an independent AI PM learning project addressing a realistic customer-feedback problem: how to synthesize feedback into consistent, traceable product themes. I started with six fixed categories and a manual LLM workflow. On an easy benchmark, a more elaborate prompt did not show an advantage, which revealed a weakness in the evaluation design. I introduced tougher synthetic feedback, and the initial versions forced all nine ambiguous or out-of-scope cases into ordinary labels. I changed the product policy to allow `needs_review`; the upgraded version correctly routed nine of nine on that challenge.
>
> I then compared a detailed and concise prompt on a separate curated 36-record holdout under the same seven-label taxonomy. Both classified all 36 correctly and flagged all 12 reference review cases, so the extra prompt complexity had not demonstrated a classification advantage. A separate output audit then found one verbatim-quote mismatch in each and a five-insight contract violation in the detailed version. My main lesson was that reliability requires more than a high classification score: we need appropriate abstention, evidence checks, output contracts, realistic evaluation datasets, and a viable human workflow. I proposed a concise five-insight dashboard with expandable themes and visible critical-risk escalation, but did not implement the UI. This was a synthetic, offline prototype rather than production deployment.

## Practice prompts for yourself

- What is the user's problem, not the AI feature?
- Which decisions should be deterministic and which can involve AI generation?
- When is the model allowed to abstain?
- What is the cost of a false negative compared with false review escalation?
- How would you build a dataset that a model has not already effectively seen?
- Which safeguards are hard gates, and which are quality metrics you can improve over time?
- How would you explain your own work without claiming AI-generated starter code is wholly hand-built?
