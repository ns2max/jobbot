# 385 — Anthropic | Staff Research Engineer, Discovery Team

**Date:** 2026-05-28
**URL:** https://job-boards.greenhouse.io/anthropic/jobs/4593216008
**Archetype:** Senior/Staff ML Engineer / ML Research Engineer
**Score:** 3.2/5
**Legitimacy:** High Confidence
**PDF:** ❌

---

## A — Match with CV

**Role asks for:**
- 8+ years of ML research experience
- Familiarity with large-scale LLM training, evaluation, and inference pipelines
- Performance optimization and distributed computing expertise
- Track record shipping ML systems for multi-step reasoning problems
- Creating benchmarks and evaluation frameworks for scientific workflows
- Scaling prototypes into production systems
- Preferred: LLM inference optimization, RL, containerization, VM/sandboxing, large-scale infra

**What lands:**
- 10+ years ML experience across research and production (MAS Holdings 2015–2020, MUSMET postdoc 2025–2025)
- End-to-end ML pipeline ownership: MUSMET (acquisition → signal processing → feature engineering → training → edge deployment → monitoring)
- Benchmark and evaluation framework creation: JAES 2026 (F1, ablations), DoMP/DoPP/DoDP datasets, MUSMET benchmark suites
- Scaling prototypes to production: MUSMET (research → production-grade AI components), MAS Holdings (CV prototypes → manufacturing scale)
- Performance optimization under constraints: 14ms inference on RPi4, 74× faster than DTW baseline
- Real-time inference pipeline engineering
- C++ and Python development for inference engines

**What doesn't land:**
- No LLM-scale training experience — "large-scale LLM training" means multi-thousand GPU clusters
- No distributed computing experience at LLM scale (PyTorch Distributed, DeepSpeed, Megatron-LM)
- No long-horizon task completion or complex reasoning research
- No containerization (Docker noted in stack but at basic level), no VM/sandboxing deployment
- "AI scientist" framing of this team — it's about building AI that does science, a specific research direction

**Score: C+ | 3.2/5** — Strong ML engineering fundamentals and benchmark methodology, but LLM infrastructure and reasoning systems are gaps.

---

## B — North Star Alignment

Staff Research Engineer and Senior/Staff ML Engineer are target archetypes. This role is the best archetype fit in this batch — it combines research engineering with production scaling and benchmark creation. However, the domain (building an AI scientist for long-horizon scientific reasoning) requires LLM systems experience that Nishal doesn't yet have.

The "Discovery Team" context means frontier research engineering at the edge of what's possible — typically requires people already working with LLMs at scale.

**Score: C+ | 3.0/5**

---

## C — Compensation

**Listed:** $350,000–$850,000 USD annually

Wide band for a Staff-level role. At Staff level, likely $500K–$850K USD. Exceeds CAD targets significantly. US-based comp.

**Score: A | 5.0/5** (comp excellent; US role)

---

## D — Cultural Signals & Location

- San Francisco, CA — hybrid, minimum 25% in-office
- Visa sponsorship: available
- Discovery Team is a prestigious internal research group at Anthropic building "scientific AGI"
- Strong engineering culture — full stack from infra to research
- No Canada-remote path visible

**Score: C | 2.5/5**

---

## E — Red Flags

1. **LLM-scale infrastructure gap:** The role requires familiarity with large-scale LLM training and inference; Nishal's experience is in edge/embedded ML, not data-center-scale systems.
2. **8+ years ML research requirement:** Nishal has 10+ years total ML experience (2015–present) — meets the floor, but the experience mix (audio/CV/embedded) is different from what this team likely expects.
3. **Long-horizon task completion research:** Specific area with no background in the CV.
4. **SF hybrid required:** No Canada-remote path.
5. **"Scientific AGI" framing:** This is frontier AI research at a very specific intersection; the team likely requires LLM systems experience as a hard prerequisite.

---

## G — Posting Legitimacy

- Active Greenhouse listing (older job ID: 4593216008 — worth noting, may be a long-running posting)
- Detailed technical requirements
- Consistent with Anthropic's known research engineering roles

**Legitimacy: High Confidence** (note: older posting ID — role may have been open for some time)

---

## Machine Summary

```yaml
num: 385
company: Anthropic
role: Staff Research Engineer, Discovery Team
date: 2026-05-28
score: 3.2
archetype: Staff ML Engineer / ML Research Engineer
location: San Francisco, CA (hybrid)
remote: partial (25% minimum in-office)
visa_sponsorship: yes
canada_remote: no
comp_usd_range: 350000-850000
apply_recommendation: against
blockers:
  - No LLM-scale training or distributed computing experience
  - No long-horizon reasoning systems research
  - SF hybrid required, no Canada-remote path
highlights:
  - Strong benchmark/evaluation methodology
  - End-to-end pipeline ownership
  - Performance optimization under constraints
  - 10+ years ML experience meets floor
legitimacy: High Confidence
notes: Older posting ID (4593216008) — may be a long-running or evergreen posting
```
