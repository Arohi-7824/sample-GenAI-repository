"""
Sentiment Analysis using Transformers
"""

from transformers import pipeline

#Loading Prerained sentiment analysis model
classifier = pipeline('sentiment-analysis')

#Test
texts=[
    "I love this product! It's amazing.",
    "This is the worst experience I've ever had.",
    "The movie was okay, not great but not terrible either."
]
for text in texts:
    result = classifier(text)[0]
    print(f"Text: {text}\nSentiment: {result['label']}: {result['score']:.2%}\n")