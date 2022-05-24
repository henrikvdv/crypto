import streamlit as st

from crypto2 import run_all

selected_crypto = st.selectbox("currency", ["ETH", "BTC"])
fig, advice = run_all(is_load_online=True, crypto="ETH")
st.plotly_chart(fig)
