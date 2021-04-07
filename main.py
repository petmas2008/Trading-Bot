import yfinance as yf
import pandas as pd
import time
import url_requests
import csv

tickerStrings = url_requests.run()
# tickerStrings = ["TSCO"]

def update_stock():
    open_list = []
    close_list = []
    ticker_list = []
    for ticker in tickerStrings:
        data = yf.download(ticker, group_by="Ticker", period="1d", interval='1m')
        options = list(data)
        print(ticker, data)
        # data['Ticker'] = ticker  # add this column becasue the dataframe doesn't contain a column with the ticker
        if len(data) > 0:
            open_list.append(data[options[0]][-1]) # index 0 refers to the open stock reference to the data
            close_list.append(data[options[3]][-1]) # index 3 refers to the close stock reference to the data
            ticker_list.append(ticker)
    save_data(ticker_list, open_list, close_list)

def save_data(ticker_list, open_list, close_list):
    with open("ticker.csv", "a", newline="") as csvfile:
        spamwriter = csv.writer(csvfile)
        for t, o, c in zip(open_list, close_list):
            spamwriter.writerow([t, str(o), str(c)])
            

def show_data():
    with open("ticker.csv") as f:
        for collumn in f:
            print(collumn)
            for row in f:
                print(row)
    
    
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
with open("ticker.csv", "w", newline="") as csvfile:
    csvfile.truncate(0)

while True:
    update_stock()
    show_data()
    time.sleep(60)    
