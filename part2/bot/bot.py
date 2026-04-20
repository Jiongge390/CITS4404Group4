"""
Bot: maps a parameter vector to a fitness score.

A parameter vector encodes the full bot configuration.
Algorithms in part2/algorithms/ call Bot.evaluate(params) as their fitness function.
"""
import numpy as np
from .filters import composite_wma, crossover_filter
from .evaluator import backtest


class Bot:
    """
    Default bot: two composite WMA signals (high/low frequency) with crossover.

    Parameter vector (14-D for two composite signals):
      [w1_h, w2_h, w3_h,  d1_h, d2_h, d3_h,  alpha_h,
       w1_l, w2_l, w3_l,  d1_l, d2_l, d3_l,  alpha_l]
    """

    PARAM_DIM = 14

    def __init__(self, prices):
        self.prices = np.asarray(prices, dtype=float)

    def signals(self, params):
        """Convert parameter vector to buy/sell signal array."""
        p = params
        high = composite_wma(self.prices,
                              weights=[p[0], p[1], p[2]],
                              durations=[max(1, int(p[3])), max(1, int(p[4])), max(1, int(p[5]))],
                              alpha=np.clip(p[6], 1e-3, 1 - 1e-3))

        low  = composite_wma(self.prices,
                              weights=[p[7], p[8], p[9]],
                              durations=[max(1, int(p[10])), max(1, int(p[11])), max(1, int(p[12]))],
                              alpha=np.clip(p[13], 1e-3, 1 - 1e-3))

        n = min(len(high), len(low))
        diff = high[-n:] - low[-n:]
        raw = np.convolve(np.sign(diff), crossover_filter(), 'same')
        return np.sign(raw)

    def evaluate(self, params):
        """Return fitness (final cash) for a given parameter vector."""
        sig = self.signals(params)
        prices = self.prices[-len(sig):]
        return backtest(prices, sig)
