import yfinance as yf
import streamlit as st
import pandas as pd
from datetime import datetime

st.write("""
# Stock Price App

Shown are the ***closing price*** and ***volume*** of Amazon!
""")


tickerSymbol = 'AMZN'

tickerData = yf.Ticker(tickerSymbol)

tickerDf =tickerData.history(period = '1d', start='2010-5-31', end= '2022-5-31')

st.write("""
## Closing price
""")

st.line_chart(tickerDf.Close)

st.write("""
## Volume
""")

st.line_chart(tickerDf.Volume)

