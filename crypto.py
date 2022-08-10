import requests
import pandas as pd
import plotly.express as px

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

btc = get_crypto_price(symbol = 'BTC', exchange = 'USD', start_date = '2020-01-01')
btc

fig = px.scatter(x=btc.index, y=btc["close"])
fig.show()

btc["close_yesterday"] = btc["close"].shift()
btc["difference"] = btc["close"] - btc["close_yesterday"]
btc["difference_pct"] = btc["difference"] /  btc["close"]
btc

initial_budget = 1000

# default_strategy just buy everything at start
ratio = (btc["close"][-1] - btc["close"][0]) / btc["close"][0]
# profit excluding trading cost
profit = ratio * initial_budget


buy_threshold = -0.02
sell_threshold = 0.02
amount_per_buy = 0.001 * initial_budget

btc["want_to_buy"] = btc["difference_pct"] < buy_threshold
btc["want_to_sell"] = btc["difference_pct"] >= sell_threshold

budget = initial_budget
for index, row in btc.iterrows():
    if (row["difference_pct"] < buy_threshold) & (budget >= amount_per_buy):
        btc.loc[index, "buy"] = amount_per_buy
        btc.loc[index, "buy_coins"] = amount_per_buy/btc.loc[index,"close"]
        budget = budget - amount_per_buy
    btc.loc[index, "budget"] = budget
ratio_new_strategy = (btc["buy_coins"].sum()*btc["close"][-1]) / initial_budget

fig = px.scatter(x=btc.index, y=btc["close"], color=btc["buy_coins"]>0)
fig.show()

fig = px.scatter(x=btc.index, y=btc["budget"], color=btc["buy_coins"]>0, title="budget")
fig.show()