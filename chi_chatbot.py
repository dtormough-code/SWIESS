from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
client = genai.Client()

chat = client.chats.create(
    model="gemini-3-flash-preview",
    config=types.GenerateContentConfig(
        system_instruction="You are a friendly tutor for beginners. Answer in two short sentences.",
        temperature=0.5,
    ),
)

print("Chatbot ready. Type 'quit' to exit.")

while True:
    user_input = input("You: ")
    if user_input == "quit":
        break
    response = chat.send_message(user_input)
    print("Bot:", response.text)