"""
[Algorithm 1 Name] — implement here.

Reference:
  [Full citation]

Usage:
  opt = Algorithm1(fitness_fn, dim, bounds)
  best_params, best_fitness, history = opt.optimise()
"""
import numpy as np
from .base import BaseOptimiser


class Algorithm1(BaseOptimiser):

    def optimise(self):
        raise NotImplementedError("Implement Algorithm 1 here.")
