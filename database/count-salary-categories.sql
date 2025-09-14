# Write your MySQL query statement below
select 'Low Salary' as category, sum(income < 20000) as accounts_count
from Accounts
union all
select 'Average Salary' as category, sum(income between 20000 and 50000) as accounts_count
from Accounts
union all
select 'High Salary' as category, sum(income > 50000) as accounts_count
from Accounts

#JOIN 横着拼列；UNION 竖着叠行。