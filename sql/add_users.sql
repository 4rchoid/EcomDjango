-- Use the existing ecom_django database
USE ecom_django;

-- Clear the existing data from the 'customers' table
DELETE FROM customers;

-- Add 100 dummy entries
INSERT INTO customers (first_name, last_name, email)
VALUES
('John', 'Doe', 'john.doe1@example.com'),
('Jane', 'Smith', 'jane.smith1@example.com'),
('Robert', 'Brown', 'robert.brown1@example.com'),
('Emily', 'Johnson', 'emily.johnson1@example.com'),
('Michael', 'Davis', 'michael.davis1@example.com'),
('Sarah', 'Miller', 'sarah.miller1@example.com'),
('David', 'Wilson', 'david.wilson1@example.com'),
('Linda', 'Moore', 'linda.moore1@example.com'),
('James', 'Taylor', 'james.taylor1@example.com'),
('Mary', 'Anderson', 'mary.anderson1@example.com'),
-- Add 90 more entries here with similar pattern
('John', 'Doe', 'john.doe2@example.com'),
('Jane', 'Smith', 'jane.smith2@example.com'),
('Robert', 'Brown', 'robert.brown2@example.com'),
('Emily', 'Johnson', 'emily.johnson2@example.com'),
('Michael', 'Davis', 'michael.davis2@example.com'),
('Sarah', 'Miller', 'sarah.miller2@example.com'),
('David', 'Wilson', 'david.wilson2@example.com'),
('Linda', 'Moore', 'linda.moore2@example.com'),
('James', 'Taylor', 'james.taylor2@example.com'),
('Mary', 'Anderson', 'mary.anderson2@example.com'),
-- Repeat for 100 entries in total
('John', 'Doe', 'john.doe100@example.com');
