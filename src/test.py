import os
import pandas as pd
import yfinance as yf


TICKERS = [
    "AAPL",
    "ADS.DE",
]

START_DATE = "2025-11-12"
END_DATE = "2025-11-13"
os.makedirs("../data/raw", exist_ok=True)
try:

    daily_data = yf.download(tickers=TICKERS, start=START_DATE, end=END_DATE)

    daily_data.to_csv("../data/raw/daily_data.csv")
    print("Daily data saved")
except Exception as e:
    print(f"Kann nicht heruntergeladen werden: {e}")
