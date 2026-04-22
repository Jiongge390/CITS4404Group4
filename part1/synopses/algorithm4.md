# Synopsis: Particle Swarm Optimization (PSO)

**Author:** Chenxiao Jiang  
**Paper:** J. Kennedy and R. Eberhart, "Particle swarm optimization," in *Proc. ICNN'95 — Int. Conf. Neural Networks*, Perth, WA, Australia, 1995, vol. 4, pp. 1942–1948.  
**Category:** Swarm Intelligence

---

## 1. What problem with existing algorithms is the new algorithm attempting to solve?

According to Kennedy and Eberhart, they attempted to develop an algorithm that is simpler and more computationally efficient than existing algorithms, especially Genetic Algorithms (GA). Although GA can perform global search, it also requires complex evolutionary operations, making it relatively expensive and difficult to implement. The authors noticed that information sharing among animals — for instance flocks of birds and schools of fish — enables groups to find unpredictably distributed resources more efficiently than individuals. They hypothesised that this collective behaviour could be the basis for a simpler but effective optimisation algorithm driven by social information sharing, without using complex genetic operators.

## 2. Why, or in what respect, have previous attempts failed?

The primary deficiency of Genetic Algorithms was their complexity, with operators such as crossover, mutation, and selection leading to significant computational overhead. In addition, the performance of genetic algorithms is highly sensitive to the tuning of multiple hyperparameters, making them difficult to apply without domain expertise. These factors motivated the search for a simpler population-based algorithm that could achieve comparable performance with fewer parameters and less implementation complexity.

## 3. What is the new idea presented in this paper?

PSO introduces a swarm of particles, where each particle represents a candidate solution moving through a multidimensional search space. Each particle maintains two key memories: its personal best position and the global best position found by the swarm. At each iteration, velocities are updated based on the rule: v_id ← v_id + 2r₁(pbest_id − x_id) + 2r₂(gbest_d − x_id), where r₁ and r₂ are independent random values between 0 and 1. Each particle's position is then updated by adding the new velocity to its current position. Compared to GA and Evolutionary Programming, PSO enables a directed collective search towards the global optimum without requiring complex genetic operations.

## 4. How is the new approach demonstrated?

The authors demonstrate PSO through iterative simulation experiments and benchmark testing, recording the algorithm's development from early bird flocking simulations to the final velocity update rule. PSO is evaluated through two applications: training a feedforward neural network on the XOR problem and the Fisher Iris dataset, and optimising Schaffer's f6 function, a standard GA benchmark with many local optima. The paper provides references based on prior work including Reynolds' bird simulations and Millonas' swarm intelligence principles. However, lack of formal reproducibility information such as random seeds may limit the ability to reproduce exact results.

## 5. What are the results or outcomes and how are they validated?

PSO is validated through comparison with both traditional and evolutionary approaches. In the XOR neural network task, PSO performed similarly to standard backpropagation, while PSO achieved 92% test accuracy in an EEG classification task compared to backpropagation's 89%. On Schaffer's f6 benchmark, PSO found the global optimum on every run, with a comparable number of evaluations to elementary GA. These results indicate that PSO is competitive with backpropagation in generalisation metrics and remains competitive with GA on benchmark optimisation, while offering much lower implementation complexity.

## 6. What is your assessment of the conclusions?

The authors conclude that PSO is a simple yet effective algorithm for optimising a wide range of functions. However, the experiments cover only two application domains, which is relatively narrow in scope, and limitations such as premature convergence were only identified in later work. Overall, PSO was chosen for this project because it satisfies the requirements of being a population-based optimisation algorithm that maintains a swarm of candidate solutions iteratively updated for improvement. Its simple structure makes it easy to implement from scratch, which is suitable for optimising the multidimensional parameter space of the trading bot.

---

## References

[1] J. Kennedy and R. Eberhart, "Particle swarm optimization," in *Proc. ICNN'95 — Int. Conf. Neural Networks*, Perth, WA, Australia, 1995, vol. 4, pp. 1942–1948.  
[2] C. W. Reynolds, "Flocks, herds and schools: A distributed behavioral model," *Computer Graphics*, vol. 21, no. 4, pp. 25–34, 1987.  
[3] M. M. Millonas, "Swarms, phase transitions, and collective intelligence," in *Artificial Life III*, C. G. Langton, Ed. Reading, MA: Addison Wesley, 1994.
