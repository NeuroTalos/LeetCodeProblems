SELECT *
FROM Cinema C
WHERE C.id % 2 != 0 and C.description NOT LIKE '%boring%'
ORDER BY C.rating DESC