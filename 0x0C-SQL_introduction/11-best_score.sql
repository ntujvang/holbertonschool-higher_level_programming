-- Script that lists all records with score >= 10 in table second_table
-- from hbtn_0c_0 database.
-- Displays score and name arranged highest to lowest
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
