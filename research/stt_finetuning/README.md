# Whisper Model Fine-Tuning

This directory contains the experiment for fine-tuning the Whisper ASR (Automatic Speech Recognition) model.

## Directory Structure

- `01_whisper_finetuning.ipynb`: The main Jupyter Notebook for running the training process.
- `requirements.txt`: Python dependencies required for this experiment.
- `data/`: A directory to store the training data.
- `output/`: The target directory where the fine-tuned model will be saved.

## Data Preparation

1.  Place all your audio files (e.g., in `.wav` format) inside the `data/` directory.
2.  Create a `metadata.csv` file inside the `data/` directory.
3.  The `metadata.csv` file must have two columns:
    -   `file_name`: The relative path to the audio file (e.g., `data/audio_01.wav`).
    -   `transcription`: The corresponding ground truth text in lowercase.

**Example `data/metadata.csv`:**

```csv
file_name,transcription
data/my_audio_001.wav,"привет как дела"
data/my_audio_002.wav,"это тестовая запись"
``` 