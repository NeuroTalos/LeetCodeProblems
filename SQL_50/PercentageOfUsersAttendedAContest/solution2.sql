SELECT R.contest_id,
       ROUND((COUNT(R.user_id) * 1.0 / total_users) * 100, 2) AS percentage
FROM Register R
CROSS JOIN (SELECT COUNT(user_id) AS total_users FROM Users) U
GROUP BY R.contest_id, total_users
ORDER BY percentage DESC, contest_id ASC;