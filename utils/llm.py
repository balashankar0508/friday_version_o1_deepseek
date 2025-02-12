# import ollama

# def chat_with_llm(input_text, language="en"):
#     print("🤖 Thinking...")

#     try:
#         response = ollama.chat(
#             model="deepseek-r1:latest",  # Ensure the correct model is used
#             messages=[{"role": "user", "content": input_text}],
#             options={"language": language}  # Ensure LLM responds in the same language
#         )
#         return response["message"]["content"]
    
#     except Exception as e:
#         print(f"❌ AI Error: {e}")
#         return "Sorry, I couldn't process that."
import ollama

def chat_with_llm(input_text, language="en"):
    print("🤖 Thinking... (Streaming response)")

    try:
        response_stream = ollama.chat(
            model="deepseek-r1:latest",  # Ensure the correct model is used
            messages=[{"role": "user", "content": input_text}],
            options={"language": language},  # Ensure LLM responds in the same language
            stream=True  # ✅ Enables streaming for faster response output
        )

        response_text = ""  # Stores the full response

        # ✅ Stream response token-by-token for faster output
        for message in response_stream:
            print(message["message"]["content"], end="", flush=True)  # Print tokens immediately
            response_text += message["message"]["content"]

        print("\n")  # Move to the next line after streaming response
        return response_text  # Return full response
    
    except Exception as e:
        print(f"❌ AI Error: {e}")
        return "Sorry, I couldn't process that."
