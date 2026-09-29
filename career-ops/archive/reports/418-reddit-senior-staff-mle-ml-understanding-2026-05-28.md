**Date:** 2026-05-28
**URL:** https://job-boards.greenhouse.io/reddit/jobs/7847148
**Archetype:** Senior / Staff ML Engineer (User Modeling / Recommender Systems)
**Score:** 2.0/5
**Legitimacy:** High Confidence
**PDF:** ❌

---

## A — Match con CV

**Alignment: Low (work auth + recommender systems domain gap)**

Positive signals:
- **10+ years building production ML**: Meets the minimum experience requirement. MAS Holdings + MUSMET + Forestpin = well-documented production ML delivery.
- **Sequential data modeling**: Nishal has deep sequence modeling experience (RNN for polyphonic pattern detection, JAES 2026; time-series at MAS Holdings). "Sequence-based learning approaches" is a genuine bridge.
- **Embedding + representation learning**: Implicit in Nishal's MIR work (feature engineering, pattern embedding for musical gesture and audio). Partial bridge.
- **Foundation model integration**: "Actively researching foundation model-based music generation" per knowledge-graph.md — early signal but no deployed LLM integration.
- **Multi-task learning**: Some evidence from multimodal MUSMET work (audio + sensor + gesture).
- **Low-latency serving**: 14ms inference at MAS; <30ms at MUSMET. Latency-aware system design is a genuine proof point.

Gaps:
- **User modeling / recommender systems**: Zero evidence in profile. This is the core domain — "unified user understanding framework," behavioral modeling, "user representation systems." Nishal has never worked on user-facing personalization systems.
- **10+ years in recommender systems**: The minimum is "10+ years building production ML systems, especially in user modeling or recommender systems." The emphasis on the sub-domain makes this a mismatch.
- **LLM integration for user profiles**: "LLMs to build richer user understanding, dynamic profiles, semantic reasoning." No LLM deployment experience.
- **Embedding storage, retrieval, low-latency serving at scale**: Infrastructure for 126M DAU user embeddings — outside Nishal's scale of operation.
- **Cross-team influence at Senior Staff level**: Company-wide adoption driving across Feeds, Notifications, Search, Ads. Nishal's leadership has been team/project-level.

**CV match score: 2.0/5**

---

## B — North Star Alignment

"User modeling" and "recommender systems" are not in Nishal's target archetypes. The role is adjacent to "AI Platform / LLMOps" but requires a product ML specialization (behavioral modeling, personalization, ranking) that doesn't appear anywhere in the profile. Sequential data modeling is the only genuine bridge — but that alone doesn't qualify at Senior Staff level.

**North Star score: 1.5/5**

---

## C — Comp

Base salary: $266,000–$372,400 USD (~$363K–$508K CAD). Senior Staff level compensation.

**Comp score: 5.0/5** (notional)

---

## D — Cultural Signals

Reddit ML Understanding team is foundational to personalization across the platform. Senior Staff IC role with company-wide scope. Remote-United States.

Red flag: **US work authorization required.** Hard blocker.

**Cultural score: 2.0/5**

---

## E — Red Flags

[Score < 3.5 — Block E shown for transparency]

1. **[CRITICAL] US work authorization required.** Remote - United States. Hard cap.
2. **Recommender systems / user modeling domain gap.** Core requirement is "10+ years in user modeling or recommender systems." Nishal has zero experience in this domain.
3. **Scale mismatch.** 126M DAU personalization infrastructure requires platform engineering at a scale Nishal hasn't operated at.
4. **LLM integration for user profiles**: No deployed LLM experience.
5. Senior Staff scope: same concern as 417 — company-wide IC leadership beyond current demonstrated level.

---

## G — Posting Legitimacy

- **Tier:** High Confidence
- Active. Salary range is realistic for Senior Staff. Reddit is actively investing in personalization (public earnings commentary on AI and recommendations).

---

## Machine Summary

```yaml
num: 418
company: Reddit
role: Senior Staff Machine Learning Engineer, ML Understanding
date: 2026-05-28
score: 2.0
archetype: Senior / Staff ML Engineer (user modeling)
url: https://job-boards.greenhouse.io/reddit/jobs/7847148
location: Remote - United States (US work auth required)
work_auth_blocker: true
domain_match: low (user modeling / recommender systems; no profile evidence)
comp_usd: 266000-372400
verdict: skip — US work auth + recommender systems domain mismatch; sequential modeling is only genuine bridge
```
