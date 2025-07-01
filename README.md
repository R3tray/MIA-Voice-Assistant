# MIA: A Modern, Neural-Powered Voice Assistant

[![Python Version](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Status](https://img.shields.io/badge/status-in%20development-orange.svg)](https://github.com/R3tray/MIA-Voice-Assistant)

**MIA** is a next-generation, open-source voice assistant built from the ground up with a focus on privacy, performance, and customization. Powered by modern neural networks, MIA aims to provide a fast, accurate, and deeply integrated assistant experience on your desktop.

---

## Core Features

*   **High-Accuracy Speech-to-Text (STT):**
    *   Built on the foundation of OpenAI's Whisper model.
    *   Planned fine-tuning for the Russian language to achieve superior accuracy in command recognition and dictation.

*   **Natural Language Understanding (NLU):**
    *   Designed to understand complex commands, not just simple keyword matching.

*   **High-Quality Text-to-Speech (TTS):**
    *   Plans to integrate state-of-the-art neural models for natural and pleasant-sounding voice output.

*   **Modular Architecture:**
    *   Each core component (STT, TTS, NLU) is designed as a separate module. This makes experimentation, upgrades, and customization straightforward.

*   **Privacy-First:**
    *   All processing happens locally on your device. Your voice and data never leave your computer.

*   **Fully Customizable:**
    *   From the activation hotkey to the AI models used, everything can be tweaked through simple configuration files.

## Tech Stack

*   **Core Language:** Python 3.10+
*   **AI/ML Framework:** PyTorch
*   **Speech Recognition:** [OpenAI Whisper](https://github.com/openai/whisper) via [Hugging Face Transformers](https://huggingface.co/transformers)
*   **Audio Processing:** SoundDevice, SciPy
*   **Interaction:** Keyboard
*   **Configuration:** PyYAML

## Project Architecture

The project is architecturally divided into two main parts:

*   `src/`: Contains the core application code for the voice assistant. This is the stable, production-ready code that makes MIA run.
    *   `src/ai/`: Holds all AI-related modules (STT, TTS, NLU).
    *   `src/core/`: Contains the core business logic that ties everything together.
*   `research/`: A dedicated directory for experiments, data exploration, and model training. This includes Jupyter Notebooks for fine-tuning our own AI models.

## Getting Started

### Prerequisites

*   Python 3.10 or higher
*   Git
*   [FFmpeg](https://ffmpeg.org/download.html) (a required dependency for Whisper)

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/R3tray/MIA-Voice-Assistant.git
    cd MIA-Voice-Assistant
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    # Windows
    python -m venv venv
    .\venv\Scripts\activate

    # macOS / Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configuration:**
    *   It is recommended to copy `config/config.yaml` to `config/config.yaml.local` and make changes there to avoid tracking them in git.
    *   Edit the `config.yaml` file to your preference (e.g., change the activation hotkey).

### Running MIA

To start the assistant, run the main application:
```bash
python src/main.py
```
Once running, press and hold the `record_key` specified in the config (defaults to `f4`), speak your command, and release. See the recognized text in the console.

## Roadmap

*   [ ] **Phase 1: Core STT**
    *   [x] Implement real-time STT based on Whisper.
    *   [x] Establish project architecture and configuration.
    *   [ ] Fine-tune the `whisper-base` model for Russian.

*   [ ] **Phase 2: NLU & Command Execution**
    *   [ ] Implement a basic intent classifier.
    *   [ ] Create a system for registering and executing basic commands (e.g., "Open Telegram").

*   [ ] **Phase 3: TTS Integration**
    *   [ ] Research and integrate a high-quality TTS model.
    *   [ ] Enable MIA to respond with voice.

*   [ ] **Phase 4: Expansion**
    *   [ ] Develop a plugin or skill system.
    *   [ ] Create a simple GUI.

## Contributing

Contributions are welcome! If you'd like to get involved with the development of MIA, please follow these steps:

1.  Fork the repository.
2.  Create a new branch for your feature (`feature/your-feature`) or fix (`fix/your-fix`).
3.  Make your changes and commit them.
4.  Create a Pull Request with a clear description of what you've done.

I recommend opening an Issue to discuss your ideas before starting significant work.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

> Crafted with ❤️ by R3tray 🚀