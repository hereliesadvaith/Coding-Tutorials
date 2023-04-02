SELECT * FROM sales_item;
/*
Conditional Operators
= : Equal
< : Less than
> : Greater than
<=: Less than or equal
>=: Greater than or equal
<>: Not Equal
!=: Not Equal
*/
SELECT * FROM sales_item
WHERE discount > 0.11;

/*
Logical Operators
AND, OR, NOT
*/

SELECT time_order_taken FROM sales_order
WHERE time_order_taken >= '2018-12-01'
AND time_order_taken <= '2019-12-01';
-- or
-- WHERE time_order_taken BETWEEN '2018-01-01' AND '2023-01-01'

SELECT * FROM sales_item
WHERE discount > 0.11
ORDER BY discount; --DESC

SELECT * FROM sales_item
WHERE discount > 0.11
ORDER BY discount DESC
LIMIT 1;

SELECT CONCAT(first_name, ' ', last_name) AS name, phone, state FROM customer
WHERE state = 'TX';

SELECT product_id, SUM(price) AS total FROM item
WHERE product_id < 3
GROUP BY product_id;

SELECT DISTINCT state FROM customer
WHERE state != 'CA'
-- WHERE state NOT IN ('CA', "NJ")
ORDER BY state;

