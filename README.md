# Data-analysis-001: Airline Passenger Satisfaction Analysis

SQL and Python analysis of airline passenger satisfaction data, built as hands-on practice ahead of a Data Analyst application.

## Dataset
Airline Passenger Satisfaction dataset (Kaggle), ~26,000 rows covering passenger demographics, service ratings, flight details, delays, and overall satisfaction.

## Tools
- SQLite for querying (loaded from CSV via pandas)
- Python (pandas, matplotlib) for data loading and visualization
- VS Code with the SQLite extension

## Files
- `load_data.py` — loads the raw CSV into a local SQLite database (`airline.db`)
- `visualization.py` — queries the database and generates a satisfaction chart
- `satisfaction_chart.png` — output visualization
- `test.csv` — source dataset

## Analysis

**1. Satisfaction by Class and Customer Type**
Grouped passengers by cabin class and loyalty status, calculating the percent satisfied in each group.

Key finding: Business class loyal customers report 74.7% satisfaction, versus just 8.5% for Eco Plus disloyal customers, a 66-point gap. Class and loyalty status matter far more to satisfaction than any single service factor.

**2. Delay Impact**
Compared satisfaction rates for passengers delayed over 30 minutes versus 30 minutes or less.

Key finding: the gap is only 8.6 points (45.1% vs 36.5%), smaller than expected. Delay alone isn't the primary driver of dissatisfaction, the class/loyalty split above matters more.

**3. Longest Flights by Class**
Used a window function (`ROW_NUMBER() OVER PARTITION BY`) to rank and extract the top 3 longest flights within each cabin class.

## Visualization
`satisfaction_chart.png` shows a grouped bar chart of satisfaction rate by class and customer type, visualizing the finding from Analysis 1.

## Next Steps
Excel reconciliation practice and a Power BI dashboard build are planned as follow-on exercises in this series.
