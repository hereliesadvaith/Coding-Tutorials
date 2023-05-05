INSERT INTO
    customer (
        first_name, last_name, email, company,
        street, city, state, zip,
        phone, birth_date, sex,
        date_entered -- we do not add id cause id is auto incrementing
    )
VALUES
    (
        'niharika', 's', 'nihu@gmail.com', 'algo world',
        'muj', 'pinkcity', 'jp', 403, 999448855,
        '2000-02-07', 'F', CURRENT_TIMESTAMP
    );

SELECT * FROM public.customer -- to select a table
ORDER BY id ASC;

INSERT INTO product_type (name)
VALUES('Business');

INSERT INTO product_type (name)
VALUES('Casusal');

INSERT INTO product_type (name)
VALUES('Athletic');

-- you dont have to mention the column name but you should put values in order
INSERT INTO product VALUES
    (1, 'Grandview', 'Allen Edmond', 'Styles to spare new even better'),
    (1,'Galaxy', 'Samsung', 'Next level innovation in your hands'),
    (2,'Futura', 'Nike', 'The future is now, step into it'),
    (3, 'Explorer', 'Ford', 'Discover more with every journey'),
    (3, 'Eclipse', 'Mitsubishi', 'Experience the beauty of the night'),
    (2, 'Zenbook', 'Asus', 'Find your inner peace with cutting-edge technology');

INSERT INTO customer VALUES
    ('John', 'Smith', 'john.smith@example.com', 'Acme Corp', '123 Main St', 'Anytown', 'CA', 12345, 5551234, '1985-06-15', 'M', '2022-01-01'),
    ('Jane', 'Doe', 'jane.doe@example.com', 'ABC Company', '456 Oak St', 'Somewhere', 'NY', 54321, 5555678, '1990-08-02', 'F', '2023-05-15'),
    ('Bob', 'Johnson', 'bob.johnson@example.com', 'XYZ Corp', '789 Maple Ave', 'Nowhere', 'TX', 67890, 5559012, '1988-02-22', 'M', '2022-11-30'),
    ('Mary', 'Williams', 'mary.williams@example.com', '123 Industries', '321 Elm St', 'Anywhere', 'FL', 23456, 5553456, '1995-12-10', 'F', '2024-02-28'),
    ('Tom', 'Jones', 'tom.jones@example.com', 'Smith Co', '567 Pine St', 'Elsewhere', 'GA', 34567, 5556789, '1987-04-01', 'M', '2023-07-15'),
    ('Sarah', 'Brown', 'sarah.brown@example.com', 'Acme Corp', '432 Cedar St', 'Nowhere', 'NC', 45678, 5558901, '1993-10-05', 'F', '2022-09-30'),
    ('David', 'Lee', 'david.lee@example.com', 'ABC Company', '876 Birch Ln', 'Somewhere', 'IL', 56789, 5552345, '1991-06-20', 'M', '2024-04-15'),
    ('Emily', 'Taylor', 'emily.taylor@example.com', 'XYZ Corp', '321 Oak St', 'Anywhere', 'MI', 67890, 5556789, '1996-03-15', 'F', '2023-10-31'),
    ('Kevin', 'Clark', 'kevin.clark@example.com', 'Smith Co', '765 Elm St', 'Nowhere', 'LA', 78901, 5559012, '1992-09-12', 'M', '2022-12-31'),
    ('Ava', 'Hernandez', 'ava.hernandez@example.com', '123 Industries', '987 Maple Ave', 'Elsewhere', 'WA', 89012, 5553456, '1994-11-25', 'F', '2024-01-31'),
    ('Mark', 'Garcia', 'mark.garcia@example.com', 'Acme Corp', '543 Pine St', 'Anywhere', 'OH', 90123, 5557890, '1989-05-30', 'M', '2023-08-15');

INSERT INTO sales_person VALUES
    ('John', 'Smith', 'john.smith@example.com', 'Acme Corp', '123 Main St', 'Anytown', 'CA', 12345, 5551234, '1985-06-15', 'M', '2022-01-01'),
    ('Jane', 'Doe', 'jane.doe@example.com', 'ABC Company', '456 Oak St', 'Somewhere', 'NY', 54321, 5555678, '1990-08-02', 'F', '2023-05-15'),
    ('Bob', 'Johnson', 'bob.johnson@example.com', 'XYZ Corp', '789 Maple Ave', 'Nowhere', 'TX', 67890, 5559012, '1988-02-22', 'M', '2022-11-30'),
    ('Mary', 'Williams', 'mary.williams@example.com', '123 Industries', '321 Elm St', 'Anywhere', 'FL', 23456, 5553456, '1995-12-10', 'F', '2024-02-28'),
    ('Tom', 'Jones', 'tom.jones@example.com', 'Smith Co', '567 Pine St', 'Elsewhere', 'GA', 34567, 5556789, '1987-04-01', 'M', '2023-07-15'),
    ('Sarah', 'Brown', 'sarah.brown@example.com', 'Acme Corp', '432 Cedar St', 'Nowhere', 'NC', 45678, 5558901, '1993-10-05', 'F', '2022-09-30'),
    ('David', 'Lee', 'david.lee@example.com', 'ABC Company', '876 Birch Ln', 'Somewhere', 'IL', 56789, 5552345, '1991-06-20', 'M', '2024-04-15'),
    ('Emily', 'Taylor', 'emily.taylor@example.com', 'XYZ Corp', '321 Oak St', 'Anywhere', 'MI', 67890, 5556789, '1996-03-15', 'F', '2023-10-31'),
    ('Kevin', 'Clark', 'kevin.clark@example.com', 'Smith Co', '765 Elm St', 'Nowhere', 'LA', 78901, 5559012, '1992-09-12', 'M', '2022-12-31'),
    ('Ava', 'Hernandez', 'ava.hernandez@example.com', '123 Industries', '987 Maple Ave', 'Elsewhere', 'WA', 89012, 5553456, '1994-11-25', 'F', '2024-01-31'),
    ('Mark', 'Garcia', 'mark.garcia@example.com', 'Acme Corp', '543 Pine St', 'Anywhere', 'OH', 90123, 5557890, '1989-05-30', 'M', '2023-08-15');

INSERT INTO item VALUES
    (2, 10, 'Gray', 'Coming Soon', 199.60),
    (1, 11, 'Black', 'Coming Soon', 160.99),
    (5, 9, 'White', 'Coming Soon', 188.88),
    (4, 8, 'Blue', 'Coming Soon', 169.69);

INSERT INTO sales_order VALUES
    (1,2,'2023-04-02 11:30:45 AM', 2345678, '2222 3333 4444 5555', '03/25', 123, 'John Johnson'),
    (3,4,'2023-04-02 12:15:12 PM', 3456789, '3333 4444 5555 6666', '06/27', 456, 'Sarah Smith'),
    (3,6,'2023-04-02 02:00:30 PM', 4567890, '4444 5555 6666 7777', '08/24', 234, 'Michael Lee'),
    (1,3,'2023-04-02 03:45:01 PM', 5678901, '5555 6666 7777 8888', '01/23', 567, 'Anna Nguyen');

INSERT INTO sales_item VALUES
    (1, 1, 2, 0.11, false, 0.0),
    (2, 1, 3, 0.12, false, 0.0),
    (3, 2, 5, 0.15, false, 0.0);