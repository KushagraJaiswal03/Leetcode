WITH daily AS (
  SELECT visited_on, SUM(amount) AS amount
  FROM Customer
  GROUP BY visited_on
)
SELECT
  d1.visited_on,
  (SELECT SUM(d2.amount)
   FROM daily d2
   WHERE d2.visited_on BETWEEN DATE_SUB(d1.visited_on, INTERVAL 6 DAY) AND d1.visited_on
  ) AS amount,
  ROUND(
    (SELECT SUM(d2.amount)
     FROM daily d2
     WHERE d2.visited_on BETWEEN DATE_SUB(d1.visited_on, INTERVAL 6 DAY) AND d1.visited_on
    ) / 7, 2
  ) AS average_amount
FROM daily d1
WHERE d1.visited_on >= (SELECT DATE_ADD(MIN(visited_on), INTERVAL 6 DAY) FROM Customer)
ORDER BY d1.visited_on;