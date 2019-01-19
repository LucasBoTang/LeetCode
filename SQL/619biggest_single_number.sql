SELECT MAX(num) AS num
FROM (SELECT num
      FROM number
      GROUP BY num
      HAVING count(num) = 1) AS one;
