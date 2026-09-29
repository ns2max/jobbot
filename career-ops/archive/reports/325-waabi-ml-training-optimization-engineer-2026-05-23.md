# Evaluation: Waabi — Senior / Staff ML Training Optimization Engineer

**Date:** 2026-05-23
**URL:** https://jobs.lever.co/waabi/eedaf111-0efd-4f8f-9c2d-ce829b5cb0eb
**Archetype:** Senior / Staff ML Engineer
**Score:** 3.4/5
**Legitimacy:** High Confidence
**PDF:** ❌

---

## Block A — Role Summary

| Field | Detail |
|-------|--------|
| Archetype | Senior / Staff ML Engineer |
| Domain | Distributed ML training infrastructure / Performance engineering |
| Function | Build — standardized training frameworks, GPU/CPU profiling, CUDA optimization |
| Seniority | Senior / Staff |
| Remote | Remote US & Canada (offices: Toronto, SF, Dallas, Pittsburgh, Phoenix) |
| Team size | Not stated |
| TL;DR | Build and optimize distributed training frameworks for AV foundation models — CUDA kernels, GPU profiling, quantization, Kubernetes-based training platforms. |

---

## Block B — Match with CV

### Strengths

| JD Requirement | CV Evidence |
|----------------|-------------|
| MS/PhD or 4+ years industry in CS / related | PhD (2025) + 10+ years industry experience |
| Python proficiency | Python listed as primary language across all roles |
| PyTorch / JAX experience | PyTorch + JAX in tech stack; used in published research |
| Distributed training awareness | AWS SageMaker, Kubernetes, Docker in stack; large-scale IoT pipelines at MAS Holdings |
| Collaborative team mindset | MUSMET postdoc (cross-institutional); MAS Holdings (cross-functional) |
| Passion for self-driving (culture) | Passion for applied ML and real-time systems |

### Gaps

| Gap | Blocker? | Mitigation |
|-----|----------|-----------|
| CPU/GPU profiling with PyTorch Profiler + NVIDIA Nsight | Hard gap — core requirement | No profiling tool experience documented; conceptually familiar with latency optimization but not GPU-level profiling |
| Custom CUDA kernel development | Hard gap — listed as preferred but likely screened for | No CUDA experience in CV or publications |
| C++ for training infrastructure (Rust mentioned) | Partial gap | C++ used at MAS Holdings (inference engines) and embedded ML, but not for training framework development |
| Bazel in monorepo environments | Nice-to-have gap | No Bazel experience; standard Python tooling used |
| Kubernetes-based training platforms | Partial gap | Kubernetes listed in stack but in MLOps context, not training platform design |
| Foundation model scale training | Hard gap | Research training at postdoc scale (single-GPU, RPi4); not at AV foundation model distributed scale |

**Gap assessment:** Nishal's profile is production inference / edge deployment — the inverse of training optimization. The role requires deep GPU internals expertise (CUDA, Nsight, profiling) and distributed training at scale. While Python/PyTorch overlap exists, the core skills (CUDA kernels, training framework design) are not demonstrated.

---

## Block C — Level and Strategy

**Level detected:** Senior / Staff ML Engineer in training infrastructure — requires 4+ years industry-focused specifically on ML training systems.

**Candidate's natural level:** Strong at Senior ML Engineer for inference / deployment. Not profiled for training infrastructure engineering.

**Sell senior plan:** Lean into end-to-end pipeline ownership (MUSMET postdoc, MAS Holdings). Frame the C++ inference engine work as systems-level ML. Emphasize benchmark-first methodology (profiling latency at edge). However, the specific training infrastructure skills are not substitutable.

**If downleveled:** Domain gap means downleveling doesn't resolve the core mismatch.

---

## Block D — Comp and Demand

| Item | Detail |
|------|--------|
| JD stated range | $141,000–$249,000 USD + equity + bonus |
| Canadian equivalent (approx) | $192K–$340K CAD |
| Comp vs target | Above C$200K target |
| Demand trend | ML training optimization specialists: scarce, high demand |

---

## Block E — Customization Plan

Not recommended for application. Core skill gaps in GPU profiling and CUDA are hard blockers.

---

## Block F — Interview Plan

Not prepared — role not recommended.

---

## Block G — Posting Legitimacy

**Freshness:** Active Lever posting. Waabi actively scaling its training infrastructure team.

**Description quality:** Specific technologies named (CUDA, Nsight, Bazel, Kubernetes). Compensation published. Realistic, well-scoped JD.

**Company hiring signals:** No layoff signals. Active growth company.

**Legitimacy verdict:** High Confidence — genuine open role.

---

## Recommendation

**Score: 3.4/5 — Skip.**

Legitimate role with excellent comp at a strong Toronto company. However, this is a training infrastructure engineering role requiring GPU-level expertise (CUDA, Nsight profiling, custom kernel development) that Nishal has not demonstrated. His strengths are on the inference/deployment end of the pipeline. Worth monitoring if he develops training systems expertise, but not actionable now.

---

## Machine Summary
```yaml
score: 3.4
archetype: Senior / Staff ML Engineer
location_accessible: true
audio_signal_match: false
```
