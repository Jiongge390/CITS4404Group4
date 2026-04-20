"""
Backtesting evaluator (spec Section 3 — Evaluation of Bots).

Rules:
  - Start with $1000 USD, 0 BTC
  - Buy signal: spend all cash (minus fee) on BTC at current price
  - Sell signal: sell all BTC for cash (minus fee) at current price
  - Transaction fee: 3%
  - End: sell remaining BTC at final price
  - Fitness: final cash amount
"""
import numpy as np

FEE = 0.03
STARTING_CASH = 1000.0


def backtest(prices, signals):
    """
    Parameters
    ----------
    prices  : 1-D array of closing prices aligned with signals
    signals : 1-D array of integers: +1 = buy, -1 = sell, 0 = hold

    Returns
    -------
    Final cash value (fitness).
    """
    cash = STARTING_CASH
    btc = 0.0

    for price, signal in zip(prices, signals):
        if signal > 0 and cash > 0:          # buy
            btc = cash * (1 - FEE) / price
            cash = 0.0
        elif signal < 0 and btc > 0:         # sell
            cash = btc * price * (1 - FEE)
            btc = 0.0

    # liquidate at end
    if btc > 0:
        cash = btc * prices[-1] * (1 - FEE)

    return cash
