# src/download_data.py
import yfinance as yf
import os
import pandas as pd

# Ensure the data directory exists
data_dir = '../data'
os.makedirs(data_dir, exist_ok=True)

# List of 20 stock tickers to download
tickers = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'META', 'TSLA', 'NFLX', 'NVDA', 
           'AMD', 'INTC', 'CSCO', 'IBM', 'ORCL', 'QCOM', 'ADBE', 'SAP', 
           'CRM', 'TXN', 'AVGO', 'BABA']

# Date range
start_date = "2018-01-01"
end_date = "2022-12-31"

# Download data for each ticker and save as CSV
for ticker in tickers:
    data = yf.download(ticker, start=start_date, end=end_date)
    data.to_csv(f'{data_dir}/{ticker}.csv')
    print(f"Downloaded data for {ticker}")
