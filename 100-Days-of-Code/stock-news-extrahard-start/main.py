import requests
import datetime as dt
from private_info import *

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_API_ENDPOINT = 'https://www.alphavantage.co/query'
NEW_API_ENDPOINT = 'https://newsapi.org/v2/everything'

STOCK_PARAMS = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY
}

stock_response = requests.get(url=STOCK_API_ENDPOINT, params=STOCK_PARAMS)
stock_data = stock_response.json()["Time Series (Daily)"]
# stock_data_list = [value for (key, value) in stock_data.items()]

today = dt.date.today()
yesterday = (today - dt.timedelta(days=1)).isoformat()
previous = (today - dt.timedelta(days=2)).isoformat()

yesterday_stock_price = float(stock_data[yesterday]["4. close"])
previous_stock_price = float(stock_data[previous]["4. close"])

diff_percent = ((yesterday_stock_price - previous_stock_price) /
                yesterday_stock_price) * 100


if abs(diff_percent) > 5:
    NEW_PARAMS = {
        'qInTitle': COMPANY_NAME,
        "apiKey": NEWS_API_KEY,
    }

    news_response = requests.get(url=NEW_API_ENDPOINT, params=NEW_PARAMS)
    news_data = news_response.json()['articles']
    first_three_news = news_data[:3]

    if diff_percent >= 0:
        diff_sign = "🔺"
    else:
        diff_sign = "🔻"

    stock_info = f"{STOCK}: {diff_sign}{round(abs(diff_percent),2)}%\n"

    for article in first_three_news:
        title = article["title"]
        desc = article["description"]
        msg = f"{stock_info}Headline: {title}\nBrief: {desc}"
        print(msg)
else:
    print('not')

# STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

# STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

# STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.

# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
