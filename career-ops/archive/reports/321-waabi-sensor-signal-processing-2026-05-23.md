# Evaluation: Waabi — Research Engineer, Sensor Signal Processing

**Date:** 2026-05-23
**URL:** https://jobs.lever.co/waabi/4a22f57b-cd17-4533-a22b-e927acef834e
**Archetype:** ML Research Engineer
**Score:** 4.5/5
**Legitimacy:** High Confidence
**PDF:** ❌

---

## A) Role Summary

- **Archetype:** ML Research Engineer / Signal Processing Specialist
- **Domain:** Autonomous Driving — Multi-Modal Sensor Signal Processing
- **Function:** Research & Engineering (IC track)
- **Seniority:** Mid–Senior (Research Engineer, no explicit level; PhD preferred)
- **Remote policy:** Remote or Hybrid — Toronto, ON Canada explicitly listed; SF, Dallas, Pittsburgh offices
- **TL;DR:** Design and implement novel signal processing techniques for camera, LiDAR, radar, and other sensor modalities. Optimize algorithms for real-time, latency-sensitive embedded/parallel computing architectures. Contribute to top-tier publications. Classic signal-first ML research role at a Physical AI company.

---

## B) Match with CV

| JD Requirement | CV Evidence |
|----------------|-------------|
| Signal processing fundamentals (classical + learning-based) | DSP · MFCC · STFT · Librosa · SciPy; PhD thesis on real-time signal processing; DAFx 2022 (SSIM-based detection); Asilomar 2018 (S-Transform onset detection) |
| Real-time / latency-sensitive algorithms under compute budget | <30ms inference on Raspberry Pi 4 (MUSMET); 14ms on RPi4 F1=0.76 (JAES 2026); C++ real-time inference engines at MAS Holdings |
| High-throughput data inputs | MAS Holdings: millions of IoT events/day across manufacturing sites; streaming audio + sensor pipelines (MUSMET) |
| Rapid prototyping (Python/Julia/MATLAB) + production-quality software | Python, MATLAB, C++; MAS Holdings production ML/CV systems; MUSMET production-grade components |
| 1D/2D/3D signal processing (nice-to-have) | 1D: audio/MIDI signal processing (DSP, MFCC, STFT); 2D: computer vision (OpenCV, care-label QC, fabric inspection); gesture + IMU multimodal (McGill) |
| Real-time methods: causal filters, RNNs, transformers (nice-to-have) | RNN polyphonic detection (JAES 2026); causal inference pipeline (MUSMET); SSIM method (DAFx 2022) |
| Numerical algorithms / optimization libraries (nice-to-have) | BLAS-adjacent: NumPy/SciPy numerical computing; mathematical optimization in ML models |
| Systems programming + performance profiling (nice-to-have) | C++ real-time engines (MAS); Elk Audio OS embedded deployment; PyTorch Profiler-adjacent optimization |
| Research publication track record | 10 peer-reviewed publications: JAES, IEEE I3DA, DAFx, Asilomar — all audio/signal processing venues |

**Gaps:**
- No LiDAR/radar/autonomous-driving-specific sensor experience (MITIGATED: autonomous driving sensor math is directly transferable from MIR signal processing — same spectral, estimation, Toeplitz matrix fundamentals)
- No BLAS/CHOLMOD/L-BFGS direct mention (MITIGATED: NumPy/SciPy equivalent numerical computing background; Gauss-Newton adjacent work)
- No autonomous driving domain experience per se (MITIGATED: signal processing fundamentals are domain-agnostic; AV sensors are 1D/2D/3D signals)

**Overall:** Extremely strong alignment on the core signal processing + real-time inference stack. The main gap is domain vocabulary (LiDAR/radar vs audio/MIDI), not capability.

---

## C) Level and Strategy

- **Seniority fit:** PhD + postdoc + 5+ years industry = strong fit for Research Engineer at Waabi (typically PhD-preferred)
- **Level signal:** "Research Engineer" at Waabi sits between Research Scientist and SWE; this is the primary IC track for applied signal processing research. PhD publication record positions Nishal well above entry.
- **"Sell senior without lying" plan:**
  - Lead with JAES 2026 as proof of signal processing research depth (peer-reviewed, top audio venue)
  - Frame MAS Holdings real-time embedded work as production-scale signal processing (not just audio) — camera arrays, IoT sensor streams, latency constraints
  - Emphasize 74× speedup over baseline: that's the optimization instinct Waabi wants
  - Mention Asilomar 2018 (S-Transform) to show classical signal processing math depth — frequency domain, spectral analysis, filtering
  - McGill multimodal sensor work shows applicability beyond audio

---

## D) Comp and Demand

- **Posted range:** $155,000–$269,000 USD + equity + annual bonus (US)
- **Canadian equivalent:** Waabi is Toronto-headquartered; Canadian comp typically 10–15% below US equivalent. Estimated $130K–$230K CAD base + equity.
- **Nishal's target:** $200K+ CAD total comp — achievable at mid-to-upper range given PhD + publications
- **Market data:** Waabi Glassdoor: Research Engineer $180K–$220K USD; Toronto ML Research Engineer median ~$148K CAD (Levels.fyi). Waabi typically pays above market.
- **Verdict:** Competitive range aligned with $200K+ CAD target if total comp (base + equity + bonus) is included.

---

## E) Customization Plan

1. **Headline swap:** "Signal Processing ML Research Engineer — Real-Time Audio, Sensor & Embedded Inference" → emphasize signal-first framing
2. **Summary:** Open with the cross-domain signal processing arc (1D audio → 2D CV → IoT sensor streams) and the <30ms latency proof point. Frame PhD as depth in real-time signal processing under compute constraints — directly maps to Waabi's sensor stack.
3. **MUSMET bullet emphasis:** Foreground the "streaming multi-modal sensor data" language from the JD; MUSMET was exactly this: audio + gesture + sensor streams in a real-time pipeline.
4. **MAS Holdings:** Add explicit mention of multi-sensor data fusion (camera + IoT sensor), parallel compute optimization, and embedded C++ inference — maps directly to "parallel computing architectures (CPU, GPU, DSP, accelerators)" requirement.
5. **Publications section:** Order as: Asilomar 2018 (S-Transform — classical DSP math), JAES 2026 (RNN real-time), DAFx 2022 (SSIM — novel signal processing method). This narrative arc shows classical → learning-based progression.

---

## F) Interview Plan

1. **Real-time inference under compute budget (STAR):** MUSMET postdoc → achieving <30ms at >90% F1 on RPi4. Result: 74× faster than DTW baseline. Maps to "latency-sensitive algorithms under limited compute and memory budget."
2. **Novel signal processing method (STAR):** DAFx 2022 → repurposed SSIM metric from computer vision to audio pattern matching. Training-free, 95% detection. Maps to "apply insights from underlying mathematics to design robust numerical algorithms."
3. **Production embedded systems (STAR):** MAS Holdings care-label QC → C++ real-time inference engine on embedded hardware with 99.5% inspection time reduction. Maps to "production-quality software" + "systems programming."
4. **Multi-sensor high-throughput pipeline (STAR):** MAS Holdings IoT data ingestion → millions of events/day, distributed manufacturing sites, real-time ETL. Maps to "high-throughput data inputs."
5. **Cross-domain algorithm transfer (STAR):** McGill gesture detection → multimodal IMU + audio inference with compute profiling for near-real-time edge deployment. Maps to novel sensor modality work.
6. **Benchmark methodology (STAR):** JAES 2026 ablation design → baselines, feature tradeoffs, latency vs accuracy curve. Maps to "comprehensively profiling" and "identifying performance bottlenecks."

---

## G) Posting Legitimacy

- **Source verification:** Listed on Communitech (Toronto tech hub), Remotive, Waabi careers page. Consistent cross-platform listing suggests active posting.
- **Freshness:** No explicit posting date found, but currently indexed on multiple active job boards (Remotive, Communitech) as of May 2026.
- **Company context:** Waabi is active and well-funded ($1B+ raised); Physical AI / autonomous trucking is a live commercial initiative.
- **Apply button:** Lever URL (403 on direct access, but linked through multiple aggregators). Active.
- **Salary posted:** Yes — a positive legitimacy signal for a startup-adjacent company.
- **Tier:** High Confidence

---

## Machine Summary
```yaml
score: 4.5
archetype: ML Research Engineer
location_accessible: true
audio_signal_match: true
```
