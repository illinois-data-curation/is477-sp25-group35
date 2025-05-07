import requests
import pandas as pd
import os
import time
import hashlib
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("ALPHAVANTAGE_API_KEY")
if not API_KEY:
    raise ValueError("Missing ALPHAVANTAGE_API_KEY in .env")

tickers = ['AAPL', 'TSLA', 'AMZN', 'MSFT', 'GOOG']
base_url = "https://www.alphavantage.co/query"
DATA_DIR = "data"
os.makedirs(DATA_DIR, exist_ok=True)

def verify_sha256(filepath, expected_hash):
    with open(filepath, 'rb') as f:
        file_hash = hashlib.sha256(f.read()).hexdigest()
    if file_hash != expected_hash:
        raise ValueError(f"[ERROR] Hash mismatch for {filepath}.\nExpected: {expected_hash}\nFound:    {file_hash}")
    print(f"[OK] {filepath} passed SHA-256 integrity check.")

for ticker in tickers:
    print(f"\nFetching data for {ticker}...")

    params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": ticker,
        "outputsize": "full",
        "apikey": API_KEY
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    if "Time Series (Daily)" not in data:
        print(f"[!] Error fetching data for {ticker}: {data}")
        continue

    ts = data["Time Series (Daily)"]
    df = pd.DataFrame.from_dict(ts, orient="index")
    df.index = pd.to_datetime(df.index)
    df = df.sort_index()
    df = df.loc["2021-02-01":"2021-03-31"]
    df = df.rename(columns={
        "1. open": "Open",
        "2. high": "High",
        "3. low": "Low",
        "4. close": "Close",
        "5. volume": "Volume"
    })[["Open", "High", "Low", "Close", "Volume"]]

    output_path = os.path.join(DATA_DIR, f"{ticker}_stock.csv")
    df.to_csv(output_path)
    print(f"[✓] Saved {ticker} data to {output_path}")

    time.sleep(15)
verify_sha256(f'{DATA_DIR}/AAPL_stock.csv', '3764305439f3d1ff382b9dae759f9a40d94fd40d5131e707b0137bd00838ad88')
verify_sha256(f'{DATA_DIR}/TSLA_stock.csv', '4d6345b39a4eb8e519ed0ddef504a1ca927e6c27d90c570073bca9d833c8fa95')
verify_sha256(f'{DATA_DIR}/AMZN_stock.csv', '63ab7be4884b12f97850e0657693d0eabfca06875314a749c14c5b6e5ffc4a2c')
verify_sha256(f'{DATA_DIR}/MSFT_stock.csv', 'a7664199bff05297f3c9b6a1708fd448e882ecfe2c6b6f315e5ecfe3c1082d22')
verify_sha256(f'{DATA_DIR}/GOOG_stock.csv', 'a72f9659d97ee86f295248434626b3c10d51bd74f1cc43c81f6073efd7b4d4c9')
