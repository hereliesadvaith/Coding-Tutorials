-- All items ever sorted by id while listing price
SELECT item_id, price
FROM item INNER JOIN sales_item
ON item.id = sales_item.item_id AND price > 120.00
ORDER BY item_id;

-- or

SELECT item_id, price
FROM sales_item, item
WHERE item.id = sales_item.item_id
AND price > 120.00
ORDER BY item_id;

-- Get orders, quantity and the total sale
SELECT sales_order.id, sales_item.quantity, item.price,
(sales_item.quantity * item.price) AS total
FROM sales_order JOIN sales_item
ON sales_item.sales_order_id = sales_order.id
JOIN item -- join it with either one of the table
ON sales_item.item_id = item.id
ORDER BY sales_order.id;

-- Get product information from two different tables
SELECT name, supplier, price
FROM product LEFT JOIN item -- good practice to avoid RIGHT JOIN
ON item.product_id = product.id
ORDER BY name;

-- Grab information from the item , sales_item tables
SELECT sales_order_id, quantity, product_id
FROM item CROSS JOIN sales_item
ORDER BY sales_order_id;

-- Unions
/* it basically going to combine the results of two or more select statements
in one result, and each result must returns the same number of columns and
data in each column and should have same datatype */
SELECT first_name, last_name, street, city, zip, birth_date
FROM customer
WHERE EXTRACT(MONTH FROM birth_date) < 12
UNION -- can join even if they don't have direct relationship
SELECT first_name, last_name, street, city, zip, birth_date
FROM sales_person
WHERE EXTRACT(MONTH FROM birth_date) < 12
ORDER BY birth_date;
