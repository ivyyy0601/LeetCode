# Write your MySQL query statement below
#难！！！！！！！！！1 #
select visited_on,
(
    select sum(amount)
    from Customer
    where visited_on between date_sub(c.visited_on, interval 6 day) and c.visited_on
) as amount,
(
    select round(sum(amount)/7,2) 
    from Customer
    where visited_on between date_sub(c.visited_on, interval 6 day) and c.visited_on
) as average_amount #题目要“最近 7 天的日均金额”，应该是 7 天总额 / 7，而不是对所有行 AVG(amount)。avr是对于全部行来讲的
from Customer c
where c.visited_on >=
(
    select date_add(min(visited_on), interval 6 day)
    from Customer
)
group by visited_on