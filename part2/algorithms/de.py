"""
Differential Evolution optimiser.

Reference:
  Storn, R. and Price, K. (1997). Differential Evolution - A Simple and
  Efficient Heuristic for Global Optimization over Continuous Spaces.

Usage:
  opt = DifferentialEvolution(fitness_fn, dim, bounds)
  best_params, best_fitness, history = opt.optimise()

  opt = DifferentialEvolution(fitness_fn, dim, bounds, minimise=True)
"""
import numpy as np

from .base import BaseOptimiser


class DifferentialEvolution(BaseOptimiser):
    """
    Differential Evolution using the DE/rand/1/bin strategy.

    Parameters
    ----------
    mutation_factor : float
        Scale factor F used during mutation.
    crossover_rate : float
        Binomial crossover probability CR.
    minimise : bool
        If True, lower fitness values are treated as better. If False, higher
        fitness values are treated as better.
    """

    def __init__(
        self,
        fitness_fn,
        dim,
        bounds,
        pop_size=30,
        max_evals=10000,
        seed=None,
        mutation_factor=0.8,
        crossover_rate=0.9,
        minimise=False,
    ):
        super().__init__(fitness_fn, dim, bounds, pop_size, max_evals, seed)
        if pop_size < 4:
            raise ValueError("Differential Evolution requires pop_size >= 4.")
        if not 0 < mutation_factor <= 2:
            raise ValueError("mutation_factor must be in the range (0, 2].")
        if not 0 <= crossover_rate <= 1:
            raise ValueError("crossover_rate must be in the range [0, 1].")
        self.mutation_factor = mutation_factor
        self.crossover_rate = crossover_rate
        self.minimise = minimise

    def _is_better(self, candidate_fitness, current_fitness):
        if self.minimise:
            return candidate_fitness < current_fitness
        return candidate_fitness > current_fitness

    def optimise(self):
        population = self._random_population()
        fitness = np.array([self._evaluate(ind) for ind in population])

        best_idx = np.argmin(fitness) if self.minimise else np.argmax(fitness)
        best_params = population[best_idx].copy()
        best_fitness = fitness[best_idx]
        self.history.append((self.eval_count, best_fitness))

        while self.eval_count < self.max_evals:
            for i in range(self.pop_size):
                if self.eval_count >= self.max_evals:
                    break

                candidates = [idx for idx in range(self.pop_size) if idx != i]
                a_idx, b_idx, c_idx = self.rng.choice(candidates, 3, replace=False)
                a, b, c = population[a_idx], population[b_idx], population[c_idx]

                mutant = self._clip(a + self.mutation_factor * (b - c))

                crossover_mask = self.rng.random(self.dim) < self.crossover_rate
                if not np.any(crossover_mask):
                    crossover_mask[self.rng.integers(0, self.dim)] = True

                trial = np.where(crossover_mask, mutant, population[i])
                trial_fitness = self._evaluate(trial)

                if self._is_better(trial_fitness, fitness[i]):
                    population[i] = trial
                    fitness[i] = trial_fitness

                    if self._is_better(trial_fitness, best_fitness):
                        best_fitness = trial_fitness
                        best_params = trial.copy()

            self.history.append((self.eval_count, best_fitness))

        return best_params, best_fitness, self.history
