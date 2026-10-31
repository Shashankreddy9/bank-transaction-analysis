
import pandas as pd
import os

# Read raw transaction data
input_file = "data/raw/bank_transactions.csv"

df = pd.read_csv(input_file)

print("Original records:", len(df))

# 1. Remove duplicate transactions
df = df.drop_duplicates(
    subset=["transaction_id"]
)

# 2. Handle missing values
df = df.dropna(
    subset=[
        "transaction_id",
        "customer_id",
        "transaction_date",
        "transaction_type",
        "amount"
    ]
)

# 3. Convert date column
df["transaction_date"] = pd.to_datetime(
    df["transaction_date"],
    errors="coerce"
)

# 4. Convert amount to numeric
df["amount"] = pd.to_numeric(
    df["amount"],
    errors="coerce"
)

# 5. Remove invalid records
df = df.dropna(
    subset=["transaction_date", "amount"]
)

df = df[df["amount"] > 0]

# 6. Standardize text columns
for col in [
    "transaction_type",
    "category",
    "payment_mode",
    "location"
]:
    df[col] = df[col].str.strip().str.title()

# 7. Save cleaned dataset
os.makedirs("data/processed", exist_ok=True)

df.to_csv(
    "data/processed/clean_transactions.csv",
    index=False
)

print("\nData cleaning completed!")
print("Clean records:", len(df))
print("Removed records:", 10000 - len(df))

print("\nMissing values:")
print(df.isnull().sum())

print("\nClean transaction summary:")
print(df.groupby("transaction_type")["amount"].agg(
    ["count", "sum", "mean"]
))
