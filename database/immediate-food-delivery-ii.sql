# Write your MySQL query statement below
select round(100 * avg( order_date= customer_pref_delivery_date ),2) as immediate_percentage
from Delivery
where (customer_id, order_date) in ( #(customer_id, order_date) IN (...)
#按 customer_id 分组，却选了未聚合的 delivery_id，这在 MySQL（开启 ONLY_FULL_GROUP_BY）下是非法的；就算没开，也会随意取一个 delivery_id，语义是错的。但是没关系！！customer_id,MIN(order_date) 已经够确认了！！！
    select customer_id,MIN(order_date) #把min放在输入层
    from Delivery
    group by customer_id
    #having MIN(order_date)
)
#在 HAVING MIN(order_date)——HAVING 里必须是一个布尔条件，像 HAVING MIN(order_date)
#Subquery returns more than 1 row. in


#！！！！！！！！！！所以严格来说，它就是“随机挑的”，你不能指望它一定和 MIN(order_date) 对应。