# Write your MySQL query statement below
SELECT w1.id
FROM Weather w1
JOIN Weather w0
  ON w1.recordDate = DATE_ADD(w0.recordDate, INTERVAL 1 DAY)
WHERE w1.temperature > w0.temperature;
