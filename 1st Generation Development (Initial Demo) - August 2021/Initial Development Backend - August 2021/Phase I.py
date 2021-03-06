# pip install yfinance
import smtplib
from email.message import EmailMessage
import yfinance as yf
from yahoo_fin import stock_info as si
from yahoofinancials import YahooFinancials



# apple = yf.Ticker("aapl")
# print(apple.recommendations)

# si.get_live_price("AAPL")
# si.get_top_crypto()
# print(si.get_live_price("AAPL"))

def OptionOne(ticker):
    upper_bound = []
    lower_bound = []

    while True:
        print("")
        print("Current Price of " + ticker + " is: " + str(si.get_live_price(ticker)))
        print("1. Set Upper Bound")
        print("2. Set Lower Bound")
        print("3. Run")
        print("4. Exit")
        result = int(input("Enter Option: "))

        if result == 1:
            upper = float(input("Enter Upper Bound: "))
            upper_bound.append(upper)
        elif result == 2:
            lower = float(input("Enter Lower Bound: "))
            lower_bound.append(lower)
        elif result == 3:
            print("Program Runs...")
            upper_bound.sort(reverse=True)
            lower_bound.sort(reverse=False)

            while len(upper_bound) > 0 or len(lower_bound) > 0:
                if len(upper_bound) > 0:
                    curr_upper = upper_bound[len(upper_bound) - 1]
                else:
                    curr_upper = 0

                if len(lower_bound) > 0:
                    curr_lower = lower_bound[len(lower_bound) - 1]
                else:
                    curr_lower = 0

                if len(lower_bound) > 0 and si.get_live_price(ticker) <= curr_lower:
                    # Send notification
                    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
                    # server.login()
                    msgMin = EmailMessage()
                    msgMin['From'] = "antoniohasabotemail@gmail.com"
                    msgMin['To'] = "8139920730@txt.att.net"
                    msgMin['Subject'] = " Minimum Alert Message for " + ticker
                    msgMin.set_content("Current Price is: " + str(curr_lower))
                    server.send_message(msgMin)
                    server.quit()

                    print("Hit Lower Bound at " + str(curr_lower))
                    lower_bound.remove(curr_lower)

                if len(upper_bound) > 0 and si.get_live_price(ticker) >= curr_upper:
                    # Send notification
                    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
                    # server.login()
                    msgMax = EmailMessage()
                    msgMax['From'] = "antoniohasabotemail@gmail.com"
                    msgMax['To'] = "8139920730@txt.att.net"
                    msgMax['Subject'] = " Maximum Alert Message for " + ticker
                    msgMax.set_content("Current Price is: " + str(curr_upper))
                    server.send_message(msgMax)
                    server.quit()

                    print("Hit Upper Bound at " + str(curr_upper))
                    upper_bound.remove(curr_upper)

        elif result == 4:
            print("Program Cancelled...")
            break
        else:
            print("Invalid Option")

    # print(si.get_live_price(ticker))


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
        print("1. Notification System ")
        print("2. Stock Information")
        print("3. Recommendation ")
        print("4. Exit Program")
        option = int(input("Enter Option: "))

        if option == 1:
            OptionOne(ticker)
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


while True:
    print("Stock Beeper Program 2.0...")
    value = (input("Enter Ticker Symbol: "))
    print(" ")

    if not value:
        break
    else:
        Options(value)
        break
