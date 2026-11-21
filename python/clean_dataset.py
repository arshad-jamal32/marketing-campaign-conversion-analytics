
import pandas as pd
from pathlib import Path

print("=" * 65)
print("MARKETING CAMPAIGN & CUSTOMER CONVERSION ANALYTICS")
print("DATA CLEANING")
print("=" * 65)

# --------------------------------------------------
# PATHS
# --------------------------------------------------

project_dir = Path(__file__).resolve().parent.parent

input_file = (
    project_dir / "dataset"
    / "digital_marketing_campaign_dataset.csv"
)

output_dir = project_dir / "dataset" / "processed"
output_dir.mkdir(parents=True, exist_ok=True)

output_file = output_dir / "marketing_campaign_cleaned.csv"

# --------------------------------------------------
# LOAD RAW DATA
# --------------------------------------------------

print("\n1. LOADING RAW DATA")
print("-" * 45)

df = pd.read_csv(input_file)

print("Original Rows:", df.shape[0])
print("Original Columns:", df.shape[1])

# --------------------------------------------------
# REMOVE CONSTANT COLUMNS
# --------------------------------------------------

print("\n2. REMOVING CONSTANT COLUMNS")
print("-" * 45)

constant_columns = [
    col for col in df.columns
    if df[col].nunique(dropna=False) <= 1
]

print("Columns Removed:", constant_columns)

df = df.drop(columns=constant_columns)

# --------------------------------------------------
# CHECK DUPLICATES
# --------------------------------------------------

print("\n3. DUPLICATE CHECK")
print("-" * 45)

duplicate_count = df.duplicated().sum()

print("Duplicate Records:", duplicate_count)

if duplicate_count > 0:
    df.drop_duplicates(inplace=True)

# --------------------------------------------------
# CHECK CUSTOMER ID
# --------------------------------------------------

print("\n4. CUSTOMER ID VALIDATION")
print("-" * 45)

print("Unique Customer IDs:", df["CustomerID"].nunique())
print("Total Customer IDs:", len(df))

# --------------------------------------------------
# STANDARDIZE COLUMN NAMES
# --------------------------------------------------

print("\n5. STANDARDIZING COLUMN NAMES")
print("-" * 45)

df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
)

print(df.columns.tolist())

# --------------------------------------------------
# FINAL DATA QUALITY CHECK
# --------------------------------------------------

print("\n6. FINAL DATA QUALITY CHECK")
print("-" * 45)

print("Rows:", df.shape[0])
print("Columns:", df.shape[1])
print("Missing Values:", df.isnull().sum().sum())
print("Duplicate Rows:", df.duplicated().sum())

# --------------------------------------------------
# SAVE CLEANED DATA
# --------------------------------------------------

df.to_csv(output_file, index=False)

print("\n7. CLEANED DATA SAVED")
print("-" * 45)

print("File:", output_file)
print("Final Dataset Shape:", df.shape)

print("\n" + "=" * 65)
print("DATA CLEANING COMPLETED SUCCESSFULLY")
print("=" * 65)
