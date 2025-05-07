import pandas as pd
import hashlib
from datetime import datetime
import os
import json
import shutil
import subprocess
DATA_DIR = 'data'
with open('kaggle-2.json', 'r') as f:
    kaggle_token = json.load(f)
os.environ['KAGGLE_USERNAME'] = kaggle_token['username']
os.environ['KAGGLE_KEY'] = kaggle_token['key']
wsb_csv = f'{DATA_DIR}/wallstreetbets.csv'
if not os.path.exists(wsb_csv):
    os.makedirs(DATA_DIR, exist_ok=True)
    subprocess.run([
        'kaggle', 'datasets', 'download',
        '-d', 'leukipp/reddit-finance-data',
        '--unzip', '-p', DATA_DIR
    ], check=True)

    shutil.copyfile(f'{DATA_DIR}/wallstreetbets/submissions_reddit.csv', f'{DATA_DIR}/wallstreetbets.csv')
    shutil.copyfile(f'{DATA_DIR}/investing/submissions_reddit.csv', f'{DATA_DIR}/investing.csv')
    shutil.copyfile(f'{DATA_DIR}/stocks/submissions_reddit.csv', f'{DATA_DIR}/stocks.csv')
    print("[INFO] Moved and renamed CSV files from topic folders.")

def verify_sha256(filepath, expected_hash):
    with open(filepath, 'rb') as f:
        file_hash = hashlib.sha256(f.read()).hexdigest()
    if file_hash != expected_hash:
        raise ValueError(f"[ERROR] Hash mismatch for {filepath}.\nExpected: {expected_hash}\nFound:    {file_hash}")
    print(f"[OK] {filepath} passed SHA-256 integrity check.")

verify_sha256(f'{DATA_DIR}/wallstreetbets.csv', '3ce3697de550f013bb45446a0807b46cafb015e172971b6d40d8ca256096eec7')
verify_sha256(f'{DATA_DIR}/investing.csv', '61d1bea344c1025c027520665f16bf36e9392e53506aaf55abb784885a60d5d2')
verify_sha256(f'{DATA_DIR}/stocks.csv', 'ffe9b306a6eb60b01784e74106d309dd705ccb1680f4150aa5f2fa685c8bfc49')
df_wsb = pd.read_csv(f'{DATA_DIR}/wallstreetbets.csv', low_memory=False)
df_investing = pd.read_csv(f'{DATA_DIR}/investing.csv', low_memory=False)
df_stocks = pd.read_csv(f'{DATA_DIR}/stocks.csv', low_memory=False)
df = pd.concat([df_wsb, df_investing, df_stocks], ignore_index=True)
print("Columns:", df.columns.tolist())
df['created'] = pd.to_datetime(df['created'], errors='coerce')
df = df.dropna(subset=['created'])
df = df[(df['created'] >= datetime(2021, 2, 1)) & (df['created'] <= datetime(2021, 3, 31))]
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
output_file = f'{DATA_DIR}/reddit_posts_clean.csv'
filtered_df.to_csv(output_file, index=False)
print(f"[DONE] Saved {len(filtered_df)} posts to {output_file}")
