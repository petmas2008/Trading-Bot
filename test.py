import yfinance as yf
import pandas as pd
import url_requests

tickerStrings = url_requests.run()

def update_stock():
    df_list = list()
    for ticker in tickerStrings:
        data = yf.download(ticker, group_by="Ticker", period="1d", interval='1m')
        data['Ticker'] = ticker  # add this column becasue the dataframe doesn't contain a column with the ticker
        df_list.append(data)
        return dir(data)
    return pd.concat(df_list)

print(update_stock())