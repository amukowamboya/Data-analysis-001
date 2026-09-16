-- SQLite
SELECT Class, [Flight Distance], rn
FROM (
    SELECT
        Class,
        [Flight Distance],
        ROW_NUMBER() OVER (PARTITION BY Class ORDER BY [Flight Distance] DESC) AS rn
    FROM passengers
) AS subquery
WHERE rn <= 3
ORDER BY Class, rn;
