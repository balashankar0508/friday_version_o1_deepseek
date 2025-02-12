import whisper
import pyaudio
import numpy as np
import torch

# Load Whisper model
whisper_model = whisper.load_model("small")

# Check if CUDA is available
device = "cuda" if torch.cuda.is_available() else "cpu"
whisper_model.to(device)

# Set up PyAudio for real-time listening
audio = pyaudio.PyAudio()
stream = audio.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=1024)

def detect_wake_word():
    """Continuously listens for 'Hey Friday' before activating AI."""
    while True:
        print("🎤 Always listening... Say 'Hey Friday' to activate.")

        # Capture audio chunk
        audio_data = np.frombuffer(stream.read(1024), dtype=np.int16)

        # ✅ Convert int16 → float32 (normalize between -1 and 1)
        audio_data = audio_data.astype(np.float32) / 32768.0  

        # ✅ Ensure NumPy array is writable before passing to Whisper
        audio_data = np.copy(audio_data)

        # ✅ Force Whisper to use English (`language="en"`)
        try:
            result = whisper_model.transcribe(audio_data, language="en")
            text = result["text"].lower()
            print(f"👂 Detected Speech: {text}")

            if "hey friday" in text:
                print("🔵 Wake word detected! Activating AI...")
                return True  # Wake up AI assistant

        except Exception as e:
            print(f"❌ Error in wake word detection: {e}")
