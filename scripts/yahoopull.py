import yfinance as yf
import pandas as pd
import hashlib
import os
tickers = ['AAPL', 'TSLA', 'AMZN', 'MSFT', 'GOOG']
start_date = '2021-02-01'
end_date = '2021-03-31'
data_dir = 'data'
def verify_sha256(filepath, expected_hash):
    with open(filepath, 'rb') as f:
        file_hash = hashlib.sha256(f.read()).hexdigest()
    if file_hash != expected_hash:
        raise ValueError(f"[ERROR] Hash mismatch for {filepath}.\nExpected: {expected_hash}\nFound:    {file_hash}")
    print(f"[OK] {filepath} passed SHA-256 integrity check.")
for ticker in tickers:
    filepath = os.path.join(data_dir, f"{ticker}_stock.csv")
    
    print(f"Downloading {ticker}...")
    stock_data = yf.download(ticker, start=start_date, end=end_date)
    
    if not stock_data.empty:
        stock_data.to_csv(filepath)
        print(f"[✓] Saved {ticker} to {filepath}")
    else:
        print(f"[!] No data found for {ticker}, skipping...")
verify_sha256('data/AAPL_stock.csv', '81e552f659f8e54073a7ade399b6f8481c7e7c79f5131f640772fc25dcd118f6')
verify_sha256('data/TSLA_stock.csv', 'aa62b8f20a174c042e876ce5d8b1983ed8049ae2710f867569b3c187a5d34f54')
verify_sha256('data/AMZN_stock.csv', 'e3768aa975331583deb87464c06676300bf56c17213491b37c32f339acfb5547')
verify_sha256('data/MSFT_stock.csv', 'beac1dd9764b4ad012ea4999ec7a9bd0b6938a29f9e7f4dabc76d9a47921c776')
verify_sha256('data/GOOG_stock.csv', 'cc62c955be8a8483d3c9ff1c62b4dacc967990f1dcd8436bfc80a8403b3aa846')