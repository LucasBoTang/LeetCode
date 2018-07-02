SELECT customer_number
FROM orders
GROUP BY customer_number
ORDER BY COUNT(DISTINCT order_number) DESC
LIMIT 1;
