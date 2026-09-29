**Date:** 2026-05-28
**URL:** https://job-boards.greenhouse.io/reddit/jobs/7074776
**Archetype:** Senior / Staff ML Engineer (ML Infrastructure / Platform)
**Score:** 1.5/5
**Legitimacy:** High Confidence
**PDF:** ❌

---

## A — Match con CV

**Alignment: Low (work auth + infrastructure specialization mismatch)**

Positive signals:
- 5+ years software engineering: Nishal well exceeds the floor.
- Python: strong match.
- Kubernetes (Docker, Kubernetes in stack), cloud (AWS), MLFlow, Apache Airflow — partial infrastructure overlap.
- "Treat internal ML engineers as customers": Nishal mentored engineers at MAS Holdings and established CI/CD practices. Adjacent signal.

Gaps:
- **Deep Kubernetes expertise (CRDs, Controllers, Operator patterns)**: This is the core technical requirement. Nishal uses Kubernetes but has not built custom Kubernetes Controllers/Operators. This is a specialized SRE/platform engineering skill.
- **JupyterHub/JupyterLab customization**: No evidence in profile.
- **Go**: Listed as required. Not in Nishal's stack.
- **GPU orchestration, CUDA containerization**: Nishal has GPU experience (embedded ML inference) but not at the data center orchestration layer.
- **Distributed training frameworks (Ray at scale)**: Nishal has used distributed deployment but not large-scale training cluster management.
- This is a platform engineering role, not an applied ML role. Nishal is an applied ML practitioner — this is an infrastructure specialization.

**CV match score: 1.5/5**

---

## B — North Star Alignment

No archetype match. "Senior / Staff ML Engineer" in Nishal's profile refers to applied ML delivery, not platform infrastructure. This role is closer to an MLInfra/Platform SWE role than to any of Nishal's target archetypes. The skills are adjacent but the specialization is orthogonal.

**North Star score: 1.0/5**

---

## C — Comp

Base salary: $216,700–$303,400 USD (~$296K–$414K CAD).

**Comp score: 4.5/5** (notional; blocked by work auth + profile mismatch)

---

## D — Cultural Signals

Reddit ML Platform team builds the infrastructure that other ML teams depend on. Strong platform/infrastructure orientation. Remote-United States.

Red flag: **US work authorization required.** Hard blocker.

**Cultural score: 2.0/5**

---

## E — Red Flags

[Score < 3.5 — Block E shown for transparency]

1. **[CRITICAL] US work authorization required.** Hard cap + further reduced by domain gap.
2. **[CRITICAL] Platform engineering specialization.** This role requires Kubernetes Operator development, JupyterHub customization, GPU cluster orchestration — none of which are in Nishal's profile.
3. Go language required: absent from stack.
4. This is among the weakest matches in this batch — both work auth and core skills are misaligned.

**Recommendation: Strong skip.** Even without the work auth issue, this role would score ~2.0 due to the platform engineering specialization gap.

---

## G — Posting Legitimacy

- **Tier:** High Confidence**
- Active. Reddit actively expanding ML infrastructure for 126M DAU platform. Specific salary range published.

---

## Machine Summary

```yaml
num: 416
company: Reddit
role: Senior Machine Learning Engineer, ML Training Platform
date: 2026-05-28
score: 1.5
archetype: Senior / Staff ML Engineer (wrong sub-type: infrastructure)
url: https://job-boards.greenhouse.io/reddit/jobs/7074776
location: Remote - United States (US work auth required)
work_auth_blocker: true
domain_match: low (platform/infra engineering, not applied ML)
comp_usd: 216700-303400
verdict: skip — US work auth + platform engineering specialization (Kubernetes Operators, JupyterHub, GPU orchestration) outside profile
```
