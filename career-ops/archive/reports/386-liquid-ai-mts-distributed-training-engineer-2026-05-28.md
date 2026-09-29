# 386 — Liquid AI | Member of Technical Staff - Distributed Training Engineer

**Date:** 2026-05-28
**URL:** https://jobs.ashbyhq.com/liquid-ai/a25b97f4-02ee-4453-a2e1-f8d5cfe2c4b4
**Archetype:** Senior/Staff ML Engineer (training infrastructure)
**Score:** 2.3/5
**Legitimacy:** High Confidence
**PDF:** ❌

---

## A — Match with CV

**Role asks for:**
- Building distributed training infrastructure for GPU clusters (PyTorch Distributed DDP/FSDP, DeepSpeed ZeRO, Megatron-LM tensor/pipeline parallelism)
- Diagnosing performance bottlenecks and failure modes (profiling, NCCL/collectives issues, OOMs, stragglers)
- Understanding of hardware accelerators (H100, A100) and networking topologies (InfiniBand, NVLink)
- Topology-aware collectives, comm/compute overlap, straggler mitigation
- Building data loading systems for multimodal datasets eliminating I/O bottlenecks
- Implementing and tuning parallelism/sharding strategies for evolving architectures

**What lands:**
- Python and C++ proficiency — core languages for this role
- Real-time inference optimization under hardware constraints: 14ms on RPi4, 74× DTW speedup
- Performance profiling and optimization: power/compute profiling at McGill, latency/throughput tradeoffs throughout MUSMET
- End-to-end ML pipeline engineering
- Embedded systems and hardware-aware development: C++ inference engines at MAS Holdings

**What doesn't land:**
- No distributed training infrastructure experience — this is the entire job
- No experience with PyTorch DDP/FSDP, DeepSpeed, or Megatron-LM
- No GPU cluster management or NCCL/collectives debugging
- No H100/A100 hardware experience (Nishal's embedded work was on RPi4 and IoT hardware)
- No InfiniBand or NVLink networking experience
- This role is training infrastructure engineering, not ML research or applied ML

**Score: D | 1.5/5** — Hardware-aware engineering instinct is real; the specific distributed training stack is a complete gap.

---

## B — North Star Alignment

Senior/Staff ML Engineer is a target archetype. But this role is a training infrastructure engineering position — it's about making training runs fast and reliable, not about the ML itself. Nishal's engineering strength is in inference and deployment (edge/embedded), not training infrastructure at data-center scale.

This is closer to a Systems/Infra Engineer role than an ML Research Engineer role. It does not map to any of Nishal's six target archetypes in substance.

**Score: D | 1.5/5**

---

## C — Compensation

**Listed:** ~$193K–$242K USD (Glassdoor estimate); 100% medical/dental/vision; equity in unicorn-stage company

Converting at ~$1.38 CAD/USD: $266K–$334K CAD. Exceeds the $180K–$220K+ CAD staff target. However, this is US-based and requires US work authorization.

**Score: B+ | 4.0/5** (strong comp if eligible; US requirement is the blocker)

---

## D — Cultural Signals & Location

- Location: San Francisco, CA (primary); Cambridge/Boston also noted
- Liquid AI: MIT CSAIL spinout, building Liquid Foundation Models (LFMs) — novel architecture (not pure transformer), small focused team
- High-ownership, fast-feedback-loop culture — "build from scratch rather than inherit mature infrastructure"
- Visa sponsorship: O-1 and H-1B sponsored for exceptional talent
- No Canada-remote path — US-based role requiring US work authorization

**Red flag:** Role requires US work auth. Liquid AI sponsors H-1B, but as a Canadian PR, Nishal would need H-1B sponsorship to work in the US — this is a meaningful friction point (lottery-dependent, multi-year process).

**Score: C- | 2.0/5**

---

## E — Red Flags

1. **US work authorization required:** Liquid AI is a US company. Canadian PR does not confer US work rights. H-1B sponsorship is available but lottery-dependent.
2. **Distributed training stack gap (critical):** PyTorch DDP/FSDP, DeepSpeed ZeRO, Megatron-LM — all absent from CV.
3. **Infrastructure engineering, not ML research:** The role is systems work (training runtime, collectives, straggler mitigation), not applied ML.
4. **GPU cluster networking:** NCCL, InfiniBand, NVLink — specialized networking stack with no background.
5. **Prior Liquid AI evaluations:** 3 previous Liquid AI roles evaluated (reports 227, 229, 230) — all discarded due to US location and role mismatch. Pattern consistent.

---

## G — Posting Legitimacy

- Active Ashby listing
- Liquid AI is a well-funded, active startup (MIT spinout, known hiring)
- Role specificity is high — not a ghost posting
- Consistent with their known training infrastructure needs

**Legitimacy: High Confidence**

---

## Machine Summary

```yaml
num: 386
company: Liquid AI
role: MTS - Distributed Training Engineer
date: 2026-05-28
score: 2.3
archetype: Senior/Staff ML Engineer (training infra)
location: San Francisco, CA / Cambridge, MA
remote: no (US-based)
visa_sponsorship: yes (H-1B, O-1)
canada_remote: no
us_work_auth_required: yes
comp_usd_range: 193000-242000
apply_recommendation: against
blockers:
  - US work authorization required (Canadian PR)
  - No distributed training infrastructure experience
  - PyTorch DDP/FSDP, DeepSpeed, Megatron-LM all absent
  - Training infra role, not ML research
highlights:
  - Hardware-aware performance optimization instinct
  - C++ and Python proficiency
  - Strong compensation range
legitimacy: High Confidence
notes: Fourth Liquid AI eval — prior 3 (reports 227, 229, 230) all discarded for similar reasons
```
