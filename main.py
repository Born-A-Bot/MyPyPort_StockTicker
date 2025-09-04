import yfinance as yf
import pandas as pd 
import matplotlib.pyplot as plt

#prompt user for share name
chk_stock = input("Enter stock name: ")

#fetch historical market data
stock_close_thirty = yf.Ticker(chk_stock ).history(period="5d")
stock_close_sixty= yf.Ticker(chk_stock).history(period="5d")
#stock_close_ninety = yf.Ticker(chk_stock).history(period="90d")
yf.download(chk_stock, start="", end="",interval="30d" )

df = list[stock_close_thirty, stock_close_sixty]
pd.DataFrame(df)

print(df)

#extract market price for last 7 days = track start and close for 5 days???
final_close_thirty = stock_close_thirty["Open"]
final_close_sixty = stock_close_sixty["Close"]
#final_close_ninety = stock_close_ninety["Open"]

#plot data
plt.title(f"{chk_stock} 30-Day Open and Close Stock Prices")
plt.xlabel("Date")
plt.ylabel('Price(USD)')
plt.plot(final_close_thirty, label= f"{stock_close_thirty}, closing price", color="blue",)
plt.plot(final_close_sixty, label = f"{stock_close_sixty}, closing price", color = "green")
#plt.plot(final_close_ninety, label = f"{stock_close_sixty}, closing price", color = "orange")
plt.show()


#display 5 day close pric
print("Stock Data:", stock_close_thirty + stock_close_sixty)
      
#option to check additional stocks
chk_another = input("Check another stock? Y or N: ")
if chk_another == "Y":
    print(chk_stock = input("Enter stock share name: "))
else:
    print("Thanks!")

