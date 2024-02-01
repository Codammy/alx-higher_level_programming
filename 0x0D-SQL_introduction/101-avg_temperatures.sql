-- selects each city and it'a average
SOURCE ./temperatures.sql
SELECT city, AVG(value) AS avg_temp FROM temperatures GROUP BY city ORDER BY value DESC;
