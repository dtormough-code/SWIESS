from dotenv import load_dotenv
from google import genai

load_dotenv()           # reads your .env file
client = genai.Client() # finds GEMINI_API_KEY on its own

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents="Explain what an API is in one sentence."
)
print(response.text)