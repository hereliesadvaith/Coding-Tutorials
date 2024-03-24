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
