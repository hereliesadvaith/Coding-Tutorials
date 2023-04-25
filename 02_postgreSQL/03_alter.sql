-- alter type of column
CREATE TYPE sex_type AS ENUM ('M', 'F');

ALTER TABLE customer 
ALTER COLUMN sex TYPE sex_type USING sex::sex_type;

ALTER TABLE sales_item ADD day_of_week VARCHAR(8);

ALTER TABLE sales_item
ALTER COLUMN day_of_week
SET
    NOT NULL;

ALTER TABLE sales_item
RENAME COLUMN day_of_week TO weekday;

-- to delete column
ALTER TABLE sales_item DROP COLUMN weekday;

--Renam Table
ALTER TABLE transaction_type
RENAME TO transaction;

ALTER TABLE customer ALTER COLUMN zip TYPE INTEGER;

ALTER TABLE sales_order ALTER COLUMN purchase_order_number TYPE BIGINT;

ALTER TABLE sales_order RENAME COLUMN credit_card_exp_month TO credit_card_exp;

ALTER TABLE sales_order ALTER COLUMN credit_card_exp TYPE VARCHAR(7);

-- to restart id sequence
ALTER SEQUENCE tablename_id_seq RESTART WITH 1;