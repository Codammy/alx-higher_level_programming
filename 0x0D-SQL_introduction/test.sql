-- 
SOURCE ./temperatures.sql
SELECT distinct city, avg(value) from temperatures GROUP BY city ORDER BY city ASC;
