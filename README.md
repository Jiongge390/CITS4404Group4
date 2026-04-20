# CITS4404 Group 4 — AI Trading Bots

**Unit:** Artificial Intelligence and Adaptive Systems  
**Project:** Building AI Trading Bots using Nature-Inspired Algorithms

## Team Members
| Name | Student ID |
|------|------------|
| Bomin Liao  | 24331475        |
| Weishan Li  | 24746589        |
| Ziqi Meng  | 24645175        |
| Chenxiao Jiang  | 24438869        |

## Deadlines
- **Deliverable 1** (Part 1 Synopses): Friday 24 April 2026, 11:59pm AWST
- **Deliverable 2** (Part 2 Full submission): Sunday 24 May 2026, 11:59pm AWST

## Project Overview

This project applies nature-inspired optimisation algorithms to build and tune AI trading bots for Bitcoin (BTC/USDT). The bot uses Weighted Moving Average (WMA) crossover signals, optimised via population-based adaptive algorithms.

### Part 1 — Research Paper
Literature review of nature-inspired algorithms. Each team member writes a synopsis of one algorithm. See [`part1/`](part1/).

### Part 2 — Experiment
Implementation and backtesting of AI trading bots. See [`part2/`](part2/).

## Repository Structure
```
├── data/               # Bitcoin historical data (see data/README.md to download)
├── part1/              # Algorithm synopses and comparison report
├── part2/
│   ├── bot/            # Core bot building blocks (filters, evaluator)
│   ├── algorithms/     # Nature-inspired optimisation algorithms
│   ├── experiments/    # Jupyter notebooks for experiments
│   └── results/        # Saved figures and logs
└── requirements.txt
```

## Setup

```bash
pip install -r requirements.txt
```

Data download instructions: see [`data/README.md`](data/README.md).

## Rules
- No external optimisation libraries (no scipy.optimize, optuna, etc.)
- All bot code must be written from scratch by the team
- Algorithm code adapted from papers must be acknowledged
