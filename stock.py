import streamlit as st
import yfinance as yf
st.title("NSE and BSE Stock Current and 52 Week High and Low Price Finder")
input_text=st.text_input("Enter the Stock Name", "TCS")
option = st.selectbox("Please Select Exchange",('NSE','BSE'))
if st.button("Find Price"):
    if option == 'NSE':
        exchange = "NS"
    elif option == "BSE":
        exchange = "BO"
    stock = yf.Ticker(input_text+'.'+exchange)
    data = stock.history(period="1y")  # Fetch historical data for 1 year
    high_52_week = round(data['High'].max(),1)  # Get the maximum high price in the past year
    low_52_week = round(data['Low'].min(),1)
    curr_data = stock.history(period="1d")
    curr_open = round(curr_data['Open'].max(),1)
    curr_high = round(curr_data['High'].max(),1)
    curr_low = round(curr_data['Low'].min(),1)
    industry = stock.info['industry']
    mf_holder = stock.mutualfund_holders
    mf_holder1 = mf_holder['Holder']

    st.write(f"**Today's Opening Price:** {curr_open}")
    st.write(f"**Today's High:** {curr_high}")
    st.write(f"**Today's Low:** {curr_low}")
    st.write(f'**52 Week High:** {high_52_week}')
    st.write(f'**52 Week Low:** {low_52_week}')
    st.write(f'**Sector:** {industry}')
    st.write(f'**Mutual Fund Holding This Company**')
    for i,j in enumerate(mf_holder1, start=1):
        st.write(f'{i}. {j}')

