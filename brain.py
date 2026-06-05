from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

conversation_history = []

def think(user_input, extra_context=""):
    message = user_input
    if extra_context:
        message = f"Context:\n{extra_context}\n\nQuestion: {user_input}"
    
    conversation_history.append({
        "role": "user",
        "content": message
    })

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": """You are JARVIS, a digital AI assistant.
You help the user by answering questions and completing tasks.
Answer in only short sentences.
Be sarcastic but still helpful.
Always call the user Sir."""},
            *conversation_history
        ]
    )

    reply = response.choices[0].message.content
    conversation_history.append({
        "role": "assistant", 
        "content": reply
    })
    return reply

def clear_memory():
    conversation_history.clear()

if __name__ == "__main__":
    print(think("Who are you?"))