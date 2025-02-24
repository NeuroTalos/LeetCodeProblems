SELECT A.name
FROM Employee A
JOIN Employee B
ON A.id = B.managerId
GROUP BY A.id, A.name
HAVING COUNT(B.managerID) > 4