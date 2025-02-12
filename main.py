# from utils.stt import recognize_speech
# from utils.llm import chat_with_llm
# from utils.tts import speak_response

# def run_assistant():
#     print("🟢 AI Assistant is always listening and responding in multiple languages.")

#     while True:
#         user_input, detected_language = recognize_speech()  # Live speech-to-text
#         if not user_input:
#             continue

#         print(f"👤 You: {user_input} (🌍 {detected_language.upper()})")

#         if "exit" in user_input.lower():
#             print("👋 Exiting...")
#             break

#         ai_response = chat_with_llm(user_input, detected_language)  # AI Response
#         print(f"🤖 AI: {ai_response}")

#         speak_response(ai_response, detected_language)  # Speak the response

# if __name__ == "__main__":
#     run_assistant()
from utils.stt import recognize_speech
from utils.llm import chat_with_llm
from utils.tts import speak_response

def run_assistant():
    print("🟢 AI Assistant is always listening and responding in multiple languages.")

    while True:
        user_input, detected_language = recognize_speech()  # Live speech-to-text
        if not user_input:
            continue

        print(f"👤 You: {user_input} (🌍 {detected_language.upper()})")

        if "exit" in user_input.lower():
            print("👋 Exiting...")
            break

        ai_response = chat_with_llm(user_input, detected_language)  # AI Response
        print(f"🤖 AI: {ai_response}")

        speak_response(ai_response, detected_language)  # ✅ Now speaks in the detected language

if __name__ == "__main__":
    run_assistant()
