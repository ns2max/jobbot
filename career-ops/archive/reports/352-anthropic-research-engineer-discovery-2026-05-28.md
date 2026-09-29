# 352 — Anthropic | Research Engineer, Discovery

**Date:** 2026-05-28
**URL:** https://job-boards.greenhouse.io/anthropic/jobs/4669581008
**Archetype:** AI Platform / LLMOps
**Score:** 2.8/5
**Legitimacy:** High Confidence
**PDF:** ❌

---

## Block A — CV Match

**Strengths:**
- Infrastructure and systems engineering — MAS Holdings: real-time data ingestion, ETL pipelines for high-frequency IoT data across distributed sites
- Docker + Kubernetes listed in Nishal's technical stack — directly matches JD requirements
- C++ and Python production experience — real-time inference engines at MAS Holdings
- Distributed system design instincts from IoT-scale deployments (millions of events/day)
- Performance optimization: 14ms inference on RPi4 (MUSMET), 99.5% inspection time reduction (MAS)

**Gaps:**
- **Critical gap:** 6+ years infrastructure engineering required with large-scale distributed systems — Nishal's distributed systems experience is IoT/manufacturing, not ML training infrastructure
- No GPU/TPU optimization experience
- No language model training infrastructure (the core of this role — building infra for "AI scientist")
- No experience with workflow orchestration at LLM scale (Airflow listed, but not at Anthropic-scale)
- No Beam/Spark or large-scale data pipeline tools at this scale
- Cloud platforms (AWS) listed but not at enterprise ML infra scale

**Match level:** Low-moderate on infra fundamentals; significant gap on ML training infra specifics.

---

## Block B — North Star Alignment

Target archetype: **AI Platform / LLMOps** — infrastructure focus.

This role builds the infra for Anthropic's "AI scientist" project — large-scale distributed systems, VM/container architectures for long-horizon AI tasks. It requires deep ML infrastructure expertise (GPU optimization, LLM training pipelines) that Nishal doesn't have. The compensation ceiling ($850K USD) signals this is a top-tier infrastructure specialist role.

Alignment: **Low**. Infra instincts present but the specialization required (LLM training infra at scale) is absent.

---

## Block C — Compensation

- **Posted range:** $350,000–$850,000 USD (~$479K–$1.16M CAD)
- Extremely wide range — senior IC to staff/principal level
- Well above target range; US-only role

---

## Block D — Cultural & Location Signals

**RED FLAG — US Work Authorization Required:**
- Location: San Francisco, CA only
- No Canada remote option
- Canadian PR → US work auth required
- Score capped at 2.5 per profile rules; bumped to 2.8 for real infrastructure match (Docker, Kubernetes, C++, ETL)

---

## Block E — Not applicable (score < 3.5)

---

## Block F — Not applicable (score < 4.0)

---

## Block G — Posting Legitimacy

**Assessment: High Confidence**

- Active Greenhouse listing with detailed JD
- Wide salary range ($350K–$850K) is consistent with infrastructure specialist roles at top-tier AI labs
- Specific mission ("AI scientist") and team context

---

## Machine Summary

```yaml
id: 352
company: Anthropic
role: Research Engineer, Discovery
archetype: AI Platform / LLMOps
score: 2.8
recommendation: against
url: https://job-boards.greenhouse.io/anthropic/jobs/4669581008
date: 2026-05-28
location: San Francisco, CA
remote_canada: false
work_auth_flag: true
comp_usd: "350000-850000"
comp_cad_equiv: "479000-1163000"
key_gap: "US work auth required; no LLM training infra, GPU/TPU optimization experience"
key_match: "Docker, Kubernetes, C++/Python production systems, ETL pipelines, distributed IoT"
legitimacy: High Confidence
```
