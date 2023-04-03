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

