# Write your MySQL query statement below
-- select Students.student_id, Students.student_name, Examinations.subject_name,count(Examinations.subject_name)
-- from Students right join Examinations
-- on Students.student_id = Examinations.student_id
-- group by Students.student_id and Examinations.subject_name

select Students.student_id, Students.student_name, Subjects.subject_name,count(Examinations.subject_name) as attended_exams
#当这个学生在某门课没有任何考试记录时，连接不上 Examinations 的那一侧就全是 NULL，始终不为 NULL（来自科目表的笛卡尔积）
#Examinations 但是计算的时候没有就是null 就是0
from Students 
CROSS JOIN Subjects
LEFT JOIN Examinations 
on Examinations.student_id = Students.student_id and Subjects.subject_name = Examinations.subject_name
group by Students.student_id , Subjects.subject_name
ORDER BY Students.student_id , Subjects.subject_name

