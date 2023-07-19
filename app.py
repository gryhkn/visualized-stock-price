import yfinance as yf
import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import plotly.graph_objects as go


def main():
    st.write("""
    # Visualized Stock Price App
    Compare the **closing price** and **volume** of different companies!
    """)

    tickers = ['AAPL', 'GOOGL', 'AAPL', 'AMZN', 'MSFT', 'FB', 'TSLA', 'BRK-A', 'JPM', 'KCHOL.IS', 'GARAN.IS', 'AKBNK.IS',
            'BIMAS.IS', 'THYAO.IS', 'HALKB.IS', 'TTKOM.IS', 'SAHOL.IS', 'VAKBN.IS']

    # Sidebar
    st.sidebar.write("## Select Options")

    # User can choose to view different sections of the app
    section = st.sidebar.radio("Section", ('View Stock Data', 'Compare Stocks'))

    if section == 'Compare Stocks':
        compare_stocks_section(tickers)
    elif section == 'View Stock Data':
        view_stock_data_section(tickers)

    for _ in range(10):
        st.sidebar.text("")
    st.sidebar.markdown("Built by ❤️ [**:blue[Giray]**](https://twitter.com/gryhkn)")


def get_ticker_data(ticker, start_date, end_date):
    try:
        ticker_data = yf.Ticker(ticker)
        ticker_df = ticker_data.history(period='1d', start=start_date.strftime('%Y-%m-%d'), end=end_date.strftime('%Y-%m-%d'))
        return ticker_df
    except Exception as e:
        st.error(f"An error occurred while fetching the data: {str(e)}")
        return None


def compare_stocks_section(tickers):
    selected_tickers = st.sidebar.multiselect('Select companies to compare', tickers, default=['AAPL'])

    month_to_look_back = st.sidebar.slider('Look back period in months', 1, 300, 100)

    end_date = datetime.today()
    start_date = end_date - timedelta(days=30*month_to_look_back)

    close_prices = pd.DataFrame()

    for ticker in selected_tickers:
        ticker_df = get_ticker_data(ticker, start_date, end_date)
        if ticker_df is not None:
            close_prices[ticker] = ticker_df['Close']

    st.subheader("Stock Closing Prices")
    st.line_chart(close_prices)


def view_stock_data_section(tickers):
    selected_ticker = st.sidebar.selectbox('Select a company', tickers, index=0)

    month_to_look_back = st.sidebar.slider('Look back period in months', 1, 300, 100)

    end_date = datetime.today()
    start_date = end_date - timedelta(days=30*month_to_look_back)

    ticker_df = get_ticker_data(selected_ticker, start_date, end_date)

    if ticker_df is not None:
        st.subheader(f"Closing Price of {selected_ticker}")
        st.line_chart(ticker_df.Close)

        st.subheader(f"Volume of {selected_ticker}")
        st.line_chart(ticker_df.Volume)

        fig = go.Figure(data=[go.Candlestick(x=ticker_df.index,
                        open=ticker_df['Open'],
                        high=ticker_df['High'],
                        low=ticker_df['Low'],
                        close=ticker_df['Close'])])

        st.subheader(f"Candlestick Chart of {selected_ticker}")
        st.plotly_chart(fig)

        window_size = st.sidebar.slider('Moving average window size', 1, 100, 20)
        ticker_df['Moving Average'] = ticker_df['Close'].rolling(window_size).mean()

        st.subheader(f"Moving Average of {selected_ticker}")
        st.line_chart(ticker_df['Moving Average'])


if __name__ == "__main__":
    main()
