-- this script query a database and displays the max temperature of each state order by name
SOURCE ./temperatures.sql
SELECT state, MAX(value) as max_temp FROM temperatures GROUP BY state;

