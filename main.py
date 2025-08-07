import yfinance as yf
import openpyxl
import pandas as pd

#prompt user for share name
CHK_STK = input("Enter stock name: ")

#create list to store results
resultsList = []

#fetch historical market data
stock_data = yf.Ticker(CHK_STK).history(period="5d")

#extract market price for last 7 days
final_market_price = stock_data["Close"].iloc[-5]

#display market price for last 7 days
print("Market prices for the last week:", final_market_price)

#save results in list
resultsList.append(stock_data)
print(resultsList)

#create excel workbook
workbook = openpyxl.Workbook()

#create sheet within workbook
sheet = workbook.active

#populate sheet w/stock data
for row in resultsList:
    if isinstance(row, (list, tuple)):
        sheet.append(row)
    
#save workbook 
workbook.save("stock_ticker.xlsx")

#notify user when file created
print('Excel file created')

#option to check additional stocks
CHK_AGAIN = input("Check another stock? Y or N: ")
if CHK_AGAIN == "Y":
    print(CHK_STK = input("Enter stock share name: "))
else:
    print("Thank you")

