# Data-analysis-001: Data Analyst Practice Portfolio

Hands-on SQL, Excel, and Power BI practice built ahead of a Data Analyst application, using public datasets to demonstrate real analytical workflows: querying, reconciliation, visualization, and outlier detection.

## Projects

### [Dataset 1: Airline Passenger Satisfaction](./dataset-1-sql)
SQL analysis (SQLite) of ~26,000 airline passenger records.
- Grouped satisfaction rates by class and customer loyalty, found a 66-point satisfaction gap between Business/Loyal (74.7%) and Eco Plus/disloyal (8.5%) customers
- Tested whether flight delays drive dissatisfaction, found only an 8.6-point gap, delay alone isn't the primary driver
- Used a window function to rank the top 3 longest flights per cabin class
- Visualized findings with a grouped bar chart (Python/matplotlib)

### Dataset 2: Superstore Sales Reconciliation (Excel)
Excel-based reconciliation and outlier detection on ~10,000 retail orders.
- Built a pivot table summarizing Sales and Profit by Region and Category, surfaced a loss-making Region/Category combination (Central/Furniture) despite strong sales volume
- Built an XLOOKUP-based price reconciliation system comparing actual vs. expected unit price, flagging mismatches over 10%
- Used conditional formatting to flag high-risk orders (discount over 40% with negative profit), found 933 orders (9.3% of all orders) matching this pattern

## Tools Used
- SQLite, Python (pandas, matplotlib)
- Excel/WPS Office (Pivot Tables, XLOOKUP, Conditional Formatting)
- VS Code, Git/GitHub

## Next Steps
Power BI dashboard build (Dataset 3) planned as the final project in this series.
