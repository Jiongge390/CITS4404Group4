"""
WMA filter building blocks (spec Section 2.1).
All filters follow the convolution pattern: signal = wma(P, N, kernel(N))
"""
import numpy as np


def pad(P, N):
    """Flip-pad the signal so the WMA starts at index 0."""
    padding = -np.flip(P[1:N])
    return np.append(padding, P)


def wma(P, N, kernel):
    """Convolve padded price series P with a filter kernel of length N."""
    return np.convolve(pad(P, N), kernel, 'valid')


def sma_filter(N):
    """Boxcar (equal-weight) filter — Simple Moving Average."""
    return np.ones(N) / N


def lma_filter(N):
    """Triangular (linearly-decaying) filter — Linear-Weighted Moving Average."""
    weights = np.array([(N - k) for k in range(N)], dtype=float)
    return weights / weights.sum()


def ema_filter(N, alpha=0.3):
    """Exponential-decay filter — Exponential Moving Average."""
    weights = np.array([alpha * (1 - alpha) ** k for k in range(N)], dtype=float)
    return weights / weights.sum()


def crossover_filter():
    """
    Detects sign changes in a difference signal (Equation 6 in spec).
    Returns +1 at a golden cross (buy) and -1 at a death cross (sell).
    """
    return np.array([0.5, -0.5])


# ── Composite signal ───────────────────────────────────────────────────────────

def composite_wma(P, weights, durations, alpha=0.3):
    """
    Weighted combination of SMA, LMA and EMA (Equation 7 in spec).

    Parameters
    ----------
    P        : price series (numpy array)
    weights  : [w_sma, w_lma, w_ema]
    durations: [d_sma, d_lma, d_ema]
    alpha    : EMA smoothing factor

    Returns
    -------
    Normalised composite WMA signal.
    """
    w1, w2, w3 = weights
    d1, d2, d3 = durations

    s = (w1 * wma(P, d1, sma_filter(d1))
         + w2 * wma(P, d2, lma_filter(d2))
         + w3 * wma(P, d3, ema_filter(d3, alpha)))

    total = w1 + w2 + w3
    return s / total if total != 0 else s
