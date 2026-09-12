# Write your MySQL query statement below
select W1.id from Weather W1 JOIN Weather W2 ON w2.recordDate = DATE_SUB(w1.recordDate, INTERVAL 1 DAY)
WHERE w1.temperature > w2.temperature;