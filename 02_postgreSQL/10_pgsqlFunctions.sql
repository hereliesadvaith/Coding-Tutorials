-- get product price by name
CREATE OR REPLACE FUNCTION fn_get_price(prod_name varchar)
RETURNS numeric AS
$body$
BEGIN
    -- use return instead of select
    RETURN item.price
    FROM item
    NATURAL JOIN product
    WHERE product.name = prod_name;
END
$body$
LANGUAGE plpgsql;

-- variables inside function 
CREATE OR REPLACE FUNCTION fn_get_sum(val1 int, val2 int)
RETURNS int AS
$body$
DECLARE
    ans int;
BEGIN
    -- assign value to int
    ans := val1 + val2;
    RETURN ans;
END
$body$
LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION fn_get_random_num(min int, max int)
RETURNS int AS
$body$
DECLARE
    ans int;
BEGIN
    SELECT random() * (max - min) + min INTO ans;
    RETURN ans;
END
$body$
LANGUAGE plpgsql

CREATE OR REPLACE FUNCTION fn_get_random_salesperson()
RETURNS varchar AS
$body$
DECLARE
    rand int;
    emp record;
BEGIN
    SELECT random() * 11 INTO rand; -- coz there's 11 employees
    SELECT * FROM sales_person
    INTO emp
    WHERE id = rand;
    RETURN CONCAT(emp.first_name, ' ', emp.last_name);
END
$body$
LANGUAGE plpgsql

CREATE OR REPLACE FUNCTION fn_get_sum2(IN v1 int, IN v2 int, OUT ans int) AS
$body$
BEGIN
    -- don't have to declare ans
    ans := v1 + v2;
END
$body$
LANGUAGE plpgsql

CREATE OR REPLACE FUNCTION fn_get_birthday
(IN mon int, OUT bd_month int, OUT bd_day int, OUT f_name varchar) AS
$body$
BEGIN
    SELECT EXTRACT(MONTH FROM birth_date), EXTRACT(DAY FROM birth_date), first_name
    INTO bd_month, bd_day, f_name
    FROM customer
    WHERE EXTRACT(MONTH FROM birth_date) = mon;
END;
$body$
LANGUAGE plpgsql

CREATE OR REPLACE FUNCTION fn_get_sales_people()
RETURNS SETOF sales_person AS
$body$
BEGIN
    RETURN QUERY
    SELECT *
    FROM sales_person;
END;
$body$
LANGUAGE plpgsql

-- return specific data from a query using multiple tables
CREATE OR REPLACE FUNCTION fn_get_product_price()
RETURNS TABLE (
    name varchar,
    supplier varchar,
    price numeric
) AS
$body$
BEGIN
    RETURN QUERY
    SELECT product.name, product.supplier, item.price
    FROM item
    NATURAL JOIN product
    ORDER BY item.price DESC;
END
$body$
LANGUAGE plpgsql

CREATE OR REPLACE FUNCTION fn_check_month_orders(the_month int)
RETURNS varchar AS
$body$
DECLARE
    total_orders int;
BEGIN
    SELECT COUNT(purchase_order_number)
    INTO total_orders
    FROM sales_order
    WHERE EXTRACT(MONTH FROM time_order_taken) = the_month;

    IF total_orders > 1 THEN
        RETURN CONCAT(total_orders, 'Orders : Doing good');
    ELSEIF total_orders < 1 THEN
        RETURN CONCAT(total_orders, 'Orders : Doing Bad');
    ELSE
        RETURN CONCAT(total_orders, 'Orders : On target');
    END IF;
END
$body$
LANGUAGE plpgsql

-- similar function using a case statement
CREATE OR REPLACE FUNCTION fn_check_month_orders(the_month int)
RETURNS varchar AS
$body$
DECLARE
    total_orders int;
BEGIN
    SELECT COUNT(purchase_order_number)
    INTO total_orders
    FROM sales_order
    WHERE EXTRACT(MONTH FROM time_order_taken) = the_month;

    CASE
        WHEN total_orders < 1 THEN
            RETURN CONCAT(total_orders, 'Orders : Terrible');
        WHEN total_orders > 1 THEN
            RETURN CONCAT(total_orders, 'Orders : Good');
        ELSE 
            RETURN CONCAT(total_orders, 'Orders : On Target');
    END CASE;
END
$body$
LANGUAGE plpgsql

/*
LOOP
    statements
    EXIT WHEN condition ia TRUE;
END LOOP
*/

CREATE OR REPLACE FUNCTION fn_loop_test(max int)
RETURNS int AS
$body$
DECLARE
    j int DEFAULT 1;
    tot_sum int DEFAULT 0;
BEGIN
    LOOP
        tot_sum := tot_sum + j;
        j := j + 1;
        EXIT WHEN j > max;
    END LOOP;
    RETURN tot_sum;
END
$body$
LANGUAGE plpgsql

CREATE OR REPLACE FUNCTION fn_for_test(max int)
RETURNS int AS
$body$
DECLARE
    tot_sum int DEFAULT 0;
BEGIN
    FOR i IN 1 .. max BY 2 -- range 1 to max step by 2
--  FOR i IN REVERSE max .. 1 BY 2
    LOOP
        tot_sum := tot_sum + i;
    END LOOP;
    RETURN tot_sum;
END
$body$
LANGUAGE plpgsql

DO
$body$
DECLARE
    rec record;
BEGIN
    FOR rec in 
        SELECT first_name, last_name
        FROM sales_person
        LIMIT 5
    LOOP
        RAISE NOTICE '% %', rec.first_name, rec.last_name;
    END LOOP;
END
$body$
LANGUAGE plpgsql

DO
$body$
DECLARE
    arr1 int[] := array[1,2,3];
    i int;
BEGIN
    FOREACH i IN ARRAY arr1
    LOOP
        RAISE NOTICE '%', i;
    END LOOP; 
END
$body$
LANGUAGE plpgsql

DO
$body$
DECLARE
    j int DEFAULT 1;
    tot_sum int DEFAULT 0;
BEGIN
    WHILE j <= 10
    LOOP
        tot_sum := tot_sum + j;
        j := j + 1;
        RAISE NOTICE '%', tot_sum;
    END LOOP; 
END
$body$
LANGUAGE plpgsql

-- odd numbers
DO
$body$
DECLARE
    i int DEFAULT 1;
BEGIN
    LOOP
        i := i + 1
        EXIT WHEN i > 10;
        CONTINUE WHEN MOD(i, 2) = 0; -- modulus of i / 2
        RAISE NOTICE 'Num : %', i;
    END LOOP; 
END
$body$
LANGUAGE plpgsql

CREATE OR REPLACE FUNCTION fn_get_supplier_value(the_supplier varchar)
RETURNS varchar AS
$body$
DECLARE
    supplier_name varchar;
    price_sum numeric;
BEGIN
    SELECT product.supplier, SUM(item.price)
    INTO supplier_name, price_sum
    FROM product, item
    WHERE product.supplier = the_supplier
    GROUP BY product.supplier;
    RETURN CONCAT(supplier_name, 'Inventory Value : $', price_sum);
END
$body$
LANGUAGE plpgsql