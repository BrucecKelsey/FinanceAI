import yfinance as yf
import time

# Initialize portfolio
cash = 10000  # Starting cash
shares = 0    # Shares owned
stock_symbol = "AAPL"  # Apple stock
buy_price = 150  # Buy if price <= $150
sell_price = 160  # Sell if price >= $160

# Log trades to a file
def log_trade(action, price, shares, cash):
    with open("trades.txt", "a") as f:
        f.write(f"{action}: {shares} shares at ${price}, Cash: ${cash:.2f}\n")

# Main trading loop
while True:
    # Fetch stock data
    stock = yf.Ticker(stock_symbol)
    price = stock.history(period="1d")["Close"].iloc[-1]  # Latest closing price
    print(f"Current price of {stock_symbol}: ${price:.2f}")

    # Trading logic
    if price <= buy_price and cash >= price * 10:  # Buy 10 shares if affordable
        shares += 10
        cash -= price * 10
        log_trade("Bought", price, 10, cash)
        print(f"Bought 10 shares at ${price:.2f}, Cash: ${cash:.2f}")
    elif price >= sell_price and shares >= 10:  # Sell 10 shares if owned
        shares -= 10
        cash += price * 10
        log_trade("Sold", price, 10, cash)
        print(f"Sold 10 shares at ${price:.2f}, Cash: ${cash:.2f}")
    
    # Wait before next check (e.g., 60 seconds)
    time.sleep(60)
