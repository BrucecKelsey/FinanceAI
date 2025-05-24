Words of Wisdom from Grok
Pretrained models for financial prediction (e.g., LSTM via TensorFlow) exist but are risky due to market complexity. Start with rule-based strategies (like V1) and explore machine learning later if needed.
Github
https://github.com/BrucecKelsey/FinanceAI - This will hold a directory of all the different code and projects involved

Ideas
Follow some people who (tjr, ict) analyze trading models to combine certain aspects of them.
Analyze fair value gaps
SMT divergence
Move this entire document to github
Plug into funded account, monthly expense, $100 month, given test to prove profitable, after, you get an allocation of lots of money ($100,000) and you get payouts. You assert no risk. 
What if there are any pretrained model out there to try and work with?
Use large language model (LLM) to interact with twitter api to determine trading strategy
Possibly implement web scraping techniques for Options Flow

Possible Python Packages
TA-Lib - Technical Indicators ### Whatever that means
Matplotlib - Chart Visualation

Tasks
Setup program to find the best graph of each stock, Trading view is best

Coding Practices
Asyncio - Understand async and await syntax (Said to be commonly used in trading)
Tools & Platforms
Broker: Thinkorswim (TD Ameritrade), Webull, or Interactive Brokers


Charting: TradingView or Thinkorswim for real-time technical analysis


News Feed: Benzinga Pro, Market Chameleon, or Twitter (for momentum/news catalysts)


Options Flow: Unusual Whales, FlowAlgo, Cheddar Flow (for tracking large institutional orders)


Strategy Type
Primarily Day Trading Weekly Options on high-volume tickers such as:
SPY / QQQ / IWM


TSLA, NVDA, AAPL, AMZN, META


Contract Focus:
0DTE (Zero Days to Expiry) or 1-2 days out


OTM contracts with tight spreads, high open interest

Risk Management
Max loss per trade: 1-2% of account


Stop loss: Hard stop below support (or soft stop based on EMA cross/VWAP break)


Position sizing: Based on account size and theta decay — usually small positions for 0DTE


No chasing! Must enter only on confirmation
Technical Indicators & Chart Setup
Exponential Moving Averages (EMAs): Commonly uses 9 EMA and 21 EMA to identify short-term trends.


Volume Profile: Analyzes volume at different price levels to identify areas of high trading activity.


Liquidity Zones: Marks areas where stop-loss orders are likely placed, anticipating potential price reversals.


Break of Structure (BOS): Identifies shifts in market structure to signal potential trend changes.


Fair Value Gaps (FVGs): Looks for price imbalances that the market may return to fill.
Entry Conditions:
Confluence of Factors: Enters trades when multiple indicators align, such as a break of structure coinciding with a fair value gap and liquidity sweep.


Market Structure: Looks for confirmation of trend direction through higher highs/lows or lower highs/lows.


Liquidity Sweeps: Waits for the market to take out liquidity before entering in the direction of the anticipated move.


Exit Strategies:
Partial Profit Taking: Secures profits at predetermined levels to reduce risk.


Trailing Stop Loss: Adjusts stop-loss orders to lock in gains as the trade moves favorably.


Time-Based Exits: Closes positions if the trade doesn't progress as expected within a certain timeframe.


Strategy V1
Step
Condition
1. Liquidity Sweep
Price breaks below a prior swing low with a large wick (stop run).
2. FVG Appears
A fair value gap forms immediately after sweep on bullish candle(s).
3. Market Structure Shift
Break of structure (BOS) above a recent lower high (bullish BOS).
4. Retest of FVG or OB
Price returns to fill FVG or taps into the OB.
5. Confirmation Candle
Bullish engulfing / pin bar / rejection candle in the FVG/OB zone.
6. Entry
Enter at retest candle close.
7. Stop Loss
Just below the liquidity sweep low.
8. Take Profit
R:R of 2:1, or opposing OB or swing high.

Short Setup = reverse the conditions (sweep of highs, bearish FVG, etc.)








Key Concepts Explained
SMT Divergence (Smart Money Tool)
Identifies when correlated assets (e.g., SPY and QQQ) move out of sync, signaling potential reversals or weak trends.


Fair Value Gap (FVG) & Imbalance FVG (IFVG)
Price gaps left by rapid moves indicating unfilled orders. Price often returns to these areas for liquidity fills.


Accumulation / Manipulation / Distribution (A/M/D)
Market phases representing smart money activity:


Accumulation: Quiet buying.


Manipulation: Stop hunts and liquidity grabs.


Distribution: Selling off into strength.


Inversions
Contradictory price or volume action against the prevailing trend, indicating potential trend exhaustion.


Price Action
Analysis of naked charts, candlestick formations, and key levels without relying solely on indicators.


Supply and Demand Zones
Price areas with historical buying or selling pressure causing significant reversals or consolidations.


Order Blocks and Rejection Blocks
Institutional order areas (order blocks) where price pauses or reverses and rejection blocks where price is aggressively turned back.


Liquidity Sweeps
Moves that "hunt" stops or liquidity clusters before reversing direction.


Buy-Side Liquidity
Stop orders placed above resistance or swing highs targeted by smart money to trigger entries or exits.



3. Strategy Framework
3.1 Setup Phase
Identify supply and demand zones on underlying assets (e.g., SPY, QQQ).


Mark order blocks where strong institutional activity occurred.


Locate Fair Value Gaps (FVG) and Imbalance FVG (IFVG) on short timeframes (1-min to 5-min charts).


Observe SMT divergence between correlated assets to gauge trend strength.


3.2 Entry Criteria
Liquidity Sweep Confirmation


Wait for price to sweep buy-side or sell-side liquidity levels (above highs or below lows) to trigger stops.


Order/Rejection Block Test


Price should reject at an identified order or rejection block or revisit an FVG zone after the sweep.


Accumulation / Manipulation / Distribution Signal


Confirm phase via volume patterns and price behavior.


Price Action Confirmation


Look for bullish or bearish candlestick signals (e.g., pin bars, engulfing candles) at key zones.


SMT Divergence Check


Validate directional bias using correlated market divergence.


3.3 Entry Execution
Buy Calls if liquidity sweep, order block rejection, bullish price action, accumulation phase, and SMT divergence all align bullishly.


Buy Puts if liquidity sweep, order block rejection, bearish price action, distribution phase, and SMT divergence confirm bearish bias.
4. Trade Management
Set stop losses just beyond order or rejection blocks or liquidity sweep extremes.


Target next FVG, supply, or demand zone for taking profits.


Monitor for inversions signaling potential exit or trade adjustment.


Consider options’ theta decay by trading near-the-money with short expiration to capitalize on intraday moves.



5. Practical Example
SPY makes a new high while QQQ fails to confirm (bearish SMT divergence).


QQQ price sweeps above a recent swing high (buy-side liquidity sweep).


Price drops back and rejects an order block zone.


Volume pattern shows accumulation and manipulation phases.


Bearish pin bar forms on QQQ chart.


Enter put options on QQQ.


Place stop loss just above the liquidity sweep high.


Target next demand zone or FVG for profit taking.



6. Additional Notes
Use 1- to 5-minute charts for intraday entries.


Volume Profile or VWAP overlays help identify supply and demand zones.


Track multiple correlated symbols for better SMT divergence confirmation.


Keep a detailed trading journal to refine and optimize strategy execution.

