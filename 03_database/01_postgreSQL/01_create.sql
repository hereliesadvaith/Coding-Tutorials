-- One table represents 1 real world object
-- Columns store 1 piece of information

CREATE TABLE customer(
	first_name VARCHAR(30) NOT NULL,
	last_name VARCHAR(30) NOT NULL,
	email VARCHAR(60) NOT NULL,
	company VARCHAR(60) NOT NULL,
	street VARCHAR(50) NOT NULL,
	city VARCHAR(30) NOT NULL,
	state CHAR(2) NOT NULL,
	zip SMALLINT NOT NULL,
	phone VARCHAR(20) NOT NULL,
	birth_date DATE NULL,
	sex CHAR(1) NOT NULL,
	date_entered TIMESTAMP NOT NULL,
	id SERIAL PRIMARY KEY
);