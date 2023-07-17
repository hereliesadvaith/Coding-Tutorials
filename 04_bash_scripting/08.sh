#!/bin/bash

# PostgreSQL database connection details
DB_HOST="localhost"
DB_PORT="5432"
DB_NAME="mydb"
DB_USER="advaith"

# Connect to the database and create a new table
psql -h $DB_HOST -p $DB_PORT -d $DB_NAME -U $DB_USER -W << EOF
CREATE TABLE devolop (id INT PRIMARY KEY, name TEXT, email TEXT);
EOF

