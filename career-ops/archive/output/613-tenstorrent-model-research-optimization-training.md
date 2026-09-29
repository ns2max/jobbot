# CV — Nishal Stanislaus Silva, PhD

**Job Posting:** https://job-boards.greenhouse.io/tenstorrent/jobs/5163484007

---

# Nishal Stanislaus Silva, PhD

ML Research Engineer — Model Optimization, Benchmarking & Hardware-Aware Inference
*Canadian Permanent Resident — eligible to work in Canada without sponsorship. Based in Toronto (hybrid-ready).*

- Email: nishal.silva@hotmail.com
- Phone: +1 817 747 8598
- Location: Toronto, ON
- Website: https://nishal.xyz
- LinkedIn: https://www.linkedin.com/in/nishal-silva

---

## Professional Summary

Published ML researcher (PhD, 10 peer-reviewed publications) with 10+ years training, evaluating, and optimizing models to run fast on unconventional hardware. Career theme: take a state-of-the-art model, understand the full stack it runs on, and make it meet hard performance targets — **14ms inference on Raspberry Pi 4 (74× faster than baseline)**, <30ms end-to-end at >90% F1 in production research systems, C++ inference engines at industrial scale. Benchmark-first methodology: systematic baselines, ablations, and architecture/compute trade-off studies. Deep PyTorch and Python; experience spanning model compression, quantization-aware deployment via ONNX, transformers, and generative models.

---

## Core Competencies

**Model Optimization & Inference:** Model compression · ONNX deployment · hardware-aware architecture selection · latency/throughput/accuracy trade-off analysis · bottleneck identification across the stack

**Training & Evaluation:** PyTorch · JAX · benchmark suite design (baselines + ablations) · experimental design · transfer learning · fine-tuning · dataset construction (7,000+ recording public benchmark datasets)

**Research to Production:** Converting research into production-ready systems · reproducible pipelines · cross-team collaboration (academic + industry partners) · technical writing (JAES, IEEE)

---

## Technical Stack

**Languages:** Python · C++ · C · MATLAB · Linux Shell

**ML / AI:** PyTorch · JAX · TensorFlow · Keras · HuggingFace Transformers · ONNX · scikit-learn · AWS SageMaker · LLMs · RAG · diffusion models · VAEs

**Systems:** Embedded/edge inference · Docker · Kubernetes · MLFlow · Airflow · CI/CD · Git · Linux

**Data:** AWS (EC2, S3, ECS, MWAA, RDS) · Snowflake · SQL · NumPy · Pandas · ETL pipelines

---

## Education

**PhD — Information Engineering and Computer Science**
*University of Trento, Italy* — 2025

**MSc — Telecommunication and Electronic Engineering**
*Sheffield Hallam University, UK* — 2018

**BEng (Hons) — Electronic Engineering**
*Sheffield Hallam University, UK* — 2014

---

## Professional Experience

### Postdoctoral Researcher | University of Trento, Italy
*Jan 2025 – Dec 2025 (EU-funded MUSMET project)*

- Led research on real-time model inference optimization under hard latency/compute constraints on edge hardware
- Trained and evaluated sequence models (RNNs) achieving **14ms inference at F1=0.76 on Raspberry Pi 4 — 74× faster than DTW baseline** (published JAES 2026)
- **Designed benchmark suites (baselines + ablations) quantifying architecture/feature trade-offs** — accuracy vs latency vs compute
- Identified bottlenecks across the stack (feature extraction, model architecture, OS-level scheduling) and converted research prototypes into production-ready, documented systems
- Coordinated across academic and industry partners; 3 peer-reviewed publications in 2025

### Visiting Researcher | McGill University, Montreal, Canada
*May 2024 – Aug 2024*

- **Built synthetic data generation (diffusion-based + VAE)** to improve model robustness under limited labeled data
- Power/compute profiling for deployment feasibility on constrained hardware

### Technical Consultant | Forestpin, Colombo, Sri Lanka
*Aug 2020 – Feb 2021*

- ML + statistical modeling for financial anomaly detection on large structured datasets; production Python scoring services

### Research Engineer | MAS Holdings, Colombo, Sri Lanka
*Jan 2015 – Jul 2020*

- Developed **C++ and Python real-time inference engines on embedded/IoT hardware** optimized for throughput, latency, reliability — 300% efficiency improvement at industrial scale
- Built real-time ingestion + ETL for high-frequency time-series across distributed sites (millions of events/day)
- Mentored engineers; established CI/CD and code-review practices to scale ML adoption

---

## Selected Publications (10 total)

- Silva, N. and Turchet, L. (2026). *Real-Time Audio Pattern Detection for Smart Musical Instruments.* Journal of the Audio Engineering Society — model/hardware co-optimization study
- Silva, N. and Turchet, L. (2024). *Real-Time Pattern Recognition of Symbolic Monophonic Music.* Audio Mostly — RNN vs DTW benchmark at scale (98% accuracy)
- Silva, N. and Turchet, L. (2022). *A Structural Similarity Index Based Method to Detect Symbolic Monophonic Patterns in Real-Time.* DAFx — training-free method, 95% accuracy

Full list: https://nishal.xyz/publications

---

## Datasets (Published on Zenodo)

| Dataset | N | Type | DOI |
|---------|---|------|-----|
| DoMP | 4,000 recordings | Monophonic MIDI | 10818617 |
| DoPP | 2,000 recordings | Polyphonic audio | 14497998 |
| DoDP/DoDP2 | 4,000 recordings | Drum patterns | 14497974 / 18395007 |

7,000+ recordings from 70 musicians — designed for reproducible model benchmarking.

---

## Projects

- **Real-Time Polyphonic Audio Pattern Detection** — RNN training + hardware-aware optimization; 14ms on RPi4 (JAES 2026)
- **DTW vs RNN Benchmark Study** — 4,000-pattern dataset; systematic scaling analysis (Audio Mostly 2024)
- **Synthetic Data Generation for Low-Label Regimes** — diffusion + VAE approaches (McGill)
- Actively researching foundation-model-based music generation and synthetic variation generation

---

## Awards & Recognition

- Finalist, MIDI Innovation Awards 2023
- GMOA Recognition — COVID-19 remote patient monitoring deployed in hospital wards

---

## Scientific Committee & Review Service

- IEEE Access (reviewer) · IEEE Internet of Sounds Symposium (program committee) · IEEE I3DA (program committee)
