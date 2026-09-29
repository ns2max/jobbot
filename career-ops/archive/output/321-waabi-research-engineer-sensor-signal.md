**Job Posting:** https://jobs.lever.co/waabi/4a22f57b-cd17-4533-a22b-e927acef834e

---

# Nishal Stanislaus Silva, PhD

Signal Processing ML Research Engineer | Real-Time · Embedded · Audio/Sensor/CV
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

PhD Signal Processing ML Research Engineer with 10+ years building and shipping real-time inference systems on 1D audio, 2D visual, and multimodal sensor data. Research focus: real-time pattern recognition under strict latency and compute constraints — **<30ms inference at >90% F1 on Raspberry Pi 4**, **74x faster than the DTW baseline** (JAES 2026). Classical signal processing math depth (S-Transform, SSIM, spectral analysis) combined with production engineering instinct (C++ inference engines, IoT-scale deployments).

Published across top audio and signal processing venues: JAES, IEEE Internet of Sounds, DAFx, Asilomar. Cross-domain experience: 1D time-series (audio/MIDI), 2D vision (industrial inspection), and multimodal sensor fusion (gesture + audio + IoT). Research page: https://nishal.xyz/research.html | Publications: https://nishal.xyz/publications

---

## Core Competencies

**Signal Processing:** Classical DSP (S-Transform, STFT, MFCC, spectral analysis, causal filtering), learning-based methods (RNN, Transformers), 1D/2D/3D signal domains, multimodal sensor fusion

**Real-Time Systems:** Latency-constrained inference (<30ms on embedded hardware), C++ inference engines, parallel compute optimization, embedded/edge deployment (RPi4, Elk Audio OS)

**Research & Benchmarking:** Experimental design, ablation methodology, baseline comparison, publication track record (10 peer-reviewed papers in audio/signal processing venues)

---

## Technical Stack

**Languages:** Python · C++ · C · MATLAB · JavaScript

**ML / AI:** PyTorch · TensorFlow · JAX · HuggingFace Transformers · scikit-learn · ONNX

**Signal & Audio:** DSP · MFCC · STFT · S-Transform · SSIM · Librosa · SciPy · JUCE · Elk Audio OS · Music Information Retrieval · Gesture/IMU Sensing

**Data & Cloud:** AWS (EC2, S3, SageMaker) · NumPy · Pandas · SQL · OpenCV · ETL pipelines

**MLOps & Dev:** Docker · Kubernetes · MLFlow · Apache Airflow · Git · CI/CD · Pytest

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

- Owned end-to-end ML pipeline for multimodal signal processing: streaming audio, sensor, gesture data — acquisition → signal processing → feature engineering → training/evaluation → edge deployment
- Achieved **14ms inference, F1=0.76 on Raspberry Pi 4**; 74x faster than DTW baseline — under live performance latency constraints
- Built real-time causal RNN inference pipeline for polyphonic audio pattern detection (<30ms streaming)
- Designed and ran ablation studies quantifying architecture/feature tradeoffs under latency/compute budgets; published methodology
- Developed novel signal processing algorithms from literature distillation; prototyped and benchmarked against baselines
- 3 peer-reviewed publications (2025); presented at IEEE Internet of Sounds and I3DA conferences

### Visiting Researcher | McGill University, Montreal, Canada
*May 2024 – Aug 2024*

- Prototyped real-time gesture detection on multimodal sensor + time-series data (IMU + audio); profiled power/compute for deployment feasibility
- Built synthetic audio data generation (diffusion-based + VAE) for limited labeled-data regimes
- Assessed near-real-time edge inference trade-offs on mobile/embedded hardware

### Research Engineer | MAS Holdings (Pvt) Ltd, Colombo, Sri Lanka
*Jan 2015 – Jul 2020*

- Built C++ and Python real-time inference engines on embedded/IoT hardware; optimized for throughput, latency, reliability
- Led end-to-end ML + computer vision systems on camera + sensor streams for production manufacturing
- **Key metrics:** 300% throughput improvement; 99.5% inspection time reduction on care label QC; 50% operator headcount reduction on fabric QC
- Developed data ingestion + ETL pipelines for high-frequency IoT sensor streams (millions of events/day) across distributed sites
- Multi-sensor fusion: camera arrays + IoT sensors for real-time quality control and capacity planning

### Visiting Researcher | University of Visual and Performing Arts, Sri Lanka
*Jan 2024 – Mar 2024*

- Human-centered evaluations of ML-driven interactive systems; combined quantitative metrics + user feedback into actionable recommendations

### Technical Consultant | Forestpin (Pvt) Ltd, Sri Lanka
*Aug 2020 – Feb 2021*

- ML + statistical modeling pipelines for financial anomaly detection and compliance monitoring at scale

---

## Publications (Signal Processing Focus)

1. **Real-Time Audio Pattern Detection for Smart Musical Instruments** (JAES, Mar 2026) — F1=0.76 at 14ms on RPi4, 74x faster than DTW. https://aes.org/publications/elibrary-page?id=23129
2. **Melody and Motion: Integrating Guitar Gesture Detection with Musical Patterns** (IEEE Internet of Sounds, Oct 2025) — multimodal IMU + audio signal fusion, real-time
3. **Interactive IoMusT-Based Concerts** (IEEE I3DA, Sep 2025) — real-time pattern recognition, signal-driven peripheral control. https://ieeexplore.ieee.org/document/11202042
4. **Real-Time Pattern Recognition of Symbolic Monophonic Music** (Audio Mostly, Sep 2024)
5. **A Structural Similarity Index Based Method to Detect Symbolic Monophonic Patterns in Real-Time** (DAFx, Sep 2022) — training-free, 95% accuracy; SSIM repurposed from 2D image processing to 1D signal matching. https://dafx2020.mdw.ac.at/proceedings/papers/DAFx20in22_paper_18.pdf
6. **Towards Real-Time Detection of Symbolic Musical Patterns: Probabilistic vs. Deterministic Methods** (FRUCT, Apr 2021)
7. **On Musical Onset Detection via the S-Transform** (Asilomar, Oct 2018) — classical DSP; frequency-dependent band splitting for onset detection

Full list: https://nishal.xyz/publications | Zenodo datasets: https://zenodo.org/record/10818617

---

## Selected Projects

- **Real-Time Polyphonic Audio Pattern Detection** — RNN, F1=0.76, 14ms on RPi4; 74x over DTW; streaming pipeline (JAES 2026)
- **SSIM-Based Real-Time Signal Detection** — Cross-domain SSIM from 2D CV to 1D audio; training-free, 95% accuracy; embedded (DAFx 2022)
- **Guitar Gesture + Audio Multimodal** — IMU + audio; real-time inference; McGill + UniTrento (IEEE Internet of Sounds 2025)
- **Automated Care Label QC** — OpenCV real-time CV; 99.5% inspection time reduction; deployed at industrial scale
- **Automated Fabric Quality Checking** — Real-time microscopic camera arrays; weave defect detection at the loom
- **Datasets (DoMP/DoPP/DoDP/DoDP2)** — 7,000+ recordings, 70 musicians; public Zenodo release

---

## Published Datasets

| Dataset | N | Type | DOI |
|---------|---|------|-----|
| DoMP | 4,000 recordings | Monophonic MIDI | 10818617 |
| DoPP | 2,000 recordings | Polyphonic audio | 14497998 |
| DoDP | 2,000 recordings | Drum patterns | 14497974 |
| DoDP2 | 2,000 recordings | Drum patterns | 18395007 |

---

## Awards & Recognition

- **Finalist, MIDI Innovation Awards** — 2023 (real-time symbolic pattern detection)
- **GMOA Recognition** — COVID-19 remote patient monitoring system deployed in hospital wards

---

## Scientific Review Service

- IEEE Access (journal reviewer)
- IEEE Internet of Sounds Symposium (program committee)
- IEEE International Conference on Immersive and 3D Audio / I3DA (program committee)
