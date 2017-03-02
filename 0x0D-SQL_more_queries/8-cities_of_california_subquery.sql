-- Script that lists all cities of California that can be found in database
SELECT id, name FROM cities
WHERE state_id IN (SELECT id from states WHERE name = 'california')
ORDER BY id ASC;
