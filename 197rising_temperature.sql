SELECT Id AS Id
FROM Weather w1
WHERE w1.Temperature > (SELECT w2.Temperature
                        FROM Weather w2
                        WHERE w2.Date = DATE_SUB(w1.Date, INTERVAL 1 DAY))
