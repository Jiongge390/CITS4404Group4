"""
Base class for all nature-inspired optimisation algorithms.
Each algorithm subclass implements `optimise()`.
"""
import numpy as np
from abc import ABC, abstractmethod


class BaseOptimiser(ABC):
    """
    Parameters
    ----------
    fitness_fn  : callable(params) -> float  (higher = better)
    dim         : dimensionality of the search space
    bounds      : list of (min, max) tuples, length == dim
    pop_size    : population size
    max_evals   : stopping criterion — maximum fitness evaluations
    seed        : random seed for reproducibility
    """

    def __init__(self, fitness_fn, dim, bounds, pop_size=30, max_evals=10000, seed=None):
        self.fitness_fn = fitness_fn
        self.dim = dim
        self.bounds = np.asarray(bounds, dtype=float)
        self.pop_size = pop_size
        self.max_evals = max_evals
        self.rng = np.random.default_rng(seed)
        self.eval_count = 0
        self.history = []      # (eval_count, best_fitness) per generation

    def _evaluate(self, params):
        self.eval_count += 1
        return self.fitness_fn(params)

    def _clip(self, params):
        return np.clip(params, self.bounds[:, 0], self.bounds[:, 1])

    def _random_population(self):
        low, high = self.bounds[:, 0], self.bounds[:, 1]
        return self.rng.uniform(low, high, size=(self.pop_size, self.dim))

    @abstractmethod
    def optimise(self):
        """
        Run the algorithm.
        Returns (best_params, best_fitness, history).
        """
