import yfinance as yf
import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(
    page_title="STOCK ANALYSIS",
    page_icon="⚡",
    initial_sidebar_state="auto"
)

st.write('''
# Stock Price App
Shown are the stock closing price and volume of Reliance Industries Ltd!       
''')

default_value = 'RELIANCE'
user_input = st.text_input("Write Your Symbol", default_value)
tickerSymbol = f'{user_input}.NS'
tickerData = yf.Ticker(tickerSymbol)
current_year = datetime.now().year
start_year = current_year - 10
start_date = f"{start_year}-04-01"
end_date = f"{current_year - 1}-03-31"
tickerDf = tickerData.history(period='1mo', start=start_date, end=end_date)

st.write(f'''
### Closing Price
{tickerSymbol.upper()}
''')
st.line_chart(tickerDf.Close)
st.write(f'''
### Volume Traded
{tickerSymbol.upper()}
''')
st.line_chart(tickerDf.Volume)
