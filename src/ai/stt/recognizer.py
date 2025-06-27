import whisper
import torch
import sounddevice as sd
import numpy as np
import tempfile
import os
import logging
import yaml
import keyboard
from queue import Queue

# Basic logging setup
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class SpeechRecognizer:
    """
    Handles real-time speech recognition by listening for a hotkey press.
    """
    def __init__(self, config):
        self.config = config['stt']
        self.model_name = self.config['model_name']
        self.record_key = self.config['record_key']
        self.samplerate = 16000
        
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        logging.info(f"Using device: {self.device}")
        
        self.model = whisper.load_model(self.model_name, device=self.device)
        logging.info(f"Whisper model '{self.model_name}' loaded.")
        
        self.audio_queue = Queue()
        self.is_recording = False

    def _start_recording(self):
        if self.is_recording:
            return
        logging.info(f"Recording started. Hold '{self.record_key}' and speak.")
        self.is_recording = True
        self.audio_queue = Queue() # Clear previous audio
        
        # This callback function will be called for each audio chunk
        def callback(indata, frames, time, status):
            if status:
                logging.warning(status)
            self.audio_queue.put(indata.copy())

        self.stream = sd.InputStream(samplerate=self.samplerate, channels=1, callback=callback)
        self.stream.start()

    def _stop_and_transcribe(self):
        if not self.is_recording:
            return
        
        self.stream.stop()
        self.stream.close()
        self.is_recording = False
        logging.info("Recording stopped. Transcribing...")

        audio_data = []
        while not self.audio_queue.empty():
            audio_data.append(self.audio_queue.get())
        
        if not audio_data:
            logging.warning("No audio data recorded.")
            return

        recording = np.concatenate(audio_data, axis=0)

        # Manually create, close, and delete the temporary file to avoid
        # file locking issues on Windows.
        tmp_file = tempfile.NamedTemporaryFile(suffix=".wav", delete=False)
        tmp_path = tmp_file.name
        tmp_file.close()

        try:
            from scipy.io.wavfile import write
            write(tmp_path, self.samplerate, recording)

            result = self.model.transcribe(tmp_path, fp16=torch.cuda.is_available())
            transcribed_text = result['text'].strip()
            if transcribed_text:
                logging.info(f"Recognized: {transcribed_text}")
            else:
                logging.info("Recognized: [empty]")
        except Exception as e:
            logging.error(f"Error during transcription or file handling: {e}")
        finally:
            os.remove(tmp_path)

    def run(self):
        """
        Starts the main loop to listen for the hotkey.
        """
        logging.info(f"Press and hold the '{self.record_key}' key to record. Release to transcribe.")
        keyboard.add_hotkey(self.record_key, self._start_recording, suppress=True, trigger_on_release=False)
        keyboard.add_hotkey(self.record_key, self._stop_and_transcribe, suppress=True, trigger_on_release=True)
        
        # Keep the script running
        keyboard.wait()


def main():
    """
    Loads configuration, sets up logging, and runs the speech recognizer.
    """
    config_path = 'config/config.yaml'
    try:
        with open(config_path) as f:
            config = yaml.safe_load(f)
    except FileNotFoundError:
        logging.error(f"Configuration file not found at {config_path}")
        return
    except yaml.YAMLError as e:
        logging.error(f"Error parsing YAML configuration: {e}")
        return

    # Setup file logging
    log_config = config.get('logging', {})
    log_level = log_config.get('level', 'INFO').upper()
    log_file = log_config.get('file', 'app.log')
    
    file_handler = logging.FileHandler(log_file, encoding='utf-8')
    file_handler.setLevel(logging.DEBUG) # Log everything to file
    file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
    
    # Configure console logging
    console_handler = logging.StreamHandler()
    console_handler.setLevel(log_level)
    console_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
    
    # Get root logger and add handlers
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.DEBUG) # Set root to lowest level
    root_logger.handlers.clear() # Clear default handlers
    root_logger.addHandler(file_handler)
    root_logger.addHandler(console_handler)

    recognizer = SpeechRecognizer(config)
    recognizer.run()


if __name__ == "__main__":
    main() 