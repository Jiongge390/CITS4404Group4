"""
Random Search — single-state baseline for comparison.
Used to benchmark population-based algorithms on equal eval budget.
"""
import numpy as np
from .base import BaseOptimiser


class RandomSearch(BaseOptimiser):

    def optimise(self):
        best_params = None
        best_fitness = -np.inf

        while self.eval_count < self.max_evals:
            params = self._clip(
                self.rng.uniform(self.bounds[:, 0], self.bounds[:, 1])
            )
            fitness = self._evaluate(params)
            if fitness > best_fitness:
                best_fitness = fitness
                best_params = params.copy()
                self.history.append((self.eval_count, best_fitness))

        return best_params, best_fitness, self.history
