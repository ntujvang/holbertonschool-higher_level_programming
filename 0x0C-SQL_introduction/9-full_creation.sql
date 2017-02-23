-- Script that creates a table second_table into hbtn_0c_0 database
-- id(INT), name(VARCHAR(256)), score(INT)
-- Also creates 4 new rows
CREATE TABLE IF NOT EXISTS second_table (id INT, name VARCHAR(256), score INT);
INSERT INTO second_table (`id`, `name`, `score`) VALUES
("1", "John", "10"), ("2", "Alex", "3"),
("3", "Bob", "14"), ("4", "Geroge", "8");
