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
ALTER TABLE sales_item DROP COLUMN day_of_week;

--Renam Table
ALTER TABLE transaction_type
RENAME TO transaction;