# Write your MySQL query statement below
select user_id,
concat(
    UPPER(SUBSTRING(name, 1, 1)), LOWER(SUBSTRING(name, 2))
)as name
from Users
order by user_id
#UPPER() 把整个字符串变成大写。  string 传进去
#LOWER() 把整个字符串变成小写。
#用 CONCAT() 或者 ||（根据数据库）把两部分拼起来：
#LEFT(name, 1) / SUBSTRING(name, 1, 1) 取第一个字符。
#SUBSTRING(name, 2) 取从第二个字符开始的子串。