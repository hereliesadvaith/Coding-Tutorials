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