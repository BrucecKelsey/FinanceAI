'''
Here’s a basic Python script to kick things off. It connects to Interactive Brokers, 
fetches real-time SPY data, and calculates EMAs—key components for your bot.

This script connects to Interactive Brokers, pulls 1-minute historical intraday price 
data for the SPY ETF, calculates two Exponential Moving Averages (EMAs), and sets up the
framework for building a trading strategy.

'''

import asyncio
from ib_insync import IB, Stock, util
import pandas as pd
import talib

# Configuration
IB_HOST = '127.0.0.1'
IB_PORT = 7497  # TWS paper trading port
IB_CLIENT_ID = 1

# Connect to Interactive Brokers
ib = IB()

async def connect_broker():
    try:
        await ib.connectAsync(IB_HOST, IB_PORT, clientId=IB_CLIENT_ID)
        print("Connected to IB")
    except Exception as e:
        print(f"Connection failed: {e}")

# Fetch real-time bar data for SPY
async def get_spy_data():
    contract = Stock('SPY', 'SMART', 'USD')
    await ib.qualifyContractsAsync(contract)
    bars = await ib.reqHistoricalDataAsync(
        contract,
        endDateTime='',
        durationStr='1 D',
        barSizeSetting='1 min',
        whatToShow='TRADES',
        useRTH=True,
        formatDate=1,
        keepUpToDate=True
    )
    df = util.df(bars)
    return df

# Calculate EMAs
def calculate_indicators(df):
    df['9_EMA'] = talib.EMA(df['close'], timeperiod=9)
    df['21_EMA'] = talib.EMA(df['close'], timeperiod=21)
    return df

# Main async function
async def main():
    await connect_broker()
    df = await get_spy_data()
    df_with_indicators = calculate_indicators(df)
    print(df_with_indicators.tail())

    # Placeholder for strategy logic
    # Add Strategy V1 conditions here later

    ib.disconnect()

# Run the bot
if __name__ == "__main__":
    asyncio.run(main())
    
    
'''
async - (short for asynchronous) is a keyword in Python that allows your code to run tasks concurrently


'''