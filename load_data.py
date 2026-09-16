import pandas as pd
import sqlite3

df = pd.read_csv("/Users/ASTROPHSYICS/Desktop/Data-analysis-001/test.csv")  # adjust to the real location
df = df.drop(columns=["Unnamed: 0"])

conn = sqlite3.connect("/Users/ASTROPHSYICS/Desktop/Data-analysis-001/airline.db")
df.to_sql("passengers", conn, if_exists="replace", index=False)
conn.close()

print("Loaded", len(df), "rows into airline.db")