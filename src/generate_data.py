
import pandas as pd
import numpy as np
import random
import os
from datetime import datetime, timedelta

# Reproducibility
np.random.seed(42)
random.seed(42)

# Create output folder
os.makedirs("data/raw", exist_ok=True)

categories = [
    "Shopping", "Food", "Travel", "Rent",
    "Bills", "Healthcare", "Entertainment",
    "Education", "Salary", "Transfer"
]

payment_modes = ["UPI", "Debit Card", "NEFT", "IMPS", "ATM"]

transactions = []

for i in range(10000):

    transaction_type = random.choice(["Credit", "Debit"])

    if transaction_type == "Credit":
        amount = round(random.uniform(1000, 80000), 2)
        category = random.choice(["Salary", "Transfer"])
    else:
        amount = round(random.uniform(50, 20000), 2)
        category = random.choice(categories[:8])

    transaction_date = datetime(2026, 1, 1) + timedelta(
        days=random.randint(0, 299)
    )

    transactions.append({
        "transaction_id": f"TXN{i+1:05d}",
        "customer_id": f"CUST{random.randint(1, 500):04d}",
        "transaction_date": transaction_date,
        "transaction_type": transaction_type,
        "amount": amount,
        "category": category,
        "payment_mode": random.choice(payment_modes),
        "location": random.choice([
            "Hyderabad", "Bangalore", "Chennai",
            "Mumbai", "Delhi"
        ])
    })

df = pd.DataFrame(transactions)

# Save dataset
df.to_csv(
    "data/raw/bank_transactions.csv",
    index=False
)

print("\nDataset generated successfully!")
print("Total transactions:", len(df))
print("\nFirst 5 transactions:")
print(df.head())

print("\nTransaction summary:")
print(df["transaction_type"].value_counts())

print("\nTotal transaction amount:")
print(round(df["amount"].sum(), 2))
