import os
import google.generativeai as genai
from dotenv import load_dotenv
from prompt_utils import build_system_prompt

# Load environment variables
load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel(model_name="gemini-1.5-flash")
chat = model.start_chat(history=[
    {"role": "user", "parts": [build_system_prompt()]}
])

# Function to send a user message and get a reply
def LLM_function(user_message):
    response = chat.send_message(user_message)
    reply = response.candidates[0].content.parts[0].text
    return reply
