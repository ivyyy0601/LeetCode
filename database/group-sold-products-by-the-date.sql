# Write your MySQL query statement below
select sell_date,
count(distinct product) as num_sold,
group_concat(
    distinct product 
    order by product
    asc SEPARATOR ","
)AS products
from Activities 
group by sell_date
order by sell_date

#GROUP_CONCAT([DISTINCT] expr ORDER BY expr ASC|DESC SEPARATOR '分隔符')