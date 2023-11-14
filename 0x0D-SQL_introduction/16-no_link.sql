-- list all records of second_table

SELECT scoe, name FROM second_table WHERE name IS NOT NULL AND name != '' ORDER BY score DESC;
