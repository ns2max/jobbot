# 344 · Together AI · Staff Machine Learning Engineer, Voice AI

**Date:** 2026-05-28
**URL:** https://job-boards.greenhouse.io/togetherai/jobs/5140763007
**Archetype:** Senior / Staff ML Engineer
**Score:** 3.2/5
**Legitimacy:** High Confidence
**PDF:** ❌

---

## Block A — Role Summary

Together AI seeks a Staff ML Engineer to lead their voice inference platform: speech-to-text, text-to-speech, and emerging speech-to-speech architectures. Responsibilities include leading the voice inference technical roadmap, optimizing latency/throughput/GPU utilization for voice models, designing serving architecture for serverless and dedicated endpoints with real-time audio streaming, building evaluation frameworks (WER, naturalness, latency), enabling audio-native LLMs and codec-based systems, managing integrations with Cartesia/Deepgram/Rime, and leading voice fine-tuning capabilities. Requires 8+ years ML engineering with model serving/inference optimization, deep expertise in LLM serving engines (vLLM, SGLang, TensorRT-LLM), expert Python + PyTorch with CUDA/GPU optimization, and proven system design at scale. Location: San Francisco. Comp: $220K-$280K USD base + equity. Preferred: speech/audio ML background, audio codecs (SNAC, Encodec, DAC), speech model training/fine-tuning at scale.

---

## Block B — Match with CV

**Strengths:**
- Audio ML is a core domain: 10+ publications in audio/MIR, PhD in signal processing, real-time audio pattern detection systems
- Real-time audio pipeline engineering: streaming audio acquisition → signal processing → feature engineering → inference → monitoring (MUSMET postdoc)
- <30ms latency on edge hardware — directly relevant to latency-sensitive voice serving mindset
- Signal processing expertise (MFCC, STFT, DSP, Librosa, SciPy) maps to audio preprocessing for ASR/TTS
- Evaluation framework design: built WER/F1/coherence benchmarks; systematic ablation methodology
- Experience with diffusion-based + VAE-based audio synthesis (McGill) — adjacent to modern TTS architectures
- Published on audio pattern detection (JAES 2026, DAFx 2022) — demonstrates audio systems thinking at depth
- IoMusT ecosystem (IEEE I3DA 2025) — real-time audio streaming infrastructure with peripheral device coordination

**Gaps:**
- Hard gap: no experience with LLM serving engines (vLLM, SGLang, TensorRT-LLM) — the role's listed core requirement
- No GPU optimization experience (CUDA, memory profiling at GPU cluster level) — work has been edge/embedded hardware
- No direct ASR/TTS model engineering experience — audio work was musical pattern detection, not speech recognition/synthesis
- Audio codec experience (SNAC, Encodec, DAC) not present — only traditional DSP codecs
- 8+ years requirement: Nishal has 10+ years total ML experience but the LLM serving specialization is absent
- No experience with production voice inference at scale (Cartesia/Deepgram-type systems)

**CV alignment: Moderate.** The audio domain alignment is the strongest match in this batch and is genuinely differentiated — very few ML engineers combine audio signal processing depth with production ML systems experience. However, the "Staff" framing at Together AI is tightly scoped around GPU inference optimization for LLM serving stacks, which is a hard technical gap. The preferred qualifications (audio background, signal processing) are a very strong fit; the required qualifications (vLLM, CUDA, GPU optimization) are a gap.

---

## Block C — Level & Strategy

Staff-level IC with technical leadership scope. The role is essentially: "senior inference engineer who also understands audio deeply." Nishal has the second half and not the first. If Together AI were willing to train on the inference stack, this would be a strong fit. Worth applying only if the job description suggests flexibility — the "preferred" audio background signals they may not easily find someone who has both, which creates an opening.

**If applying:** Lead with the audio domain expertise as differentiator. JAES 2026 (<30ms, F1=0.76), MUSMET real-time pipeline, diffusion synthesis at McGill. Frame the latency engineering at edge as transferable inference optimization methodology. Be explicit about GPU serving gap but position as the candidate who can close it fast given the infrastructure background. Target the "preferred" overlap heavily.

---

## Block D — Comp & Location

- **Location:** San Francisco — US onsite. **Work auth required for US. Score capped given this is a US-only role.**
- However, Together AI has a distributed presence (Singapore, Amsterdam offices) and some remote tolerance. Not confirmed for this role.
- **Comp:** $220K-$280K USD base — well within Staff ML Engineer range; compelling if accessible.
- No explicit relocation support mentioned.

---

## Block E — Customization Plan

*(Score 3.2 — borderline. Included given the uniquely strong audio domain alignment and differentiated profile opportunity.)*

**CV headline:** Staff ML Engineer — Audio, Real-Time Inference & Voice Systems

**Professional summary emphasis:**
- Lead with: "Published audio ML researcher (AES, IEEE) and production systems engineer with <30ms real-time audio inference on edge hardware and 300% throughput gains at industrial scale"
- Frame: "Among the few ML engineers who combine deep signal processing expertise with production ML deployment — built complete audio pipelines from streaming input through feature extraction to deployed inference under strict latency constraints"

**Key proof points to surface:**
1. JAES 2026: <30ms audio pattern detection on RPi4, F1=0.76, 74x faster than baseline — real-time audio inference under hardware constraints
2. MUSMET: end-to-end real-time audio pipeline in production (streaming → processing → inference → monitoring)
3. McGill: diffusion-based + VAE-based audio synthesis — adjacent to modern TTS generative architectures
4. IEEE I3DA 2025: IoMusT real-time audio streaming coordinating peripheral devices — multi-system audio serving architecture

**Cover letter angle:** "Voice AI is at an inflection point where the hardest problems are at the intersection of audio signal understanding and low-latency serving infrastructure. I've spent 10 years on the audio side — now I want to apply that domain depth to the serving challenges at Together AI's scale."

---

## Block G — Posting Legitimacy

**Tier: High Confidence**

- Greenhouse-hosted with active apply flow
- Highly specific role (voice inference platform, Cartesia/Deepgram/Rime integrations named explicitly)
- Realistic comp range for Staff ML Engineer
- Together AI has active voice product investments — legitimate organizational need
- Preferred qualifications (audio codecs, ASR/TTS) suggest genuine search for domain specialist

---

## Machine Summary
```yaml
score: 3.2
archetype: Senior / Staff ML Engineer
location_accessible: false
audio_signal_match: true
```
