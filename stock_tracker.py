# CodeAlpha - Stock Portfolio Tracker

stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 420,
    "AMZN": 180
}

total_investment = 0

print("===================================")
print("      STOCK PORTFOLIO TRACKER")
print("===================================")

print("\nAvailable Stocks:")

for stock, price in stocks.items():
    print(stock, "=", "$", price)

while True:
    stock_name = input("\nEnter stock name (or 'done' to finish): ").upper()

    if stock_name == "DONE":
        break

    if stock_name not in stocks:
        print("Stock not available.")
        continue

    quantity = int(input("Enter quantity: "))

    investment = stocks[stock_name] * quantity
    total_investment += investment

    print("Investment in", stock_name, "=", "$", investment)

print("\n===================================")
print("Total Investment Value = $", total_investment)
print("===================================")