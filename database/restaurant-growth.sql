# Write your MySQL query statement below
#难！！！！！！！！！1
select visited_on,
(
    select sum(amount)
    from Customer
    where visited_on BETWEEN DATE_SUB(c.visited_on, INTERVAL 6 DAY) AND c.visited_on
)as amount,ROUND(
    (
        select sum(amount)/7
        from Customer
        where visited_on BETWEEN DATE_SUB(c.visited_on, INTERVAL 6 DAY) AND c.visited_on
    )
,2)as average_amount
from Customer c
where c.visited_on >= (
    select DATE_ADD(MIN(visited_on), INTERVAL 6 DAY)# ③ 只从第 7 天开始输出（保证窗口凑满 7 天）
    from customer
)
group by visited_on 
# 由于 customer 可能一天多行，这里按天去重成一行()