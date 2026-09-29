**Job Posting:** https://jobs.ashbyhq.com/liquid-ai/7ce97c55-52f3-4534-b452-917ae8afdc37

---

# Nishal Stanislaus Silva, PhD

Member of Technical Staff, Audio ML | Multimodal · Real-Time Inference · Production Pipelines
*Canadian Permanent Resident — eligible to work in Canada without sponsorship*

- Email: nishal.silva@hotmail.com
- Phone: +1 817 747 8598
- Location: Toronto, ON M6P 1Z2
- Website: https://nishal.xyz
- LinkedIn: https://www.linkedin.com/in/nishal-silva
- GitHub: https://github.com/ns2max
- ORCID: https://orcid.org/0000-0003-0406-7459

---

## Professional Summary

PhD ML Engineer with 10+ years building audio ML systems end-to-end — data pipelines, model training, evaluation infrastructure, and production deployment under hard latency constraints. In my EU-funded MUSMET postdoc, I owned the complete audio ML pipeline from streaming acquisition through edge deployment: **14ms inference with F1=0.76 on Raspberry Pi 4**, 74x faster than baseline. At McGill, I built multimodal audio + IMU sensor systems in real time. At MAS Holdings, I shipped C++ inference engines on industrial IoT hardware at scale.

Production-grade code, rigorous evaluation methodology, and edge inference discipline — built under the constraint of compute budgets that make GPU-scale assumptions a luxury.

10 peer-reviewed publications in audio ML (JAES, IEEE, DAFx, Asilomar). 4 public Zenodo evaluation datasets (7,000+ recordings, 70 musicians).

---

## Core Competencies

**Audio ML:** Real-time audio inference, streaming audio pipelines, multimodal audio + sensor fusion, music information retrieval, audio data curation and evaluation design

**Production Systems:** End-to-end ML pipeline ownership (data → training → eval → deployment), edge-constrained inference (<30ms on RPi4), C++ + Python production code, reproducible research-to-production translation

**Evaluation & Benchmarking:** Ablation methodology, benchmark design from scratch, dataset construction, statistical significance testing (p<0.05 published), distributed evaluation tooling

---

## Technical Stack

**Languages:** Python · C++ · C · MATLAB · JavaScript

**ML / AI:** PyTorch · TensorFlow · JAX · HuggingFace Transformers · scikit-learn · ONNX

**Audio & Signal:** Librosa · SciPy · JUCE · Elk Audio OS · MFCC · STFT · DSP · S-Transform · Real-Time Signal Analysis

**Data & Cloud:** AWS (EC2, S3, SageMaker, MWAA) · Snowflake · SQL · NumPy · Pandas · ETL pipelines

**MLOps:** Docker · Kubernetes · MLFlow · Apache Airflow · Git · CI/CD · Pytest

---

## Education

**Ph.D — Information Engineering and Computer Science**
*University of Trento, Italy* — Jan 2025
*Dissertation: Embedded Real-Time Musical Pattern Detection for Smart Musical Instruments*

**M.Sc — Telecommunication and Electronic Engineering**
*Sheffield Hallam University, UK* — Aug 2018

**B.Eng (Hons) — Electronic Engineering**
*Sheffield Hallam University, UK* — Mar 2014

---

## Professional Experience

### Postdoctoral Researcher | University of Trento, Italy
*Jan 2025 – Dec 2025 | EU-funded MUSMET project*

- Owned full audio ML pipeline end-to-end: streaming audio acquisition → feature engineering → model training → evaluation → edge deployment → monitoring
- **Edge inference:** 14ms latency, F1=0.76 on Raspberry Pi 4; 74× faster than DTW baseline; streaming real-time pipeline (<30ms) with >90% F1 across device profiles
- Built multimodal data pipelines: audio + sensor + gesture data — acquisition, processing, alignment, evaluation
- Curated and released evaluation datasets (DoMP/DoPP/DoDP/DoDP2: 7,000+ recordings, 70 musicians) with rigorous collection protocols; published Zenodo
- Designed evaluation infrastructure: ablation suites, baseline comparisons, latency/compute tradeoff analysis under strict hardware constraints
- Built synthetic audio data generation (VAE + diffusion) for limited labeled-data regimes
- Translated research prototypes into production-grade AI components with reproducible pipelines and deployment documentation

### Visiting Researcher | McGill University, Montreal, Canada
*May 2024 – Aug 2024*

- Prototyped real-time multimodal gesture detection on IMU + audio sensor streams
- Profiled power/compute for edge deployment feasibility; assessed near-real-time inference tradeoffs on mobile/embedded hardware
- Built VAE-based and diffusion-based synthetic audio data generation

### Research Engineer | MAS Holdings (Pvt) Ltd, Colombo, Sri Lanka
*Jan 2015 – Jul 2020*

- Developed C++ and Python real-time inference engines on embedded/IoT hardware: optimized for throughput, latency, reliability
- Built real-time ETL pipelines for high-frequency IoT sensor streams (millions of events/day) across geographically distributed sites
- **Key metrics:** 300% throughput improvement; 99.5% inspection time reduction; 50% operator headcount reduction
- Multi-sensor fusion: camera arrays + IoT sensors for real-time quality control and capacity planning

### Technical Consultant | Forestpin (Pvt) Ltd, Colombo, Sri Lanka
*Aug 2020 – Feb 2021*

- ML + statistical modeling pipelines for financial anomaly detection on large structured datasets
- Python-based backend scoring services for production anomaly flagging

---

## Selected Publications

1. **Real-Time Audio Pattern Detection for Smart Musical Instruments** (JAES, Mar 2026) — F1=0.76 at 14ms on RPi4; 74× over DTW; streaming pipeline
2. **Melody and Motion: Integrating Guitar Gesture Detection with Musical Patterns** (IEEE Internet of Sounds, Oct 2025) — multimodal IMU + audio fusion, real-time
3. **Interactive IoMusT-Based Concerts** (IEEE I3DA, Sep 2025) — real-time audio + sensor streaming; p<0.05 evaluation
4. **A Structural Similarity Index Based Method** (DAFx, Sep 2022) — training-free; 95% accuracy; embedded hardware; SSIM cross-domain from CV to audio

Full list: https://nishal.xyz/publications | Zenodo datasets: https://zenodo.org/record/10818617

---

## Published Datasets

| Dataset | N | Type | DOI |
|---------|---|------|-----|
| DoMP | 4,000 recordings | Monophonic MIDI | 10818617 |
| DoPP | 2,000 recordings | Polyphonic audio | 14497998 |
| DoDP | 2,000 recordings | Drum patterns | 14497974 |
| DoDP2 | 2,000 recordings | Drum patterns | 18395007 |

---

## Scientific Review Service

- IEEE Access (journal reviewer)
- IEEE Internet of Sounds Symposium (program committee)
- IEEE International Conference on Immersive and 3D Audio / I3DA (program committee)

---

## Awards & Recognition

- **Finalist, MIDI Innovation Awards** — 2023
- **GMOA Recognition** — COVID-19 remote patient monitoring deployed in hospital wards
