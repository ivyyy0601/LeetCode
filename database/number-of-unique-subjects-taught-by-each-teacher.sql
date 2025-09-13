# Write your MySQL query statement below
select teacher_id, count(DISTINCT subject_id) as cnt # unique subjects 就行
from Teacher
group by teacher_id