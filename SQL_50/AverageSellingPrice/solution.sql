SELECT P.product_id,
       ROUND(
           COALESCE(SUM(U.units * P.price), 0) * 1.0 / COALESCE(SUM(U.units), 1), 2
       ) AS average_price
FROM Prices P 
LEFT JOIN UnitsSold U
  ON P.product_id = U.product_id 
  AND U.purchase_date >= P.start_date
  AND U.purchase_date <= P.end_date
GROUP BY P.product_id;