**Date:** 2026-05-28
**URL:** https://job-boards.greenhouse.io/reddit/jobs/7833622
**Archetype:** Senior / Staff ML Engineer (Search & Recommendation)
**Score:** 2.0/5
**Legitimacy:** High Confidence
**PDF:** ❌

---

## A — Match con CV

**Alignment: Low (work auth + search/recsys domain gap)**

Positive signals:
- **10+ years production ML**: Meets the experience floor. MAS Holdings + MUSMET postdoc = well-documented.
- **PyTorch**: In Nishal's stack. JD requires "PyTorch or TensorFlow for building large-scale ML models."
- **Python**: Strong match. JD requires Python or Golang.
- **Ranking systems**: Listed in Nishal's ML domain stack (knowledge-graph.md: "Ranking Systems"). No deployed ranking system evidence, but the concept is in the profile.
- **Information Retrieval**: Listed in Nishal's stack (knowledge-graph.md: "Information Retrieval"). Partial bridge.
- **Lexical and semantic retrieval**: Implicit in Nishal's MIR work (symbolic pattern matching = lexical; embedding-based detection = semantic analogy). Weak bridge.
- **LLM production experience**: JD requires "production experience with large language models, including tuning and deployment." Not met — but "actively researching foundation model-based music generation" is an early signal.

Gaps:
- **Large-scale search and recommendation systems**: Core requirement. "10+ years of industry experience with deep expertise in large-scale search and recommendation systems." Nishal has zero search/recsys deployed system experience.
- **Search relevance infrastructure**: Index scaling, retrieval ranking, query understanding — none in profile.
- **LLM tuning and deployment in production**: No deployed LLM systems.
- **Golang**: Not in Nishal's stack; listed as equivalent to Python.
- **10+ years in search specifically**: The JD emphasis makes this a domain specialist hire. Nishal is a domain specialist in audio/embedded ML, not search.
- **Organizational technical strategy**: Senior Staff scope — same concern across all Senior Staff Reddit roles.

**CV match score: 2.0/5**

---

## B — North Star Alignment

No archetype match. "Search & Recommendation" is a distinct ML discipline (information retrieval, ranking, query understanding, personalized ranking). Nishal's Information Retrieval listing in the stack is a course/concept-level entry, not a deployed system. The gap between "has IR in the stack" and "10+ years leading large-scale search at 126M DAU" is substantial.

**North Star score: 1.5/5**

---

## C — Comp

Base salary: $266,000–$372,400 USD (~$363K–$508K CAD). Senior Staff level.

**Comp score: 5.0/5** (notional)

---

## D — Cultural Signals

Reddit Search & Recommendation team is core to content discovery across the platform. Senior Staff IC with direct influence on product direction. Remote-United States.

Red flag: **US work authorization required.** Hard blocker.

**Cultural score: 2.0/5**

---

## E — Red Flags

[Score < 3.5 — Block E shown for transparency]

1. **[CRITICAL] US work authorization required.** Remote - United States. Hard cap.
2. **[CRITICAL] Search & Recommendation domain gap.** Core requirement is deep expertise in large-scale search and recommendation systems. No search/recsys production experience in profile.
3. **LLM deployment gap.** Production LLM tuning and deployment required. Not met.
4. Golang: preferred; absent from stack.
5. Same Senior Staff scope concern as 417, 418 — company-wide strategy requires demonstrated IC leadership at this level.

---

## G — Posting Legitimacy

- **Tier:** High Confidence
- Active. Salary range consistent with Senior Staff at Reddit. Search is a strategic investment area for Reddit (public commentary on improving search quality).

---

## Machine Summary

```yaml
num: 419
company: Reddit
role: Senior Staff ML Engineer, Search & Recommendation
date: 2026-05-28
score: 2.0
archetype: Senior / Staff ML Engineer (search/recsys)
url: https://job-boards.greenhouse.io/reddit/jobs/7833622
location: Remote - United States (US work auth required)
work_auth_blocker: true
domain_match: low (search/recsys specialization; no deployed systems in profile)
comp_usd: 266000-372400
verdict: skip — US work auth + search & recommendation domain specialization outside profile
```
