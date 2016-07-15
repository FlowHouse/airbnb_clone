-- Creating 1 user1 for the test db: test
CREATE USER 'airbnb_user_test'@'%' IDENTIFIED BY 'test1';

-- Creating database: test
CREATE DATABASE airbnb_test CHARACTER SET utf8 COLLATE utf8_general_ci;

-- Granting PRIVILEGES to user test
GRANT ALL PRIVILEGES ON airbnb_dev . * TO airbnb_user_test;
