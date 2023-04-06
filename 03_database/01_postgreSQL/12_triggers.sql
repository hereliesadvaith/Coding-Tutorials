-- Insert, Update, Truncate, Delete
-- Triggers can execute before or after an event executes.
-- Multiple triggers on a table executes in alphabetical order

CREATE TABLE distributor(
    id SERIAL PRIMARY KEY,
    name VARCHAR(100)
);

INSERT INTO distributor(name)
VALUES
    ('Parawholesales'),
    ('J & B sales'),
    ('Steel city clothing');

CREATE TABLE distributor_audit(
    id SERIAL PRIMARY KEY,
    dist_id INT NOT NULL,
    name VARCHAR(100) NOT NULL,
    edit_date TIMESTAMP NOT NULL
);

-- trigger function
CREATE OR REPLACE FUNCTION fn_log_dist_name_change()
RETURNS TRIGGER
LANGUAGE plpgsql
AS
$body$
BEGIN
    IF NEW.name <> OLD.name THEN
        INSERT INTO distributor_audit(
            dist_id, name, edit_date
        ) VALUES
        (OLD.id, OLD.name, NOW());
    END IF;
    RAISE NOTICE 'Trigger Name: %', TG_NAME;
    RAISE NOTICE 'Table Name: %', TG_TABLE_NAME;
    RAISE NOTICE 'Operation : %', TG_OP;
    RAISE NOTICE 'Executed time: %', TG_WHEN;
    RAISE NOTICE 'Row or Statement: %', TG_LEVEL;
    RAISE NOTICE 'Schema: %', TG_TABLE_SCHEMA;
    RETURN NEW;
END
$body$

--trigger
CREATE TRIGGER tr_dist_name_changed
BEFORE UPDATE
ON distributor
FOR EACH ROW
EXECUTE PROCEDURE fn_log_dist_name_change();

UPDATE distributor
SET name = 'Western Clothing'
WHERE id = 2;

-- conditional trigger
CREATE OR REPLACE FUNCTION fn_block_weekend_changes()
RETURNS TRIGGER
LANGUAGE plpgsql
AS
$body$
BEGIN
    RAISE NOTICE 'No database changes allowed on the weekend';
    RETURN NULl;
END
$body$

-- if you try to add something on weekend
CREATE TRIGGER tr_block_weekend_changes
BEFORE UPDATE OR INSERT OR DELETE OR TRUNCATE
ON distributor
FOR EACH STATEMENT
WHEN(
    EXTRACT('DOW' FROM CURRENT_TIMESTAMP) = 7
)
EXECUTE PROCEDURE fn_block_weekend_changes();

-- to delete trigger
DROP EVENT TRIGGER tr_block_weekend_changes;
