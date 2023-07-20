import pandas as pd
from sqlalchemy import create_engine, text

# Create an engine that's connected to your SQLite database
engine = create_engine("sqlite:///ffxiv_pvp.db")
query = "SELECT * FROM players"

with engine.begin() as conn:
    df = pd.read_sql(sql=text(query), con=conn)

print(df.head())

query = "SELECT * FROM verifications"

with engine.begin() as conn:
    df = pd.read_sql(sql=text(query), con=conn)

print(df.head())
