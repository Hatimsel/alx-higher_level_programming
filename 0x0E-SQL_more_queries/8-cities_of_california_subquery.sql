-- Lists all the cities of California that can be found
SELECT id, name FROM cities
WHERE state_id = 1
ORDER BY cities.id ASC;
