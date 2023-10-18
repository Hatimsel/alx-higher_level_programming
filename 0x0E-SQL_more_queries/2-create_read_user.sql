-- Read user
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
SET GLOBAL validate_password.policy = LOW;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
SET GLOBAL validate_password.policy = MEDIUM;
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
