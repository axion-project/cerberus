# Cerberus: The Three-Headed Guardian for Gemini

---

## 🛡️ Project Overview

Welcome to **Cerberus**, an advanced, agentic AI security solution designed to proactively safeguard Google's Gemini models and their integrated ecosystems. Much like its mythical namesake, Cerberus operates with a multi-pronged defense strategy, anticipating, identifying, and neutralizing threats with intelligence and agility.

Developed by **axion-project**, the creator of ORAC and Project THORAC, Cerberus embodies a forward-thinking approach to AI security, moving beyond reactive measures to establish an adaptive, predictive defense. This project aims to set new benchmarks in autonomous AI security, ensuring Gemini's operations remain robust, secure, and uncompromised.

---

## ✨ Core Philosophy

Cerberus isn't just a security tool; it's a living, learning sentinel. Our philosophy is rooted in:

* **Proactive Defense:** Anticipating threats before they materialize.
* **Adaptive Intelligence:** Learning from every interaction and evolving defense mechanisms.
* **Lean, Smart, and Fast:** Optimized for efficiency, even in mobile-first environments (like Termux on a Samsung S23 Ultra), ensuring rapid threat response.
* **Security by Design:** Integrating robust security practices from the ground up, including Zero Trust and Least Privilege principles.

---

## 🏛️ The Three Heads of Cerberus

Cerberus is architected into three distinct, intelligent "heads," each specializing in a critical aspect of security:

1.  ### The Oracle Head (Threat Intelligence & Prediction)
    * **Function:** Continuously consumes and analyzes global threat intelligence, security research, and adversarial tactics. It leverages Gemini's reasoning to identify emerging attack patterns and simulate potential vulnerabilities.
    * **Innovation:** Goes beyond mere detection by *predicting* future threats and proactively developing countermeasures through internal red-teaming simulations. Think "Minority Report" for cyber threats.

2.  ### The Engineer Head (Vulnerability Scanning & Hardening)
    * **Function:** Scans Gemini's configurations, integrated tools, APIs, and data pipelines for misconfigurations, prompt injection vectors, and other security flaws.
    * **Innovation:** Utilizes Gemini's generative capabilities to *recommend and apply secure code snippets* or *refined prompt templates*, significantly reducing manual patching and hardening efforts.

3.  ### The Watchman Head (Real-time Anomaly Detection & Response)
    * **Function:** Monitors Gemini's real-time interactions, API calls, and data flows for anomalous behavior, suspicious queries, and signs of model manipulation.
    * **Innovation:** Features a "self-healing" mechanism, allowing Gemini to dynamically *reconfigure its own safety parameters* or *regenerate compromised components* in response to ongoing attacks, learning and adapting on the fly.

---

## 🚀 Getting Started

This project is under active development. The initial commit provides the foundational **Watchman Head** module for **Prompt Injection Detection**.

### Prerequisites

* Python 3.8+
* `pip` for package management

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/axion-project/cerberus.git
    cd cerberus
    ```
2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    # If pytector has specific model dependencies, they might need to be downloaded or installed separately.
    # Refer to pytector's official documentation for details.
    ```
    *Note: If `pytector` installation fails or you prefer to run without it initially, the system will gracefully fall back to a dummy detector for development.*

### Usage (Watchman Head - Prompt Injection Detection)

To run the initial demonstration of the **Watchman Head**'s prompt injection detection:

```bash
python -m src.watchman_head.main_watchman # Or wherever you place the main executable
