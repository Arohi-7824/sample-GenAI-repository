import pandas as pd

print("="*50)
print("Pandas version:", pd.__version__)
print("Pandas for data manipulation and analysis.")
print("="*50)

data={
    'text': ['I love this', 'This is a bad product','Great Service','He is a terrible person'],
    'sentiment':['positive','negative','positive','negative'],
    'score':[0.95,0.93,0.89,0.92],
    'length':[11,21,13,23]
}

df=pd.DataFrame(data)
print("\n 1 Dataset")
print(df)

print("\n 2. Info")
print(df.info())

print("\n 3. Statistics")
print(df.describe())

print("\n 4. Value Counts")
print("\n Sentiment Distribution")
print(df['sentiment'].value_counts())

print("\n 5. Filtering")
high_score=df[df['score']>0.90]

print("\n High Confidence Samples")
print(high_score)