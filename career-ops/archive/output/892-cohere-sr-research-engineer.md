**Job Posting:** https://jobs.ashbyhq.com/cohere/2d4d224f-94d4-40ce-88d5-5d340bc0da4e

# Nishal Stanislaus Silva, PhD

Machine Learning Research Engineer | Data Pipelines, Benchmarking & Real-Time Inference
*Canadian Permanent Resident — eligible to work in Canada without sponsorship*

- Email: nishal.silva@hotmail.com
- Phone: +1 613 200 2030
- Location: Toronto, ON
- Website: https://nishal.xyz
- LinkedIn: https://www.linkedin.com/in/nishal-silva
- GitHub: https://github.com/ns2max

---

## Professional Summary

Machine Learning Research Engineer with 10+ years across industry and academia, specializing in the intersection of data tooling, benchmarking, and production ML. I own data pipelines end-to-end — acquisition, feature engineering, synthetic + real data integration, training/evaluation, and deployment — and design the benchmark suites (baselines + ablations) that tell teams which architecture and data choices actually move the needle. My postdoctoral work on the EU-funded MUSMET project delivered real-time inference pipelines at <30ms latency and >90% F1, with reproducible, documented tooling built for long-term maintainability. Earlier, at MAS Holdings, I built real-time ETL/ingestion pipelines processing millions of IoT events/day across distributed manufacturing sites, and established the CI/CD and code-review standards that scaled ML adoption across engineering teams. Published researcher (10 peer-reviewed papers, AES/IEEE/DAFx) with a benchmark-first, statistically rigorous approach to experimental design.

---

## Core Competencies

**Data & ML Tooling:** Data Pipeline Design, Real + Synthetic Data Integration, ETL Pipelines, Data Validation & Quality Processes, Benchmarking & Ablations, Experimental Design

**ML Engineering:** End-to-End ML Lifecycle, Real-Time / Low-Latency Inference, Production Deployment, MLOps, Human-in-the-Loop Systems, Model Compression

**Research & Leadership:** Statistical Analysis, Algorithm Design, Cross-Functional Collaboration, Technical Standards Ownership, Team Mentoring, Peer-Reviewed Publications

---

## Technical Stack

**Languages:** Python, C++, C, JavaScript, MATLAB, C#

**ML / AI:** PyTorch, JAX, TensorFlow, Keras, scikit-learn, HuggingFace Transformers, AWS SageMaker, ONNX, Transfer Learning, Diffusion Models, VAE-Based Synthesis

**Data & Analytics:** SQL, Snowflake, AWS (EC2, S3, ECS, MWAA, RDS), NumPy, Pandas, SciPy, ETL Pipelines, Information Retrieval

**Dev & MLOps:** Docker, Kubernetes, MLFlow, Apache Airflow, Jenkins, Git, Pytest, CI/CD, REST APIs

---

## Education

**Ph.D — Information Engineering and Computer Science**
*University of Trento, Italy* — Jan 2025

**M.Sc — Telecommunication and Electronic Engineering**
*Sheffield Hallam University, UK* — Aug 2018

**B.Eng (Hons) — Electronic Engineering**
*Sheffield Hallam University, UK* — Mar 2014

---

## Professional Experience

### Postdoctoral Researcher | University of Trento, Italy
*Jan 2025 – Dec 2025 (EU-funded MUSMET project)*

- Owned the full data pipeline for streaming audio, sensor, and gesture data — acquisition → signal processing → feature engineering → training/evaluation → edge deployment → monitoring — building the tooling that let the team iterate quickly with reproducible results
- Designed benchmark suites (baselines + ablations) to systematically identify architecture and feature coverage gaps, quantifying tradeoffs under latency and compute constraints; achieved <30ms inference at >90% F1 (14ms, F1=0.76, 74× faster than DTW baseline)
- Translated research prototypes into maintainable, production-grade components with reproducible pipelines and deployment documentation — standards adopted by academic and industry partners
- Coordinated cross-institutionally on 3 peer-reviewed publications in 2025

### Visiting Researcher | McGill University, Montreal, Canada
*May 2024 – Aug 2024*

- Built synthetic data generation pipelines (diffusion-based and VAE-based) combined with real multimodal sensor + time-series data to improve model robustness under limited labeled-data regimes
- Computed power/compute profiling to assess real-time inference feasibility and deployment tradeoffs; findings directly shaped deployment decisions

### Technical Consultant | Forestpin (Pvt) Ltd, Colombo, Sri Lanka
*Aug 2020 – Feb 2021*

- Designed and deployed ML and statistical modeling pipelines for financial forensics, compliance monitoring, and risk detection on large structured enterprise datasets
- Built Python + SQL backend scoring services for anomaly flagging and production triage; translated compliance/risk requirements into technical specs

### Research Engineer | MAS Holdings (Pvt) Ltd, Colombo, Sri Lanka
*Jan 2015 – Jul 2020*

- Built real-time data ingestion and ETL pipelines processing millions of IoT and operational time-series events/day across geographically distributed manufacturing sites, with validation and monitoring for consistent reliability
- Led end-to-end ML + CV system development integrating camera and sensor streams into production workflows — operational efficiency improved up to 300%, inspection time reduced 99.5%
- Established CI/CD and code-review standards, mentored engineers, and scaled ML adoption across teams — turning opinionated engineering practices into team-wide defaults
- Cross-functional collaboration with product, operations, and engineering to convert ambiguous business needs into measurable technical specs

---

## Selected Publications

- Silva, N. and Turchet, L. *Real-Time Audio Pattern Detection for Smart Musical Instruments*. Journal of the Audio Engineering Society (JAES), Mar 2026. F1=0.76 at 14ms on RPi4, 74× faster than DTW baseline.
- Silva, N. and Turchet, L. *A Structural Similarity Index Based Method to Detect Symbolic Monophonic Patterns in Real-Time*. DAFx 2022. 95% accuracy, training-free.
- Silva, N., Boem, A. and Turchet, L. *Interactive IoMusT-Based Concerts: Real-Time Pattern Recognition and Audience Experience*. IEEE I3DA 2025.

Full list: https://nishal.xyz/publications

---

## Datasets (Published on Zenodo)

| Dataset | N | Type | DOI |
|---------|---|------|-----|
| DoMP | 4,000 recordings | Monophonic MIDI | 10818617 |
| DoPP | 2,000 recordings | Polyphonic audio | 14497998 |
| DoDP / DoDP2 | 4,000 recordings | Drum patterns | 14497974 / 18395007 |

Total: 7,000+ recordings from 70 musicians. https://zenodo.org/record/10818617

---

## Awards & Recognition

- Finalist, MIDI Innovation Awards (Sep 2023) — real-time symbolic pattern detection for smart instruments
- GMOA Recognition (Sri Lanka) — computer vision system for COVID-19 patient vitals monitoring, deployed across hospital wards
