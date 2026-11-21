
import pandas as pd
from pathlib import Path

print("=" * 65)
print("MARKETING CAMPAIGN & CUSTOMER CONVERSION ANALYTICS")
print("DETAILED DATA PROFILING")
print("=" * 65)

# Load dataset
project_dir = Path(__file__).resolve().parent.parent
file_path = project_dir / "dataset" / "digital_marketing_campaign_dataset.csv"

df = pd.read_csv(file_path)

# --------------------------------------------------
# 1. CATEGORICAL COLUMN ANALYSIS
# --------------------------------------------------

print("\n1. CATEGORICAL COLUMN ANALYSIS")
print("-" * 50)

categorical_columns = df.select_dtypes(include=["object", "str"]).columns

for col in categorical_columns:
    print(f"\n{col}")
    print("Unique Values:", df[col].nunique())
    print(df[col].value_counts().to_string())

# --------------------------------------------------
# 2. CONVERSION DISTRIBUTION
# --------------------------------------------------

print("\n2. CONVERSION DISTRIBUTION")
print("-" * 50)

conversion_counts = df["Conversion"].value_counts().sort_index()
conversion_percentage = df["Conversion"].value_counts(
    normalize=True
).sort_index() * 100

conversion_summary = pd.DataFrame({
    "Customers": conversion_counts,
    "Percentage": conversion_percentage.round(2)
})

print(conversion_summary)

# --------------------------------------------------
# 3. CUSTOMER ID UNIQUENESS
# --------------------------------------------------

print("\n3. CUSTOMER ID CHECK")
print("-" * 50)

print("Total Customer IDs:", df["CustomerID"].count())
print("Unique Customer IDs:", df["CustomerID"].nunique())
print("Duplicate Customer IDs:", df["CustomerID"].duplicated().sum())

# --------------------------------------------------
# 4. CONSTANT COLUMN CHECK
# --------------------------------------------------

print("\n4. CONSTANT COLUMN CHECK")
print("-" * 50)

constant_columns = [
    col for col in df.columns
    if df[col].nunique() == 1
]

print("Constant Columns:", constant_columns)

# --------------------------------------------------
# 5. NUMERICAL RANGE VALIDATION
# --------------------------------------------------

print("\n5. NUMERICAL RANGE VALIDATION")
print("-" * 50)

checks = {
    "Age": (df["Age"].between(18, 100)),
    "Income": (df["Income"] >= 0),
    "AdSpend": (df["AdSpend"] >= 0),
    "ClickThroughRate": (df["ClickThroughRate"].between(0, 1)),
    "ConversionRate": (df["ConversionRate"].between(0, 1)),
    "PagesPerVisit": (df["PagesPerVisit"] >= 0),
    "TimeOnSite": (df["TimeOnSite"] >= 0),
    "Conversion": (df["Conversion"].isin([0, 1]))
}

for column, condition in checks.items():
    invalid_count = (~condition).sum()
    print(f"{column}: {invalid_count} invalid records")

# --------------------------------------------------
# 6. FINAL SUMMARY
# --------------------------------------------------

print("\n6. DATA PROFILING SUMMARY")
print("-" * 50)

print("Total Rows:", df.shape[0])
print("Total Columns:", df.shape[1])
print("Missing Values:", df.isnull().sum().sum())
print("Duplicate Rows:", df.duplicated().sum())

print("\n" + "=" * 65)
print("DETAILED DATA PROFILING COMPLETED")
print("=" * 65)
