# Write your MySQL query statement below
select customer_id
from Visits left join Transactions
on Visits.visit_id = Transactions.visit_id
where transaction_id is NULL



#####3非常好