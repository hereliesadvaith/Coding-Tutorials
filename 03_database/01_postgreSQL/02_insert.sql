INSERT INTO customer(
    first_name, last_name, email, company, street, city, state, zip,
    phone, birth_date, sex, date_entered -- we do not add id cause id is auto incrementing
)
VALUES(
    'niharika', 's', 'nihu@gmail.com', 'algo world', 'muj', 'pinkcity', 'jp', 403, 999448855,
    '2000-02-07', 'F', CURRENT_TIMESTAMP
);