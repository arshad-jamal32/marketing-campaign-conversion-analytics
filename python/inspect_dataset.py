
import pandas as pd
from pathlib import Path

print("=" * 65)
print("MARKETING CAMPAIGN & CUSTOMER CONVERSION ANALYTICS")
print("DATASET INSPECTION")
print("=" * 65)

# --------------------------------------------------
# LOAD DATASET
# --------------------------------------------------

project_dir = Path(__file__).resolve().parent.parent

file_path = (
    project_dir
    / "dataset"
    / "digital_marketing_campaign_dataset.csv"
)

print("\nLoading dataset...")

df = pd.read_csv(file_path)

print("Dataset loaded successfully!")

# --------------------------------------------------
# BASIC INFORMATION
# --------------------------------------------------

print("\n1. DATASET DIMENSIONS")
print("-" * 40)

print("Total Rows:", df.shape[0])
print("Total Columns:", df.shape[1])

# --------------------------------------------------
# COLUMN INFORMATION
# --------------------------------------------------

print("\n2. COLUMN NAMES")
print("-" * 40)

print(df.columns.tolist())

# --------------------------------------------------
# FIRST FIVE RECORDS
# --------------------------------------------------

print("\n3. FIRST 5 RECORDS")
print("-" * 40)

print(df.head().to_string(index=False))

# --------------------------------------------------
# DATA TYPES
# --------------------------------------------------

print("\n4. DATA TYPES")
print("-" * 40)

print(df.dtypes)

# --------------------------------------------------
# MISSING VALUES
# --------------------------------------------------

print("\n5. MISSING VALUES")
print("-" * 40)

missing = df.isnull().sum()

print(missing[missing > 0] if missing.sum() > 0
      else "No missing values found!")

# --------------------------------------------------
# DUPLICATE RECORDS
# --------------------------------------------------

print("\n6. DUPLICATE RECORDS")
print("-" * 40)

print("Total Duplicates:", df.duplicated().sum())

# --------------------------------------------------
# STATISTICAL SUMMARY
# --------------------------------------------------

print("\n7. NUMERICAL SUMMARY")
print("-" * 40)

print(df.describe().to_string())

print("\n" + "=" * 65)
print("DATASET INSPECTION COMPLETED")
print("=" * 65)
