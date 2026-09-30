# Stock Portfolio Tracker

# Predefined stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 2800,
    "AMZN": 3400,
    "MSFT": 300
}

# Store user's portfolio
portfolio = {}

# Get number of stocks
n = int(input("Enter number of stocks: "))

# Get stock details
for i in range(n):
    stock_name = input("\nEnter stock name: ").upper()

    if stock_name in stock_prices:
        quantity = int(input("Enter quantity: "))
        portfolio[stock_name] = quantity
    else:
        print("Stock not available in database!")

# Calculate total investment
total_value = 0

print("\n----- Portfolio Summary -----")

for stock, quantity in portfolio.items():
    price = stock_prices[stock]
    investment = price * quantity

    total_value += investment

    print("Stock:", stock)
    print("Quantity:", quantity)
    print("Price per Stock: $", price)
    print("Investment Value: $", investment)
    print("----------------------------")

# Display total value
print("Total Investment Value: $", total_value)

# Save results to a text file
with open("portfolio_result.txt", "w") as file:
    file.write("Stock Portfolio Summary\n")
    file.write("-----------------------\n")

    for stock, quantity in portfolio.items():
        investment = stock_prices[stock] * quantity
        file.write(
            f"{stock} - Quantity: {quantity}, "
            f"Value: ${investment}\n"
        )

    file.write(f"\nTotal Investment Value: ${total_value}")

print("\nPortfolio details saved successfully!")