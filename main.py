import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from textblob import TextBlob
import nltk

# Download required NLTK resources
nltk.download('punkt')
nltk.download('stopwords')

# Load dataset
df = pd.read_csv("D:/ProdigyInfoTech/PRODIGY_DS_04/twitter_sentiments.csv", names=columns, header=None)

# Ensure the text column is correctly named
if 'text' not in df.columns:
    for col in ['Tweet', 'content']:
        if col in df.columns:
            df.rename(columns={col: 'text'}, inplace=True)
            break

# Perform sentiment analysis using TextBlob
df['polarity'] = df['text'].apply(lambda x: TextBlob(str(x)).sentiment.polarity)
df['sentiment'] = df['polarity'].apply(
    lambda x: 'Positive' if x > 0 else ('Negative' if x < 0 else 'Neutral')
)

# Plot sentiment distribution
plt.figure(figsize=(8, 5))
sns.countplot(data=df, x='sentiment', palette='Set2', order=['Positive', 'Neutral', 'Negative'])
plt.title("Sentiment Distribution")
plt.xlabel("Sentiment")
plt.ylabel("Tweet Count")
plt.tight_layout()
plt.show()
