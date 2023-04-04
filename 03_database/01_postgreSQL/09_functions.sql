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