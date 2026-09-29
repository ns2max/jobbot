# Reddit — Staff Machine Learning Engineer, AI Serving

**Date:** 2026-05-28
**URL:** https://job-boards.greenhouse.io/reddit/jobs/7886459
**Archetype:** AI Platform / LLMOps
**Score:** 2.0/5
**Legitimacy:** Proceed with Caution
**PDF:** ❌

---

## Block A — Match with CV

**Archetype fit:** AI Platform / LLMOps — inference infrastructure, GPU serving, Kubernetes at scale.

Reddit is looking for 7+ years in ML Engineering or AI Platform Engineering. The role is heavily infrastructure-focused: GPU-based model serving, Kubernetes orchestration, Go + Python, Triton/vLLM/Dynamo. Nishal's background is strong in ML pipeline ownership and real-time inference, but the stack mismatch is significant — no Go, no Triton/vLLM, no multi-cluster Kubernetes at production internet scale. Embedded inference on RPi4 is the opposite end of the compute spectrum from Reddit's GPU cluster serving. LLMOps observability is adjacent to ML monitoring work but not directly practiced.

**CV alignment:** Partial. Real-time inference (MUSMET, MAS), MLOps/Docker/CI-CD, benchmarking methodology are present. GPU serving infrastructure, Go, Triton, and cloud-scale Kubernetes at Reddit's traffic volumes are not.

**Score: 2.5/5**

---

## Block B — North Star Alignment

Target archetypes for Nishal: Senior/Staff ML Engineer, ML Research Engineer, Applied Scientist, Research Scientist, AI/ML Technical Lead, Solutions Architect.

Staff MLE AI Serving fits "Senior/Staff ML Engineer" in title only. The actual work is pure MLOps/infrastructure — no modeling, no research, no algorithm development. This is a platform engineering role, not an applied ML or research-adjacent role. It does not align with the research-to-production arc Nishal is returning from.

**Score: 1.5/5**

---

## Block C — Compensation

Salary range: $253,300–$354,600 USD. This is top-quartile FAANG comp for the US market. However, this is a US-remote role requiring US work authorization — Nishal cannot work in the US without sponsorship (Canadian PR). Even if work auth were obtained, the comp reference point is USD, and Nishal's targets are CAD-based.

**Score: N/A — work auth blocker (see Block D)**

---

## Block D — Cultural Signals

Reddit is a scaled consumer platform. The role operates in a product-first, high-throughput engineering environment. No research publication expectations. The tech stack (Go, Kubernetes, Triton) signals a systems-heavy culture. Remote-US indicates a distributed team with async norms. No red flags on culture per se, but this is not an environment that would leverage Nishal's research depth or domain expertise in audio/signal/CV.

**Score: 2.5/5**

---

## Block E — Red Flags

- **[!] US work authorization required.** Role is listed as "Remote - United States." Nishal is a Canadian PR and cannot work in the US without sponsorship. Rule: cap score at 2.5.
- **Stack mismatch:** Go is required; no Go in Nishal's stack. Triton/vLLM/Dynamo — no demonstrated experience.
- **7+ year minimum:** Nishal's total industry experience spans the required range but is not concentrated in ML platform/infrastructure.
- **No modeling work:** This role does not involve building or training models, only serving them at scale.

**Score: 1.0/5 (multiple hard blockers)**

---

## Block F — Global Score

Not applicable (score below 4.0).

| Dimension | Score |
|-----------|-------|
| CV Match | 2.5 |
| North Star | 1.5 |
| Comp | N/A (blocked) |
| Culture | 2.5 |
| Red Flags | 1.0 |
| **Global** | **2.0/5** |

**Recommendation: Do not apply.** US work auth required (hard blocker). Role archetype (serving infrastructure, Go, Triton) does not match Nishal's strengths or targets. Score capped at 2.5 per work-auth rule; actual fit lands at 2.0.

---

## Block G — Posting Legitimacy

- Reddit is a public company (NYSE: RDDT) — real employer, stable.
- Greenhouse ATS hosting is standard for legitimate postings.
- JD is technically specific (Go, Triton, Dynamo, Kubernetes) — not a ghost posting template.
- Salary range published — positive signal.
- No repost history in scan-history.tsv for this specific role.

**Tier: High Confidence** — Real, active posting. Work auth blocker is the issue, not legitimacy.

---

## Machine Summary

```yaml
num: 420
company: Reddit
role: Staff Machine Learning Engineer, AI Serving
date: 2026-05-28
score: 2.0
archetype: AI Platform / LLMOps
location: Remote - United States
work_auth_required: true
ca_eligible: false
legitimacy: High Confidence
apply: false
reason: US work authorization required; stack mismatch (Go, Triton, GPU serving infra); pure infrastructure role not aligned with ML research/applied archetype
```
