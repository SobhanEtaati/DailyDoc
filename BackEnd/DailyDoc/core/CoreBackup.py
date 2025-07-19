import os
import google.generativeai as genai
from dotenv import load_dotenv
from prompt_utils import build_system_prompt

# Load environment variables
load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Initialize the model and the chat session once
#model = genai.chat(model="gemini-1.5-flash", prompt=build_system_prompt())


model = genai.GenerativeModel(model_name="gemini-1.5-flash")
chat = model.start_chat(history=[
    {"role": "user", "parts": [build_system_prompt()]}
])


# Function to send a user message and get a reply
def LLM_function(user_message):
    response = chat.send_message(user_message)
    reply = response.candidates[0].content.parts[0].text
    return reply

# Function to print structured results if in JSON markdown
def print_result(result):
    try:
        print(result)
    except Exception as e:
        print("⚠️ Could not parse structured advice.\n")
        print(result)

# Main chat loop
if __name__ == "__main__":
    print("👋 Welcome to Daily Doctor!")
    print("How are you feeling today?")

    while True:
        user_input = input("> ").strip().lower()

        # End conversation on polite goodbyes
        if any(word in user_input for word in ["bye", "thank", "thanks", "ok", "okay", "see you"]):
            print("👋 No problem, take care!")
            break

        # Send the user message and get reply
        reply = LLM_function(user_input)

        # Try structured JSON formatting first
        print_result(reply)
