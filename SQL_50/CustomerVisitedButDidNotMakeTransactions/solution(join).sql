SELECT V.customer_id, COUNT(*) as count_no_trans
FROM Visits V
LEFT JOIN Transactions T 
ON T.visit_id = V.visit_id
WHERE T.visit_id IS NULL
GROUP BY V.customer_id;