from bs4 import BeautifulSoup
import csv
import requests

request = requests.get("https://uk.finance.yahoo.com/gainers")
soup = BeautifulSoup(request.content, "html.parser")

def get_stock_names():
    stock_names = []
    lost = []
    for link in soup.find_all("a"):
        if int(link.get("data-reactid")) > 73:
            #~ stock_names.append((link.string, link.get("data-reactid")))
            stock_names.append(link.string)
        else:
            #~ lost.append((link.string, link.get("data-reactid")))
            lost.append(link.string)
    return stock_names[:5]

def save_stock_names():
    with open("stock_names.csv", "w", newline="") as f:
        stock_names = get_stock_names()
        writer = csv.writer(f)
        for stock_name in stock_names:
            writer.writerow([stock_name])

def show_file_contents():
    stocks = []
    with open('stock_names.csv') as f:
        for stock in f:
            stocks.append(stock.strip("\n"))
    return stocks

def run():
    save_stock_names()
    stocks = show_file_contents()
    return stocks