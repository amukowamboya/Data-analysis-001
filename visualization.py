import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

conn = sqlite3.connect("airline.db")
df = pd.read_sql_query('''
SELECT
    Class,
    "Customer Type",
    ROUND(100.0 * SUM(CASE WHEN satisfaction = 'satisfied' THEN 1 ELSE 0 END) / COUNT(*), 1) AS percent_satisfied
FROM passengers
GROUP BY Class, "Customer Type"
''', conn)
conn.close()

pivot = df.pivot(index="Class", columns="Customer Type", values="percent_satisfied")

pivot.plot(kind="bar", figsize=(8, 5))
plt.title("Satisfaction Rate by Class and Customer Type")
plt.ylabel("% Satisfied")
plt.xticks(rotation=0)
plt.legend(title="Customer Type")
plt.tight_layout()
plt.savefig("satisfaction_chart.png")
plt.show()