-- Script that creates database hbtn_0d_usa and table cities inside on MYSQL
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
id INT PRIMARY KEY AUTO_INCREMENT UNIQUE, state_id INT,
FOREIGN KEY(state_id) REFERENCES hbtn_0d_usa.states(id),
name VARCHAR(256) NOT NULL);
