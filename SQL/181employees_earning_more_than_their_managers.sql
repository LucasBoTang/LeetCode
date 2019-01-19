SELECT employer.Name AS Employee
FROM  Employee employer
JOIN Employee manager
ON employer.ManagerId = manager.Id
WHERE employer.Salary > manager.Salary;
