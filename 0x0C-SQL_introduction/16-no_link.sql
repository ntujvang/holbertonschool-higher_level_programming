-- Script that lists all records of the table second_table
-- from hbtn_0c_0 database
SELECT score, name FROM second_table HAVING name IS NOT NULL
ORDER BY score DESC;
