**Date:** 2026-05-28
**URL:** https://job-boards.greenhouse.io/reddit/jobs/7891887
**Archetype:** Senior / Staff ML Engineer (Security / MLOps)
**Score:** 2.5/5
**Legitimacy:** High Confidence
**PDF:** ❌

---

## A — Match con CV

**Alignment: Moderate (capped by work auth; production ML lifecycle is a genuine match)**

Positive signals:
- **Complete ML lifecycle ownership**: Nishal owns "problem definition, data ETL, feature engineering, training, evaluation, deployment, monitoring, and retraining" — exactly what this JD lists. MAS Holdings and MUSMET postdoc both demonstrate full-stack ownership.
- **Anomaly detection experience**: Forestpin — "compliance monitoring, risk detection on large structured enterprise datasets." Directly relevant to "guardrail models, semantic classifiers, and anomaly detection systems."
- **MLOps workflows**: Docker, Kubernetes, MLFlow, Apache Airflow, CI/CD — all in Nishal's stack (knowledge-graph.md). JD prefers "Airflow, Ray, MLflow, Kubernetes."
- **Rigorous evaluation suites**: JAES 2026 benchmarking (adversarial/edge cases explicitly tested in the embedded ML context). "Precision/recall, false positive analysis, calibration" — standard methodology Nishal uses.
- **PyTorch**: In Nishal's stack.
- **Large-scale data pipelines**: MAS Holdings (millions of IoT events/day, ETL across distributed manufacturing sites).
- **Synthetic data generation**: McGill — "diffusion + VAE approaches for limited label regimes." JD prefers "labeling strategy, synthetic data, distillation."
- **5+ years production ML**: 10+ years total; 5+ years at MAS Holdings alone.

Gaps:
- No security/privacy/trust-safety ML experience. The "GenAI Security" framing (zero-trust, defense-in-depth, LLM traffic protection) is outside Nishal's profile.
- No fine-tuning neural text models for adversarial/long-context security inputs.
- Python + Go: Python strong; Go not listed in Nishal's stack.
- LLM guardrail models: no direct experience.

**CV match score: 3.2/5** (before work auth cap)

---

## B — North Star Alignment

Closest archetype: Senior / Staff ML Engineer. The role maps to production ML lifecycle ownership + MLOps — Nishal's strongest industrial archetype. However, the security/GenAI domain requires LLM-specific knowledge (guardrail models, LLM traffic classification) that is outside the current profile.

The Forestpin anomaly detection work is the clearest bridge. If Nishal were positioning into ML security, this role would be a reasonable stretch target.

**North Star score: 2.5/5**

---

## C — Comp

Base salary: $216,700–$303,400 USD (~$296K–$414K CAD). Well above Nishal's $140K–$188K CAD Senior MLE target in Toronto. However, this is US comp for a US-remote role.

**Comp score: 4.5/5** (notional; blocked by work auth)

---

## D — Cultural Signals

Reddit is a public company with 126M DAU. The Security/Privacy/Assurance org is mission-critical. Remote-United States means strong async culture. The role provides technical direction — room for senior IC growth.

Red flag: **Remote - United States** = US work authorization required. No indication of Canadian remote or sponsorship.

**Cultural score: 3.0/5**

---

## E — Red Flags

[Score < 3.5 — Block E shown for transparency]

1. **[CRITICAL] US work authorization required.** "Remote - United States" explicitly excludes Canadian workers without US work auth. Hard cap at 2.5.
2. **Domain gap: GenAI security.** No LLM guardrail, zero-trust AI security, or adversarial text classification in Nishal's background.
3. Go language: not in Nishal's stack; preferred by Reddit.
4. Without the work auth issue, this role would score ~3.5 as a stretch target given the MLOps/anomaly detection alignment.

---

## G — Posting Legitimacy

- **Tier:** High Confidence
- Active posting with specific salary range. Reddit is publicly traded (RDDT) — job boards are actively maintained.
- Security org hiring is consistent with Reddit's 2025 AI investment trajectory.
- "Remote - United States" is a clear, honest job description signal.

---

## Machine Summary

```yaml
num: 415
company: Reddit
role: Senior Machine Learning Engineer, GenAI Security
date: 2026-05-28
score: 2.5
archetype: Senior / Staff ML Engineer
url: https://job-boards.greenhouse.io/reddit/jobs/7891887
location: Remote - United States (US work auth required)
work_auth_blocker: true
domain_match: medium (MLOps/anomaly detection match; GenAI security gap)
comp_usd: 216700-303400
verdict: skip — US work auth; strongest CV alignment of the Reddit Senior MLE batch on production ML lifecycle
```
