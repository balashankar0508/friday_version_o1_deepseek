# from TTS.api import TTS
# import os
# import torch
# import re

# # ✅ Load default English TTS model
# tts_model = TTS("tts_models/en/ljspeech/tacotron2-DDC")

# # ✅ Language-to-TTS model mapping (Update as needed)
# TTS_MODELS = {
#     "en": "tts_models/en/ljspeech/tacotron2-DDC",
#     "es": "tts_models/es/css10",
#     "fr": "tts_models/fr/css10",
#     "de": "tts_models/de/thorsten",
#     "zh": "tts_models/zh-CN/baker",
# }

# # ✅ Check if CUDA is available
# device = "cuda" if torch.cuda.is_available() else "cpu"
# tts_model.to(device)

# def clean_text(text):
#     """Removes unsupported characters."""
#     text = re.sub(r"[^a-zA-Z0-9 .,!?'äöüßéàèùçñ]", "", text)  # Allow common special characters
#     text = text.strip()
#     return text if len(text) > 1 else "I didn't understand that."

# def speak_response(response_text, language="en"):
#     response_text = clean_text(response_text)  # Clean text before speaking

#     # ✅ Select appropriate TTS model based on detected language
#     model_name = TTS_MODELS.get(language, "tts_models/en/ljspeech/tacotron2-DDC")
    
#     global tts_model
#     if tts_model.model_name != model_name:
#         print(f"🔄 Switching TTS model to {language} ({model_name})...")
#         tts_model = TTS(model_name)
#         tts_model.to(device)

#     print(f"🔊 Speaking in {language.upper()}: {response_text}")

#     try:
#         tts_model.tts_to_file(text=response_text, file_path="audio/response.wav")
#         os.system("start audio/response.wav")  # Windows Media Player
#     except Exception as e:
#         print(f"❌ TTS Error: {e}")
from TTS.api import TTS
import os
import torch
import re
import simpleaudio as sa  # ✅ Play audio instantly
from pydub import AudioSegment  # ✅ Convert audio for playback

# ✅ Language-to-TTS model mapping (Supports Multiple Languages)
TTS_MODELS = {
    "en": "tts_models/en/ljspeech/tacotron2-DDC",
    "es": "tts_models/es/css10",
    "fr": "tts_models/fr/css10",
    "de": "tts_models/de/thorsten",
    "zh": "tts_models/zh-CN/baker",
    "it": "tts_models/it/riccardo_fasol",
    "ru": "tts_models/ru/viktor",
}

# ✅ Load Default English TTS Model
default_model = TTS_MODELS["en"]
tts_model = TTS(default_model)

# ✅ Check if CUDA is available
device = "cuda" if torch.cuda.is_available() else "cpu"
tts_model.to(device)

def clean_text(text):
    """Removes unsupported characters."""
    text = re.sub(r"[^a-zA-Z0-9 .,!?'äöüßéàèùçñ]", "", text)  # Allow common special characters
    text = text.strip()
    return text if len(text) > 1 else "I didn't understand that."

def speak_response(response_text, detected_language="en"):
    response_text = clean_text(response_text)  # Clean text before speaking

    # ✅ Select appropriate TTS model based on detected language
    model_name = TTS_MODELS.get(detected_language, default_model)
    
    global tts_model
    if tts_model.model_name != model_name:
        print(f"🔄 Switching TTS model to {detected_language} ({model_name})...")
        tts_model = TTS(model_name)
        tts_model.to(device)

    print(f"🔊 Speaking in {detected_language.upper()}: {response_text}")

    try:
        # ✅ Generate audio file (saved as WAV)
        audio_file = "audio/response.wav"
        tts_model.tts_to_file(text=response_text, file_path=audio_file)

        # ✅ Convert WAV to Playable Audio
        audio = AudioSegment.from_wav(audio_file)
        play_obj = sa.play_buffer(audio.raw_data, num_channels=1, bytes_per_sample=2, sample_rate=audio.frame_rate)
        play_obj.wait_done()  # ✅ Wait until playback is complete before continuing

    except Exception as e:
        print(f"❌ TTS Error: {e}")
