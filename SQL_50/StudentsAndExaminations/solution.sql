SELECT St.student_id, St.student_name, Sbj.subject_name,
    COUNT(EX.subject_name) as attended_exams
FROM Students St
CROSS JOIN Subjects Sbj
LEFT JOIN Examinations Ex
ON St.student_id = Ex.Student_id AND Sbj.subject_name = Ex.subject_name
GROUP BY St.student_id, St.student_name, Sbj.subject_name
ORDER BY St.student_id, Sbj.subject_name