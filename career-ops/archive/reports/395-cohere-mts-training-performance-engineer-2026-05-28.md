# 395 — Cohere — Member of Technical Staff, Training Performance Engineer

**Date:** 2026-05-28
**URL:** https://jobs.ashbyhq.com/cohere/d42f5fd4-1ffc-45b9-957c-f09862db6af6
**Archetype:** Senior / Staff ML Engineer
**Score:** 2.8 / 5
**Legitimacy:** High Confidence
**PDF:** ❌

---

## A — Match with CV

**Alignment: Weak — specialized systems role**

This is the Pre-Training team's performance engineering role. The work is optimizing LLM training throughput, GPU/accelerator utilization, and removing bottlenecks in large-scale distributed training. Requirements:
- Extremely strong software engineering skills
- Python + JAX, PyTorch, XLA/MLIR
- Experience writing GPU kernels using CUDA, triton
- Experience with large-scale distributed training strategies
- Familiarity with autoregressive sequence models (Transformers)

**What matches:**
- **Python + ML frameworks:** PyTorch, JAX, TF — confirmed in Nishal's stack
- **Software engineering fundamentals:** C++ and Python production codebases at MAS Holdings; real-time inference optimization
- **Performance optimization instinct:** 14ms inference on RPi4 (74× faster than baseline) demonstrates deep performance optimization under hardware constraints
- **Transformer familiarity:** Listed in ML domains; JAES 2026 uses sequence models
- **Benchmarking methodology:** F1, ablations, latency profiling at MUSMET — transfers to profiling/benchmarking training runs
- **Bonus:** Publications at JAES, IEEE, DAFx qualify for the paper-at-top-tier-venue bonus

**What doesn't match:**
- **CUDA/triton kernel writing:** Not documented in Nishal's background. This is the core hard skill for this role.
- **XLA/MLIR:** Not in Nishal's documented stack
- **Large-scale distributed training:** Nishal's scale is edge/embedded (RPi4), not GPU clusters with thousands of accelerators
- **Pre-training LLM pipelines:** No experience with LLM pre-training; Nishal's training work is domain-specific small models (audio pattern detection, gesture recognition)
- **Training throughput optimization at cluster scale:** Fundamentally different from embedded inference optimization

**Gap assessment:** The performance optimization instinct is there, but the specific technical domain (GPU kernel writing, CUDA/triton, distributed training at cluster scale) is a deep specialization gap. This requires years of low-level GPU programming experience that isn't in Nishal's background.

---

## B — North Star Alignment

**Archetype match: Partial — Senior/Staff ML Engineer**

The archetype is closest to Senior/Staff ML Engineer (systems-focused), but the specific sub-domain (GPU kernel engineering for pre-training) is the most specialized role in this batch. Nishal's differentiators don't apply here:
- Signal processing / audio / MIR: not relevant
- Embedded ML: different optimization layer entirely
- Published research: bonus qualification only, not differentiating for this role
- Multimodal systems: not the focus

The performance optimization mindset transfers conceptually, but the execution requires skills Nishal doesn't currently have.

---

## C — Compensation

**No explicit salary posted.** Cohere MTS compensation estimate: $120K–$160K CAD base + equity (same band as #394, possibly higher for infra specialization).

Given the deep specialization required (CUDA/triton), candidates who clear the bar typically command premium comp. However, Nishal would not be a top candidate for this role, limiting negotiating leverage.

Score: **2.5 / 5** — Comp range not differentiated enough to overcome fit concerns.

---

## D — Cultural Signals

Same Cohere overview as #393/#394. Toronto-based, remote-flexible.

**Specific to Pre-Training team:**
- Deep technical team; highly specialized
- Close to Cohere's core technical moat (training frontier LLMs)
- Long iteration cycles (pre-training runs take days/weeks)
- Intellectually rigorous environment; publications valued

**Positives:**
- Cohere's pre-training team is technically elite
- Toronto HQ, no location friction
- Strong learning opportunity for GPU systems

**Concerns:**
- This role hires specialists; generalists rarely clear the bar without CUDA experience
- Career path highly dependent on GPU kernel expertise — narrow specialization

---

## E — Red Flags

1. **Core specialization gap: CUDA/triton kernel writing.** This is the primary hard requirement and it's not in Nishal's background. Not a bridgeable gap for an application today.
2. **Distributed training at LLM scale.** Fundamentally different from embedded inference; months to years of ramp time.
3. **XLA/MLIR not in stack.** Secondary requirement but adds to gap.
4. **Role is a deep specialization hire.** Companies hiring for Training Performance Engineer want someone who has already done it. Less amenable to adjacent-skills pivots than research/applied science roles.

---

## G — Posting Legitimacy

- **Apply button:** Active on Ashby; multiple aggregators list this role (BeBee, Index Ventures, Remote IT Jobs)
- **Posting age:** Active; no closure signals
- **Role-company fit:** Very high — training performance is core to Cohere's competitive moat
- **No ghost signals**

**Verdict: High Confidence** — Real, active opening. The problem is fit, not legitimacy.

---

## Machine Summary

```yaml
num: 395
company: Cohere
role: Member of Technical Staff, Training Performance Engineer
score: 2.8
archetype: Senior / Staff ML Engineer (training infra specialization)
location: Remote-flexible (Toronto HQ) — no location friction
location_risk: none — Canadian company
comp_cad_est: 130000-170000 base + equity (estimated)
us_work_auth_required: false
apply_recommendation: against — CUDA/triton kernel writing is a hard requirement not in background
top_gap: CUDA/triton GPU kernel writing; large-scale distributed training; XLA/MLIR
top_strength: Performance optimization instinct (14ms embedded, 74x speedup), Python/JAX/PyTorch, publications at top-tier venues (bonus)
legitimacy: High Confidence
status: Evaluated
```
