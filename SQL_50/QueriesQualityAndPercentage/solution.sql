SELECT Q.query_name,
    ROUND(SUM(Q.rating * 1.0/Q.position)/COUNT(Q.query_name) 
        , 2) as quality,
    ROUND((COUNT(CASE WHEN Q.rating < 3 THEN 1 END)*1.0/COUNT(Q.query_name)) * 100.0
        , 2) as poor_query_percentage 
FROM Queries Q
GROUP BY Q.query_name