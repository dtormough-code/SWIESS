from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
client = genai.Client()

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents="What is a database?",
    config=types.GenerateContentConfig(
        system_instruction="You are a friendly tutor for beginners. Answer in two short sentences.",
        temperature=0.2,
    ),
)
print(response.text)