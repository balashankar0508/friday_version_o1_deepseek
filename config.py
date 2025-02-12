# config.py

# Model Paths
WHISPER_MODEL = "base"  # Whisper model for Speech-to-Text (STT)
TTS_MODEL = "tts_models/en/ljspeech/tacotron2-DDC"  # Coqui TTS model
LLM_MODEL = "deepseek/deepseek-llm-7b"  # Local LLM (Ollama)

# Wake Word
WAKE_WORD = "hey friday"  # Change this if you want a different wake word

# Audio Settings
SPEECH_THRESHOLD = 1000  # Adjust to filter out background noise
SAMPLE_RATE = 16000  # Audio recording sample rate

# Paths for storing audio files
INPUT_AUDIO_PATH = "audio/input.wav"
OUTPUT_AUDIO_PATH = "audio/response.wav"

# Enable Debug Mode
DEBUG_MODE = False  # Set to True to print additional logs
