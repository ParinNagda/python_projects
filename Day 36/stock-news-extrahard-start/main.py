import requests
import os
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()

STOCK = "RELIANCE"
COMPANY_NAME = "Reliance Industries"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "F81AK5HXIXE90VQ6"
NEWS_API_KEY = "ed4d54bdadd74da494940729b824b03d"
account_sid = os.environ.get('TWILIO_ACCOUNT')
auth_token = os.environ.get('TWILIO_TOKEN')

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": "RELIANCE.BSE",
    "apikey":STOCK_API_KEY
}

response = requests.get(STOCK_ENDPOINT,params=stock_params)
print(response.json())
daily_response = response.json()['Time Series (Daily)']
data_list = [value for (key, value) in  daily_response.items()]
yesterday = data_list[0]
yesterday_closing = yesterday['4. close']

day_before = data_list[1]
day_before_closing = day_before['4. close']

difference = abs(float(yesterday_closing) - float(day_before_closing))
up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"
difference_percent = round(difference/float(yesterday_closing) * 100)


if abs(difference_percent) > 1:

    news_api = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,

    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_api)
    news_response.raise_for_status()
    articles = news_response.json()['articles']
    three_articles = articles[:3]
    print(type(three_articles))
    formatted_articles = [f"{STOCK}:{up_down}{difference_percent} Headline: {article['title']} .\nBrief: {article['description']}" for article in three_articles]
    client = Client(account_sid, auth_token)
    print(formatted_articles)
    try:
        for article in formatted_articles:
            print(article)
            print("\n")
            message = client.messages.create(
                from_='+18103446383',
                body=article,
                to='+917977525271'
            )
            print(f"Message sent: {message.body}")
    except Exception as e:
            print(f"Failed to send message: {e}")
#Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

