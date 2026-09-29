# 346 · Anthropic · ML Infrastructure Engineer, Safeguards

**Date:** 2026-05-28
**URL:** https://job-boards.greenhouse.io/anthropic/jobs/4778843008
**Archetype:** Senior / Staff ML Engineer
**Score:** 2.5/5
**Legitimacy:** High Confidence
**PDF:** ❌

---

## Block A — Role Summary

Anthropic seeks an ML Infrastructure Engineer for their Safeguards team to build scalable ML infrastructure supporting real-time and batch classifier and safety evaluations. Responsibilities include designing scalable ML infrastructure for safety classifiers, developing monitoring tools for safety-critical applications, collaborating with research teams to implement safety techniques at scale, and optimizing inference performance with reliability as priority. Location: San Francisco, CA (25% in-office required). Comp: $320K-$405K USD annually. Requires 5+ years building production ML infrastructure in safety-critical domains, Python + PyTorch/TensorFlow/JAX, cloud (AWS/GCP) + Kubernetes, distributed systems for high-throughput workloads, and Spark/Airflow data pipelines. Preferred: LLM experience, A/B testing frameworks, ML monitoring, automated labeling infrastructure, trust & safety domain knowledge, privacy-preserving ML.

---

## Block B — Match with CV

**Strengths:**
- Production ML infrastructure is a genuine strength: end-to-end pipelines at MAS Holdings (millions of IoT events/day, distributed sites, real-time ingestion + ETL)
- Python + PyTorch + JAX in tech stack — exact match to language requirements
- AWS infrastructure experience (EC2, S3, ECS, MWAA, RDS) — direct match to cloud requirement
- Docker + Kubernetes in tech stack — listed requirement met
- Apache Airflow experience — listed requirement met
- MLFlow for experiment tracking and pipeline management
- Safety-critical systems instinct: MAS Holdings manufacturing QC (production-line failure consequences), COVID-19 patient monitoring (deployed in hospital wards, GMOA recognition)
- Monitoring and reliability focus: real-time monitoring at manufacturing scale, <30ms SLAs in MUSMET
- Benchmark-first methodology and ablation design — directly applicable to classifier evaluation infrastructure
- Anomaly detection and compliance monitoring at Forestpin — maps to classifier and safety evaluation patterns
- Human-in-the-loop systems (MAS Holdings inspection models) — relevant to safety classifier workflows

**Gaps:**
- No direct experience with LLM-scale safety classifiers or trust & safety infrastructure
- No experience with Anthropic's specific safety evaluation frameworks or alignment-adjacent tooling
- Kubernetes expertise listed in tech stack but no deep cluster orchestration at ML-serving scale
- San Francisco location: US work authorization required
- No A/B testing framework development or automated labeling infrastructure experience at scale

**CV alignment: Moderate-Good.** This is the strongest technical match in the batch. The ML infrastructure credentials (AWS, Airflow, Docker/Kubernetes, MLFlow, distributed ETL, real-time monitoring) map directly to requirements. Safety-critical deployment instinct is demonstrated (hospital monitoring, manufacturing QC). The gaps are domain-specific (LLM/safety classifier) rather than infrastructure-level. The location is still a hard blocker.

---

## Block C — Level & Strategy

Senior IC role on safety-critical ML infrastructure. Anthropic's Safeguards team builds classifiers that run on every Claude interaction — high-stakes, high-throughput, reliability-first. Nishal's infrastructure and safety-critical deployment credentials map well. The LLM-specific gap is real but this is an infrastructure role, not a research role — the ask is reliable ML pipelines, not frontier model development.

If location were not a blocker, this would score 3.8-4.0: strong infrastructure match, safety-critical deployment experience, right tech stack, relevant methodology. With the US location constraint, capped at 2.5.

**If location resolved (remote or sponsorship):** Worth applying. Frame MAS Holdings as the primary evidence of production ML infrastructure at scale with safety consequences. Forestpin anomaly detection as classifier/monitoring infrastructure analog. Highlight AWS + Airflow + Docker/Kubernetes match explicitly.

---

## Block D — Comp & Location

- **Location:** San Francisco, CA — 25% in-office. **US work authorization required. Score capped at 2.5 per rules.**
- **Comp:** $320K-$405K USD — top-quartile compensation, among the highest in this batch. Inaccessible without US work auth.
- Visa sponsorship available "with reasonable effort" — Anthropic has a stated policy of assessing sponsorship cases. This is one of the more explicit sponsorship openings in this batch.
- **Note:** Anthropic's sponsorship language is meaningfully more open than xAI's. If Nishal is willing to explore US immigration (TN visa as Canadian, O-1 through research credentials), this is worth a direct inquiry before discarding.

---

## Block E — Customization Plan

*(Score 2.5 with location cap — included because of strong technical match and Anthropic's explicit sponsorship openness. Conditional on location resolution.)*

**CV headline:** ML Infrastructure Engineer — Production Safety-Critical Systems

**Key proof points to surface:**
1. MAS Holdings: production ML infrastructure at scale — millions of IoT events/day, distributed sites, real-time ETL, reliability-critical (factory production line)
2. COVID-19 monitoring: deployed ML system in hospital wards during pandemic — GMOA recognition for safety-critical impact
3. Forestpin: classifier-adjacent anomaly detection + compliance monitoring pipeline in Python
4. MUSMET: real-time ML pipeline with <30ms SLAs — monitoring + reliability focus
5. Tech stack: AWS (EC2, S3, ECS, MWAA), Airflow, Docker, Kubernetes, MLFlow, PyTorch, JAX — exact requirements match

**Cover letter angle:** "I've built ML infrastructure where failures have real consequences — manufacturing lines stopping, hospital monitoring failing. The reliability-first mindset the Safeguards team needs is the same engineering discipline I've applied across production deployments. The domain shifts from factory floors to safety classifiers; the infrastructure principles don't."

---

## Block F — Interview Plan

*(Conditional on applying — strong enough technical match to prep)*

**Likely technical focus:**
1. Design a real-time safety classifier serving system at scale (LLM throughput, low latency, high availability)
2. ML pipeline design: data → labeling → training → evaluation → monitoring → feedback loop
3. Distributed systems: how to handle high-throughput classifier workloads with reliability guarantees
4. Incident response: how to detect and respond to classifier performance degradation in production

**Stories to prep:**
- MAS Holdings: scaling from prototype to multi-site production deployment (STAR: problem → architecture decision → tradeoffs → outcome)
- COVID-19 monitoring: reliability under constraints in safety-critical context
- MUSMET: <30ms SLA maintenance and monitoring strategy
- Forestpin: compliance monitoring pipeline design and anomaly flagging logic

**Questions to ask:**
- What's the current throughput and latency budget for safety classifiers running on Claude traffic?
- How does the Safeguards team balance speed of classifier iteration with production reliability requirements?
- What does the feedback loop from safety incidents back to classifier retraining look like?

---

## Block G — Posting Legitimacy

**Tier: High Confidence**

- Greenhouse-hosted with active apply flow
- Specific technical requirements and preferred qualifications (trust & safety, privacy-preserving ML, automated labeling)
- Comp range clearly specified ($320K-$405K) — high transparency
- Anthropic is actively building safety infrastructure for deployed Claude — legitimate, well-funded need
- 25% in-office requirement and rolling review timeline suggest active hiring process

---

## Machine Summary
```yaml
score: 2.5
archetype: Senior / Staff ML Engineer
location_accessible: false
audio_signal_match: false
```
