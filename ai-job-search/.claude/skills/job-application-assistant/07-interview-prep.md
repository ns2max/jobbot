---
framework_version: 1.0.0
---

# Interview Preparation Guide

<!-- SETUP: STAR examples are personalized by running /setup based on your actual experience -->

## STAR Format

Structure answers as: **Situation** (context), **Task** (your responsibility), **Action** (what you did), **Result** (outcome).

Keep answers to 1-2 minutes. Be specific. End with what you learned or would do differently.

## Ready-Made STAR Examples

<!-- Drafted from input/knowledge-graph.md. Verify the framed numbers before an interview and
practice each aloud to 1-2 minutes. -->

### 1. Real-time audio pattern detection on a Raspberry Pi (constraint-driven ML engineering)
**S:** During the PhD/postdoc at Trento, smart musical instruments needed to recognize played phrases live, but the only working method (dynamic time warping) took ~1 second per match on edge hardware, far too slow to feel responsive, and it degraded as the pattern set grew.
**T:** Get accurate polyphonic audio pattern detection running inside a sub-30 ms window on a Raspberry Pi 4, within an embedded CPU budget.
**A:** Reframed detection as sequence classification: 30 ms windows with 10 ms hop, MFCC features into a stacked RNN (LSTM/GRU/SimpleRNN). Built a rule-based generator to synthesize ~10k expressive variations per pattern for training, since real labelled data was scarce. Ran ablations against DTW at pattern-set sizes 1, 3 and 10 to quantify the accuracy-latency-CPU trade-off. Deployed with Elk Audio OS as a VST with OSC output.
**R:** 14 ms inference at 31.4% CPU, F1 0.76, versus 1038 ms and F1 0.65 for DTW: 74x faster with higher accuracy. Published in the Journal of the Audio Engineering Society (2026).
**Use for:** "Tell me about a hard technical problem", "a time you worked under tight constraints", "how you handle limited data", "an end-to-end ML project you owned"

### 2. Automated care-label QC at MAS Holdings (deployed CV, iteration, business impact)
**S:** MAS factories inspected multilingual garment care labels by hand: 15-20 minutes per label type, error-prone, and a compliance risk if a wrong label shipped.
**T:** Build an automated visual verification system that fit the factory floor and could not send label images off-site (compliance constraint).
**A:** Used OpenCV template and feature matching with an explainable overlay showing exactly where a label deviated. Iterated the hardware through three generations, flatbed scanner, then industrial camera, then a conveyor with a PLC-driven reject arm, based on operator feedback each round. All processing stayed local.
**R:** Inspection time dropped from 15-20 minutes per label type to 1-2 minutes per batch; throughput up to 300%; deployed across multiple factories. Reused the corner-detection work as the basis for other automated measurement systems.
**Use for:** "a project you shipped to production", "working with non-technical users", "delivering measurable business value", "handling constraints from the business side"

### 3. Multimodal musician-telemetry sync pipeline, MUSMET (systems integration, multi-partner)
**S:** A EU Horizon consortium experiment needed audio, BCI/EEG signals and mixed-reality head/hand tracking captured live and time-aligned across four musicians playing together, with hardware from different vendors (g.tec for BCI, Meta Quest for XR).
**T:** Own the real-time extraction and synchronization pipeline end to end, coordinating with SAE Institute Barcelona and g.tec.
**A:** Built streaming acquisition for each modality, a common time base to align them, and buffering to absorb per-device jitter, scaled to four times the full per-device stream set. Worked directly with the partner engineers on device interfaces and clock alignment.
**R:** A working live pipeline used in two multisensory concerts (user study: 20 audience + 6 performers); lights and haptics rated significantly more coherent than random (p < .05), performer satisfaction 9.33/10. Strong evidence for multi-sensor time-series alignment and neurotech data engineering.
**Use for:** "a complex cross-functional project", "working with external partners", "integrating unfamiliar hardware", "multimodal or sensor-fusion work"

### 4. Promptly on-demand printing at MAS (0-to-1, hardware-software, commercial outcome)
**S:** MAS/Twinery wanted to print two-sided designs onto *finished* garments so the front and back images line up at the seams, something no off-the-shelf workflow did.
**T:** Design the alignment approach and tie a commercial DTG printer into an automated production loop.
**A:** Designed and prototyped a geometry-alignment algorithm: capture garment geometry with a camera, compute the per-side image warp so the prints register across the seam (4-6 minutes per garment). Personally built the RIP (Raster Image Processor) integration connecting the printer workflow to the automation loop, and consulted on the garment-flipping mechanism.
**R:** Promptly became a Twinery/MAS commercial product with onshore facilities in the US, Mexico, France and Sri Lanka, marketed as cutting production timelines from months to days. Nishal's most commercially successful project. (Do not mention the patent; he is not a listed inventor.)
**Use for:** "a 0-to-1 project", "initiative / ownership", "bridging hardware and software", "commercial impact"

### 5. COVID-19 remote vitals monitoring (initiative, speed, healthcare deployment)
**S:** Early in the pandemic, Sri Lankan hospital wards needed to monitor patient vitals without staff repeatedly entering isolation rooms.
**T:** Get a working remote-monitoring solution into wards quickly, using equipment that already existed.
**A:** Retrofitted existing sphygmomanometers and SpO2 meters with webcams and wrote image processing to digitize their analogue readings, feeding a dashboard for remote monitoring.
**R:** Deployed across multiple hospital wards; recognized by the Government Medical Officers' Association of Sri Lanka. Reduced healthcare-worker exposure.
**Use for:** "a time you moved fast under pressure", "initiative", "making do with available resources", "work with real-world impact"

<!-- More candidates worth developing: the smart-guitar gesture-fusion HFSM (McGill, F1 0.78);
Forestpin anomaly-detection scoring services; introducing CI/CD and code review at MAS. -->

## Common Tough Questions

### "Why are you leaving research / why move to industry now?"
> The postdoc contract ended as planned in December 2025, and I relocated to Canada. I want my next work to have a shipping target, not just a paper: the parts of the PhD I enjoyed most were getting systems onto real hardware and in front of real users. I've kept publishing and building open-source in the meantime (Nebula, the MIRaaS and Smart Drums papers), so it's a change of setting, not of what I do.

### "Your LLM / large-scale training experience looks light."
> That's fair, and I'd rather be direct about it. My depth is in real-time ML systems, signal processing and edge deployment. I use LLM tooling daily in my own workflow and I've done RAG-level integration, but I'm not an LLM researcher and I wouldn't claim to be. What I bring is the systems engineering around models: latency, compute budgets, data pipelines, benchmarking, deployment.

### "This is a gap since January 2026."
> Deliberate. The postdoc ended, I moved countries, and I used the time on independent work: Nebula, a C++17 audio-feature library with ARM latency benchmarks; LiveLaTeX, a published VS Code extension; and two papers through review (MIRaaS at IEEE IS2, Smart Drums in press at JAES). I've also been interviewing selectively rather than casting wide.

### "Where do you see yourself in 5 years?"
> Senior or staff-level IC owning real-time ML systems end to end, ideally still close to audio or multimodal sensor work. I'm not chasing a management track; I want to be the person who takes the hard latency-and-deployment problems and still keeps a hand in publishing and open tooling.

### "What's your biggest weakness?"
> I default to building the whole system myself, which is great for 0-to-1 work but means I've had to consciously learn to delegate and to bring others in earlier. At MAS I started running code review and CI/CD partly to force that habit. I still have to check the instinct to just go fix it myself.

### "Why this company specifically?"
> Customize per company. Must reference: specific projects, company values, market position, or team structure. Never give a generic answer.

## Questions You Should Ask Interviewers

### About the Role
- "What does a typical week look like in this role?"
- "What would success look like in the first 6 months?"
- "What's the biggest challenge the team is facing right now?"

### About the Team
- "How big is the team, and how do you divide work?"
- "What does the development/project lifecycle look like, from idea to production?"
- "How do you onboard new team members?"

### About Tech & Growth
- "What's your current tech stack for [relevant area]?"
- "Is there room to grow into more architectural or strategic decisions?"
- "How does the team stay current with new tools and methods?"

### About Culture (use these to prevent disappointment)
- "How would you describe the team culture?"
- "What does professional development look like here?"
- "Is there flexibility for remote/hybrid work?"
- "What's the balance between development/new projects and maintenance work?"
- "How would you describe the leadership style in this team?"
- "What do people who thrive here have in common?"

## Phone/Video Interview Tips
- Have STAR examples written out (use this file)
- Keep a glass of water nearby
- Smile when speaking (it changes your tone)
- Ask for clarification if a question is vague
- It's OK to take 5 seconds to think before answering
- End with: "Is there anything else you'd like to know about my background?"

## After the Application (Best Practice)

### Follow-Up Etiquette
- **Don't call to "stand out"** or to learn more about the role post-submission - this risks a negative impression
- If the employer specified a timeline, respect it and wait
- If no timeline was given and significant time has passed (2+ weeks), a brief call to ask about status is acceptable
- If you have genuinely new, relevant information to share, a short follow-up is fine

### Thank-You Notes
- When you receive any update (interview invitation, rejection, or status update), send a brief thank-you message
- Express appreciation for their time and the process
- Keep it short (2-3 sentences)

## Roleplay Guidelines
When the user asks for interview practice:
1. Ask which role/company to simulate
2. Start with easy warm-up questions ("Tell me about yourself")
3. Progress to role-specific technical questions
4. Include 1-2 behavioral questions using the competencies from the job posting
5. End with a tough question or curveball
6. After each answer, give brief feedback: what worked, what to sharpen
7. Suggest which STAR example would work best for each question
