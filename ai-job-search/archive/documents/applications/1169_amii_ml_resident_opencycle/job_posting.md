<!-- Job posting: https://ca.linkedin.com/jobs/view/machine-learning-resident-%E2%80%93-client-opencycle-12-month-term-at-amii-alberta-machine-intelligence-institute-4457043959 -->
<!-- Archived verbatim from linkedin-search detail on 2026-09-03 (job id 1169). Deadline 2026-09-04. -->

# Machine Learning Resident – Client: OpenCycle (12 month term)

**Company:** Amii (Alberta Machine Intelligence Institute)
**Location:** Edmonton, Alberta, Canada

---

"If you are interested in the application of machine learning to real-world audio for monitoring the noise industry puts into people's lives, this is the right opportunity for you. Be a part of the team of research and machine learning scientists building acoustic intelligence for industrial sites from the ground up and get mentored by some of the best minds in AI during the process." — Kunwar Saaim, Machine Learning Scientist, Advanced Technology

## About The Role

This is a paid residency that will be undertaken over a 12-month period with the potential to be hired by our client, OpenCycle, afterwards (note: at the discretion of the client). The Resident will report to an Amii Scientist and regularly consult with the client team to share insights and engage in knowledge transfer activities. Successful candidates will be members of a cross-functional project team with backgrounds in ML research, project management, software engineering, and new product development. This is a rare opportunity to be mentored by world-class scientists and to develop something truly impactful.

## About The Client

OpenCycle is a Calgary-based acoustic compliance and site-management platform for the energy, municipal, and heavy industries. The company grew out of four decades of professional acoustics consulting: its founders and senior staff have spent their careers on noise impact assessments, complaint investigations, mitigation design, and regulatory negotiation across Alberta, British Columbia, Saskatchewan, and Manitoba. OpenCycle exists to turn that hard-won expertise into software, so that noise compliance — which has traditionally meant months of specialist fieldwork and manual reporting — can be predicted, documented, and cleared in days. Today the platform combines regulatory modelling, site and asset management, and a growing fleet of in-house-designed acoustic monitoring hardware deployed at customer sites across Alberta and BC. Machine learning is not a side project here — it is the core of the company's next generation of product, developed by an in-house engineering team working directly alongside practising acousticians. That proximity is the point: models are specified, labelled, sanity-checked, and ultimately signed off by domain experts inside the same organization, and there is a short, direct line from a research result to a sensor running in a field. The company's mission is to reduce the impact industrial emissions have on people's lives. Noise is where OpenCycle starts, because it is the emission that most directly affects the communities living next to energy and infrastructure development — and because it is the problem this team knows better than anyone.

## About The Project

Environmental noise compliance today answers one question well: how loud was it? A sound level meter returns a number. What it cannot say is what made the noise. Attribution — deciding which of the several sources on and around a site is responsible for the level measured at a home or a receptor — is still done by an acoustician listening to recordings by hand. It is the most expensive and least scalable step in the entire compliance workflow, and it is the step this project automates.

The technical problem. The system has to answer four questions from a single learned representation: is a sound source present, what kind of source is it, which specific physical unit is it, and is that unit operating normally? It has to do this in the open air, where several sources overlap continuously and the interesting one is rarely the loudest. And it has to do it on a battery-powered outdoor node with microcontroller-class compute, reporting over a long-range radio link whose payload is measured in tens of bytes. Sending the audio to a large cloud model is not an option, so the central research question is how much of this capability survives compression to an edge budget.

What already exists. This is not a greenfield exercise. There is a deployed fleet of sound-level-meter nodes running a separately certifiable IEC 61672 measurement chain and validated against reference instruments in the field; a working detection-plus-embedding architecture with quantized, radio-sized payloads; an on-device inference path verified stage-by-stage against the research reference; and a frozen benchmark protocol with cross-site and cross-device evaluation tiers, built deliberately to expose the failure modes this team has already been burned by. There is also a substantial written record of experiments — including the ones that failed, which are often the more useful half.

The open problems. Four, and the Resident would help shape which ones to attack. First, channel invariance: our identity embeddings are currently key on the recording channel rather than the source, and six remediation strategies plus the data-scale hypothesis have been eliminated under controlled comparison, pointing at a label-ontology root cause. Second, tracking and temporal accumulation: fusing observations of the same source over time is the single largest measured improvement we have, turning a hard single-look problem into a tractable one — making the tracker first-class and validating it on real polyphonic field recordings is the dominant unknown before deployment. Third, condition detection from scarce labels: whether the operating state can be represented separately from identity when almost no per-unit multi-state data exists publicly. Fourth, compression: distilling the cross-site stability of a large pretrained audio backbone into something that fits the sensor's compute and bandwidth budget.

What the year looks like. Real deployed hardware and real field data rather than a benchmark exercise; a measurement culture that treats negative results as results and freezes evaluation protocols so experiments months apart stay comparable; scope to publish; and a direct path from a research result to a device in a field that changes how a regulator makes a decision affecting a community. The Resident will work with OpenCycle's engineering team and its acousticians, with field access to the sensor fleet and to the domain experts who produce the ground truth.

## Required Skills / Expertise

We're looking for a talented and enthusiastic individual with a solid background in machine learning, specifically deep learning for audio and acoustic signal processing — sound event detection, audio representation learning, and evaluation that holds up under real-world domain shift.

## Key Responsibilities

- Design, implement, optimize, and evaluate models for far-field acoustic sensing tasks — sound event detection, open-set source identification, and operating-condition / anomaly detection — from a shared learned audio representation.
- Prepare, curate, and preprocess high-quality audio datasets for training or fine-tuning, and validating models, including feature front-end design (log-Mel, PCEN, per-channel and frequency-wise normalization), audio augmentation, label-ontology definition, and work with weak, scarce, or noisy annotations.
- Utilize state-of-the-art pretrained audio backbones (e.g., PANNs / CNN14, AST, BEATs, CLAP) and ML frameworks, tools, and open-source libraries to enhance model performance, accelerate workflows, and optimize data processing.
- Undertake applied research on ML and audio representation-learning techniques to address the limitations in existing models — in particular channel and recording-device invariance, open-set metric learning, and representing operating state separably from source identity.
- Optimize ML pipelines to ensure efficiency, scalability, and real-time streaming processing capabilities on compute- and bandwidth-constrained hardware.
- Collaborate with the project team and stakeholders to develop MVP and client-focused solutions.
- Engage in regular client meetings, contributing to presentations and reports on project progress, and work directly with the practising acousticians who define and sign off on ground truth.

## Required Qualifications

- Completion of an MSc. or PhD in Computer Science or Electrical / Computer Engineering (or a related graduate degree program) with specialization in audio, speech, or acoustic machine learning, signal processing, or a closely related time-series domain.
- Demonstrated hands-on experience applying deep learning to audio — for example, sound event detection, audio classification, audio embedding and verification, or anomalous sound detection.
- Working knowledge of audio signal processing fundamentals: spectrograms and their time–frequency trade-offs.
- Proficient in developing and training, fine-tuning and evaluating machine learning and deep neural network models in PyTorch and/or TensorFlow.
- Proficient in Python programming language and related ML frameworks, libraries, and toolkits (e.g., PyTorch, torchaudio, librosa, HuggingFace, ONNX).
- Solid understanding of classical statistics and its application in model validation.
- Familiarity with Linux, Git version control, and writing clean code.
- A positive attitude towards learning and understanding a new applied domain (environmental acoustics and industrial site operations).
- Must be legally eligible to work in Canada.

## Preferred Qualifications

- Familiarity with and hands-on experience with far-field or environmental audio data.
- Experience with audio embedding and metric learning for open-set recognition, and with domain generalization across recording devices and deployment sites.
- Publication record in peer-reviewed academic conferences or relevant journals in machine learning (e.g., DCASE, ICASSP, INTERSPEECH).
- Good to have: experience deploying models to edge or embedded hardware — quantization, distillation, and designing to a fixed compute budget, with tooling such as ONNX or TFLite.
- Experience/familiarity with software engineering best practices.
- Experience with deploying machine learning models in production environments or strong software engineering (or MLE) skills is a plus.

## Non-Technical Requirements

- Desire to take ownership of a problem and demonstrate leadership skills.
- Interdisciplinary team player enthusiastic about working together to achieve excellence.
- Capable of critical and independent thought.
- Able to communicate technical concepts clearly and advise on the application of machine intelligence.
- Intellectual curiosity and the desire to learn new things, techniques, and technologies.

## Why You Should Apply

Work under the mentorship of an Amii Scientist for the duration of the project. Participate in professional development activities. Gain access to the Amii community and events. Get paid for your work (a fair and equitable rate of pay will be negotiated at the time of offer). Build your professional network. The opportunity for an ongoing machine learning role at the client's organization at the end of the term (at the client's discretion).

## About Amii

One of Canada's three main institutes for artificial intelligence (AI) and machine learning, our world-renowned researchers drive fundamental and applied research at the University of Alberta (and other academic institutions), training some of the world's top scientific talent. Our cross-functional teams work collaboratively with Alberta-based businesses and organizations to build AI capacity and translate scientific advancement into industry adoption and economic impact.

## How to Apply

Closing September 4, 2026 (the posting may come down sooner if the right candidate is found). Send your resume and cover letter indicating why you think you'd be a fit for Amii. In your cover letter, please include one professional accomplishment you are most proud of and why. Applicants must be legally eligible to work in Canada at the time of application. Amii is an equal opportunity employer and values a diverse workforce.
