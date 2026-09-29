# Evaluation Report — Member of Technical Staff, Pre-Training Data @ Cohere

**Date:** 2026-05-28
**URL:** https://jobs.ashbyhq.com/cohere/859e2e47-02fb-4afe-bb8a-e83bf4d8c265
**Archetype:** Senior / Staff ML Engineer
**Score:** 3.4/5
**Legitimacy:** Proceed with Caution
**PDF:** ❌

---

## A — Match with CV

**Alignment: Moderate**

Pre-training data engineering focuses on building and maintaining data pipelines for training large language models: ingestion, cleaning, filtering, deduplication, quality assessment, data mixture experiments, and working with web/code/multilingual corpora. Core stack: Python, Apache Spark/Beam, large-scale data processing.

**Matching signals:**
- End-to-end ML pipeline ownership at MAS Holdings: data ingestion, ETL pipelines, high-frequency IoT and operational time-series at scale — demonstrates pipeline engineering at scale
- Forestpin: data pipelines for financial forensics on large structured enterprise datasets
- Python proficiency throughout; data processing and feature engineering are consistent themes
- Dataset creation and curation: Nishal published 4 Zenodo datasets (DoMP, DoPP, DoDP, DoDP2 — 7,000+ recordings, 70 musicians) — direct data curation and quality control experience
- Experimental design with data ablations (JAES 2026 — ablations on architecture + data configurations) — relevant to data mixture experiments

**Gaps:**
- No web-scale data processing experience (Common Crawl, web crawls, NLP corpora)
- No experience with Spark, Beam, or distributed data frameworks (stack has Pandas, NumPy, SQL — not big-data scale)
- No multilingual data or code data pipelines
- Data volume is research-scale (7,000 recordings) vs. petabyte-scale web data
- Role is specifically for pre-training data at a frontier LLM lab — highly specialized

The pipeline engineering instinct is real, but the scale mismatch is significant. Pre-training data at Cohere means petabyte-scale web data, not domain-specific research datasets.

**CV match score: 3.0/5**

---

## B — North Star Alignment

**Archetype fit: Senior / Staff ML Engineer (data-side)**

This is the weakest alignment across all Cohere roles evaluated. Pre-training data is infrastructure-heavy, not research-heavy, and the domain (web-scale NLP data) doesn't connect to Nishal's signal processing / audio / embedded ML expertise. While the pipeline fundamentals are transferable, this role would represent a significant pivot away from core competencies.

**North Star score: 3.0/5**

---

## C — Compensation

**Estimate:** Same Cohere MTS band — $185K–$300K CAD range. Data engineering roles may skew slightly lower than modeling/research roles.

**Comp score: 3.8/5**

---

## D — Cultural Signals

- Pre-training data is foundational but less visible than modeling roles
- Remote-friendly, Toronto-accessible
- Same strong Cohere benefits package
- Posting not confirmed active in Ashby live board — found via aggregators

**Culture score: 3.5/5**

---

## G — Posting Legitimacy

- Not found in Ashby live job board as of 2026-05-28
- Multiple job aggregators (BeBee, ZipRecruiter, RemoteITJobs, StudySmarter) have cached the listing
- Posting likely 2–4 months old based on aggregator activity patterns
- Possible the role has been filled or is on hold

**Verdict: Proceed with Caution** (not confirmed active)

---

## Machine Summary

```yaml
role: "Member of Technical Staff, Pre-Training Data"
company: "Cohere"
date: "2026-05-28"
score: 3.4
archetype: "Senior / Staff ML Engineer"
legitimacy: "Proceed with Caution"
location: "London / Toronto / SF / NYC (Remote)"
work_auth_issue: false
url: "https://jobs.ashbyhq.com/cohere/859e2e47-02fb-4afe-bb8a-e83bf4d8c265"
top_match_signals:
  - "ETL and data pipeline engineering at scale (MAS Holdings, Forestpin)"
  - "Dataset curation and quality control (Zenodo datasets)"
  - "Data ablation methodology (JAES 2026)"
key_gaps:
  - "No web-scale or NLP corpus data processing experience"
  - "No Spark/Beam or distributed data framework experience"
  - "Domain mismatch: signal/audio data vs. web/code/multilingual corpora"
recommendation: "Against applying — significant domain gap; verify posting active before considering"
```
