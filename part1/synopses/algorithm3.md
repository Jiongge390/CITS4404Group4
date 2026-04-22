# Synopsis: Differential Evolution (DE)

**Author:** Ziqi Meng  
**Paper:** R. Storn and K. Price, "Differential evolution — A simple and efficient heuristic for global optimization over continuous spaces," *Journal of Global Optimization*, vol. 11, no. 4, pp. 341–359, 1997.  
**Category:** Evolutionary Algorithm

---

## 1. What problem with existing algorithms is the new algorithm attempting to solve?

Differential Evolution was first proposed by Storn and Price as a method for global optimisation in continuous spaces. Traditional optimisation methods, such as gradient-based techniques, require smooth and differentiable objective functions, which limits their applicability in real-world scenarios. Many practical problems, including parameter tuning in trading strategies, involve irregular search spaces where such assumptions do not hold.

## 2. Why, or in what respect, have previous attempts failed?

Earlier optimisation approaches, including gradient descent and classical numerical methods, often struggled with getting trapped in local optima, requiring derivative information, and performing poorly in high-dimensional or noisy search spaces. Even earlier evolutionary algorithms like Genetic Algorithms (GA) involve complex operations such as encoding and crossover design, making them harder to tune and implement effectively. These limitations highlighted the need for a more flexible and simpler optimisation approach.

## 3. What is the new idea presented in this paper?

The core innovation of DE lies in its mutation strategy based on vector differences between individuals in the population. Instead of relying on predefined probability distributions, DE generates new candidate solutions by combining existing ones: v = x₁ + F·(x₂ − x₃), where x₁, x₂, x₃ are randomly selected individuals and F is a scaling factor. This approach allows DE to adaptively explore the search space, maintain diversity without complex operators, and efficiently balance exploration and exploitation. The simplicity and effectiveness of this mechanism distinguish DE from other evolutionary algorithms.

## 4. How is the new approach demonstrated?

DE operates through a population-based iterative process consisting of four main steps: (1) Initialisation — generate an initial population of candidate solutions randomly; (2) Mutation — create a mutant vector using the weighted difference of other individuals; (3) Crossover — combine the mutant vector with the target vector to form a trial solution; (4) Selection — replace the target solution if the trial solution has better fitness. This process is repeated until a stopping condition is met, such as a maximum number of iterations or convergence. The approach is demonstrated through standard benchmark functions and comparisons with other algorithms.

## 5. What are the results or outcomes and how are they validated?

DE has been widely tested on benchmark optimisation problems and compared with other algorithms such as Genetic Algorithms and Particle Swarm Optimisation. Results generally show that DE achieves faster convergence, provides competitive or superior accuracy, and performs particularly well on continuous optimisation problems. Validation is conducted using standard benchmark functions, with performance measured in terms of convergence speed and solution quality.

## 6. What is your assessment of the conclusions?

The conclusions presented in studies on DE are generally well-supported by experimental results. The algorithm demonstrates strong performance across a variety of problem types, particularly in continuous domains. Its simplicity, combined with a small number of control parameters (F and CR), makes it both practical and efficient. For this project, DE is a suitable choice as it aligns well with the optimisation of trading bot parameters, which involve continuous variables. Its balance between performance and implementation simplicity makes it a strong candidate for further experimentation in Part 2.

---

## References

[1] R. Storn and K. Price, "Differential evolution — A simple and efficient heuristic for global optimization over continuous spaces," *Journal of Global Optimization*, vol. 11, no. 4, pp. 341–359, 1997.  
[2] T. Eltaeib and A. Mahmood, "Differential evolution: A survey and analysis," *Applied Sciences*, vol. 8, no. 10, p. 1945, 2018.
