SELECT S.user_id, 
       COALESCE(
           ROUND(
               (COUNT(CASE WHEN C.action = 'confirmed' THEN 1 END) * 1.0) 
               / NULLIF(COUNT(C.action), 0), 2
           ), 0) AS confirmation_rate
FROM Signups S
LEFT JOIN Confirmations C
  ON S.user_id = C.user_id
GROUP BY S.user_id;