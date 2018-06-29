SELECT name, bonus
FROM Employee e
left JOIN Bonus b
ON e.empId = b.empId
WHERE bonus < 1000 or bonus IS NULL
