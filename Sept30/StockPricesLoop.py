number_of_stocks = int(input("Enter the number of stocks: "))

stock_names = []
stock_prices = []
for _ in range (number_of_stocks):
    stock_names.append(input("Enter the stock name: "))
    stock_prices.append(float(input("Enter the stock price: ")))

print(stock_names)
print(stock_prices)


