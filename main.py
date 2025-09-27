
import yfinance as yf
import matplotlib.pyplot as plt

#prompt user for share name
chk_stock = input("Enter stock name: ")

#fetch historical market data for past 5 days
stock_data = yf.Ticker(chk_stock).history(period="5d")

#extract close price
final_market_prices = stock_data["Close"]

#display 5 day close price
print("Stock Close Prices:", final_market_prices)

#plot the data
fig, ax = plt.subplots()
ax.plot(final_market_prices)
ax.set_title("Five Day Stock Data")
ax.set_ylabel('Close Price - U.S. Dollars ($)')
ax.set_xlabel('Date')
plt.show()


