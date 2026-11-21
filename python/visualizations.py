
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sqlalchemy import create_engine, URL
from pathlib import Path
from getpass import getpass


# ==================================================
# MARKETING CAMPAIGN & CUSTOMER CONVERSION ANALYTICS
# PYTHON DATA VISUALIZATION
# ==================================================

print("=" * 65)
print("MARKETING CAMPAIGN & CUSTOMER CONVERSION ANALYTICS")
print("PYTHON DATA VISUALIZATION")
print("=" * 65)


# --------------------------------------------------
# 1. PATHS AND DATABASE CONNECTION
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

REPORTS_DIR = BASE_DIR / "reports"
REPORTS_DIR.mkdir(exist_ok=True)

password = getpass("Enter PostgreSQL password: ")

connection_url = URL.create(
    drivername="postgresql+psycopg2",
    username="postgres",
    password=password,
    host="localhost",
    port=5432,
    database="marketing_campaign_db"
)

engine = create_engine(connection_url)


try:

    print("\nConnecting to PostgreSQL...")

    df = pd.read_sql_query(
        "SELECT * FROM marketing_campaigns",
        engine
    )

    print("Database connection successful!")
    print("Dataset loaded:", df.shape)


    # --------------------------------------------------
    # 2. VISUALIZATION SETTINGS
    # --------------------------------------------------

    sns.set_theme(style="whitegrid")

    plt.rcParams["figure.figsize"] = (10, 6)
    plt.rcParams["figure.dpi"] = 120
    plt.rcParams["font.size"] = 10


    def save_chart(filename):

        plt.tight_layout()

        plt.savefig(
            REPORTS_DIR / filename,
            bbox_inches="tight",
            dpi=300
        )

        plt.close()

        print(f"Saved: {filename}")


    def add_percentage_labels(ax):

        for bar in ax.patches:

            height = bar.get_height()

            if pd.notna(height):

                ax.annotate(
                    f"{height:.2f}%",
                    (
                        bar.get_x() + bar.get_width() / 2,
                        height
                    ),
                    ha="center",
                    va="bottom",
                    xytext=(0, 5),
                    textcoords="offset points",
                    fontsize=9
                )


    # --------------------------------------------------
    # 3. OVERALL CONVERSION DISTRIBUTION
    # --------------------------------------------------

    conversion_counts = (
        df["conversion"]
        .value_counts()
        .sort_index()
    )

    plt.figure(figsize=(9, 7))

    plt.pie(
        conversion_counts,
        labels=[
            f"Not Converted\n({conversion_counts.loc[0]:,})",
            f"Converted\n({conversion_counts.loc[1]:,})"
        ],
        autopct="%1.1f%%",
        startangle=90,
        textprops={"fontsize": 11},
        wedgeprops={"edgecolor": "white", "linewidth": 1}
    )

    plt.title(
        "Overall Customer Conversion Distribution",
        fontsize=14,
        pad=15
    )

    save_chart("01_conversion_distribution.png")


    # --------------------------------------------------
    # 4. CONVERSION RATE BY CAMPAIGN CHANNEL
    # --------------------------------------------------

    channel_data = (
        df.groupby("campaignchannel")["conversion"]
        .mean()
        .mul(100)
        .sort_values(ascending=False)
        .reset_index()
    )

    plt.figure(figsize=(10, 6))

    ax = sns.barplot(
        data=channel_data,
        x="campaignchannel",
        y="conversion"
    )

    add_percentage_labels(ax)

    plt.title(
        "Conversion Rate by Campaign Channel",
        fontsize=14,
        pad=15
    )

    plt.xlabel("Campaign Channel")
    plt.ylabel("Conversion Rate (%)")

    plt.ylim(0, 100)
    plt.xticks(rotation=20)

    save_chart("02_channel_conversion.png")


    # --------------------------------------------------
    # 5. CONVERSION RATE BY CAMPAIGN TYPE
    # --------------------------------------------------

    type_data = (
        df.groupby("campaigntype")["conversion"]
        .mean()
        .mul(100)
        .sort_values(ascending=False)
        .reset_index()
    )

    plt.figure(figsize=(10, 6))

    ax = sns.barplot(
        data=type_data,
        x="campaigntype",
        y="conversion"
    )

    add_percentage_labels(ax)

    plt.title(
        "Conversion Rate by Campaign Type",
        fontsize=14,
        pad=15
    )

    plt.xlabel("Campaign Type")
    plt.ylabel("Conversion Rate (%)")

    plt.ylim(0, 100)
    plt.xticks(rotation=15)

    save_chart("03_campaign_type_conversion.png")


    # --------------------------------------------------
    # 6. CONVERSION RATE BY AGE GROUP
    # --------------------------------------------------

    df["age_group"] = pd.cut(
        df["age"],
        bins=[17, 24, 34, 44, 54, 64, 100],
        labels=[
            "18-24",
            "25-34",
            "35-44",
            "45-54",
            "55-64",
            "65+"
        ]
    )

    age_data = (
        df.groupby("age_group", observed=False)["conversion"]
        .mean()
        .mul(100)
        .reset_index()
    )

    plt.figure(figsize=(10, 6))

    ax = sns.barplot(
        data=age_data,
        x="age_group",
        y="conversion"
    )

    add_percentage_labels(ax)

    plt.title(
        "Conversion Rate by Age Group",
        fontsize=14,
        pad=15
    )

    plt.xlabel("Age Group")
    plt.ylabel("Conversion Rate (%)")

    plt.ylim(0, 100)

    save_chart("04_age_group_conversion.png")


    # --------------------------------------------------
    # 7. CUSTOMER ENGAGEMENT BY CONVERSION STATUS
    # --------------------------------------------------

    engagement_data = (
        df.groupby("conversion")[
            [
                "websitevisits",
                "pagespervisit",
                "timeonsite",
                "emailopens",
                "emailclicks"
            ]
        ]
        .mean()
        .T
    )

    engagement_data.columns = [
        "Not Converted",
        "Converted"
    ]

    ax = engagement_data.plot(
        kind="bar",
        figsize=(12, 7),
        width=0.75
    )

    for container in ax.containers:

        ax.bar_label(
            container,
            fmt="%.2f",
            padding=3,
            fontsize=8
        )

    plt.title(
        "Customer Engagement by Conversion Status",
        fontsize=14,
        pad=15
    )

    plt.xlabel("Engagement Metrics")
    plt.ylabel("Average Value")

    plt.xticks(rotation=15)
    plt.legend(title="Conversion Status")

    save_chart("05_customer_engagement.png")


    # --------------------------------------------------
    # 8. ADVERTISING SPEND SEGMENTATION VS CONVERSION
    # --------------------------------------------------

    df["spend_quartile"] = pd.qcut(
        df["adspend"],
        q=4,
        labels=[
            "Low",
            "Medium",
            "High",
            "Very High"
        ]
    )

    spend_data = (
        df.groupby("spend_quartile", observed=False)["conversion"]
        .mean()
        .mul(100)
        .reset_index()
    )

    plt.figure(figsize=(10, 6))

    ax = sns.barplot(
        data=spend_data,
        x="spend_quartile",
        y="conversion"
    )

    add_percentage_labels(ax)

    plt.title(
        "Conversion Rate by Advertising Spend Group",
        fontsize=14,
        pad=15
    )

    plt.xlabel("Advertising Spend Group")
    plt.ylabel("Conversion Rate (%)")

    plt.ylim(0, 100)

    save_chart("06_ad_spend_conversion.png")


    # --------------------------------------------------
    # 9. FINAL STATUS
    # --------------------------------------------------

    print("\n" + "=" * 65)
    print("ALL VISUALIZATIONS CREATED SUCCESSFULLY!")
    print("Total Charts Generated: 6")
    print("Charts saved inside:", REPORTS_DIR)
    print("=" * 65)


finally:

    engine.dispose()

    print("\nDatabase connection closed.")
