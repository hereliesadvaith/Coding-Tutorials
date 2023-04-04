-- receive to int and returns an int
CREATE OR REPLACE FUNCTION fn_add_ints(int, int)
RETURNS int AS
/*
'
SELECT $1 + $2;
'
or */ 
$body$
    SELECT $1 + $2;
$body$ 
LANGUAGE SQL

SELECT fn_add_ints(4, 6);

CREATE OR REPLACE FUNCTION fn_update_employee_state()
RETURNS void AS
$body$
    UPDATE sales_person
    SET state = 'PA'
    WHERE state is NULL
$body$
LANGUAGE SQL

CREATE OR REPLACE FUNCTION fn_product_with_max_price()
RETURNS numeric AS
$body$
    SELECT MAX(price)
    FROM item;
$body$
LANGUAGE SQL

CREATE OR REPLACE FUNCTION fn_number_customers()
RETURNS numeric AS
$body$
    SELECT COUNT(*)
    FROM customer;
    -- WHERE phone is NULL - to get customers without phone number
$body$
LANGUAGE SQL

CREATE OR REPLACE FUNCTION fn_get_customer_number_from_state(state_name char(2))
RETURNS numeric AS
$body$
    SELECT COUNT(*)
    FROM customer
    WHERE state = state_name;
$body$
LANGUAGE SQL

CREATE OR REPLACE 
FUNCTION fn_get_orders_number_from_customer(fname varchar, lname varchar)
RETURNS numeric AS
$body$
    SELECT COUNT(*)
    FROM sales_order
    NATURAL JOIN customer
    WHERE customer.first_name = fname AND customer.last_name = lname;
$body$
LANGUAGE SQL

-- get an entire row
CREATE OR REPLACE FUNCTION fn_get_last_order()
RETURNS sales_order AS
$body$
    SELECT *
    FROM sales_order
    ORDER BY time_order_taken DESC
    LIMIT 1;
$body$
LANGUAGE SQL

SELECT fn_get_last_order();
-- to get this as a table
SELECT (fn_get_last_order()).*; -- or get individual data by .customer_id

--get multiple row
CREATE OR REPLACE FUNCTION fn_get_employees_location(loc varchar)
RETURNS SETOF sales_person AS
$body$
    SELECT *
    FROM sales_person
    WHERE state = loc;
$body$
LANGUAGE SQL

SELECT first_name, last_name, phone
FROM fn_get_employees_location('jp');
-- or
SELECT (fn_get_employees_location('CA')).*;