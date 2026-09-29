<!-- Job posting: https://ca.linkedin.com/jobs/view/machine-learning-engineer-at-invision-ai-4460322410 -->

# Part A — Concrete edits

1. **File:** `cv/1131_main_invision_ai_machine_learning_engineer.tex`  
   **old_string:** `VAE and diffusion prototypes; model compression, quantization and ARM latency profiling (familiarity with ONNX and TFLite)`  
   **new_string:** `VAE and diffusion prototypes; familiarity with model compression, quantization, ONNX and TFLite; ARM latency profiling`  
   **reason:** grounding  
   Quantization and ONNX are lighter-evidence skills, so the wording must not imply shipped ownership.

2. **File:** `cv/1131_main_invision_ai_machine_learning_engineer.tex`  
   **old_string:** `full lifecycle ownership, data-labeling and label-ontology design, training and evaluation under domain shift, benchmark and dataset design, ablation studies, evaluation-metric design tied to operational outcomes, drift and failure diagnosis, TensorFlow/Keras, PyTorch, scikit-learn`  
   **new_string:** `data-labeling and label-ontology design, training and evaluation under domain shift, benchmark and dataset design, ablation studies, evaluation-metric design tied to operational outcomes, deployment monitoring and failure diagnosis, TensorFlow/Keras, PyTorch, scikit-learn`  
   **reason:** reframing  
   Removes generic ownership language and avoids presenting formal production drift-monitoring as established tooling while retaining honest diagnostic evidence.

3. **File:** `cover_letters/1131_cover_invision_ai_machine_learning_engineer.tex`  
   **old_string:** `I am a computer vision and ML engineer with a PhD from the University of Trento and 10+ years across industry and academia, and I have already done the core of this job: at MAS Holdings I built and deployed production computer-vision inspection systems onto the factory floor, integrating camera, sensor and IoT streams into live workflows and cutting inspection time by 99.5\%.`  
   **new_string:** `I am a computer vision and ML engineer with a PhD from the University of Trento and 10+ years across industry and academia. At MAS Holdings, I built and deployed production computer-vision inspection systems onto the factory floor, integrating camera, sensor and IoT streams into live workflows and cutting inspection time by 99.5\%.`  
   **reason:** style  
   Softens the overclaim that Nishal has already performed the whole role, particularly its transportation and multi-camera 3-D-digital-twin domain.

4. **File:** `cover_letters/1131_cover_invision_ai_machine_learning_engineer.tex`  
   **old_string:** `I own the pipeline end to end in TensorFlow and PyTorch, from data labeling and label-ontology design through evaluation under domain shift to on-device deployment, monitoring and drift diagnosis, with CI/CD and code review that I introduced at MAS.`  
   **new_string:** `My work spans data labeling and label-ontology design, evaluation under domain shift, on-device deployment and monitoring; at MAS, I also introduced CI/CD and code review.`  
   **reason:** grounding  
   This avoids implying equivalent production ownership in both TensorFlow and PyTorch or formal drift-diagnosis tooling, neither of which is directly evidenced.

5. **File:** `cover_letters/1131_cover_invision_ai_machine_learning_engineer.tex`  
   **old_string:** `Experiment-tracking and ML-observability tooling, ONNX Runtime and TensorRT, and modern production CNN backbones are the parts I would ramp on, building on the benchmark design, reproducible pipelines and ARM profiling I already do.`  
   **new_string:** `I would build on my benchmark design, reproducible pipelines and ARM profiling while ramping on formal experiment-tracking and ML-observability tooling, ONNX Runtime, TensorRT and modern production CNN backbones.`  
   **reason:** keyword match  
   Keeps each honest gap explicit but makes the transferable evidence and requested terms easier to scan.

6. **File:** `cover_letters/1131_cover_invision_ai_machine_learning_engineer.tex`  
   **old_string:** `Invision AI's platform builds multi-camera 3D awareness for intelligent infrastructure and transportation, with the models running at the edge.`  
   **new_string:** `Invision AI describes a platform with single-camera 3-D awareness and collaborative multi-camera meshes for smart infrastructure and mobility.`  
   **reason:** company angle  
   Uses the verified company-research wording precisely, without implying Nishal has prior 3-D-digital-twin or geospatial product experience.

7. **File:** `cover_letters/1131_cover_invision_ai_machine_learning_engineer.tex`  
   **old_string:** `build the data-labeling and evaluation systems that tie model metrics to what the deployment actually needs`  
   **new_string:** `help build data-labeling and evaluation systems that tie model metrics to deployment needs`  
   **reason:** reframing  
   Preserves a useful forward-looking contribution while avoiding an unsupported promise of sole ownership of a product line and its data systems.

# Part B — Narrative notes

## Missed keywords / requirements

| Posting term | CV status | Note |
|---|---|---|
| computer vision; production | covered | MAS bullets provide direct production OpenCV inspection evidence. |
| edge; resource-constrained; embedded | covered | Raspberry Pi, ARM profiling, embedded Linux and C++/Python inference are explicit. |
| sensor fusion | covered | Multi-sensor capture plus the McGill IMU/audio fusion result are explicit. |
| object detection; image classification | honest gap | The CV supports industrial defect detection, template/feature matching and OCR, but not named modern object-detection or image-classification product work. Do not add the terms as experience claims. |
| OpenCV; C++; Python; TensorFlow; PyTorch; Docker | covered | Each is listed, with direct MAS or research support. PyTorch should remain a skill, not be overstated as equivalent shipped-platform ownership. |
| CNN / modern architectures; open-source model adaptation | honest gap | CNN knowledge is listed; modern production CNN deployment and open-source model adaptation are not substantiated. |
| experiment tracking; dataset versioning; ML observability; monitoring; model drift | synonym / honest gap | Benchmarks, reproducible pipelines, monitoring and failure diagnosis are relevant adjacent evidence. Named experiment-tracking, versioning, observability platforms and formal drift tooling remain gaps. |
| deployment; CI/CD; testing; version control; documentation; code review | covered | The CV names deployment, CI/CD, pytest, Git, documentation and code review. |
| ONNX; TensorRT; quantization / pruning / distillation | honest gap / familiarity | ONNX and quantization must stay labelled familiarity; TensorRT is a stated ramp-up area. There is no evidence for shipping TensorRT, pruning or distillation. |
| GPU programming; geospatial tracking; 3-D multi-camera digital twins | honest gap | Do not imply prior product delivery in these domains. |

## Company / department angles

The verified research supports a focused company paragraph: Invision describes single-camera 3-D awareness and collaborative multi-camera meshes, and positions these for smart infrastructure and safe, efficient, green mobility. The letter should connect Nishal's industrial CV, multi-sensor integration and edge profiling to those product constraints, not claim direct transportation, geospatial tracking or 3-D-digital-twin delivery. Its Toronto base and cited edge-AI / embedded-systems focus make the local, hybrid availability statement relevant.

## Action-oriented reframing

The MAS bullets are already strong action/outcome statements. The generic competency phrase `full lifecycle ownership` and the letter's repeated `I own` phrasing should yield to precise pipeline stages and results. “Take ownership of one product line” is a strong but speculative first-year promise; “help build” is more credible while still forward-looking. Keep the 14 ms, F1 0.76, 31.4% CPU and 74x result ahead of the self-reported MAS numbers when space permits.

## Tone / style

The register is warm, direct and technically specific. The original “I have already done the core of this job” opening is too broad because the role includes transportation and multi-camera 3-D awareness that are adjacent rather than documented experience; the proposed opening leads with the directly comparable factory-floor CV work instead. No em-dashes or cliches were found. The grounded 95% SSIM detection figure is valid and should remain. MAS is correctly one entry (Jan 2015–Jul 2020), and neither draft makes a Promptly patent claim.
