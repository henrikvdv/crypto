import streamlit as st

from crypto2 import run_all

selected_crypto_1 = st.selectbox("currency 1", ["ETH", "BTC"], 0)
selected_crypto_2 = st.selectbox("currency 2", ["ETH", "BTC"], 1)
print("selected: {}, {}".format(selected_crypto_1, selected_crypto_2))
fig, advice = run_all(crypto_1=selected_crypto_1, crypto_2=selected_crypto_2)
st.plotly_chart(fig)
