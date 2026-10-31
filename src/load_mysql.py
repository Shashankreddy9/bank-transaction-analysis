import pandas as pd
from sqlalchemy import create_engine
from urllib.parse import quote_plus

username = "root"
password = quote_plus("Bujji")

host = "localhost"
port = 3306
database = "bank_analysis"

engine = create_engine(
    f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}"
)

df = pd.read_csv("data/processed/clean_transactions.csv")

df.to_sql(
    "bank_transactions",
    engine,
    if_exists="append",
    index=False
)

print("Data loaded successfully into MySQL!")
print("Records uploaded:", len(df))

engine.dispose()