# Evaluation Report — Senior AI Engineer, Voice Biometrics & Conversational AI @ US Mobile

**Date:** 2026-05-29
**URL:** https://jobs.lever.co/USMobile/fdd50e1b-d3af-4a50-a8d1-957dc1f8bcdd
**Archetype:** ML Research Engineer / Senior / Staff ML Engineer
**Score:** 3.2/5
**Legitimacy:** High Confidence
**PDF:** ❌

---

## A — Match with CV

**Alignment: Moderate**

The role has two phases. Phase 1 (primary focus): voice biometrics and authentication — speaker verification/identification, x-vector/d-vector embeddings, liveness detection, anti-spoofing/deepfake detection. Phase 2 (roadmap): voice AI agents — ASR + LLM + TTS pipelines, streaming audio, low-latency conversational AI.

**What matches:**
- Real-time streaming audio pipelines: Nishal's core — <30ms inference in production, live concert environments (MUSMET)
- Signal processing depth: MFCC, STFT, DSP, onset detection (Asilomar 2018)
- Low-latency audio inference: 14ms on RPi4, C++ production engines
- PyTorch + audio fundamentals: directly applicable to SpeechBrain/model training
- Production edge deployment instinct: would translate to cloud audio inference
- Phase 2 (voice agents) maps closely to Nishal's real-time audio + multimodal system design

**What doesn't match:**
- Phase 1 (primary hire mandate): voice biometrics — x-vectors, d-vectors, speaker embedding extraction, anti-spoofing models — not in Nishal's publication or project record
- Speaker verification/identification: different subdomain from musical pattern recognition, even though both use audio
- SpeechBrain, NVIDIA Riva, Kaldi: not in documented stack
- ASR/TTS pipelines: not demonstrated (musical audio, not speech)
- Deepfake/liveness detection: security domain with no demonstrated background

The gap is subdomain-specific: audio ML fundamentals are directly transferable, but voice biometrics is a distinct specialty requiring speaker recognition experience.

Score: **2.8/5**

---

## B — North Star Alignment

**Alignment: Moderate**

Phase 2 of this role (voice AI agents, ASR+LLM+TTS, speech-to-speech) is exactly the trajectory Nishal is targeting in audio AI. Phase 1 (biometrics) is a useful deep-audio subdomain — not the ideal entry point, but not off-trajectory. The company (US Mobile) is a fast-growing telecom startup, not an AI-first research company. Culture will be more product/engineering-focused than research-oriented. North Star alignment is moderate.

Score: **3.0/5**

---

## C — Location & Work Auth

**Location: Excellent**

Montreal / Toronto. US Mobile is a US company but has a Canadian office in both cities. As a Canadian PR in Toronto, Nishal is work-authorized without any friction. Salary posted: competitive, flexible hours, health insurance, professional development stipend.

Score: **5.0/5**

---

## D — Requirements Gap

**Hard gaps:**
- Voice biometrics experience (x-vectors, speaker verification): not demonstrated
- Anti-spoofing / deepfake audio detection: not demonstrated
- ASR systems (recognition pipeline design): not demonstrated
- SpeechBrain / NVIDIA Riva / Kaldi: not in stack
- 6+ years in speech/audio AI specifically: 10 years total ML, but audio is 5 years (PhD onward)

**Genuine strengths:**
- Real-time audio processing, DSP, streaming pipelines
- Edge inference under latency constraints (<30ms)
- PyTorch, production ML pipelines
- PhD-level audio ML rigor (JAES 2026, Asilomar 2018)

Score: **2.5/5**

---

## E — Culture & Legitimacy

US Mobile is a legitimate company (Forbes top 500 startups, Consumer Reports #1 rated carrier 2 years running, Inc 5000 rank 94). The Montreal/Toronto offices are real, not just registered addresses. Culture is fast-paced startup: "if you work fast, flexibly, and collaboratively." Not a research-first culture. Benefits are solid (competitive salary, flexible hours, health insurance, professional development).

Score: **3.5/5**

---

## F — Decision

**Score: 3.2/5 — Decent but not ideal. Do not apply as first-choice.**

The real-time audio pipeline expertise and low-latency inference background are directly applicable to the Phase 2 roadmap (voice agents). However, the Phase 1 mandate — which is the actual hire focus — is voice biometrics (speaker verification, anti-spoofing), a specialized subdomain with no demonstrated background. The interviewer will ask about x-vector training, speaker embedding extraction, and liveness detection — none of which are in the record.

Worth applying only after audio/speech-focused roles are exhausted. If applying, frame around Phase 2 trajectory and real-time audio system design; acknowledge the biometrics ramp explicitly.

---

## G — Posting Legitimacy

**Tier: High Confidence** — Active on Lever. US Mobile is a real, funded company with Canadian offices.

---

## Machine Summary

```yaml
num: 454
company: US Mobile
role: Senior AI Engineer, Voice Biometrics & Conversational AI
archetype: ML Research Engineer / Senior ML Engineer
score: 3.2
location: Montreal / Toronto (Canadian company, no auth friction)
work_auth: ok
recommendation: skip for now; revisit if audio speech roles exhausted
key_gap: Voice biometrics (x-vectors/speaker verification/anti-spoofing) — subdomain mismatch
key_strength: Real-time streaming audio, <30ms inference, DSP, PyTorch, production audio ML
```
