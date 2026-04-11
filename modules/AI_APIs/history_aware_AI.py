"""
Groq API- Basic Usage
"""

from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client=Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

conversation_history=[
    {
        "role":"system",
        "content":"You are helpful AI Assistant"
    }
]

def chat(user_message):
    """Send message and get response"""

    conversation_history.append({
        "role":"user",
        "content":user_message  
    })

    response=client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=conversation_history,
        max_tokens=1000,
        temperature=0.7
    )
    assitant_message= response.choices[0].message.content
    conversation_history.append({
        "role":"assistant",
        "content":assitant_message
    })
    print(conversation_history)
    return assitant_message

print(chat("What is python"))
print(chat("I want to learn python so give me a roadmap"))

