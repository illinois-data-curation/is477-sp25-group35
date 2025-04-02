## Overview
The goal of this project is two determine the strength and correlation between social media posts and stock market performances. Utilizing top publicly listed companies we
plan to analyze specific social media updates and the pattern of change in the market associated with them. In 2025, it is essential to understand that social media makes a big impact when it comes to what people spend their money on and that stands true for investors as well. There are countless forums and posts regarding what investors plan to invest in and what their strategy is behind their choices. One example that we will be utilizing in this project is Reddit. Reddit contains several forums and communities regarding investing and people’s views in the current market.
Throughout this project we plan to collect data from social media sources like Reddit and stock market sources like Yahoo Finance. We would like to develop code that takes data from both sources, clean the data, and conduct an analysis on the social media posts and how the stock/market moved that day. This would include placing filters on different subreddits to locate the posts we are looking for and narrowing our stock analysis down to have matching posts and stock data. After that, we can analyze the trends and see if there is enough evidence to conclude that social media effects stock performance.
## Research Question
Is there a correlation between the social media discussions about specific technology companies and their stock price movements?
## Team
This project will be completed by a team of two members.

Will Baysingar’s responsibilities:
Designing and implementing the Reddit API data acquisition pipeline
Conducting analysis on social media content
Creating data visualizations to illustrate findings
Developing automated workflow scripts for reproducibility
Creating appropriate metadata and documentation

Kareem Adi’s responsibilities:
Implementing the Yahoo Finance data pipeline
Conducting data quality assessment and cleaning for Yahoo Finance
Performing data integration and correlation analysis
Testing and validating the end-to-end workflow

Shared responsibilities:
Regular team meetings to align efforts and solve challenges
Final results analysis and interpretation, and collaborative writing
Going through all the documentation and code together to verify quality and completeness
Collaborative writing of project reports and final submission documents
GitHub repository maintenance and release documentation
## Datasets
The two data sets that are necessary for this project are the Reddit source for social media posts and the Yahoo Finance source for stock market information. We will be using specific subreddits to complete the project including r/wallstreetbets, r/investing, and r/stocks. These subreddits will have different opinions posted by community members about the stocks we will be analyzing. Using the Reddit API with PRAW we will be able to extract this information to be used to test correlation. In addition, to keep the sheer amount of data low and manageable we will be using data from the past two months of February and March. Next, we will utilize the Yahoo Finance API with yfinance Python library. We plan to measure daily stock price including the open price, high price, low price, and close price. Using big tech companies that are less volatile is important so we can see the changes associated with social media so we will be using Apple, Tesla, Amazon, Microsoft, and Google as our five stocks to analyze.
## Timeline
Week 1-2 (April 3-15)
In the first two weeks we will set up our repository and link it with Github. After creating this project plan, we will create the initial scripts for both the Reddit and Yahoo Finance API’s. After that, we will test how the API’s work and determine how much data we will be pulling from each and what constraints we will put on each of them. We will then focus on making a data schema for the data we pulled in. Lastly, we will begin profiling the data to understand it fully and create and submit our interim report.
Week 3 (April 16-22)
In this week will assess the quality of both of the data sets. Next, we will clean both data sets and address and quality issues we found earlier. Utilizing a variety of text analysis libraires we will conduct a sentiment analysis for the Reddit posts. We will then manually create labels for the posts we are using under positive, negative, or neutral. This will give us a good sample of how most people would react to these posts so we can properly analyze the stock changes associated with the posts. After the labeling step, we will focusing on creating integration scripts to align the social media posts with the stock data we pulled from Yahoo Finance. Lastly, we will begin our data analysis by looking for potential outliers and viewing possible correlations in the trends.
Week 4 (April 23-29)
In week 4 we will complete or integration and our analysis identifying correlations and their strengths. We will then create multiple visualizations, so it is easy to view our conclusions we have found. Next, we will use Snakemake to create a reproducible workflow and implement and end-to-end automated workflow. Lastly, we will document our steps and create the needed metadata describing the packages and dataset we used.
Week 5 (April 30-May 1)
This week being is very short so we will only have a few steps to complete. We will test the entire workflow and make sure our documentation is accurate. We will then create a list of sources we used with citations and fill out our README with the instructions for reproducing this data. Finally, we will archive the project and get a persistent identifier by May 1st to submit.