# Write your MySQL query statement below
select max(num) as num
from MyNumbers
where num in
(select num
from MyNumbers
group by num
having count(num)=1)


#HAVING 只能跟在 GROUP BY 后面