rule all:
    input:
        "results/overall_sentiment_vs_return.png",
        "results/correlation_summary.csv"

rule pull_reddit:
    output:
        "data/wallstreetbets.csv"
    script:
        "scripts/redditpull.py"

rule pull_yahoo:
    output:
        "data/stocks.csv"
    script:
        "scripts/yahoopull.py"

rule integrate_data:
    input:
        "data/wallstreetbets.csv",
        "data/stocks.csv"
    output:
        "data/reddit_stock_merged.csv"
    script:
        "scripts/integrate.py"

rule sentiment_analysis:
    input:
        "data/reddit_stock_merged.csv"
    output:
        "data/reddit_stock_sentiment.csv"
    script:
        "scripts/pos_neg.py"

rule final_analysis:
    input:
        "data/reddit_stock_sentiment.csv"
    output:
        "results/overall_sentiment_vs_return.png",
        "results/correlation_summary.csv"
    script:
        "scripts/final_analysis.py"