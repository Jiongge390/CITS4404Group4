# Data

Large data files are NOT committed to this repo. Download manually.

## Bitcoin Historical Dataset (Kaggle)

Source: https://www.kaggle.com/datasets/prasoonkottarathil/btcinusd

Download the dataset and place files into `data/raw/`:

```
data/raw/
├── BTC-Daily.csv      # Daily OHLCV (~2652 rows, 2014–2022)
├── BTC-Hourly.csv     # Hourly OHLCV
└── BTC-Minutely.csv   # Per-minute OHLCV (~600k rows/year)
```

## Train / Test Split

Per project specification:
- **Train:** data prior to 2020
- **Test:** data from 2020 onwards (held out, used only for final evaluation)

Preprocessing scripts are in `part2/experiments/01_data_exploration.ipynb`.
