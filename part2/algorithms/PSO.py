"""
Particle Swarm Optimization (PSO)

Reference:
  J. Kennedy and R. Eberhart, "Particle swarm optimization,"
  in Proc. ICNN'95 - Int. Conf. Neural Networks, 1995, vol. 4, pp. 1942–1948.

  Inertia weight variant:
  Y. Shi and R. Eberhart, "A modified particle swarm optimizer,"
  in Proc. IEEE ICEC, 1998, pp. 69-73.

Usage:
  opt = PSO(fitness_fn, dim, bounds, pop_size=20, max_evals=10000, seed=42)
  best_params, best_fitness, history = opt.optimise()
"""
import numpy as np
from .base import BaseOptimiser


class PSO(BaseOptimiser):
    """
    Particle Swarm Optimization with inertia weight.

    Parameters
    ----------
    w  : inertia weight (default 0.7)
    c1 : cognitive coefficient, attraction to personal best (default 2.0)
    c2 : social coefficient, attraction to global best (default 2.0)
    """

    def __init__(self, fitness_fn, dim, bounds,
                 pop_size=20, max_evals=10000, seed=None,
                 w=0.7, c1=2.0, c2=2.0):
        super().__init__(fitness_fn, dim, bounds, pop_size, max_evals, seed)
        self.w  = w
        self.c1 = c1
        self.c2 = c2

    def optimise(self):
        # --- Step 1: Initialise positions and velocities ---
        positions  = self._random_population()
        vel_range  = self.bounds[:, 1] - self.bounds[:, 0]
        velocities = self.rng.uniform(
            -vel_range, vel_range, size=(self.pop_size, self.dim)
        )

        # --- Step 2: Evaluate initial swarm ---
        fitness   = np.array([self._evaluate(positions[i]) for i in range(self.pop_size)])
        pbest_pos = positions.copy()
        pbest_val = fitness.copy()

        gbest_idx = np.argmax(pbest_val)
        gbest_pos = pbest_pos[gbest_idx].copy()
        gbest_val = pbest_val[gbest_idx]

        self.history.append((self.eval_count, gbest_val))

        # --- Step 3: Main loop ---
        while self.eval_count < self.max_evals:
            for i in range(self.pop_size):
                if self.eval_count >= self.max_evals:
                    break

                # Update velocity
                # v = w*v + c1*r1*(pbest - x) + c2*r2*(gbest - x)
                r1 = self.rng.random(self.dim)
                r2 = self.rng.random(self.dim)
                velocities[i] = (
                    self.w  * velocities[i]
                    + self.c1 * r1 * (pbest_pos[i] - positions[i])
                    + self.c2 * r2 * (gbest_pos    - positions[i])
                )

                # Update position and clip to bounds
                positions[i] = self._clip(positions[i] + velocities[i])

                # Evaluate and update pbest / gbest
                val = self._evaluate(positions[i])
                if val > pbest_val[i]:
                    pbest_val[i] = val
                    pbest_pos[i] = positions[i].copy()
                if val > gbest_val:
                    gbest_val = val
                    gbest_pos = positions[i].copy()

            self.history.append((self.eval_count, gbest_val))

        best_params = self._clip(gbest_pos)
        return best_params, gbest_val, self.history