import streamlit as st

try:
    import datetime
    import matplotlib.pyplot as plt
    import plotly.express as px
    import yfinance as yf
    from yahoo_fin import stock_info
    from PIL import Image
       
    import plotly.graph_objs as ago


except ModuleNotFoundError as e:
    st.error(
        f"Looks like requirements are not installed: '{e}'. Run the following command to install requirements"
    )

    st.code(
        "pip install streamlit matplotlib mplfinance plotly git+https://github.com/StreamAlpha/pynse.git"
    )
else:

    def TESST():

        with st.sidebar:
            st.write("TEST")
            from_date = st.date_input(
                "From date", datetime.date.today() - datetime.timedelta(30)
            )

            to_date = st.date_input("To Date", datetime.date.today())
            segment = st.selectbox("Select Segment", ["Cash", "FnO"])
            
        st.write(f"To be updated soon, until then try using crypto ")

        
        

    def crypto_display():

        with st.sidebar:
            st.write("Crypto Inputs")
            symbol = st.selectbox("Select Symbol",stock_info.get_top_crypto())
            a = st.date_input("From date", datetime.date.today() - datetime.timedelta(30)) 
            b = st.date_input("To Date", datetime.date.today())

            # from_date = st.date_input(
            #     "From date", datetime.date.today() - datetime.timedelta(30)
            # )

            # to_date = st.date_input("To Date", datetime.date.today())

        cdata = yf.download(tickers=symbol, start=a, end=b)



        fig = ago.Figure()


        fig.add_trace(ago.Candlestick(x=cdata.index,open=cdata['Open'],high=cdata['High'],low=cdata['Low'],close=cdata['Close'], name = 'market data'))

        fig.update_layout(title=f'{symbol} live share price evolution',yaxis_title='Stock Price (USD per Shares)')

        fig.update_xaxes(
            rangeslider_visible=True,
            rangeselector=dict(
                buttons=list([
                    dict(count=15, label="15m", step="minute", stepmode="backward"),
                    dict(count=45, label="45m", step="minute", stepmode="backward"),
                    dict(count=1, label="HTD", step="hour", stepmode="todate"),
                    dict(count=3, label="3h", step="hour", stepmode="backward"),
                    dict(step="all")])))
        st.write(fig)

    analysis_dict = {
        "Volume": TESST,
        "Stock Delivery Data": TESST,
        # __________________
        "Crypto": crypto_display, 
        "High/Low Delivery": TESST,
        "Stock OI Data": TESST,
        "Future Builtup": TESST,
        "Historical Option Chain": TESST,
        "Put Call Ratio": TESST,
        "Max Pain": TESST,
    }

    with st.sidebar:
        image = Image.open('logo.jpg')
        st.image(image, caption='By Crypher financial solutions (TE COMPS)')
        st.markdown('<h1 style="float: left;">WITH LOVE :)</h1>',unsafe_allow_html=True,)
        selected_analysis = st.radio("Select Analysis", list(analysis_dict.keys()))
        st.write("---")

    st.header(selected_analysis)

    analysis_dict[selected_analysis]()
