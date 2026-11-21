
import pandas as pd
from pathlib import Path

print("=" * 65)
print("MARKETING CAMPAIGN & CUSTOMER CONVERSION ANALYTICS")
print("INITIAL CONVERSION ANALYSIS")
print("=" * 65)

# Load dataset
project_dir = Path(__file__).resolve().parent.parent
file_path = project_dir / "dataset" / "digital_marketing_campaign_dataset.csv"

df = pd.read_csv(file_path)

# --------------------------------------------------
# 1. CONVERSION BY CAMPAIGN CHANNEL
# --------------------------------------------------

print("\n1. CONVERSION BY CAMPAIGN CHANNEL")
print("-" * 50)

channel_analysis = df.groupby("CampaignChannel").agg(
    Total_Customers=("CustomerID", "count"),
    Converted_Customers=("Conversion", "sum"),
    Conversion_Rate=("Conversion", "mean")
)

channel_analysis["Conversion_Rate"] *= 100

print(channel_analysis.round(2).to_string())

# --------------------------------------------------
# 2. CONVERSION BY CAMPAIGN TYPE
# --------------------------------------------------

print("\n2. CONVERSION BY CAMPAIGN TYPE")
print("-" * 50)

type_analysis = df.groupby("CampaignType").agg(
    Total_Customers=("CustomerID", "count"),
    Converted_Customers=("Conversion", "sum"),
    Conversion_Rate=("Conversion", "mean")
)

type_analysis["Conversion_Rate"] *= 100

print(type_analysis.round(2).to_string())

# --------------------------------------------------
# 3. CONVERSION BY GENDER
# --------------------------------------------------

print("\n3. CONVERSION BY GENDER")
print("-" * 50)

gender_analysis = df.groupby("Gender").agg(
    Total_Customers=("CustomerID", "count"),
    Converted_Customers=("Conversion", "sum"),
    Conversion_Rate=("Conversion", "mean")
)

gender_analysis["Conversion_Rate"] *= 100

print(gender_analysis.round(2).to_string())

# --------------------------------------------------
# 4. CONVERTED VS NON-CONVERTED CUSTOMERS
# --------------------------------------------------

print("\n4. CUSTOMER BEHAVIOUR COMPARISON")
print("-" * 50)

comparison_columns = [
    "Age",
    "Income",
    "AdSpend",
    "WebsiteVisits",
    "PagesPerVisit",
    "TimeOnSite",
    "EmailOpens",
    "EmailClicks",
    "PreviousPurchases"
]

comparison = df.groupby("Conversion")[comparison_columns].mean().T

comparison.columns = ["Not_Converted", "Converted"]

print(comparison.round(2).to_string())

# --------------------------------------------------
# 5. CORRELATION WITH CONVERSION
# --------------------------------------------------

print("\n5. NUMERICAL CORRELATION WITH CONVERSION")
print("-" * 50)

correlation = (
    df.select_dtypes(include="number")
    .corr()["Conversion"]
    .drop(["Conversion", "CustomerID"])
    .sort_values(ascending=False)
)

print(correlation.round(3).to_string())

print("\n" + "=" * 65)
print("INITIAL CONVERSION ANALYSIS COMPLETED")
print("=" * 65)
