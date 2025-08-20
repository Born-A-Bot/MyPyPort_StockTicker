import yfinance as yf

#prompt user for share name
CHK_STK = input("Enter stock name: ")


#fetch historical market data
stock_data = yf.Ticker(CHK_STK).history(period="5d")

#extract market price for last 7 days
final_market_price = stock_data["Close"].iloc[-5]

#display 5 day close price
print("Stock Data:", final_market_price)


#option to check additional stocks
CHK_AGAIN = input("Check another stock? Y or N: ")
if CHK_AGAIN == "Y":
    print(CHK_STK = input("Enter stock share name: "))
else:
    print("Thanks!")

