# pip install yfinance
import yfinance as yf
from yahoo_fin import stock_info as si
from yahoofinancials import YahooFinancials

def OptionTwo(ticker):
    stock = yf.Ticker(ticker)
    print("")
    print("Granting Request for Information on... " + ticker)
    print(si.get_company_info(ticker))
    print("")
    print(si.get_company_officers(ticker))
    print("")
    print(stock.earnings)
    print("")
    print(stock.balance_sheet)
    print("")
    print(stock.cashflow)
    print("")
    print(stock.financials)
    print("")


def OptionThree(ticker):
    stock = yf.Ticker(ticker)
    print("")
    print(type(stock.recommendations))
    print("")
    si.get


def Options(ticker):
    while True:
        print("Stock Options... ")
        print("1. Notification System - BROKEN")
        print("2. Stock Information")
        print("3. Recommendation ")
        print("4. Exit Program")
        option = int(input("Enter Option: "))

        if option == 1:
            print("")
            print("Exiting Program...")
            break
        elif option == 2:
            OptionTwo(ticker)
        elif option == 3:
            OptionThree(ticker)
        elif option == 4:
            print("")
            print("Exiting Program...")
            break
        else:
            print("Invalid Option")

def main():
    while True:
        print("Stock Beeper Program 2.0...")
        value = (input("Enter Ticker Symbol: "))
        print(" ")

        if not value:
            break
        else:
            Options(value)
            break

if __name__ == '__main__':
    main()