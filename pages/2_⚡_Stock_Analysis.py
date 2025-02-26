import yfinance as yf
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Stock Analysis",
    page_icon="⚡",
    initial_sidebar_state="auto"
)

st.write("## Stock Price App")
st.write("Shown are the stock closing price and volume.")

# User input for stock symbol
default_value = "RELIANCE"
user_input = st.text_input("Write Your Symbol (e.g., RELIANCE)", default_value).upper()
tickerSymbol = f"{user_input}.NS"  # Ensure NSE format

# Fetch stock data
try:
    tickerData = yf.Ticker(tickerSymbol)
    tickerDf = tickerData.history(period="10y")  # Fetch last 10 years

    if tickerDf.empty:
        st.error("No data found for the given stock symbol. Try another one!")
    else:
        st.write(f"### Closing Price: {tickerSymbol.upper()}")
        st.line_chart(tickerDf["Close"])

        st.write(f"### Volume Traded: {tickerSymbol.upper()}")
        st.line_chart(tickerDf["Volume"])

        # Debugging Output
        st.write("#### Raw Data Preview")
        st.dataframe(tickerDf.tail())

except Exception as e:
    st.error(f"Error fetching data: {e}")
