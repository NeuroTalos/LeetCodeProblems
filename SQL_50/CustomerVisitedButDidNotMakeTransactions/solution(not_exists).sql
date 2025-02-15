SELECT V.customer_id, COUNT(*) as count_no_trans
FROM Visits V
WHERE NOT EXISTS (
    SELECT 1
    FROM Transactions T
    WHERE T.visit_id = V.visit_id
)
GROUP BY customer_id;