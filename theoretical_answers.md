1) Part 1 — Theoretical Analysis (written answers)

Q1: How AI-driven code generation tools (e.g., GitHub Copilot) reduce development time. What are their limitations?

Answer (beginner):
GitHub Copilot watches what you type and suggests code snippets or whole lines. This speeds up development because the tool can:

autocomplete repetitive code patterns (loops, getters, setters),

suggest common functions (file I/O, parsing),

provide quick examples for APIs you don’t know well,

generate test skeletons or docstrings.

Limitations:

Incorrect or insecure suggestions: sometimes it suggests code that looks good but has bugs or security issues.

Context limits: it may not fully understand the whole project; suggestions can be out-of-context.

Over-reliance: developers may accept code without understanding it.

Licensing/privacy concerns: suggestions might resemble public code; you should check license compatibility.

Not a replacement for design: Copilot helps write code but doesn’t replace architecture decisions, testing, or critical thinking.

Q2: Compare supervised and unsupervised learning in the context of automated bug detection.

Answer (beginner):

Supervised learning uses labeled examples (e.g., code samples labeled “bug” or “no bug”). It learns to map input → label. For bug detection, we can train a classifier to say whether a piece of code is buggy. Pros: high accuracy if labels are good. Cons: needs many labeled examples which are expensive to create.

Unsupervised learning finds patterns without labels (e.g., clustering or anomaly detection). For bug detection, unsupervised models can flag unusual code patterns as anomalies (possible bugs). Pros: works without labels, good for finding novel issues. Cons: more false positives and harder to interpret.

Q3: Why is bias mitigation critical when using AI for user experience personalization?

Answer (beginner):
If an AI personalizes an app (for example shows job ads or content), bias can mean certain groups get worse experiences or fewer opportunities. This hurts fairness and can be illegal. Bias mitigation is needed to:

ensure equal treatment across groups,

avoid reinforcing stereotypes,

maintain trust with users,

comply with fairness rules and company policy.

Case Study: AI in DevOps — How AIOps improves deployment efficiency (two examples)

Short answer (beginner):
AIOps applies AI to IT operations to make deployments more reliable and faster.

Predictive failure detection: AIOps monitors logs and metrics to predict issues before deployment finishes (e.g., high error rate after release). This lets engineers roll back or pause automatically — fewer failed deployments and less downtime.

Automating rollback and remediation: When deployment problems are detected, AIOps can suggest or automatically run rollback steps or run remediation scripts (e.g., restart service, reconfigure load balancer) — speeds up recovery and reduces manual triage.
