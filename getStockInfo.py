import twstock
import serial
import time
import os


def GetSpecifyStock():
    file_path = os.path.join(os.path.join(os.getcwd()), "ini", "stock_symbol.txt")
    with open(file_path) as f:
        stocks = f.readlines()
    return stocks

def GetRealTimePrice(stock):
    return stock.get('realtime')['latest_trade_price']

def TransmitDataToSerial(code, latest_trade_price):
    ser = serial.Serial (port = "/dev/ttyACM0", bytesize = 8, stopbits = 1)
    ser.baudrate = 115200 
    sleep_time = 0.05  
    ser.write('\x41') #240
    time.sleep(sleep_time)
    ser.write('\x41') #right value A
    time.sleep(sleep_time)
    ser.write('\x41') #right value A
    ser.close()  

def Run():
    stocks = GetSpecifyStock()
    for code in stocks:
        code = code.split("\n")[0].strip()
        # Parser realtime info
        stock_info = twstock.realtime.get(code)
        # Get real time price
        latest_trade_price = GetRealTimePrice(stock_info)
        print("Stock symbol : %s, Latest_trade_price : %s"%(code, latest_trade_price))

        # stock_info = twstock.Stock(stock)
        # stock_price = stock_info.price[-5:]
        # print(stock_price)


if __name__ == "__main__" :
    Run()