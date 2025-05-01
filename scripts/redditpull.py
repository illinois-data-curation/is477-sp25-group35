import pandas as pd
import hashlib
from datetime import datetime
df_wsb = pd.read_csv('../data/wallstreetbets.csv', low_memory=False)
df_investing = pd.read_csv('../data/investing.csv', low_memory=False)
df_stocks = pd.read_csv('../data/stocks.csv', low_memory=False)
df = pd.concat([df_wsb, df_investing, df_stocks], ignore_index=True)
print("Columns:", df.columns.tolist())
df['created'] = pd.to_datetime(df['created'], errors='coerce')
df = df.dropna(subset=['created'])
start_time = datetime(2021, 2, 1)
end_time = datetime(2021, 3, 31)
df = df[(df['created'] >= start_time) & (df['created'] <= end_time)]
companies = ['Apple', 'AAPL', 'Tesla', 'TSLA', 'Amazon', 'AMZN', 'Microsoft', 'MSFT', 'Google', 'GOOG', 'GOOGL']
def find_company(text):
    if pd.isnull(text):
        return None
    for company in companies:
        if company.lower() in text.lower():
            return company
    return None
df['matched_company'] = df['title'].apply(find_company)
filtered_df = df[df['matched_company'].notnull()]
filtered_df.to_csv('../data/reddit_posts_clean.csv', index=False)
print(f"Saved {len(filtered_df)} posts mentioning target companies.")