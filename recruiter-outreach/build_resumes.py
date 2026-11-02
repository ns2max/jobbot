#!/usr/bin/env python3
"""Build recruiter-specific resumes from the GOLDEN generic resume with minimal, auditable edits.

Source: ai-job-search/resume_generic/Nishal_Silva_ML_Research_Engineer.tex (never compiled in place).
Every edit is an exact string replacement on the golden text; the build fails if any anchor is missing,
so a change to the golden file can't silently produce a wrong resume.

Output per recruiter: recruiter-outreach/<NN>_<org>/Nishal_Silva_Resume.{tex,pdf,txt} + CHANGES.md
Usage: python3 recruiter-outreach/build_resumes.py
"""
import re
import shutil
import subprocess
import sys
from pathlib import Path

from pypdf import PdfReader

ROOT = Path(__file__).resolve().parent
GOLDEN = ROOT.parent / "ai-job-search/resume_generic/Nishal_Silva_ML_Research_Engineer.tex"

# ---------------------------------------------------------------- golden anchors
G_TAGLINE = "Machine Learning Research Engineer | Deep Learning, Time-Series, Pattern Detection | Applied ML"
G_STATUS = r"Canadian Permanent Resident $\cdot$ Eligible to work in Canada without sponsorship"
G_SUM3 = ("My work spans across real-time and streaming ML, time-series modeling, and pattern/anomaly "
          "detection across sequential data, computer vision, and structured datasets.")
G_DOMAIN = ("Time-Series Analysis, Anomaly Detection, Recommender Systems, Ranking Systems, Computer Vision, "
            "Multimodal Data Modeling, Embeddings, Pattern Recognition, NLP, Signal Processing / DSP, Generative AI")
G_MLENG = "Multi-Tenant ML Systems, MLOps, Prompt engineering, AI Ethics, Human-in-the-Loop Systems"
G_MLAI = ("Tensorflow, Keras, PyTorch, JAX, scikit-learn, HuggingFace Transformers, LLMs, RAG, AWS SageMaker, "
          "Transfer Learning, OpenCV, Librosa, NumPy, Pandas, SciPy")
G_DEVOPS_LINE = (r"\textbf{Dev \& MLOps:} Docker, Kubernetes, MLFlow, Apache Airflow, Jenkins, Git, Linux/UNIX, "
                 "Pytest, Unit Testing, CI/CD, REST APIs, ONNX")
G_NEBULA = "Released Nebula, an open-source C++17 feature-extraction library for sequential time series data."
G_PD1 = ("Owned full ML pipelines for streaming multi-dimensional data (EU-funded MUSMET project), covering data "
         "acquisition, signal processing, feature engineering, training/evaluation, and deployment with monitoring.")
G_PD4 = (r"    \item Coordinated with academic and industry partners to move ML prototypes from research into "
         "documented, production-grade components, covering the full arc from novel prototyping to deployment.\n")
G_FP2 = ("Worked with compliance and risk stakeholders to define detection requirements and turn them into "
         "technical specs, keeping business and engineering tightly aligned.")
G_MAS3 = ("Developed ML-driven optimization and decision engines to support real-time monitoring and long-term "
          "capacity/efficiency planning from streaming machine and sensor data.")
G_MAS5 = (r"    \item Worked closely with product, operations, and engineering stakeholders to define scope and "
          "delivery milestones, consistently turning business needs into specific, measurable technical solutions.\n")

EMBEDDED_LINE = (r"\\" "\n" r"\textbf{Embedded \& Hardware:} Raspberry Pi / ARM, Embedded Linux, Arduino, STM32, PIC, "
                 r"IMU / I2C Sensors, PLC Interfacing")
AUDIO_LINE = (r"\\" "\n" r"\textbf{Audio \& Real-Time:} JUCE, VST, Elk Audio OS, OSC, MIDI, FFTW, libsndfile, "
              "Raspberry Pi / ARM")

# ---------------------------------------------------------------- edits applied to every resume
# Both fixes come from knowledge-graph.md §15-16 / the ai-job-search verification checklist.
COMMON = [
    ("Retire '>90% F1' (KG §16: never cite it) -> verified 74x-vs-DTW figure",
     r"(<30ms real-time inference, >90\% F1, and up to 300\%",
     r"(<30ms real-time inference, 74x faster than a DTW baseline, and up to 300\%"),
    ("Postdoc bullet: '>90% F1' -> published 14ms / F1 0.76 on Raspberry Pi 4",
     r"hitting <30ms latency at >90\% F1, with",
     r"hitting <30ms latency (published: 14ms on Raspberry Pi 4, F1 0.76), with"),
    ("Line spacing 1.05 -> 1.03 so the minimal edits keep the golden 2-page layout",
     r"\setstretch{1.05}", r"\setstretch{1.03}"),
    ("Date ranges use an ASCII hyphen instead of an en-dash (ATS date parsing)",
     r"\textit{\small #4 -- #5}", r"\textit{\small #4 - #5}"),
]

# ---------------------------------------------------------------- variant edit sets
V1 = []  # golden as-is

INDUSTRIAL_CV = [
    ("Tagline -> industrial CV focus (V5)", G_TAGLINE,
     r"Computer Vision \& ML Engineer | Industrial Inspection, Real-Time \& Edge Deployment | Applied ML"),
    ("Summary: lead the domain list with production CV / inspection", G_SUM3,
     "My work spans across production computer vision and industrial inspection, real-time and streaming ML, "
     "time-series modeling, and pattern/anomaly detection across image, sensor, and structured datasets."),
    ("Domain Expertise: Computer Vision + Industrial Inspection moved first (reorder, nothing removed)", G_DOMAIN,
     r"Computer Vision, Industrial Inspection \& Defect Detection, Time-Series Analysis, Anomaly Detection, "
     "Pattern Recognition, Multimodal Data Modeling, Signal Processing / DSP, Embeddings, Recommender Systems, "
     "Ranking Systems, NLP, Generative AI"),
    ("ML Engineering: swap Multi-Tenant/Prompt engineering/AI Ethics for Edge Deployment + Camera & PLC Integration",
     G_MLENG, r"MLOps, Edge Deployment, Camera \& PLC Integration, Human-in-the-Loop Systems"),
    ("ML/AI stack: OpenCV moved to second position", G_MLAI,
     "OpenCV, PyTorch, Tensorflow, Keras, scikit-learn, JAX, HuggingFace Transformers, LLMs, RAG, AWS SageMaker, "
     "Transfer Learning, Librosa, NumPy, Pandas, SciPy"),
    ("Postdoc trimmed to 3 bullets (V5 weighting: MAS carries the CV evidence)", G_PD4, ""),
    ("MAS: generic optimization bullet -> concrete vision-plus-machinery integration (Promptly, PLC/C++)", G_MAS3,
     "Integrated vision with production machinery: geometry-alignment algorithm for two-sided garment printing "
     "(Promptly, now a commercial Twinery product) and C++ closed-loop PLC/RIP control on industrial printers."),
    ("MAS: stakeholder bullet -> named inspection results (care-label QC, fabric defect detection)", G_MAS5,
     r"    \item Built multilingual care-label QC (OpenCV feature matching, conveyor + PLC reject; -99.5\% inspection "
     r"time) and a microscopic camera-array fabric defect detector (-50\% operators)." "\n"),
]

AUDIO = [
    ("Tagline -> audio / DSP focus (V4)", G_TAGLINE,
     r"Machine Learning Research Engineer | Audio ML, DSP \& Real-Time Embedded Inference | Applied ML"),
    ("Summary: lead the domain list with real-time audio / signal ML", G_SUM3,
     "My work spans across real-time audio and signal ML, embedded/edge inference, time-series modeling, and "
     "pattern/anomaly detection across sequential data, computer vision, and structured datasets."),
    ("Domain Expertise: Signal Processing / DSP + Audio ML/MIR moved first (reorder, nothing removed)", G_DOMAIN,
     r"Signal Processing / DSP, Audio ML \& Music Information Retrieval, Time-Series Analysis, Pattern Recognition, "
     "Anomaly Detection, Multimodal Data Modeling, Computer Vision, Embeddings, Recommender Systems, "
     "Ranking Systems, NLP, Generative AI"),
    ("ML/AI stack: Librosa moved up", G_MLAI,
     "Tensorflow, Keras, PyTorch, Librosa, JAX, scikit-learn, HuggingFace Transformers, LLMs, RAG, "
     "AWS SageMaker, Transfer Learning, OpenCV, NumPy, Pandas, SciPy"),
    ("Technical Stack: + 'Audio & Real-Time' line (JUCE, VST, Elk Audio OS, OSC, MIDI, FFTW)",
     G_DEVOPS_LINE, G_DEVOPS_LINE + AUDIO_LINE),
    ("Nebula bullet: name the audio features and ARM latency benchmarks", G_NEBULA,
     "Released Nebula, an open-source C++17 audio feature-extraction library with ARM latency benchmarks."),
    ("Postdoc bullet 1: 'multi-dimensional data' -> audio + IMU, deployed as VST on Raspberry Pi / Elk Audio OS",
     G_PD1,
     "Owned full ML pipelines for streaming audio + IMU data (EU-funded MUSMET project), covering acquisition, "
     "DSP, feature engineering, training/evaluation, and deployment as VST plugins on Raspberry Pi / Elk Audio OS."),
    ("Postdoc trimmed to 3 bullets to hold 2 pages after the added stack line", G_PD4, ""),
]

SIGNAL_MED = [
    ("Tagline -> real-time signal / time-series focus", G_TAGLINE,
     r"Machine Learning Research Engineer | Real-Time Signal ML, Time-Series \& Edge Inference | Applied ML"),
    ("Summary: lead with raw-signal / sensor ML and note deployed healthcare monitoring", G_SUM3,
     "My work spans across real-time signal and sensor ML, time-series modeling, and pattern/anomaly detection "
     "across raw signals, computer vision, and structured datasets, including a hospital-deployed monitoring system."),
    ("Domain Expertise: Signal Processing first, + Sensor Fusion (reorder, nothing removed)", G_DOMAIN,
     r"Signal Processing / DSP, Time-Series Analysis, Pattern Recognition, Anomaly Detection, "
     r"Multimodal Data Modeling \& Sensor Fusion, Computer Vision, Embeddings, Recommender Systems, Ranking Systems, "
     "NLP, Generative AI"),
    ("Postdoc bullet 4: partner-coordination -> multimodal audio + BCI/EEG + XR sync pipeline (KG §4.1)", G_PD4,
     r"    \item Built a real-time sync pipeline for audio, BCI/EEG (with g.tec) and mixed-reality tracking across 4 performers." "\n"),
]

FINANCE = [
    ("Tagline: 'Pattern Detection' -> 'Anomaly Detection'", G_TAGLINE,
     "Machine Learning Research Engineer | Deep Learning, Time-Series, Anomaly Detection | Applied ML"),
    ("Domain Expertise: Anomaly Detection first, + Tabular / Structured Data Modeling", G_DOMAIN,
     "Anomaly Detection, Time-Series Analysis, Tabular / Structured Data Modeling, Computer Vision, "
     "Recommender Systems, Ranking Systems, Multimodal Data Modeling, Embeddings, Pattern Recognition, NLP, "
     "Signal Processing / DSP, Generative AI"),
    ("Forestpin: + production SQL/Python anomaly-scoring bullet (KG §4.4)", G_FP2,
     G_FP2 + "\n" r"    \item Built SQL + Python backend scoring services for anomaly flagging and triage in production."),
    ("Postdoc trimmed to 3 bullets to hold 2 pages", G_PD4, ""),
]

EDGE = [
    ("Tagline -> edge / embedded focus (V3)", G_TAGLINE,
     r"ML Research Engineer | Real-Time \& Edge Inference | Audio, Sensor \& Time-Series"),
    ("Summary: lead with embedded / edge inference and sensing", G_SUM3,
     "My work spans across real-time ML on embedded and edge hardware, sensor and signal processing, time-series "
     "modeling, and pattern/anomaly detection across sequential data, computer vision, and structured datasets."),
    ("Domain Expertise: Signal Processing first (reorder, nothing removed)", G_DOMAIN,
     r"Signal Processing / DSP, Time-Series Analysis, Pattern Recognition, Multimodal Data Modeling \& Sensor Fusion, "
     "Computer Vision, Anomaly Detection, Embeddings, Recommender Systems, Ranking Systems, NLP, Generative AI"),
    ("Technical Stack: + 'Embedded & Hardware' line (RPi/ARM, STM32, PIC, IMU/I2C, PLC)",
     G_DEVOPS_LINE, G_DEVOPS_LINE + EMBEDDED_LINE),
    ("Nebula bullet: + ARM/Raspberry Pi latency benchmarks", G_NEBULA,
     "Released Nebula, an open-source C++17 time-series feature-extraction library with ARM latency benchmarks."),
    ("Postdoc trimmed to 3 bullets to hold 2 pages after the added stack line", G_PD4, ""),
]

# Recipient-level extras
FETCH_EXTRA = [("Domain Expertise: Computer Vision moved to second (firm recruits ML + CV specialists)", G_DOMAIN,
                "Time-Series Analysis, Computer Vision, Anomaly Detection, Recommender Systems, Ranking Systems, "
                "Multimodal Data Modeling, Embeddings, Pattern Recognition, NLP, Signal Processing / DSP, Generative AI")]
MEDTECH_HW_EXTRA = [("Technical Stack: + 'Embedded & Hardware' line (MedTech / product-development searches)",
                     G_DEVOPS_LINE, G_DEVOPS_LINE + EMBEDDED_LINE)]
SOUNDSKRIT_EXTRA = [("Languages: C++ listed first (audio software / embedded C++ team)",
                     "Python, C++, C, JavaScript, MATLAB, C\\#", "C++, Python, C, JavaScript, MATLAB, C\\#")]


def status(extra):
    return ("Status line: + '" + extra + "'", G_STATUS, G_STATUS + r" $\cdot$ " + extra)


# ---------------------------------------------------------------- recipients (published-email rows only)
# (folder, org, contact, email, csv priority, variant name, edits)
RECIPIENTS = [
    ("01_luxtronic", "LuxTronic", "James C. Evans (hiring inbox)", "contact@luxtronic.ai", "1", "Industrial CV (V5)",
     INDUSTRIAL_CV + [status("Available for remote work from Canada")]),
    ("02_bluewrist", "Bluewrist", "Hiring team", "jobs@bluewrist.com", "1", "Industrial CV (V5)", INDUSTRIAL_CV),
    ("03_novarc-technologies", "Novarc Technologies", "Technical hiring team", "careers@novarctech.com", "1",
     "Industrial CV (V5)", INDUSTRIAL_CV + [status("Open to relocation to Vancouver")]),
    ("04_aavaa", "AAVAA", "Hiring team", "info@aavaa.com", "1", "Audio / DSP (V4-lite)",
     AUDIO + [status("Open to relocation to Montreal")]),
    ("05_layer6-td", "Layer 6 / TD", "Recruitment team", "career@layer6.ai", "1", "Applied ML - anomaly/finance (V1)",
     FINANCE),
    ("06_fetch-recruiters", "Fetch Recruiters", "Alexia Corrado (alternate: Carlos Morales)",
     "alexia@fetchrecruiters.com", "1", "Applied ML (V1)",
     FETCH_EXTRA + [status("Open to Toronto or Montreal")]),
    ("07_mac-recruitment", "MAC Recruitment", "Morgan Rich (shared inbox)", "hello@macrecruitment.ca", "1",
     "Signal ML + embedded hardware (V3/V5 blend)",
     [e for e in SIGNAL_MED if e[1] != G_PD4]
     + [("Postdoc trimmed to 3 bullets so the added hardware line holds 2 pages", G_PD4, "")]
     + MEDTECH_HW_EXTRA + [status("Open to roles across Canada")]),
    ("08_groom-associates", "Groom & Associates", "Emily Woods", "emily.woods@groomassocies.com", "1",
     "Applied ML (V1)", [status("Open to relocation to Montreal")]),
    ("09_goldbeck-recruiting", "Goldbeck Recruiting", "Reiniell Gan", "reiniell@goldbeck.com", "1",
     "Industrial CV (V5)", INDUSTRIAL_CV + [status("Open to relocation to Vancouver")]),
    ("10_oncoustics", "Oncoustics", "Founders / hiring team", "founders@oncoustics.com", "2",
     "Real-time signal ML (V1 signal-focused)", SIGNAL_MED),
    ("11_soundskrit", "Soundskrit", "Frederic Lepoutre / software team", "contactus@soundskrit.ca", "2",
     "Audio / DSP (V4-lite)", AUDIO + SOUNDSKRIT_EXTRA + [status("Open to relocation to Montreal")]),
    ("12_canny-vision", "Canny Vision", "Founders / engineering team", "contacts@canny.vision", "2",
     "Industrial CV (V5)", INDUSTRIAL_CV),
    ("13_gurulink", "GuruLink", "AI / data recruitment team", "info@gurulink.ca", "2", "Applied ML (V1)",
     [status("Open to Toronto, Montreal, Vancouver or remote")]),
    ("14_stack-it-recruitment", "STACK IT Recruitment", "Data & AI recruitment team", "info@stackitrecruitment.com",
     "2", "Applied ML (V1)", [status("Open to roles across Canada")]),
    ("15_10-percent-recruiting", "10 Percent Recruiting", "AI recruitment team", "hello@10pr.ca", "2",
     "Applied ML (V1)", [status("Open to relocation to Alberta")]),
    ("16_hays", "Hays", "Casey Thompson", "casey.thompson@hays.ca", "2", "Applied ML (V1)", V1),
    ("17_vanjobs", "VANJOBS", "Mark Strong (portal preferred)", "mark@vanjobs.ca", "2", "Edge / embedded (V3)",
     EDGE + [status("Open to relocation to Vancouver")]),
    ("18_kovasys", "Kovasys", "Technology / data recruitment team", "talent@kovasys.com", "3", "Applied ML (V1)",
     [status("Open to relocation within Canada")]),
]


def apply(text, edits):
    log = []
    for desc, old, new in edits:
        n = text.count(old)
        if n != 1:
            sys.exit(f"anchor for '{desc}' found {n} times; golden resume changed?")
        text = text.replace(old, new)
        log.append(desc)
    return text, log


def verify(pdf, txt):
    pages = len(PdfReader(str(pdf)).pages)
    subprocess.run(["pdftotext", "-layout", str(pdf), str(txt)], check=True)
    t = txt.read_text()
    flat = re.sub(r"\s+", " ", t)
    checks = {
        "pages == 2": pages == 2,
        "no (cid:) / U+FFFD": "(cid:" not in t and "�" not in t,
        "email literal": "nishal.silva@hotmail.com" in t,
        "phone literal": "+1 613 200 2030" in t,
        "no '>90% F1'": ">90%" not in flat,
        "no en-dash in date ranges": not re.search(r"(19|20)\d\d\s*–", t),
        "PR line present": "Canadian Permanent Resident" in flat,
    }
    return pages, checks


def main():
    golden = GOLDEN.read_text()
    header = ("% Recruiter cold-outreach resume generated by recruiter-outreach/build_resumes.py from the GOLDEN\n"
              "% generic resume with minimal edits; see CHANGES.md next to this file.\n")
    golden = golden.split("\n", 3)[3]  # drop the 3 golden-file comment lines
    rows = []
    for folder, org, contact, email, prio, variant, edits in RECIPIENTS:
        out = ROOT / folder
        out.mkdir(exist_ok=True)
        text, log = apply(golden, COMMON + edits)
        tex = out / "Nishal_Silva_Resume.tex"
        tex.write_text(header + f"% Recipient: {contact}, {org} <{email}>\n" + text)
        for _ in range(2):
            r = subprocess.run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error", tex.name],
                               cwd=out, capture_output=True, text=True)
            if r.returncode:
                sys.exit(f"{folder}: pdflatex failed\n{r.stdout[-2000:]}")
        for ext in (".aux", ".log", ".out"):
            (out / ("Nishal_Silva_Resume" + ext)).unlink(missing_ok=True)
        pages, checks = verify(out / "Nishal_Silva_Resume.pdf", out / "Nishal_Silva_Resume.txt")
        ok = all(checks.values())
        (out / "CHANGES.md").write_text(
            f"# {org}: resume changelog\n\n"
            f"- **Send to:** {contact} <{email}>\n- **CSV priority:** {prio}\n- **Variant:** {variant}\n"
            f"- **Base:** golden `resume_generic/Nishal_Silva_ML_Research_Engineer` (minimal-edit rule)\n"
            f"- **Pages:** {pages}\n\n## Edits vs golden\n\n" + "".join(f"- {d}\n" for d in log) +
            "\n## Verification\n\n" + "".join(f"- [{'x' if v else ' '}] {k}\n" for k, v in checks.items()))
        rows.append((folder, ok, pages, [k for k, v in checks.items() if not v]))
        print(f"{'PASS' if ok else 'FAIL'}  {folder:28s} pages={pages} {rows[-1][3] or ''}")
    if not all(r[1] for r in rows):
        sys.exit(1)


if __name__ == "__main__":
    main()
