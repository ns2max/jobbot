<!-- Job posting: https://ca.linkedin.com/jobs/view/ai-platform-machine-learning-engineer-at-xyz-reality-4456262756 -->

# 1150 XYZ Reality — AI Platform & ML Engineer — Changelog (2026-09-03)

Pipeline: main-thread eval (61/100 Good Fit) → Fable draft (from the 1131 V1 reference) → main-thread review + compile + trim + verify. Codex exhausted until Oct 3.

## CV — `cv/1116_main_xyz_reality_ai_platform_machine_learning_engineer.tex`
- **Variant V1 (AI-Industry, default).** Tagline `Machine Learning Research Engineer | Deep Learning, Time-Series, Pattern Detection | Applied ML` (byte-identical in cover). The role is applied AI-platform / MLOps engineering — V1's ML-Engineering-first framing (lifecycle, benchmarking, dataset management, CI/CD) is the right lens.
- Summary + Competencies led with the platform-relevant record: **end-to-end ML lifecycle ownership** (acquire → label → train → evaluate → deploy → monitor); **automated frozen-protocol benchmarking + model-validation pipelines**; **large-scale dataset ingestion / management / validation + label-ontology design** (MAS real-time IoT ETL across three continents; 4 open datasets with frozen protocols); **synthetic data generation** (rule-based variation generators + VAE/diffusion prototypes); **CI/CD for ML**; **cloud-to-edge deployment** (14 ms RPi4; MIRaaS edge-to-server; scalable REST APIs; Docker); computer vision; XR head/hand tracking (MUSMET).
- Stack marks PyTorch "working level", Kubernetes "working knowledge"; AWS + Docker held. No MLflow / W&B / Ray / Kubeflow, Jetson/CUDA/TensorRT, Azure/GCP, distributed training, PEFT/LoRA/continual/federated — all named as ramp-up in the cover letter.
- **Grounding fix (Fable stretch flag):** moved the VAE/diffusion clause off the postdoc MUSMET bullet onto the McGill bullet (KG §4.2 sources it there). All numbers verified (14 ms / F1 0.76 / 74x / 31.4% CPU; 300% / 99.5%; F1 0.78); MAS one entry Jan 2015-Jul 2020; Promptly = geometry-alignment algorithm + RIP integration + mechanism consulting, **no patent**; English only; Claude Code named.
- **Cut for the 2-page budget:** template `\newpage`; Forestpin role (low relevance to an AR-platform MLOps role); PhD thesis sub-line; trimmed summary + Highlights; shortened Portfolio/Nebula/LiveLaTeX link text. `\enlargethispage{5\baselineskip}` moved to before Selected Publications (so it stretches page 2, not page 3).
- **Final: exactly 2 pages** (V1 budget). Page 1 ends with full Education, page 2 opens with Portfolio — no orphaned titles. ATS text layer clean (0 cid/replacement, email + phone literal, single-ASCII-hyphen dates). Covered: ML lifecycle, dataset, benchmarking, model-validation, synthetic data, CI/CD, deployment, monitoring, training, Python, PyTorch, Docker, Kubernetes, computer vision, label(-ontology). Honest gaps (cover letter): experiment tracking / model registry, distributed training, MLflow/W&B/Ray/Kubeflow, PEFT/LoRA/continual/federated learning, Jetson/CUDA/TensorRT.

## Cover Letter — `cover_letters/1116_cover_xyz_reality_ai_platform_machine_learning_engineer.tex`
- Plain `article`, 4 paragraphs, "Dear Hiring Manager,". **~1 page.**
- P1: research-to-production hook + full-lifecycle ownership (postdoc + MAS) + the JAES 2026 production result (14 ms / F1 0.76 / 74x).
- P2: the posting's asks in its own vocabulary — scalable training/deploy infrastructure, reproducible environments, automated benchmarking + model-validation, dataset ingestion/management/validation + annotation/label-ontology, synthetic data (rule-based + VAE/diffusion), CI/CD for ML, cloud + embedded deployment, scalable REST inference APIs + edge-to-server.
- **P3 honest ramp note:** hands-on PyTorch (secondary framework), distributed training pipelines, the experiment-tracking / model-registry stack (MLflow, W&B, Ray, Kubeflow), PEFT/LoRA/continual/federated learning, and Jetson/CUDA/TensorRT are areas to ramp on, built on the ML-lifecycle + benchmark-methodology + synthetic-data foundation; his current equivalent of experiment tracking is frozen protocols + versioned data splits + a written experiment record.
- P4: why XYZ Reality — engineering-grade AR for construction; next-gen wearable AI (CV + localisation + BIM + semantic reasoning + AR); new Calgary R&D hub; cloud-to-edge — connected to his industrial-CV + edge-deployment + MUSMET XR-telemetry record. Then PR / no sponsorship / available immediately / open to relocating to Calgary for the new technology hub.

## Company research
- `company_research/xyz-reality.json` (engineering-grade AR for construction; Series B; new Calgary R&D hub; works with CV/Navigation/Embedded/Cloud teams; also posted on Ashby; no grade/salary stated anywhere).

## Open flags for Nishal
- **AI-platform / MLOps role** — under-uses his modelling depth; infra-over-modelling scope is a partial drain.
- **Calgary relocation** for the new technology hub (likely on-site).
- Several named tools run light-to-gap (PyTorch-primacy, distributed training, MLflow/W&B/Ray/Kubeflow, PEFT/LoRA/federated learning, Jetson/CUDA/TensorRT) — the cover letter is upfront.
- No grade/band or salary disclosed. No stated deadline. Canonical apply URL is Ashby (`jobs.ashbyhq.com/xyz-reality`).
