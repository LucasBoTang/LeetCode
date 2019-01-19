SELECT DISTINCT a.seat_id
FROM cinema a
JOIN cinema b
ON abs(a.seat_id -b.seat_id) = 1
WHERE a.free = 1 AND b.free = 1
ORDER BY a.seat_id;
