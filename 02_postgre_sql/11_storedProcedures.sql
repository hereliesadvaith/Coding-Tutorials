-- stored procedures with parameter called dynamic and without parameter called static
CREATE TABLE past_due(
    id SERIAL PRIMARY KEY,
    cust_id INTEGER NOT NULL,
    balance NUMERIC(6, 2) NOT NULL
);

INSERT INTO past_due(cust_id, balance)
VALUES
    (1, 120.99),
    (2, 200.30),
    (3, 600.30);

CREATE OR REPLACE PROCEDURE pr_debt_paid(
    past_due_id int,
    payment numeric
    -- workaround for returning values
    INOUT varchar
) AS
$body$
DECLARE
BEGIN
    UPDATE past_due
    SET balance = balance - payment
    WHERE id = past_due_id;
    COMMIT; -- you have to call for commit 
END
$body$
LANGUAGE plpgsql;

CALL pr_debt_paid(1, 10); -- pass in cust id and 10 dollars