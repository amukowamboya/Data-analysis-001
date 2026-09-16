-- SQLite
SELECT
    Class,
    "Customer Type",
    COUNT(*) AS total_passengers,
    SUM(CASE WHEN satisfaction = 'satisfied' THEN 1 ELSE 0 END) AS satisfied_count,
    ROUND(
        100.0 * SUM(CASE WHEN satisfaction = 'satisfied' THEN 1 ELSE 0 END) / COUNT(*),
        1
    ) AS percent_satisfied
FROM passengers
GROUP BY Class, "Customer Type"
ORDER BY percent_satisfied DESC;