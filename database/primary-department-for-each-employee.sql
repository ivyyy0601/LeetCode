# Write your MySQL query statement below
select employee_id, department_id
from Employee 
where primary_flag ='Y' #一个yes就够；
or (employee_id) in (
    select employee_id
    from Employee
    group by employee_id
    having count(department_id) =1 #一个count=1就够了！！一个就是n
) 
-- select employee_id, department_id
-- from Employee 
-- where (employee_id) in (
--     select employee_id
--     from Employee
--     group by employee_id
--     having count(department_id)>=2 
-- ) and primary_flag ='Y' #一个yes就够；
-- or (employee_id) in (
--     select employee_id
--     from Employee
--     group by employee_id
--     having count(department_id) =1 #一个count=1就够了！！
-- ) and primary_flag ='N'




