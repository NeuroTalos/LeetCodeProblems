SELECT R.contest_id,
    ROUND((COUNT(R.user_id) * 1.0 / (SELECT COUNT(U.user_id) FROM Users U)) * 100, 2) as percentage 
FROM Register R
GROUP BY R.contest_id
ORDER BY percentage DESC, contest_id ASC;