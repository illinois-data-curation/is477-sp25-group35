import yfinance as yf
import pandas as pd
tickers = ['AAPL', 'TSLA', 'AMZN', 'MSFT', 'GOOG']
start_date = '2021-02-01'
end_date = '2021-03-31'

for ticker in tickers:
    stock_data = yf.download(ticker, start=start_date, end=end_date)
    
    if not stock_data.empty:
        stock_data.to_csv(f'../data/{ticker}_stock.csv')