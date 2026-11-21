
import pandas as pd
from pathlib import Path

print("=" * 65)
print("FINAL CLEANED DATASET VALIDATION")
print("=" * 65)

project_dir = Path(__file__).resolve().parent.parent

file_path = (
    project_dir
    / "dataset"
    / "processed"
    / "marketing_campaign_cleaned.csv"
)

df = pd.read_csv(file_path)

print("\n1. DATASET SHAPE")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

print("\n2. COLUMN NAMES")
print(df.columns.tolist())

print("\n3. DATA TYPES")
print(df.dtypes)

print("\n4. MISSING VALUES")
print(df.isnull().sum().sum())

print("\n5. DUPLICATE RECORDS")
print(df.duplicated().sum())

print("\n6. CUSTOMER ID VALIDATION")
print("Unique IDs:", df["customerid"].nunique())

print("\n7. CONVERSION DISTRIBUTION")
print(df["conversion"].value_counts())

print("\n8. FIRST FIVE RECORDS")
print(df.head().to_string(index=False))

print("\n" + "=" * 65)
print("FINAL VALIDATION COMPLETED")
print("=" * 65)
