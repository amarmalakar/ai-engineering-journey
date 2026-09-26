# Data

Day 3 uses the Titanic passenger dataset: one row per passenger, with survival, class, sex, age, and fare.

## Files

| File | Commit it? | Why |
| --- | --- | --- |
| `sample.json` | Yes | Six rows from the real dataset, including one missing age. Used by the read-JSON notebook. |
| `titanic.csv` | No | The full file. `*.csv` is ignored by the repository `.gitignore`. |

## Download the full CSV

From `03-pandas`:

```bash
curl -L -o data/titanic.csv https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv
```

`src/explore.ipynb` should load `data/titanic.csv`. The practice notebook for JSON should load `data/sample.json`.

## Columns used in the exercises

- `Survived`, `Pclass`, `Sex`, `Age`, `Fare`, `Embarked` for filtering, sorting, missing values, and group-by summaries
- `PassengerId` as the key when combining tables
