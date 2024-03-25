## SQL

### Entity Relationship Diagram
While setting up a new database we need to create an "Entity Relationship Diagram" (ERD) to describe all the tables within the database and the relations between them.

### SQL Statemenst and Syntax
There are three types of SQL statemesnts.

#### 1. Data Defnition Language (DDL):
DDL commands modify the actual structure of a database rather than database's contents. For example:
- Generating a table.
- Altering the structure of a table.

#### 2. Data Control Language (DCL):
DCL allows you to manipulate and manage user access rights on database objects. It consists of two commands:
- the GRANT command. Used to add database permissions for a user.
- the REVOKE command. Used to remove existing permissions.

#### 3. Data Manipulation Language (DML):
DML is used for searching, inserting, updating and deleting data.

### Creating Database
We can create database using:
```sql
CREATE DATABASE mydatabase;
```
We can also conditionally create database if it doesn't already exist using:
```sql
CREATE DATABASE IF NOT EXISTS mydatabase;
```

### Deleting Database
To delete database use:
```sql
DROP DATABASE mydatabase;
```
To delete only the contents of a database use:
```sql
DELETE DATABASE mydatabase;
```

### Creating Table
We can create table using:
```sql
CREATE TABLE IF NOT EXISTS customer(
    first_name VARCHAR(30) NOT NULL,
    last_name VARCHAR(30) NOT NULL,
    email VARCHAR(60) NOT NULL,
    city VARCHAR(30) NOT NULL,
    country VARCHAR(50) NOT NULL,
    birth_date DATE NULL,
    sex CHAR(1) NOT NULL,
    id SERIAL PRIMARY KEY
);

CREATE TABLE IF NOT EXISTS office(
    officeCode VARCHAR(10) NOT NULL,
    phone VARCHAR(50) NOT NULL,
    city VARCHAR(50) NOT NULL,
    country VARCHAR(50) NOT NULL,
    postalCode VARCHAR(15) NOT NULL,
    PRIMARY KEY (officeCode)
);
```
A primary key uniquely identifies a row in a table. You cannot store NULL or duplicate values in a primary key column.
