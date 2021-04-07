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
        for t, o, c in zip(ticker_list, open_list, close_list):
            spamwriter.writerow([t, str(o), str(c)])
            

def show_data():
    with open("ticker.csv") as f:
        for collumn in f:
            print(collumn)
            for row in f:
                print(row)

with open("ticker.csv", "w", newline="") as csvfile:
    csvfile.truncate(0)

while True:
    update_stock()
    show_data()
    time.sleep(60)    
