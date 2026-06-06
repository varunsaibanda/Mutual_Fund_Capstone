import pandas as pd

# Load datasets
nav = pd.read_csv("data/raw/02_nav_history.csv")
investor = pd.read_csv("data/raw/08_investor_transactions.csv")
performance = pd.read_csv("data/raw/07_scheme_performance.csv")

# NAV Cleaning
nav = nav.drop_duplicates()

for col in nav.columns:
    if "date" in col.lower():
        nav[col] = pd.to_datetime(nav[col], errors="coerce")

# Investor Cleaning
investor = investor.drop_duplicates()

for col in investor.columns:
    if "date" in col.lower():
        investor[col] = pd.to_datetime(investor[col], errors="coerce")

# Performance Cleaning
performance = performance.drop_duplicates()

# Save cleaned files
nav.to_csv("data/processed/nav_history_clean.csv", index=False)
investor.to_csv("data/processed/investor_transactions_clean.csv", index=False)
performance.to_csv("data/processed/scheme_performance_clean.csv", index=False)

print("Cleaning completed successfully")