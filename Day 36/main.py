import requests
import os
from twilio.rest import Client

STOCK_NAME="MSFT"
COMPANY="Microsoft"

ALPHA_ENDPOINT="https://www.alphavantage.co/query"
NEWS_ENDPOINT="https://newsapi.org/v2/everything"

ALPHA_API_KEY=os.environ.get("ALPHA_API_KEY")
NEWS_API_KEY=os.environ.get("NEWS_API_KEY")
ACCOUNT_SID = ''
AUTH_TOKEN = ''


alpha_param={
    "function":"TIME_SERIES_DAILY_ADJUSTED",
    "symbol":STOCK_NAME,
    "outputsize":"full",
    "apikey":ALPHA_API_KEY,

}

news_param={
    "apiKey":NEWS_API_KEY,
    "qInTitle":COMPANY,
    # "searchIn":"title",
    "sortBy":"popularity"

}


data=requests.get(ALPHA_ENDPOINT,params=alpha_param)
data.raise_for_status()
data=data.json()
datas=data["Time Series (Daily)"]
#you can use datetime module to get date and later use to as key for grabbing close value.

data_list=[value for (key,value) in datas.items()]
yesterday_closing_price=data_list[0]["4. close"]
day_before_yesterday_closing_price=data_list[1]["4. close"]

difference=abs(float(yesterday_closing_price)-float(day_before_yesterday_closing_price))
diff_percent=difference/float(yesterday_closing_price)*100

#print(difference)
#print(diff_percent)


if difference > 0:
    up_down = "📈"
else:
    up_down = "📉"
print(up_down)
if diff_percent > 5:
    news_response=requests.get(NEWS_ENDPOINT,params=news_param)
    news_response.raise_for_status()
    three_news=news_response.json()["articles"][:3]
    news_msg=[f"Stock:{round(up_down,2)} {diff_percent}% \n Headline:{article['title']}. \n Brief:{article['description'].split('. ')[0]}"for article in three_news]
    
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    for item in news_msg:
        message = client.messages \
            .create(
            body=item,
            from_='your_twilio_trial_no',
            to='verified_num'
        )
        print(message.status)
