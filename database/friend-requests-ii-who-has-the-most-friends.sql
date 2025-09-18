# Write your MySQL query statement below
#COUNT(user_id) 是聚合函数，只能和 GROUP BY 一起用。
#你在外层又包了一层 MAX()，但是没有对应的分组或子查询
select user_id as id, count(user_id) as num
from(
    select requester_id as user_id from RequestAccepted
    union all
    select accepter_id as user_id from RequestAccepted
)as t
#Every derived table must have its own alias MySQL 要求子查询必须有别名
group by user_id
order by count(user_id) desc
limit 1