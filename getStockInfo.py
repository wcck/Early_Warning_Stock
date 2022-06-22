import twstock
import os


def GetSpecifyStock():
    file_path = os.path.join(os.path.join(os.getcwd()), "ini", "stock_symbol.txt")
    with open(file_path) as f:
        stocks = f.readlines()
    return stocks

def Run():
    stocks = GetSpecifyStock()
    for stock in stocks:
        stock = stock.split("\n")[0].strip()
        stock_info = twstock.Stock(stock)
        stock_price = stock_info.price[-5:]
        print(stock_price)


if __name__ == "__main__" :
    Run()