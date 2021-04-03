import yfinance as yf
import pandas as pd
import time
import plotly.graph_objects as go
import url_requests

tickerStrings = url_requests.run()

def update_stock():
    df_list = list()
    for ticker in tickerStrings:
        data = yf.download(ticker, group_by="Ticker", period="1d", interval='2m')
        print(ticker)
        data['Ticker'] = ticker  # add this column becasue the dataframe doesn't contain a column with the ticker
        df_list.append(data)
    # combine all dataframes into a single dataframe
    df = pd.concat(df_list)
    # save to csv
    df.to_csv('ticker.csv')

def show_data():
    with open('ticker.csv') as f:
        for collumn in f:
            for row in f:
                for c, r in zip(collumn.split(","), row.split(",")):
                    print(f"{c} => {r}")
    
    
def show_chart():
    fig = go.Figure()
    # Candlestick chart
    fig.add_trace(go.Candlestick(x=data.index,
                    open=data['Open'],
                    high=data['High'],
                    low=data['Low'],
                    close=data['Close'], name='market data'))
    
    # Add Titles
    fig.update_layout(
        title="Tesla live share price evolution",
        yaxis_title="Stock Price (USD per shares)",
    )
    
    #x-axes
    fig.update_xaxes(
        rangeslider_visible=True,
        rangeselector=dict(
            buttons=list([
                dict(count=15, label="15m", step="minute", stepmode="backward"),
                dict(count=45, label="45m", step="minute", stepmode="backward"),
                dict(count=1, label="HTD", step="hour", stepmode="todate"),
                dict(count=2, label="2h", step="hour", stepmode="backward"),
                dict(step="all")
            ])
        )
        )
    
    #Show
    fig.show()

#~ while True:
    #~ update_stock()
    #~ show_data()

update_stock()
show_data()
    