# Day 03 — Pandas

## Goal

Load a dataset and answer questions about it with Pandas.

## Topics

- DataFrames and Series
- Cleaning and filtering
- Summary statistics

## Project

Data analysis

## Deliverable

A short dataset analysis

## Setup

From `03-pandas`, with the virtual environment active:

```bash
pip install -r requirements.txt
```

`data/titanic.csv` is the raw file. `*.csv` is gitignored, so it stays on this machine.

## Run

```bash
python src/clean.py
```

Then open `src/explore.ipynb` and run all cells. Findings are in `results/summary.md`. The cleaned table is `data/processed/titanic_clean.csv`.

## Example

891 passengers. Women survived at 74.2%, men at 18.9%. 1st class survived at 63.0%, 3rd class at 24.2%. Age was missing for 177 rows; the clean step fills those with the median and keeps an `AgeWasMissing` flag.

## What I Learned

_Fill this in at the end of the day._

## Challenges

_Fill this in at the end of the day._

## Next Step

_Fill this in at the end of the day._

## Commit

day-03: analyze dataset with pandas
