from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
RAW_CSV = ROOT / "data" / "titanic.csv"
CLEAN_CSV = ROOT / "data" / "processed" / "titanic_clean.csv"


def load(path=RAW_CSV):
    return pd.read_csv(path)


def inspect(df):
    print("shape:", df.shape)
    print(df.dtypes)
    print("missing:\n", df.isnull().sum())
    print("duplicate rows:", int(df.duplicated().sum()))
    print("duplicate PassengerId:", int(df["PassengerId"].duplicated().sum()))
    print(df[["Age", "Fare"]].describe())
    return df


def clean(df):
    """Return a new table. The raw frame is left as loaded."""
    out = df.drop_duplicates(subset=["PassengerId"]).copy()
    # Keep a flag so a filled age is not treated as a known age.
    out["AgeWasMissing"] = out["Age"].isna().astype(int)
    out["Age"] = out["Age"].fillna(out["Age"].median())
    out["Embarked"] = out["Embarked"].fillna(out["Embarked"].mode().iloc[0])
    out["HasCabin"] = out["Cabin"].notna().astype(int)
    return out.drop(columns=["Cabin"])


def save(df, path=CLEAN_CSV):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False)
    print("wrote", path, df.shape)
    return path


if __name__ == "__main__":
    raw = load()
    inspect(raw)
    save(clean(raw))
