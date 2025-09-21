# Write your MySQL query statement below
select user_id, name, mail
from Users
where mail REGEXP  '^[a-zA-Z][a-zA-Z0-9_.-]@leetcode\\.com$'
#：REGEXP BINARY（强制大小写敏感）