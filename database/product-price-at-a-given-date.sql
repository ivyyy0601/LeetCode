# Write your MySQL query statement below
select 
product_id,
case when change_date > '2019-08-16' then 10
else new_price end as price
from Products
where (product_id,change_date) in
(
    select product_id, max(change_date)
    from Products
    where change_date <= '2019-08-16'
    group by product_id
) 
or (product_id,change_date) in
(
    select product_id, change_date
    from Products
    group by product_id
    having count(product_id)=1
)