# Day 01 — Python

## Goal

Become comfortable writing Python, and ship a CLI expense tracker with JSON persistence.

## Topics

- Python 3.11+, venv, pip, Git, environment variables
- Variables, data types, lists, tuples, dictionaries, sets
- Conditions, loops, functions, comprehensions
- Classes, modules, exceptions, async programming, args/kwargs

## Project

CLI expense tracker: add, delete, list, filter by category, totals, save and load JSON.

## Deliverable

A working Python CLI with JSON persistence.

## Setup

From the repository root:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install pytest
```

## Run

From `01-python`:

```bash
export PYTHONPATH=src
export EXPENSE_FILE=data/expenses.json
python -m expense_tracker.cli add --amount 240.5 --category food --note lunch
python -m expense_tracker.cli list
python -m expense_tracker.cli list --category food
python -m expense_tracker.cli total
python -m expense_tracker.cli total --category food
python -m expense_tracker.cli delete --id 1
```

Practice scripts:

```bash
python practice/1_collections.py
python practice/2_control_flow.py
python practice/3_language.py
```

Tests:

```bash
PYTHONPATH=src pytest
```

## Example

```
added #1 food 240.50
#1  240.50  food  lunch
food: 240.50
all: 240.50
```

## What I Learned

Python packages, `argparse`, and JSON load/save are enough for a small CLI. An environment variable (`EXPENSE_FILE`) chooses the data file, and `pytest` checks add, filter, total, delete, and async load without touching the real expense file.

## Challenges

Running the package needs `PYTHONPATH=src` so `expense_tracker` imports resolve. The live expense file has to stay out of Git while the example JSON stays committed.

## Next Step

Day 02 — NumPy forward pass.

## Commit

day-01: build python cli
