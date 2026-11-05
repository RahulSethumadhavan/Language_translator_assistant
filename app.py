import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=GEMINI_API_KEY)

def language_translator(user_prompt):
    response = client.models.generate_content(
        model="models/gemini-3.5-flash-lite",
        contents=user_prompt,
    )
    return response

if __name__ == "__main__":
    prompt = "Translate 'Hello, how are you?' to German"
    print(language_translator(prompt).text)