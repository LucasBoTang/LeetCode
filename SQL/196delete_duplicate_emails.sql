DELETE FROM Person
WHERE Id NOT IN (SELECT min_Id
                 FROM (SELECT MIN(Id) AS min_Id
                       FROM Person
                       Group BY Email) AS romove_Id);
