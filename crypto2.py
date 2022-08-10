import numpy as np
import requests
import pandas as pd
import plotly.express as px
from cachetools import cached, TTLCache


@cached(cache=TTLCache(maxsize=1024, ttl=600))
def get_crypto_price(symbol, exchange, start_date=None):
    api_key = "YOUR API KEY"
    api_url = (
        f"https://www.alphavantage.co/query?function=DIGITAL_"
        f"CURRENCY_DAILY&symbol={symbol}&market={exchange}&"
        f"apikey={api_key}"
    )
    raw_df = requests.get(api_url).json()
    df = pd.DataFrame(raw_df["Time Series (Digital Currency Daily)"]).T
    df = df.rename(
        columns={
            "1a. open (USD)": "open",
            "2a. high (USD)": "high",
            "3a. low (USD)": "low",
            "4a. close (USD)": "close",
            "5. volume": "volume",
        }
    )
    for i in df.columns:
        df[i] = df[i].astype(float)
    df.index = pd.to_datetime(df.index)
    df = df.iloc[::-1].drop(
        [
            "1b. open (USD)",
            "2b. high (USD)",
            "3b. low (USD)",
            "4b. close (USD)",
            "6. market cap (USD)",
        ],
        axis=1,
    )
    if start_date:
        df = df[df.index >= start_date]
    return df


def give_advise(close_values, threshold_sell, threshold_buy):
    ratio = close_values[-1] / close_values[-2]
    if ratio > threshold_sell:
        advice = "sell"
    elif ratio < threshold_buy:
        advice = "buy"
    else:
        advice = "do nothing"
    return advice


def run_all(crypto_1: str, crypto_2: str):
    exchange = "USD"
    start_date = "2020-01-01"
    data_1 = get_crypto_price(
        symbol=crypto_1, exchange=exchange, start_date=start_date
    )
    data_2 = get_crypto_price(
        symbol=crypto_2, exchange=exchange, start_date=start_date
    )

    close_1 = list(data_1["close"].values)
    close_2 = list(data_2["close"].values)

    ratio = np.array(close_2) / np.array(close_1)
    ratio_name = f"{crypto_2} / {crypto_1}"
    date = list(data_1.index.values)

    plot_ratio = plot_time_series(date, ratio, ratio_name)
    plot_1 = plot_time_series(date, close_1, crypto_1)
    plot_2 = plot_time_series(date, close_2, crypto_2)

    # advice
    advice = give_advise(ratio, 0.01, 0.01)
    return plot_ratio, advice, plot_1, plot_2


def plot_time_series(date, ratio, ratio_name):
    # plot
    fig = px.scatter(x=date, y=ratio)
    fig.update_layout(
        title=ratio_name, xaxis_title="Date", yaxis_title=ratio_name
    )
    return fig
