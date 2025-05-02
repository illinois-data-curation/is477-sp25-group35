import pandas as pd

reddit_df = pd.read_csv('data/reddit_posts_clean.csv', parse_dates=['created'])

companies_tickers = {
    'Apple': 'AAPL',
    'AAPL': 'AAPL',
    'Tesla': 'TSLA',
    'TSLA': 'TSLA',
    'Amazon': 'AMZN',
    'AMZN': 'AMZN',
    'Microsoft': 'MSFT',
    'MSFT': 'MSFT',
    'Google': 'GOOG',
    'GOOG': 'GOOG',
    'GOOGL': 'GOOG'
}

stocks_data = {}
for ticker in set(companies_tickers.values()):
    stock_df = pd.read_csv(f'data/{ticker}_stock.csv', index_col=0, parse_dates=True)
    stock_df.reset_index(inplace=True)
    stock_df.rename(columns={stock_df.columns[0]: 'Date'}, inplace=True)
    stock_df['Date'] = pd.to_datetime(stock_df['Date'], errors='coerce')
    stocks_data[ticker] = stock_df[['Date', 'Close']]

merged_data = []
for idx, row in reddit_df.iterrows():
    company_key = row['matched_company']
    ticker = companies_tickers.get(company_key)
    if not ticker:
        continue
    post_date = row['created'].date()
    stock_df = stocks_data[ticker]
    future_stock = stock_df[stock_df['Date'].dt.date >= post_date]
    if not future_stock.empty:
        close_price = future_stock.iloc[0]['Close']
        close_date = future_stock.iloc[0]['Date'].date()
        merged_data.append({
            'post_id': row['id'],
            'company': company_key,
            'ticker': ticker,
            'post_date': post_date,
            'stock_date': close_date,
            'title': row['title'],
            'selftext': row.get('selftext', ''),
            'stock_close_price': close_price
        })

final_df = pd.DataFrame(merged_data)
final_df.to_csv('../data/reddit_stock_merged.csv', index=False)
