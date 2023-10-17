-- Number by score
SELECT score, COUNT(score) AS number
FROM second_table
GROUP BY score
HAVING COUNT(score) > 1
ORDER BY number DESC;
