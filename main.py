
import yfinance as yf
import matplotlib.pyplot as plt


#prompt user for share name
chk_stock = input("Enter stock name: ")
#fetch historical market data
stock_data = yf.Ticker(chk_stock).history(period="5d")
#extract market price for last 7 days = track start and close for 5 days???
final_market_prices = stock_data["Close"]
#display 5 day close price
print("Stock Data:", final_market_prices)

#plot the data
fig, ax = plt.subplots()
ax.plot(final_market_prices)
ax.set_title("Five Day Stock Data")
ax.set_ylabel('Close Price (U.S. Dollars ($))')
ax.set_xlabel('Date')
plt.show()

#option to check additional stocks
chk_another = input("Check another stock? Y or N: ")
if chk_another == "Y":
    print(chk_stock = input("Enter stock share name: "))
else:
    print("Thanks!")
