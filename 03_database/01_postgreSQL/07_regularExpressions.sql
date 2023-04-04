SELECT first_name, last_name
FROM customer
WHERE first_name SIMILAR TO 'N%' OR -- %  matches 0 or more character after N
WHERE first_name LIKE 'n_______'; -- _ matches specific number of character

/*
. : Any single character
* : 0 or more
+ : 1 or more
^ : Beginning of string
$ : End of string
[^ab] : Not a and b
[ab] : Only a and b
[A-Z] : All uppercase letters
[a-z] : lowercase
[0-9] : numbers
{n} : n instances of 
{m, n} : between m and n instances of 
m | n : match m or n
*/

SELECT first_name, last_name
FROM customer
WHERE first_name ~ 'Ni'; -- name starts with 'Ni'

SELECT EXTRACT(MONTH FROM birth_date) AS MONTH, COUNT(*) AS amuont
FROM customer
GROUP BY MONTH
HAVING COUNT(*) > 1 -- narrows the list with condition
ORDER BY MONTH;

-- Aggregate function
SELECT SUM(price)
FROM item;

SELECT COUNT(*) AS items
SUM(price) AS value
ROUND(AVG(price), 0) AS average
MIN(price) AS min
MAX(price) AS max
FROM item;