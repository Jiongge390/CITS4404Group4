# Synopsis: Grey Wolf Optimizer (GWO)

**Author:** Bomin Liao  
**Paper:** Mirjalili, S., Mirjalili, S.M. & Lewis, A. (2014). Grey Wolf Optimizer. *Advances in Engineering Software*, 69, 46–61.  
**Category:** Swarm Intelligence

---

## Q1. What problem with existing algorithms is GWO attempting to solve?

Although Swarm Intelligence is widely used in algorithms, no one has yet attempted to use the social hierarchy of gray wolves to guide the search direction. This approach utilizes the social and hunting behaviors of gray wolves to simulate the algorithm. By simulating the alpha/beta/delta/omega hierarchy of gray wolves, the search direction is guided simultaneously by the three optimal solutions, thus achieving a more natural balance between exploration and exploitation.

## Q2. Why, or in what respect, have previous attempts failed?

In previous Evolutionary algorithms (EA), EA-type algorithms (GA, DE) discarded information from each generation, wasting search experience. Furthermore, none of the existing algorithms adequately addressed the balance between exploration and exploitation. In Swarm Intelligence (SI) algorithms, no algorithm utilizes social hierarchies to guide the search, leaving an unfilled gap.

## Q3. What is the new idea presented in this paper?

In this paper, four levels — α, β, δ, and ω — represent the quality ranking of candidate solutions. The three best solutions (α, β, and δ) collectively guide the movement of other solutions. The parameter A decreases with iteration; in the first half, |A|≥1 forces exploration, and in the second half, |A|<1 forces utilisation, with automatic switching. Simultaneously, the three best solutions are retained, and all other wolves are updated with the average position of these three solutions to avoid being misled by a single optimal solution. Random coefficients A and C are used to control convergence and divergence, naturally achieving the switching between global and local search.

## Q4. How is the new approach demonstrated?

The paper uses 29 standard test functions for verification, divided into four categories: unimodal functions (F1–F7) for testing exploitation capabilities, multimodal functions (F8–F13) for testing exploration capabilities, fixed-dimensional multimodal functions (F14–F23) for testing local optimum escape capabilities, and composite functions (F24–F29) for simultaneously testing both. Comparisons are made with PSO, GSA, DE, EP, and ES, with each function run 30 times and the average and standard deviation calculated. Furthermore, the paper uses three real-world engineering problems — spring compression design, welded beam design, and pressure vessel design — for verification, and also optimises the design of photonic crystal waveguides (PCWs) in optical engineering.

## Q5. What are the results or outcomes and how are they validated?

In testing unimodal functions for exploitation, GWO outperformed PSO, GSA, DE, and EP on multiple functions, and performed excellently on multimodal functions for exploration, demonstrating strong global search capabilities. It outperformed all others on half of the composite functions and remained competitive in the rest. In practical engineering applications, GWO found the lightest design for spring design, the lowest-cost design for welded beams, and the lowest-cost design for pressure vessels, outperforming PSO, GA, DE, and ES. In real-world optical engineering applications, it significantly improved bandwidth by 93% and NDBP by 65%. The verification method involved running each function 30 times, recording the mean and standard deviation, and comparing horizontally with five algorithms (PSO, GSA, DE, EP, and ES), as well as against mathematical methods and other heuristic algorithms on engineering problems.

## Q6. What is your assessment of the conclusions?

The conclusions are generally reliable, and the experimental design is relatively comprehensive. However, the comparison algorithms are somewhat outdated, and GWO's generalisation ability in high-dimensional scenarios still needs to be verified. Nevertheless, GWO's simplicity and adaptive mechanism make it a promising candidate for the parameter optimisation task in this project. Specifically, optimising a trading bot requires tuning continuous parameters such as moving average window sizes, where the search space is multi-dimensional but the evaluation function (e.g. return on investment) is straightforward to compute. GWO's few tunable parameters and its ability to balance exploration and exploitation adaptively make it well-suited for this type of problem.

---

## References

Mirjalili, S., Mirjalili, S.M. & Lewis, A. (2014). Grey Wolf Optimizer. *Advances in Engineering Software*, 69, 46–61. https://doi.org/10.1016/j.advengsoft.2013.12.007
