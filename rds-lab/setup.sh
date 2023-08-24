#!/usr/bin/bash

# User ~/.profile for accessing environment variables
source ~/.profile

# Remotely connect to the rds instance
# Create a database, users 
# Create a table, users with columns id, name, email and password 
psql -h $RDS_HOST -U $RDS_USERNAME -p $RDS_PORT \
     -c " CREATE DATABASE $RDS_DATABASE; " \
     -c "\c $RDS_DATABASE" \
     -c "CREATE TABLE users (
        id SERIAL PRIMARY KEY,
        name VARCHAR(50),
        email VARCHAR(50),
        password VARCHAR(50)
        );"

# Log out message
echo "Database has been created successfully!"
echo "Database table has been created successfully!"