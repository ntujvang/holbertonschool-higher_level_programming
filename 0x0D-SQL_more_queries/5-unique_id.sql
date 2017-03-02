-- Script that creates table unique_id onto MySQL server
CREATE TABLE IF NOT EXISTS unique_id (
id INT UNIQUE DEFAULT 1, name VARCHAR(256));
