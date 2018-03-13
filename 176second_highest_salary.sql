SELECT DISTINCT Salary AS SecondHighestSalary
FROM Employee UNION SELECT NULL
ORDER BY SecondHighestSalary DESC
LIMIT 1, 1
