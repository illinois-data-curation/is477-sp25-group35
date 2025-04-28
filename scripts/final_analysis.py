import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
df = pd.read_csv('data/reddit_stock_sentiment.csv')
df['stock_date'] = pd.to_datetime(df['stock_date'])
if 'Return' not in df.columns:
    if 'stock_close_price' in df.columns:
        df['Return'] = df['stock_close_price'].pct_change()
    else:
        raise ValueError("No 'stock_close_price' column found to calculate returns.")
df = df.dropna(subset=['Return', 'sentiment_score'])
if os.path.exists('results'):
    for file in os.listdir('results'):
        os.remove(os.path.join('results', file))
else:
    os.makedirs('results')

print("\n=== Overall Analysis ===")
correlation = df['Return'].corr(df['sentiment_score'])
print(f"Overall Correlation between Reddit Sentiment and Stock Return: {correlation:.4f}")

plt.figure(figsize=(8,6))
plt.scatter(df['sentiment_score'], df['Return'], alpha=0.6)
m, b = np.polyfit(df['sentiment_score'], df['Return'], 1)
plt.plot(df['sentiment_score'], m*df['sentiment_score'] + b, color='red', label='Trend Line')
plt.title('Overall: Reddit Sentiment vs Stock Daily Return')
plt.xlabel('Sentiment Score')
plt.ylabel('Daily Return')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig('results/overall_sentiment_vs_return.png')
plt.close()
tickers = df['ticker'].unique()
summary = []

for ticker in tickers:
    df_ticker = df[df['ticker'] == ticker]

    print(f"\n=== Analysis for {ticker} ===")
    correlation = df_ticker['Return'].corr(df_ticker['sentiment_score'])
    print(f"{ticker} Correlation between Reddit Sentiment and Stock Return: {correlation:.4f}")

    summary.append({
        'Ticker': ticker,
        'Correlation': correlation
    })

    plt.figure(figsize=(8,6))
    plt.scatter(df_ticker['sentiment_score'], df_ticker['Return'], alpha=0.6)
    if len(df_ticker) > 1:
        m, b = np.polyfit(df_ticker['sentiment_score'], df_ticker['Return'], 1)
        plt.plot(df_ticker['sentiment_score'], m*df_ticker['sentiment_score'] + b, color='red', label='Trend Line')

    plt.title(f'{ticker}: Reddit Sentiment vs Stock Daily Return')
    plt.xlabel('Sentiment Score')
    plt.ylabel('Daily Return')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig(f'results/{ticker}_sentiment_vs_return.png')
    plt.close()
summary_df = pd.DataFrame(summary)
summary_df = summary_df.sort_values(by='Correlation', ascending=False)
summary_df.to_csv('results/correlation_summary.csv', index=False)