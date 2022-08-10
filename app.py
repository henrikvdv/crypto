import pandas as pd
import streamlit as st

from crypto2 import run_all

symbols = list(pd.read_csv("crypto_symbols.csv", sep=";")["Symbol"])
selected_crypto_1 = st.selectbox("currency 1", symbols, 0)
selected_crypto_2 = st.selectbox("currency 2", symbols, 1)
print("selected: {}, {}".format(selected_crypto_1, selected_crypto_2))
fig, advice, fig_1, fig_2 = run_all(
    crypto_1=selected_crypto_1, crypto_2=selected_crypto_2
)
st.plotly_chart(fig)
st.plotly_chart(fig_1)
st.plotly_chart(fig_2)
