import yfinance as yf

#prompt user for share name
CHK_STK = input("Enter stock name: ")

#fetch historical market data
data = yf.Ticker(CHK_STK).history(period="5d")

#extract market price for last 7 days
final_market_price = data["Close"].iloc[-5]

#create list to store results
resultsList = []

#save results in list
resultsList.append(data)

#display market price for last 7 days
print("Market prices for the last week:", final_market_price)
print(resultsList)

#option to check additional stocks
CHK_AGAIN = input("Check another stock? Y or N: ")
if CHK_AGAIN == "Y":
    print(CHK_STK = input("Enter stock share name: "))
else:
    print("Thank you")

