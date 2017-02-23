-- Script that lists the number of records with the same score in
-- table second_table from hbtn_0c_0 database.
SELECT score, COUNT(1) AS number FROM second_table
GROUP BY score ORDER BY number DESC;
