import pandas as pd
from textblob import TextBlob
df = pd.read_csv('data/reddit_stock_merged.csv')
def get_sentiment(text):
    if pd.isnull(text) or text.strip() == "":
        return 0.0
    return TextBlob(text).sentiment.polarity
df['full_text'] = df['title'].fillna('') + " " + df['selftext'].fillna('')
df['sentiment_score'] = df['full_text'].apply(get_sentiment)
def label_sentiment(score):
    if score > 0.1:
        return 'positive'
    elif score < -0.1:
        return 'negative'
    else:
        return 'neutral'
df['sentiment_label'] = df['sentiment_score'].apply(label_sentiment)
df.to_csv('../data/reddit_stock_sentiment.csv', index=False)