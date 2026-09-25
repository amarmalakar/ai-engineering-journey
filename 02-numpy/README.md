# Day 02 — NumPy

## Goal

Implement a forward pass with NumPy arrays.

## Topics

- ndarrays and broadcasting
- Vector and matrix operations
- A simple forward pass

## Project

Mini neural-network math engine: inputs, weights, matrix multiplication, bias, activation, output.

## Deliverable

A two-layer NumPy forward pass in `src/forward_pass.ipynb`.

## Setup

From `02-numpy`:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install numpy jupyterlab
```

Use the kernel that points at `02-numpy/.venv`.

## Run

Open `src/forward_pass.ipynb` and run all cells.

Practice notebooks:

```text
notebooks/01_arrays.ipynb
notebooks/02_slicing_sorting.ipynb
notebooks/03_axis_vectors.ipynb
notebooks/04_save_load.ipynb
```

## Example

```text
Output:::  [[6.5]
 [2.5]]
```

Two samples go in. Each comes out as one number. The first scores 6.5 and the second scores 2.5.

## What I Learned

`@` is matrix multiplication. The inner dimensions must match, and a bias vector is added to every row. ReLU clears negative hidden values. The same inputs and weights always produce the same output.

## Challenges

The notebook kernel has to be the `02-numpy` virtual environment. Another Python on the machine does not have NumPy installed.

## Next Step

Day 03 — analyze a dataset with Pandas.

## Commit

day-02: implement numpy forward pass
