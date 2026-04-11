"""
Groq API- Sentiment Analyzer
"""

from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client=Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def analyze_sentiment(text):
    """Analyze sentiment of text"""

    response=client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=(
            {
                "role":"system",
                "content":"You are a sentiment analysis expert. Classify the sentiment as Positive Negative or Neutral. Provide a confidence score "
            },
            {
                "role":"user",
                "content":f"Analyse the sentiment of {text}"
            }
        ),
        
        temperature=0.7
    )
    return response.choices[0].message.content

reviews=[
    "This product is amazing! I love it",
    "Terrible quality and a waste of money",
    "It's ok, nothing special"
]

for review in reviews:
    print(f"\n Review: {review}")
    print(f"Sentiment: {analyze_sentiment(review)}")
    

