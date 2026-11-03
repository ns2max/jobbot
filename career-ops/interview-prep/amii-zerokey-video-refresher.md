# Video Refresher — Amii × ZeroKey Technical Interview

**Job ID:** 1085 · **Companion to:** `amii-zerokey-ml-resident-technical.md` (section numbers below match it) and `amii-zerokey-case-scenarios.md`
**Compiled:** 2026-09-30

Every link below was found through a web search that returned the video's own YouTube page. Videos are chosen for **refreshing**, not learning from scratch: short, visual explainers first, with a longer lecture only where the topic needs it.

**Channels you'll see most:**
- **StatQuest** (Josh Starmer): statistics and classical ML, 5–20 min each.
- **3Blue1Brown**: visual intuition for maths and deep learning.
- **UMich EECS 498** (Justin Johnson): full computer-vision lectures, ~1 hour each; skim at 1.5×.
- **First Principles of Computer Vision** (Shree Nayar, Columbia): short, precise geometry and optical-flow lectures.
- **Cyrill Stachniss** and **MATLAB**: Kalman filtering and state estimation.

---

## If you only have ~5 hours

Watch these in order. They cover the Tier 1 topics from the study-priority table.

| # | Video | Why |
|---|---|---|
| 1 | [Machine Learning Fundamentals: Bias and Variance](https://www.youtube.com/watch?v=EuBBz3bI-aA) (StatQuest) | Fundamentals warm-up |
| 2 | [p-values: What they are and how to interpret them](https://www.youtube.com/watch?v=vemZtEM63GY) (StatQuest) | The most commonly botched stats question |
| 3 | [ROC and AUC, Clearly Explained!](https://www.youtube.com/watch?v=4jRBRDbJemM) (StatQuest) | Evaluation under imbalance |
| 4 | [Long Short-Term Memory (LSTM), Clearly Explained](https://www.youtube.com/watch?v=YCzL96nL7j0) (StatQuest) | Your core model family |
| 5 | [Attention in transformers, visually explained](https://www.youtube.com/watch?v=eMlx5fFNoYc) (3Blue1Brown) | Attention, √d_k, Q/K/V |
| 6 | [Why Use Kalman Filters? — Understanding Kalman Filters, Part 1](https://www.youtube.com/watch?v=mwn8xhgNpFY) (MATLAB) | Headline motion topic |
| 7 | [Kalman Filter & EKF](https://www.youtube.com/watch?v=E-6paM_Iwfc) (Cyrill Stachniss) | The equations, derived properly |
| 8 | [Dynamic Time Warping (DTW) Explained](https://www.youtube.com/watch?v=C5joZ6Bwvmk) | Your DTW → RNN story |
| 9 | [Lecture 16: Detection and Segmentation](https://www.youtube.com/watch?v=zHSjrqS0jAY) (UMich EECS 498) | Detection, Mask R-CNN, keypoints |
| 10 | [Lecture 18: Videos](https://www.youtube.com/watch?v=-9xmRTekLvg) (UMich EECS 498) | Two-stream, 3D CNNs, SlowFast |
| 11 | [ML System Design Question — Create an ETA System for Maps (full mock)](https://www.youtube.com/watch?v=l-2m6YXlEjM) | See the case-study format done live |

---

## §1.1 Core ML concepts

| Concept | Video | Focus on |
|---|---|---|
| Bias–variance | [Machine Learning Fundamentals: Bias and Variance](https://www.youtube.com/watch?v=EuBBz3bI-aA) (StatQuest) | Overfitting vs. underfitting intuition |
| Cross-validation | [Machine Learning Fundamentals: Cross Validation](https://www.youtube.com/watch?v=fSytzGwwBVw) (StatQuest) | k-fold; then think "why this breaks for time series" |
| L2 regularization | [Regularization Part 1: Ridge (L2) Regression](https://www.youtube.com/watch?v=Q81RR3yKn30) (StatQuest) | Shrinkage |
| L1 regularization | [Regularization Part 2: Lasso (L1) Regression](https://www.youtube.com/watch?v=NGf0voTMlcs) (StatQuest) | Sparsity |
| Why L1 gives zeros | [Ridge vs Lasso Regression, Visualized!!!](https://www.youtube.com/watch?v=Xm2C_gTAl8c) (StatQuest) | The geometric picture |
| Neural networks | [But what is a neural network?](https://www.youtube.com/watch?v=aircAruvnKk) (3Blue1Brown) | Only if you want a warm-up |
| Gradient descent | [Gradient descent, how neural networks learn](https://www.youtube.com/watch?v=IHZwWFHWa-w) (3Blue1Brown) | Loss landscape intuition |
| Backpropagation | [Backpropagation, intuitively](https://www.youtube.com/watch?v=Ilg3gGewQ5U) and [Backpropagation calculus](https://www.youtube.com/watch?v=tIeHLnjs5U8) (3Blue1Brown) | Chain rule; vanishing gradients |
| Adam | [Adam Optimization Algorithm (C2W2L08)](https://www.youtube.com/watch?v=JXQT_vxqwIs) (Andrew Ng) | Momentum + RMSprop combined |
| Random forest | [Random Forests Part 1 — Building, Using and Evaluating](https://www.youtube.com/watch?v=J4Wdy0Wc_xQ) (StatQuest) | Bagging reduces variance |
| Gradient boosting | [Gradient Boost Part 1: Regression Main Ideas](https://www.youtube.com/watch?v=3CC4N4z3GJc) (StatQuest) | Fitting residuals sequentially |
| XGBoost | [XGBoost Part 1: Regression](https://www.youtube.com/watch?v=OtD8wVaFm6E) (StatQuest) | Regularized boosting |
| PCA | [Principal Component Analysis (PCA), Step-by-Step](https://www.youtube.com/watch?v=FgakZw6K1QQ) (StatQuest) | Eigenvectors of the covariance matrix |
| SVD | [Singular Value Decomposition (SVD): Overview](https://www.youtube.com/watch?v=gXbThCXjZFM) (Steve Brunton) | Also needed for Kabsch (§6.7) |
| Entropy, cross-entropy, KL | [A Short Introduction to Entropy, Cross-Entropy and KL-Divergence](https://www.youtube.com/watch?v=ErfnhcEV1O8) | Why cross-entropy is the classification loss |

## §1.2 Statistics

| Concept | Video | Focus on |
|---|---|---|
| Bayes' rule | [Bayes theorem, the geometry of changing beliefs](https://www.youtube.com/watch?v=HZGCoVF3YvM) (3Blue1Brown) | **Base-rate fallacy**: directly relevant to rare-event alarms |
| MLE | [Maximum Likelihood, clearly explained!!!](https://www.youtube.com/watch?v=XepXtl9YKwc) (StatQuest) | Then link MLE → MSE/cross-entropy losses |
| Probability vs. likelihood | [In Statistics, Probability is not Likelihood.](https://www.youtube.com/watch?v=pYxNSUDSFH4) (StatQuest) | A common trick question |
| Central limit theorem | [But what is the Central Limit Theorem?](https://www.youtube.com/watch?v=zeJD6dqJ5lo) (3Blue1Brown) | Why SE = σ/√n |
| Standard error | [The standard error, Clearly Explained!!!](https://www.youtube.com/watch?v=XNgt7F6FqDU) (StatQuest) | |
| Confidence intervals | [Confidence Intervals, Clearly Explained!!!](https://www.youtube.com/watch?v=TqOeMYtOc1w) (StatQuest) | Frequentist interpretation |
| Bootstrap | [Bootstrapping Main Ideas!!!](https://www.youtube.com/watch?v=Xz0x-8-cgaQ) (StatQuest) | Then remember: **block** bootstrap for time series |
| p-values | [p-values: What they are and how to interpret them](https://www.youtube.com/watch?v=vemZtEM63GY) (StatQuest) | What a p-value is *not* |
| Multiple comparisons | [False Discovery Rates, FDR, clearly explained](https://www.youtube.com/watch?v=K8LQSvtjcEo) (StatQuest) | Benjamini–Hochberg |
| Simpson's paradox | [Simpson's Paradox](https://www.youtube.com/watch?v=ebEkn-BiW5k) (MinutePhysics) | Confounders (shift, experience) |
| Difference-in-differences | [Causality: Difference-in-Differences](https://www.youtube.com/watch?v=8RQWEykGAjM) | "Did the intervention reduce risk?" |
| Stationarity, ACF/PACF, ARIMA | [Understanding Stationarity, ACF, PACF, and ARIMA Fundamentals](https://www.youtube.com/watch?v=lw3QooVLsL0) | Classical time-series baseline |
| ROC vs. PR | [ROC and AUC, Clearly Explained!](https://www.youtube.com/watch?v=4jRBRDbJemM) (StatQuest) and [Precision-Recall Curve Explained with Simple Examples](https://www.youtube.com/watch?v=ejGCjAVi2Ck) | Why PR-AUC under imbalance |
| Calibration | [Probability Calibration for Classification (Platt, isotonic, logistic and beta)](https://www.youtube.com/watch?v=O5undKIazqs) | Reliability diagrams, Platt scaling |

## §2 Data handling and evaluation

| Concept | Video | Focus on |
|---|---|---|
| Time-series CV / leakage | [Time Series Cross Validation Explained](https://www.youtube.com/watch?v=_TbzrO9jErU) | Forward-chaining splits |
| Data leakage in general | [Understanding and Avoiding Data Leakage with Hamel Husain](https://www.youtube.com/watch?v=EBJBgyzLGvI) | Practical leakage stories; pairs with Scenario T |

## §3 Deep learning for time series

| Concept | Video | Focus on |
|---|---|---|
| RNNs | [Lecture 12: Recurrent Neural Networks](https://www.youtube.com/watch?v=tQUetA6A4ts) (UMich EECS 498) | Only the vanishing-gradient part if short on time |
| LSTM | [Long Short-Term Memory (LSTM), Clearly Explained](https://www.youtube.com/watch?v=YCzL96nL7j0) (StatQuest) | Gates and the cell-state path |
| TCN | [Temporal Convolutional Networks, The Next Revolution for Time-Series?](https://www.youtube.com/watch?v=CGxnBAo90VM) | Dilated causal convolutions; it includes a motion-detection case study |
| Attention | [Attention for Neural Networks, Clearly Explained!!!](https://www.youtube.com/watch?v=PSs6nxngL6k) (StatQuest) and [Attention in transformers, visually explained](https://www.youtube.com/watch?v=eMlx5fFNoYc) (3Blue1Brown) | Q/K/V, scaling, multi-head |
| Transformers | [Transformer Neural Networks, ChatGPT's foundation, Clearly Explained!!!](https://www.youtube.com/watch?v=zxQyTK8quyY) (StatQuest) | Positional encoding, the block |
| Graph networks | [Lecture 6.1 — Introduction to Graph Neural Networks](https://www.youtube.com/watch?v=F3PgltDzllc) (Stanford CS224W) | Message passing |
| ST-GCN | [ST-GCN: Spatial Temporal Graph Convolutional Networks for Skeleton-Based Action Recognition](https://www.youtube.com/watch?v=HZZ4ZRsVP9w) | Closest model to RTLS multi-tag data |
| Temporal segmentation | [MS-TCN: Multi-Stage Temporal Convolutional Network for Action Segmentation (CVPR 2019)](https://www.youtube.com/watch?v=9XphWB9w7p8) | SOP step segmentation |
| HMM / Viterbi | [Hidden Markov Models (HMMs) Explained with the Viterbi Algorithm](https://www.youtube.com/watch?v=sRAxuyq1buk) | Steps as hidden states |
| Self-supervised / contrastive | [Tutorial 17: Self Supervised Contrastive Learning with SimCLR (Part 1)](https://www.youtube.com/watch?v=waVZDFR-06U) | The idea transfers to TS2Vec |
| Time-series foundation models | [Chronos: Learning the Language of Time Series](https://www.youtube.com/watch?v=yKKWCqABspw) | Tokenizing values; zero-shot forecasting |

*No good video found for PatchTST. Read the abstract of the paper ("A Time Series is Worth 64 Words", Nie et al., 2023) instead.*

## §4 Deep learning for computer vision

| Concept | Video | Focus on |
|---|---|---|
| CNNs | [Lecture 7: Convolutional Networks](https://www.youtube.com/watch?v=gJ5UENsAQGY) (UMich EECS 498) | Receptive fields, weight sharing |
| ResNet and architectures | [Lecture 8: CNN Architectures](https://www.youtube.com/watch?v=Y78DttDmkr8) (UMich EECS 498) | Residual connections |
| Vision Transformer | [An Image is Worth 16x16 Words (Paper Explained)](https://www.youtube.com/watch?v=TrdevFK_am4) (Yannic Kilcher) | Patches as tokens; needs pre-training |
| DINO | [DINO: Emerging Properties in Self-Supervised Vision Transformers](https://www.youtube.com/watch?v=h3ij3F3cPIk) (Yannic Kilcher) | Label-free features |
| SAM | [Segment Anything Paper Explained](https://www.youtube.com/watch?v=JUMmqX-EHMY) | Promptable segmentation |
| Object detection | [Lecture 15: Object Detection](https://www.youtube.com/watch?v=MshSNnwF1Qg) (UMich EECS 498) | IoU, NMS, one- vs. two-stage |
| Segmentation, Mask R-CNN, keypoints | [Lecture 16: Detection and Segmentation](https://www.youtube.com/watch?v=zHSjrqS0jAY) (UMich EECS 498) | Includes keypoint (pose) R-CNN |
| DETR | [DETR — End to end object detection with transformers (ECCV 2020)](https://www.youtube.com/watch?v=utxbUlo9CyY) | Set prediction, no NMS |
| U-Net | [Semantic Segmentation with U Net Made Easy](https://www.youtube.com/watch?v=XQpFzkixhKw) | Encoder–decoder with skips |
| Pose estimation | [Realtime Multi-Person 2D Human Pose Estimation using Part Affinity Fields, CVPR 2017 Oral](https://www.youtube.com/watch?v=pW6nZXeWlGM) | Bottom-up pose (OpenPose) |
| Video / action recognition | [Lecture 18: Videos](https://www.youtube.com/watch?v=-9xmRTekLvg) (UMich EECS 498) | Two-stream, I3D, SlowFast |
| Optical flow | [Overview — Optical Flow](https://www.youtube.com/watch?v=lnXFcmLB7sM) and [Lucas-Kanade Method](https://www.youtube.com/watch?v=6wMoHgpVUn8) (First Principles of CV) | Brightness constancy |
| Multi-object tracking | [DeepSORT Object Tracking Explained](https://www.youtube.com/watch?v=MWi3BaAdw4g) | Kalman + Hungarian matching + appearance |
| Pinhole camera, K[R\|t] | [Linear Camera Model](https://www.youtube.com/watch?v=qByYk6JggQU) and [Intrinsic and Extrinsic Matrices](https://www.youtube.com/watch?v=2XM2Rb2pfyQ) (First Principles of CV) | |
| Homography | [Computing Homography](https://www.youtube.com/watch?v=l_qjO4cM74o) and [Dealing with Outliers: RANSAC](https://www.youtube.com/watch?v=EkYXjmiolBg) (First Principles of CV) | Camera → floor-plan mapping |
| Epipolar geometry | [Epipolar Geometry — Uncalibrated Stereo](https://www.youtube.com/watch?v=6kpBqfgSPRc) (First Principles of CV) | Multi-view triangulation |
| Industrial anomaly detection (PatchCore) | [Paper review: Towards Total Recall in Industrial Anomaly Detection](https://www.youtube.com/watch?v=mEY4qjZcNsw) | Memory bank of patch features |

## §5 Practical industry tasks and deployment

| Concept | Video | Focus on |
|---|---|---|
| Quantization | [From FP32 to INT8: Post-Training Quantization Explained in PyTorch](https://www.youtube.com/watch?v=7a8b6hgOjgc) | Scale/zero-point, PTQ vs. QAT |
| Knowledge distillation | [Knowledge Distillation: A Good Teacher is Patient and Consistent](https://www.youtube.com/watch?v=gZPUGje1PCI) | Teacher → edge student |
| Anomaly detection (classical) | [Gaussian Mixture Model (GMM) for Anomaly Detection](https://www.youtube.com/watch?v=uurHuhahT6U) | Density-based baseline |
| Change-point detection | [Change Point Detection in Time Series](https://www.youtube.com/watch?v=JrOnOcnkR-8) and [Bayesian Online Change-Point Detection](https://www.youtube.com/watch?v=cas__TaFk9U) | Segmenting streams (Scenario I) |

## §6 Mathematical methods for analyzing motion

| Concept | Video | Focus on |
|---|---|---|
| Kalman intuition | [Why Use Kalman Filters? — Understanding Kalman Filters, Part 1](https://www.youtube.com/watch?v=mwn8xhgNpFY) (MATLAB) | Continue with the rest of the MATLAB series if time allows |
| Kalman in 5 minutes | [Kalman Filter — 5 Minutes with Cyrill](https://www.youtube.com/watch?v=o_HW6GnLqvg) | Quick recap the night before |
| Kalman + EKF equations | [Kalman Filter & EKF](https://www.youtube.com/watch?v=E-6paM_Iwfc) (Cyrill Stachniss) | Predict/update, linearization |
| UKF | [SLAM Course — 06 — Unscented Kalman Filter](https://www.youtube.com/watch?v=DWDzmweTKsQ) (Cyrill Stachniss) | Sigma points |
| Particle filter | [MSR Course — 07 Particle Filter](https://www.youtube.com/watch?v=uYIjB93oAUo) (Cyrill Stachniss) | Multimodal cases |
| DTW | [Dynamic Time Warping (DTW) Explained](https://www.youtube.com/watch?v=C5joZ6Bwvmk) | Dynamic-programming table |
| Fourier transform | [But what is the Fourier Transform? A visual introduction](https://www.youtube.com/watch?v=spUNpyF58BY) (3Blue1Brown) | Repetitive-motion analysis |
| Quaternions | [Quaternions and 3d rotation, explained interactively](https://www.youtube.com/watch?v=zjMuIxRvygQ) (3Blue1Brown) | q and −q are the same rotation |
| Euler angles / gimbal lock | [Euler Angles and Gimbal Lock, Explained](https://www.youtube.com/watch?v=BczeMqU_u2Y) | Why not Euler angles |
| Kabsch / Procrustes | [Kabsch-Umeyama Algorithm — How to Align Point Patterns](https://www.youtube.com/watch?v=nCs_e6fP7Jo) | Rotation via SVD (Scenario P) |
| Multilateration | [How Does Trilateration Work in GPS Positioning?](https://www.youtube.com/watch?v=2sFHajTVBi0) | Same maths as ultrasonic ranging |
| NIOSH lifting equation | [The NIOSH Lifting Equation: Example 2](https://www.youtube.com/watch?v=eLmGm3JXBNs) | Worked RWL example |
| PINNs | [Physics Informed Neural Networks (PINNs)](https://www.youtube.com/watch?v=-zrY7P2dVC4) (Steve Brunton) | Xu Han's area |
| Neural ODEs | [Neural Ordinary Differential Equations (Neural ODEs): Implementation](https://www.youtube.com/watch?v=9ZYNMkhPQgE) | ResNet ↔ Euler step |

*No good videos found for Savitzky–Golay filtering, the RTS smoother, Fréchet distance, or KalmanNet. The prep guide's own sections (§6.2–§6.4) are enough for the interview.*

## §7 AI agents

| Concept | Video | Focus on |
|---|---|---|
| LLM overview | [1hr Talk: Intro to Large Language Models](https://www.youtube.com/watch?v=zjkBMFhNj_g) (Andrej Karpathy) | Tools, agents, security sections |
| ReAct | [ReAct AI Agents, clearly explained!](https://www.youtube.com/watch?v=vFdIrZyKEwQ) | Reason → act → observe loop |
| MCP | [Model Context Protocol (MCP), clearly explained (why it matters)](https://www.youtube.com/watch?v=7j_NE6Pjv-E) | Tools, resources, prompts |
| RAG | [What is Retrieval-Augmented Generation (RAG)?](https://www.youtube.com/watch?v=T-D1OfcDW1M) (IBM Technology) | Grounding answers in SOP documents |
| LoRA | [Low-Rank Adaptation (LoRA) Explained](https://www.youtube.com/watch?v=CNmsM6JGJz0) | You used it on MusicGen |

## §8 Reinforcement learning (just in case)

| Concept | Video | Focus on |
|---|---|---|
| RL foundations | [RL Course by David Silver — Lecture 1: Introduction to Reinforcement Learning](https://www.youtube.com/watch?v=2pWv7GOvuf0) | MDPs, value functions; Amii's home field |
| RL in one lecture | [Lecture 21: Reinforcement Learning](https://www.youtube.com/watch?v=6lFXlxsnDBY) (UMich EECS 498) | Q-learning, policy gradients, faster than Silver |
| PPO | [Proximal Policy Optimization Explained](https://www.youtube.com/watch?v=HrapVFNBN64) | The clipped objective |

## Part B — Case study practice

| Video | Why |
|---|---|
| [ML System Design Question — Create an ETA System for Maps (full mock)](https://www.youtube.com/watch?v=l-2m6YXlEjM) | Closest to a time-series/industry problem |
| [ML System Design Mock Interview — Build an ML System That Classifies Which Tweets Are Toxic](https://www.youtube.com/watch?v=ZjNoipQAqRM) | Rare-positive classification, like risk detection |
| [Full ML Design Mock by ex-Meta Staff Engineer (with feedback)](https://www.youtube.com/watch?v=9U48NlbOzCU) | The feedback section shows what interviewers reward |

These mocks are recommendation- and web-flavoured, so watch them for **structure and pacing**, not content. Your case will be industrial.

---

## Suggested schedule (if the interview is 2–3 days out)

- **Day 1 (~3 h):** the "~5 hours" list, items 1–8.
- **Day 2 (~3 h):** items 9–11, then §4 pose, tracking and camera geometry; §6 quaternions and Kabsch.
- **Day 3 (~1.5 h):** §7 agents (ReAct, MCP), one case-study mock, then rehearse Scenarios T and I out loud.
