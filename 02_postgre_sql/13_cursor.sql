-- get list of customers
DO
$body$
DECLARE
    msg TEXT DEFAULT '';
    rec_customer RECORD;
    cur_custormers CURSOR
    FOR
        SELECT * FROM customers;
BEGIN
    OPEN cur_custormers;
    LOOP
        FETCH cur_custormers INTO rec_customer;
        EXIT WHEN NOT FOUND;
        msg := msg || rec_customer.first_name || ' ' || rec_customer.last_name || ', ';
    END LOOP;
    RAISE NOTICE 'Customers : %', msg;
END
$body$

-- cursors with a fucntion
CREATE OR REPLACE FUNCTION fn_get_cust_by_state(c_state varchar)
RETURNS TEXT
LANGUAGE plpgsql
AS
$body$
DECLARE
    cust_names TEXT DEFAULT '';
    rec_customer RECORD;
    cur_cust_by_state CURSOR (c_state varchar)
    FOR
        SELECT first_name, last_name, state
        FROM customer 
        WHERE state = c_state;
BEGIN
    OPEN cur_cust_by_state(c_state);
    LOOP
        FETCH cur_cust_by_state INTO rec_customer;
        EXIT WHEN NOT FOUND;
        cust_names := cust_names || rec_customer.first_name || ' ' || rec_customer.last_name || ', ';
    END LOOP;
    CLOSE cur_cust_by_state;
    RETURN cust_names;
END
$body$