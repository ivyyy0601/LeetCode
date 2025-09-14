# Write your MySQL query statement below
select distinct l1.num as ConsecutiveNums #注意要distinct
from Logs l1 
join Logs l2 on l1.num=l2.num
join Logs l3 on l2.num=l3.num #这样子已经相当于已经出现了连续出现三次了，我太聪明了
where l1.id=l2.id-1 and l2.id=l3.id-1 
