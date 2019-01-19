SELECT MIN(ABS(a.x - b.x)) AS shortest
FROM point a
JOIN point b
WHERE a.x != b.x;
