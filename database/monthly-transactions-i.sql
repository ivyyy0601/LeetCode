# Write your MySQL query statement below
SELECT 
DATE_FORMAT(trans_date, '%Y-%m')  AS month,
country,
count(id) as trans_count,
sum(state='approved') as approved_count,
#SUM(state = 'approved')：MySQL 会把布尔值当 0/1，加总就是数量。 不可以用count，只要 expr 的结果不是 NULL，就会计数。
sum(amount) as trans_total_amount,
sum(CASE WHEN state='approved' THEN amount ELSE 0 END) as approved_total_amount
from Transactions
group by month, country
