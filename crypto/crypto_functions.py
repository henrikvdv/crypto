from typing import List

import numpy as np
import pandas as pd
import plotly.express as px
import requests
from cachetools import cached, TTLCache


@cached(cache=TTLCache(maxsize=1024, ttl=600))
def get_crypto_price(symbol, exchange, start_date=None):
    api_key = "YOUR API KEY"
    api_url = (
        f"https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_DAILY"
        f"&symbol={symbol}&market={exchange}&apikey={api_key}"
    )
    raw_df = requests.get(api_url).json()
    if (type(raw_df) == dict) and ("Note" in raw_df.keys()):
        raise ValueError(f"data could not be parsed. {raw_df}")
    df = pd.DataFrame(raw_df["Time Series (Digital Currency Daily)"]).T

    df = df.rename(
        columns={
            f"1a. open ({exchange})": "open",
            f"2a. high ({exchange})": "high",
            f"3a. low ({exchange})": "low",
            f"4a. close ({exchange})": "close",
            "5. volume": "volume",
        }
    )
    for i in df.columns:
        df[i] = df[i].astype(float)
    df.index = pd.to_datetime(df.index)
    df = df.iloc[::-1].drop(
        [
            f"1b. open ({exchange})",
            f"2b. high ({exchange})",
            f"3b. low ({exchange})",
            f"4b. close ({exchange})",
            f"6. market cap ({exchange})",
        ],
        axis=1,
    )
    if start_date:
        df = df[df.index >= start_date]
    return df


def give_advise(close_values: List[float]) -> str:
    if close_values[-1] > close_values[-2]:
        advice = "sell"
    elif close_values[-1] < close_values[-2]:
        advice = "buy"
    else:
        advice = "do nothing"
    return advice


def run_all(crypto_1: str, crypto_2: str):
    exchange = "USD"
    start_date = "2021-01-01"
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

    plot_ratio = plot_time_series(date, ratio, ratio_name, None)
    plot_1 = plot_time_series(date, close_1, crypto_1, exchange)
    plot_2 = plot_time_series(date, close_2, crypto_2, exchange)

    # advice
    advice = give_advise(ratio)
    return plot_ratio, advice, plot_1, plot_2


def plot_time_series(
    date: List[np.datetime64],
    ratio: List[np.float],
    graph_name: str,
    exchange: str,
) -> px.line:
    # plot
    fig = px.line(x=date, y=ratio)
    name = graph_name
    if exchange is not None:
        name = f"{graph_name} ({exchange})"
    fig.update_layout(title=graph_name, xaxis_title="Date", yaxis_title=name)
    return fig
