# import whisper
# import speech_recognition as sr
# import numpy as np
# import torch
# import tempfile
# import os

# # ✅ Load Whisper `base` model
# whisper_model = whisper.load_model("base")

# # ✅ Check if CUDA is available for GPU acceleration
# device = "cuda" if torch.cuda.is_available() else "cpu"
# whisper_model.to(device)

# def recognize_speech():
#     recognizer = sr.Recognizer()

#     with sr.Microphone() as source:
#         print("🎤 Listening for speech...")
#         recognizer.adjust_for_ambient_noise(source)  # Reduce background noise
#         audio = recognizer.listen(source)  # Capture live speech
    
#     try:
#         print("📝 Detecting language and transcribing...")

#         # ✅ Save temporary WAV file (Needed for Whisper)
#         with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_wav:
#             temp_wav.write(audio.get_wav_data())
#             temp_wav_path = temp_wav.name
        
#         # ✅ Use Whisper to transcribe the saved WAV file
#         result = whisper_model.transcribe(temp_wav_path)
#         os.remove(temp_wav_path)  # Cleanup temporary file

#         text = result["text"]
#         detected_language = result["language"]

#         print(f"🌍 Detected Language: {detected_language}")
#         print(f"👤 You: {text}")

#         return text, detected_language  # Return both text and detected language
    
#     except Exception as e:
#         print(f"❌ STT Error: {e}")
#         return None, None
import whisper
import speech_recognition as sr
import tempfile
import os
import torch

# ✅ Load Whisper `base` model
whisper_model = whisper.load_model("base")

# ✅ Check if CUDA is available for GPU acceleration
device = "cuda" if torch.cuda.is_available() else "cpu"
whisper_model.to(device)

def recognize_speech():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("🎤 Listening... Speak now.")
        recognizer.adjust_for_ambient_noise(source)  # Reduce background noise

        # ✅ Waits for user to stop speaking before processing
        audio = recognizer.listen(source, timeout=None, phrase_time_limit=None)  
        print("🛑 Detected silence. Processing speech...")

    try:
        # ✅ Save speech to temporary WAV file (Whisper requires a file)
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_wav:
            temp_wav.write(audio.get_wav_data())
            temp_wav_path = temp_wav.name
        
        # ✅ Use Whisper to transcribe the saved audio file
        result = whisper_model.transcribe(temp_wav_path)
        os.remove(temp_wav_path)  # Cleanup temporary file

        text = result["text"]
        detected_language = result["language"]

        print(f"🌍 Detected Language: {detected_language}")
        print(f"👤 You: {text}")

        return text, detected_language  # Return transcribed text & detected language
    
    except Exception as e:
        print(f"❌ STT Error: {e}")
        return None, None
