# EU AI Act Compliance Navigator

An algorithmic decision-support tool designed to operationalize the legal criteria of the EU AI Act (Regulation 2024/1689).

[**📊 Run Interactive Navigator**](https://ai-act-compliance-navigator-g7js7fwafmpct3dwk4qtjv.streamlit.app/)

## Project Overview
This tool converts the complex regulatory text of the EU AI Act into a functional logic tree. It enables users to determine the risk level of AI systems and identify specific mandatory obligations through a deterministic "Legal Engineering" approach.

### Key Regulatory Modules:
- **Article 5 (Prohibited Practices):** Identification of banned AI applications.
- **Article 6 (High-Risk AI):** Classification logic for Annex I and Annex III systems, including the Article 6(3) Significant Risk Filter.
- **Article 50 (Transparency):** Assessment of disclosure obligations for chatbots, deepfakes, and biometric systems.
- **Articles 51-55 (GPAI Models):** Classification of General-Purpose AI and assessment of systemic risk based on compute thresholds ($10^{25}$ FLOPs).

## Research Motivation
In the field of **Responsible Computing**, abstract legal requirements must be translated into verifiable technical workflows. This project utilizes a "computational law" lens to reduce regulatory uncertainty and ensure **Accountability-by-Design**.

## Technical Implementation
- **Architecture:** Rule-based deterministic logic engine.
- **Framework:** Python / Streamlit.
- **Source of Truth:** Official text of the European AI Office (Regulation 2024/1689).
