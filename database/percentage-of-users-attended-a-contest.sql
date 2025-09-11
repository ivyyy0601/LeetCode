# Write your MySQL query statement below
select contest_id,
ROUND(100.0 * count(DISTINCT Register.user_id)/(SELECT COUNT(*) FROM Users),2) as percentage
from Users right join Register
on Users.user_id = Register.user_id
group by Register.contest_id
order by percentage desc , Register.contest_id ASC;

#count(DISTINCT(Users.user_id)))。不可以，只会统计 在 Register 里出现过的用户，而不会包含系统中那些完全没参赛的用户。
#两位数！！