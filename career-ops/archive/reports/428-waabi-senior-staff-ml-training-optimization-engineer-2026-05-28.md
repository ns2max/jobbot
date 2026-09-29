# Waabi — Senior / Staff ML Training Optimization Engineer

**Date:** 2026-05-28
**URL:** https://jobs.lever.co/waabi/eedaf111-0efd-4f8f-9c2d-ce829b5cb0eb
**Archetype:** Senior / Staff ML Engineer
**Score:** 3.0/5
**Legitimacy:** High Confidence
**PDF:** ❌

---

## Block A — Match with CV

**Archetype fit:** Senior/Staff ML Engineer — distributed training infrastructure, ML training optimization, CUDA profiling, model compilation and deployment.

The role focuses on: scaling distributed training frameworks; profiling CPU/GPU code (PyTorch Profiler, NVIDIA Nsight); identifying bottlenecks in training and inference; evaluating emerging technologies (efficient CUDA kernels, quantization, model compilation, TensorRT); Python + C++/Rust; PyTorch deep experience; data processing + distributed training + deployment pipeline coverage; Bazel build systems (bonus); MS/PhD or BS + 6 years experience.

Nishal's profile: Python + C++ are core. PyTorch is the primary ML framework. End-to-end ML pipeline ownership (data → training → evaluation → deployment) is demonstrated at MUSMET and MAS. Real-time inference optimization is a strength — latency optimization down to 14ms on RPi4, C++ inference engines for embedded/IoT. ONNX is in the stack (relevant for model export). Docker/Kubernetes/MLFlow/CI-CD cover the MLOps side.

Key gaps: GPU training infrastructure at scale is not demonstrated. Nishal's inference optimization is on embedded/edge hardware (RPi4, IoT), not cloud GPU clusters. No CUDA kernel development experience. No NVIDIA Nsight profiling experience. No distributed training at Waabi-scale (multi-node, hundreds of GPUs). Rust is unmet. TensorRT and model compilation pipelines are adjacent (ONNX) but not direct experience.

**CV alignment:** Moderate. Pipeline ownership, deployment, PyTorch, C++, and inference optimization mindset are strong. GPU cluster training infrastructure and CUDA-level profiling are gaps.

**Score: 3.0/5**

---

## Block B — North Star Alignment

"Senior/Staff ML Engineer" is a direct target archetype. The training optimization specialization is infrastructure-adjacent rather than research-adjacent, but it's closer to Nishal's production ML strengths than the pure research scientist roles. Waabi's Toronto/CA eligibility removes the work auth barrier. The role would leverage Nishal's low-latency inference expertise in a new context (GPU training vs. embedded inference).

**Score: 3.0/5**

---

## Block C — Compensation

Salary: $158,000–$269,000 USD for US positions. Toronto equivalent is likely $180K–$280K+ CAD (Waabi is known to pay US-equivalent in Toronto for senior roles). This is at the top of Nishal's target range ($140K–$220K CAD base for Senior MLE, $180K–$220K+ for Staff). Equity + bonus. Strong comp for the right candidate.

**Score: 4.0/5**

---

## Block D — Cultural Signals

Same strong Waabi signals: Raquel Urtasun's team, Toronto HQ, strong engineering culture, competitive comp. Toronto/SF/Dallas/Pittsburgh — CA eligible. The training optimization team works closely with algorithm researchers, which would give Nishal exposure to the core modeling work. Collaborative, open-minded team culture emphasized. Unlimited vacation, flexible hours.

**Score: 4.0/5**

---

## Block E — Red Flags

- **Infrastructure focus:** This is a systems engineering role more than an applied ML role. The work is training pipelines, profiling, CUDA optimization — not modeling, research, or algorithm development. This may feel like a step away from Nishal's research-to-production narrative.
- **GPU infrastructure gap:** No demonstrated experience with large-scale GPU training clusters. Nishal's inference optimization is embedded, not cloud-GPU. This is a teachable gap but a real one.
- **CUDA development:** Custom CUDA kernel development is a bonus but reflects the expected depth — Nishal has no CUDA experience listed.
- **Rust language gap:** Waabi uses Rust; not in Nishal's stack.
- **Level calibration:** "Senior/Staff" implies 6+ years; Nishal's total industry experience covers this, but training optimization infrastructure specifically is not a prior role.

**Score: 2.5/5**

---

## Block F — Global Score

Not applicable (score below 4.0).

| Dimension | Score |
|-----------|-------|
| CV Match | 3.0 |
| North Star | 3.0 |
| Comp | 4.0 |
| Culture | 4.0 |
| Red Flags | 2.5 |
| **Global** | **3.0/5** |

**Recommendation: Decent but not ideal.** Waabi is the right company (Toronto, strong culture, CA eligible, competitive comp). The training optimization role is the closest technical fit among the Waabi batch for Nishal's production ML engineering background. But the gaps in GPU cluster training, CUDA profiling, and large-scale distributed systems are real. Score lands at 3.0 — "decent, apply only if specific reason." Nishal should apply if actively targeting Waabi and willing to frame the embedded inference optimization work as transferable to GPU training optimization (the latency mindset + C++ + PyTorch + pipeline ownership is a credible story).

**If applying:** Lead with MAS Holdings (end-to-end pipeline ownership, C++ inference at scale), MUSMET (14ms RPi4 inference — latency optimization, production-grade ML components), and the ONNX/Docker/CI-CD infrastructure work. Acknowledge the GPU-scale gap directly and frame it as the next frontier from embedded → cloud.

---

## Block G — Posting Legitimacy

- Waabi, well-known AV startup. Lever ATS.
- Detailed technical JD (PyTorch Profiler, NVIDIA Nsight, TensorRT, CUDA, Bazel) — genuine engineering role.
- Salary range published. Multiple consistent listings.
- Remote US+CA and Toronto eligible — active posting.

**Tier: High Confidence** — Real, active posting.

---

## Machine Summary

```yaml
num: 428
company: Waabi
role: Senior / Staff ML Training Optimization Engineer
date: 2026-05-28
score: 3.0
archetype: Senior / Staff ML Engineer
location: Toronto, ON / San Francisco, CA / Remote US+CA
work_auth_required: false
ca_eligible: true
legitimacy: High Confidence
apply: maybe
reason: Best Waabi fit in this batch. Gaps in GPU cluster training and CUDA profiling are real but bridgeable. Strong comp, right company, CA eligible. Consider if actively targeting Waabi.
```
