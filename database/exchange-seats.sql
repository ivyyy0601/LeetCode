# Write your MySQL query statement below
# Write your MySQL query statement below
#思路直接改写 id，把学生分配到对应的新 id 上
#case when... then
#     when... then
#     else
#end as....
select 
    case 
        when id % 2 =1 and id+1 in (select id from Seat) then id+1
        when id % 2 =0 then id-1
        else id
    end as id, student 
from Seat
order by id