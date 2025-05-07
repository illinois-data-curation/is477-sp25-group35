# List of stock tickers
TICKERS = ["AAPL", "TSLA", "AMZN", "MSFT", "GOOG"]

rule all:
    input:
        "data/reddit_stock_sentiment.csv",
        "results/overall_sentiment_vs_return.png",
        "results/correlation_summary.csv",
        expand("results/{ticker}_sentiment_vs_return.png", ticker=TICKERS)

rule pull_reddit_data:
    output:
        "data/reddit_posts_clean.csv"
    shell:
        "python scripts/redditpull.py"

rule pull_stock_data:
    output:
        expand("data/{ticker}_stock.csv", ticker=TICKERS)
    shell:
        "python scripts/alphavantage.py"

rule integrate_reddit_and_stocks:
    input:
        "data/reddit_posts_clean.csv",
        expand("data/{ticker}_stock.csv", ticker=TICKERS)
    output:
        "data/reddit_stock_merged.csv"
    shell:
        "python scripts/integrate.py"

rule label_sentiment:
    input:
        "data/reddit_stock_merged.csv"
    output:
        "data/reddit_stock_sentiment.csv"
    shell:
        "python scripts/pos_neg.py"

rule final_analysis:
    input:
        "data/reddit_stock_sentiment.csv"
    output:
        "results/overall_sentiment_vs_return.png",
        "results/correlation_summary.csv",
        expand("results/{ticker}_sentiment_vs_return.png", ticker=TICKERS)
    shell:
        "python scripts/final_analysis.py"