# 362 — Anthropic | Research Engineer, Performance RL

**Date:** 2026-05-28
**URL:** https://job-boards.greenhouse.io/anthropic/jobs/5160330008
**Archetype:** ML Research Engineer
**Score:** 2.5/5
**Legitimacy:** High Confidence
**PDF:** ❌

---

## A — Match con CV

**Role asks for:** CUDA/ROCm/Triton/Pallas expertise, ML frameworks (JAX/PyTorch), full-stack accelerator experience (kernels, model code, distributed systems), RL environments and evaluations for accelerator performance, RL experience, LLM training methodology, porting ML workloads across accelerator types.

**CV match:**
- JAX, PyTorch: both listed in stack — present
- C++: production real-time inference engines at MAS Holdings (embedded/IoT hardware) — relevant but not GPU kernel programming
- Python: extensive — strong
- RL environments + evaluations: limited; RL listed in stack but no published RL research
- CUDA/ROCm/Triton/Pallas: **not demonstrated in CV or knowledge graph** — this is the core technical requirement and a significant gap
- GPU kernel programming / accelerator optimization: no evidence in CV; Nishal's embedded work is on ARM (RPi4) and IoT hardware, not NVIDIA GPU compute
- Full-stack ML model code: present at framework level (PyTorch/JAX), not at kernel level
- Distributed systems: present at IoT/pipeline scale, not GPU-cluster HPC
- LLM training methodology: listed conceptually in stack; not a demonstrated specialty
- Benchmark/experimental design: strong (transferable to RL eval design, but domain gap remains)

**Honest gap:** The Performance RL role sits at the intersection of two specializations Nishal does not have: (1) GPU kernel programming (CUDA/Triton) and (2) reinforcement learning for accelerator workloads. The C++ systems depth and benchmarking methodology are transferable, but the core requirements are not met.

**Score: 2.0/5** (raw) → **2.5/5** (US location cap applied as floor)

---

## B — North Star Alignment

"ML Research Engineer" archetype is a target, but Performance RL is a hardware-systems specialization focused on making GPU kernels run faster for RL training. This is the farthest from Nishal's trajectory (audio/signal/embedded ML) of all 8 roles evaluated.

**Score: 1.5/5** (raw domain alignment)

---

## C — Comp

$350,000–$850,000 USD annually. Top Anthropic range for specialized hardware/RL work. Moot given location.

**Score: 5.0/5** (comp alone)

---

## D — Cultural Signals

- San Francisco only; 25% in-office required
- High specialization role within Code RL team
- Anthropic safety mission
- US work authorization required; visa sponsorship available

Red flag: **US location; requires US work authorization.** Per profile rules: cap = 2.5. Additionally, the technical requirements (CUDA/GPU kernel expertise) represent a fundamental skills gap beyond the location issue.

**Score: 2.5/5**

---

## E — Red Flags

- US location (H-1B visa required; lottery risk)
- CUDA/ROCm/Triton kernel programming — not demonstrated in CV
- RL for accelerator performance — double specialization gap
- Role is among the most technically specialized of all Anthropic RE positions

---

## G — Posting Legitimacy

**Tier: High Confidence**

- Active Greenhouse listing
- Very specific technical requirements (CUDA, ROCm, Triton, Pallas, accelerator porting)
- Anthropic Code RL team is a known initiative
- No ghost signals; specialized enough to be a real, targeted hire

---

## Machine Summary

```yaml
num: 362
company: Anthropic
role: Research Engineer, Performance RL
archetype: ML Research Engineer
score: 2.5
location: San Francisco, CA (US)
remote: false
visa_cap: true
comp_usd: "350000-850000"
legitimacy: High Confidence
apply: false
reason: US work auth required (visa cap); CUDA/GPU kernel expertise and RL-for-accelerators are both material gaps
date: 2026-05-28
```
