# Synopsis: Simulated Annealing (SA)

**Author:** Weishan Li  
**Paper:** S. Kirkpatrick, C. D. Gelatt, and M. P. Vecchi, "Optimization by simulated annealing," *Science*, vol. 220, no. 4598, pp. 671–680, May 1983.  
**Category:** Single-State Stochastic

---

## 1. What problem with existing algorithms is the new algorithm attempting to solve?

SA escapes local optima by accepting worse outcomes with a certain probability in order to obtain the true optimal result. For NP-complete problems, exact solution methods require computing effort that grows exponentially with problem size, making them practically infeasible. SA addresses this by providing a heuristic approach that can find near-optimal solutions efficiently.

## 2. Why, or in what respect, have previous attempts failed?

For NP-complete problems, the computational cost of finding an exact solution grows exponentially with the problem size, making it practically infeasible. Furthermore, the mainstream iterative improvement methods at the time only accepted modifications that improved the result; once trapped in local optima, they could not escape, and the final result depended heavily on the initial point. Multiple random restarts were used as a workaround, but this was inefficient and provided no guarantee of finding the global optimum.

## 3. What is the new idea presented in this paper?

SA allows for the acceptance of worse solutions with a certain probability, rather than only accepting better solutions. When a new solution is worse (ΔE > 0), it is not rejected outright, but accepted with a probability of exp(−ΔE/T). The higher the temperature T, the greater the probability of accepting a worse solution. The simulated annealing process mirrors the physical cooling process in metallurgy. In the high-temperature stage, worse solutions are accepted with a high probability, enabling extensive exploration; in the low-temperature stage, better solutions are accepted almost exclusively, enabling fine-grained exploitation. The temperature gradually decreases according to an annealing schedule, automatically switching from exploration to exploitation.

## 4. How is the new approach demonstrated?

This paper uses three real-world computer hardware design problems for validation. Problem 1 involves distributing 98 chips of an IBM 370 microprocessor across two chipsets, aiming to minimise the number of interconnects. Problem 2 is a chip placement problem, placing circuit chips in physical locations with the goal of minimising interconnect length and congestion. Problem 3 is a wiring problem, using SA to find optimal paths for interconnects between chips, aiming to minimise peak interconnect density. Additionally, a classic Travelling Salesman Problem (TSP) with 400 cities is included to demonstrate generalisation.

## 5. What are the results or outcomes and how are they validated?

For the chip partitioning problem, the scheme found by SA (271 and 183 pins) is superior to rapid cooling (approximately 700 pins), significantly reducing interconnects. For the chip placement problem, peak congestion after SA is approximately 30% lower than the original design, and total interconnect length is reduced by approximately 10%, requiring only 250,000 exchanges (about 12 minutes). In the wiring experiment, SA improved over random routing by 57% and showed significant improvements over other heuristic methods. For the TSP, SA found near-optimal paths, exhibiting chaotic paths at high temperatures and converging into clear local structures at low temperatures, verifying the effectiveness of the cooling mechanism. Results are validated by comparison with random methods and rapid quenching, supported by visualisations of the annealing process.

## 6. What is your assessment of the conclusions?

The conclusions are generally credible, and the algorithm demonstrates practical significance across three real-world engineering problems. Requiring only four ingredients, it can be applied to any optimisation problem. However, the validation method is weak — it lacks statistical analysis across multiple runs, and there is no systematic comparison with other algorithms beyond random methods and rapid quenching. The annealing schedule requires manual tuning with no universal guidelines provided. In this project, SA is a single-state algorithm maintaining only one solution at a time, resulting in lower computational cost than population-based algorithms. SA serves as a useful baseline for comparison with population-based algorithms such as PSO and GWO, though its convergence speed in high-dimensional parameter spaces may be slower due to the absence of population information sharing.

---

## References

[1] S. Kirkpatrick, C. D. Gelatt, and M. P. Vecchi, "Optimization by simulated annealing," *Science*, vol. 220, no. 4598, pp. 671–680, May 1983.
