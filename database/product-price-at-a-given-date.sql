# Write your MySQL query statement below
select 
distinct product_id,
case when change_date > '2019-08-16' then 10
else new_price end as price
from Products
where (product_id,change_date) in # 截止日前最后一次
(
    select product_id, max(change_date)
    from Products
    where change_date <= '2019-08-16'
    group by product_id
) 
or (product_id,change_date) in #在截至日期后 但是从来都没有出现过在截止日前 所以就是10 而且这个product我们只记录一次
(
    select  distinct product_id ,change_date
    from Products
    where change_date > '2019-08-16' and
    product_id not in (
        select product_id
        from Products
        where change_date <= '2019-08-16'
    )
)


--  (product_id, new_price, change_date) IN (
--         SELECT DISTINCT product_id, 10, change_date
-- 这意味着只有当表里真的存在 new_price=10 的那行时才会匹配；如果表里没出现过 10，就不会返回这类产品（违背“默认价=10”的本意）