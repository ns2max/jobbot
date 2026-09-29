<!-- Job posting: https://ca.linkedin.com/jobs/view/machine-learning-resident-%E2%80%93-client-opencycle-12-month-term-at-amii-alberta-machine-intelligence-institute-4457043959 -->

# 1169 Amii / OpenCycle — CV + Cover Letter Changelog (2026-09-03)

## CV — `cv/1135_main_amii_ml_resident_opencycle.tex`
- **Variant: V3 (Edge / Embedded).** Tagline `ML Research Engineer | Real-Time & Edge Inference | Audio, Sensor & Time-Series` (byte-identical in the cover letter). The JD's required-skills line (DL for audio, SED, representation learning, evaluation under domain shift, real-time streaming on compute/bandwidth-constrained hardware) and its central research question (capability vs. edge budget) map onto V3 almost exactly.
- **Emphasized:** streaming-audio pipeline ownership; spectrogram + feature front-ends (STFT/log-Mel/MFCC/PCEN/normalization); compression/quantization to an edge budget; JAES 14 ms / F1 0.76 / 74x / 31.4% CPU; frozen-protocol benchmark suites + negative-results record; label taxonomy + dataset curation (4 Zenodo sets); temporal accumulation via hierarchical-FSM fusion (F1 0.78); scarce-label training-free + VAE/diffusion; delivery to non-ML domain experts (MAS); open-set recognition; academic service (reviewer + PC).
- **Cut:** LiveLaTeX (portfolio + experience — irrelevant to acoustics); UVPA visiting-researcher role (human-centred eval, lowest relevance); Melody & Motion + ACM Audio Mostly publications (kept 5: JAES, Smart Drums, MIRaaS, DAFx SSIM, Asilomar); Smart Drums project bullet (overlaps a publication); merged Data & Cloud + Dev & MLOps stack lines; the hardcoded template `\newpage` (was stranding a near-empty page 2).
- **Grounding fixes from the Codex-equivalent reviewer:** "four open audio datasets" → "musical-pattern datasets" (3 of 4 are MIDI); "microcontroller-class hardware" → "ARM embedded hardware"; MAS "models handed to non-ML operators who signed off on production" → "the overlay letting line operators adjudicate borderline rejects"; DoDP/DoDP2 "recordings" → "MIDI recordings"; "distillation" removed from the stack (profile evidences quantization + ARM profiling, not distillation); "9,800+" / "70+ musicians" kept as the sanctioned phrasing. **95% SSIM figure kept** — verified in knowledge-graph §13/§16 (reviewer flagged it, but it is grounded).
- **Final page count: 3** (V3 budget is 2-3). ATS text layer clean (pdftotext, 0 cid/replacement chars, email + phone literal, date ranges single ASCII hyphen).
- Keyword coverage: covered — sound event detection, audio representation, domain shift, log-Mel, PCEN, spectrogram, quantization, torchaudio, ONNX, TFLite, open-set, label-ontology, PyTorch, TensorFlow, streaming, embedded. Honestly absent (gap, addressed in the cover letter, not stuffed): far-field, IEC 61672, distillation, DCASE/ICASSP/INTERSPEECH venues.

## Cover Letter — `cover_letters/1135_cover_amii_ml_resident_opencycle.tex`
- **5 short paragraphs**, per the posting's override of the default 4-paragraph template. Addressee "Dear Hiring Manager,".
- P1 hook: role + the JAES 14 ms / F1 0.76 / 74x proof point tied to the compression-to-edge question.
- P2: honest position on 3 of the 4 open problems (pipeline ownership in TF+PyTorch; label-ontology match; temporal accumulation via McGill HFSM, F1 0.78); open-set metric learning, PCEN, the named backbones, and far-field acoustics + IEC 61672 named explicitly as learn-on-the-job, with the manufacturing/forensics domain-transfer precedent.
- P3 (mandatory): proudest accomplishment = the JAES 2026 system, with an explicit personal "why" (research result + on-device system + answer to "how much can you strip away").
- P4 (mandatory): why **Amii** specifically — one of Canada's three national AI institutes (Mila, Vector); residency structure corrected (resident reports to an Amii Scientist, cross-functional team); MAS = "five and a half years" (fixed from the draft's "a decade"); OpenCycle specifics from verified research — "regulator accepted", millions of validated data points, 1,000+ monitoring days, 30 years as Patching Associates (why the labels exist).
- P5: PR / no sponsorship / available immediately / open to Alberta relocation.
- **Grounding/style fixes:** Re: line em-dash → comma; "ten years" → "10+ years" (twice); "I have defined the ontology" softened to "I defined the label taxonomy and curated the annotations"; "channel invariance IS a label-ontology problem" → "your suspicion that ... matches what I ran into" (posting says *suspected*); "I would rather work on it than almost anything else" toned down; cut the redundant second half of P3.
- Trimmed twice to hold **exactly 1 page**.
- `% VERIFY` claims both confirmed by research and inlined: Amii = 1 of Canada's 3 national AI institutes; Amii RL reputation + U of A ties (the RL sentence was then cut as inert name-dropping).

## Company research written
- `company_research/amii.json`, `company_research/opencycle.json` (OpenCycle = formerly Patching Associates Acoustical Engineering, Calgary).

## Open flags for Nishal
- 12-month fixed term, conversion at OpenCycle's sole discretion; comp likely below the CAD 120-150k benchmark; Edmonton/Calgary relocation away from the live eBay Toronto + SciNet processes. Confirm before submitting.
- Deadline **2026-09-04**, may close earlier.
