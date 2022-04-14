import requests
import pandas as pd
import plotly.express as px

def get_crypto_price_csv():
    return pd.read_csv("btc.csv", sep=";")

def get_crypto_price(symbol, exchange, start_date = None):
    api_key = 'YOUR API KEY'
    api_url = f'https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_DAILY&symbol={symbol}&market={exchange}&apikey={api_key}'
    raw_df = requests.get(api_url).json()
    df = pd.DataFrame(raw_df['Time Series (Digital Currency Daily)']).T
    df = df.rename(columns = {'1a. open (USD)': 'open', '2a. high (USD)': 'high', '3a. low (USD)': 'low', '4a. close (USD)': 'close', '5. volume': 'volume'})
    for i in df.columns:
        df[i] = df[i].astype(float)
    df.index = pd.to_datetime(df.index)
    df = df.iloc[::-1].drop(['1b. open (USD)', '2b. high (USD)', '3b. low (USD)', '4b. close (USD)', '6. market cap (USD)'], axis = 1)
    if start_date:
        df = df[df.index >= start_date]
    return df

def give_advise(close_values, threshold_sell, threshold_buy):
    ratio = close_values[-1]/close_values[-2]
    if ratio >= threshold_sell:
        advice = "sell"
    elif ratio < threshold_buy:
        advice = "buy"
    else:
        advice = "do nothing"
    return advice

is_load_online = True
# get data
if is_load_online:
    btc = get_crypto_price(symbol = 'BTC', exchange = 'USD', start_date = '2020-01-01')
else:
    btc = get_crypto_price_csv()


close = list(btc["close"].values)
date = list(btc.index.values)

# plot
fig = px.scatter(x=date, y=close)
fig.show()

# advice
advice = give_advise(close, 0.01, 0.01)
print("advice is to {}".format(advice))