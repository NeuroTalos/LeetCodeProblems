SELECT A.machine_id, 
       CAST((AVG(B.timestamp - A.timestamp) * 1000) AS INT) / 1000.0 AS processing_time
FROM Activity A
JOIN Activity B
  ON A.machine_id = B.machine_id
  AND A.process_id = B.process_id
WHERE A.activity_type = 'start'
  AND B.activity_type = 'end'
GROUP BY A.machine_id;