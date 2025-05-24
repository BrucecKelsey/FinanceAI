import yfinance as yf
import pandas as pd
import time

# Initialize portfolio
cash = 10000
shares = 0
stock_symbol = "TSLA"  # Tesla stock

# Log trades
def log_trade(action, price, shares, cash):
    with open("trades_sma.txt", "a") as f:
        f.write(f"{action}: {shares} shares at ${price:.2f}, Cash: ${cash:.2f}\n")

# Calculate SMA and check for signals
def get_trading_signal():
    stock = yf.Ticker(stock_symbol)
    data = stock.history(period="30d")  # Get 30 days of data
    close_prices = data["Close"]
    
    # Calculate 20-day SMA
    sma = close_prices.rolling(window=20).mean().iloc[-1]
    current_price = close_prices.iloc[-1]
    
    print(f"Current Price: ${current_price:.2f}, 20-day SMA: ${sma:.2f}")
    
    # Buy if price > SMA, sell if price < SMA
    if current_price > sma and cash >= current_price * 10:
        return "buy", current_price
    elif current_price < sma and shares >= 10:
        return "sell", current_price
    return None, current_price

# Main loop (run daily for simplicity)
for _ in range(5):  # Simulate 5 days
    action, price = get_trading_signal()
    
    if action == "buy":
        shares += 10
        cash -= price * 10
        log_trade("Bought", price, 10, cash)
        print(f"Bought 10 shares at ${price:.2f}, Cash: ${cash:.2f}")
    elif action == "sell":
        shares -= 10
        cash += price * 10
        log_trade("Sold", price, 10, cash)
        print(f"Sold 10 shares at ${price:.2f}, Cash: ${cash:.2f}")
    
    # Simulate waiting a day
    print("Waiting for next day...")
    time.sleep(5)  # Shortened for testing
