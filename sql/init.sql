-- Create the database
CREATE DATABASE IF NOT EXISTS ecom_django;

-- Use the created database
USE ecom_django;

-- Create a table 'customers' with id, first_name, last_name, and email
CREATE TABLE IF NOT EXISTS customers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL
)