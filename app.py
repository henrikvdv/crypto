import streamlit as st

from crypto2 import run_all

selected_crypto = st.selectbox("currency", ["ETH", "BTC"])
print("selected: {}".format(selected_crypto))
fig, advice = run_all(is_load_online=True, crypto=selected_crypto)
st.plotly_chart(fig)
