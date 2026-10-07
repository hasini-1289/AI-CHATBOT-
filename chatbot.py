import os
from dotenv import load_dotenv
from groq import Groq
load_dotenv()  # Load environment variables from .env file
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

messages =[
    {
        "role": "system",
        "content": "You are My AI Chatbot, a helpful assistant."
    }
]


while True:
    user_input = input("You: ")
    if user_input.lower() == "done":
        break
    messages.append({"role": "user", "content": user_input})
    response = client.chat.completions.create(
        model= "openai/gpt-oss-20b",
        messages= messages
    )

    assistant_message = response.choices[0].message.content
    print("Bot: ", assistant_message)
    
    messages.append({"role": "assistant", "content": assistant_message})


