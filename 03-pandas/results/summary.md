# Titanic inspection

891 passengers, 12 columns. 342 survived (38.4%).

## What I checked

- Missing: Age 177, Cabin 687, Embarked 2. No duplicate rows and no duplicate PassengerId.
- Age of known passengers: median 28, mean 29.7, from 0.42 to 80.
- Fare median by class: 60.29 (1st), 14.25 (2nd), 8.05 (3rd).

## Observations

1. Women survived at 74.2%. Men survived at 18.9%.
2. Survival falls with class: 63.0% in 1st, 47.3% in 2nd, 24.2% in 3rd.
3. Those two factors stack. 1st-class women survived at 96.8%. 3rd-class women survived at 50%. 1st-class men survived at 36.9%.
4. Cabin is empty for 77% of rows, so the cleaned file keeps `HasCabin` and drops the cabin text.
5. Age is empty for 177 rows. The clean step fills those with the median, 28, and sets `AgeWasMissing` to 1. That fill is a placeholder, not a known age.
6. Two missing embarkation ports are filled with S, the most common port (644 passengers).
7. Passengers who boarded at C survived at 55.4%, Q at 39.0%, S at 33.7%.
8. Among passengers with a known age, 83 were under 16 and 59.0% of them survived, above the overall 38.4%.
9. Fare tracks class. A 3rd-class median fare is about 8; a 1st-class median fare is about 60.
10. There were no duplicate passengers to remove. Cleaning changed missing values and dropped `Cabin`. The row count stays 891.

Cleaned table: `data/processed/titanic_clean.csv` (gitignored, same as the raw CSV). Regenerate it with `python src/clean.py` from `03-pandas`.
