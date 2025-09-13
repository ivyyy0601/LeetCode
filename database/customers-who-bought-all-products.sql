# Write your MySQL query statement below
select customer_id
from Customer 
group by customer_id
having count(DISTINCT product_key)=(
    select count(*)
    from Product
)
#原因是题目说 Customer 表可能有重复行，同一顾客可能把同一个 product_key 记录多次
#我太聪明了✌️