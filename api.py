import requests
import datetime as dt
import os
from dotenv import load_dotenv

load_dotenv(override=True)

tickers = ["AAPL", "TSLA"]

end = dt.datetime.now()
start = end - dt.timedelta(days=2)
endParsed = end.strftime("%Y-%m-%d")
startParsed = start.strftime("%Y-%m-%d")
StockAPIKey = os.getenv("StockAPIKey")

for ticker in tickers:
    StockURL = f"https://finnhub.io/api/v1/company-news"
    params = {
        "symbol": ticker,
        "from": startParsed,
        "to": endParsed,
        "token": StockAPIKey
    }
    response = requests.get(StockURL, params=params)
    print(response.json())