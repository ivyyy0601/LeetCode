# Write your MySQL query statement below
SELECT name
FROM Customer
WHERE referee_id <> 2 OR referee_id  IS NULL

##判断空值要用 IS NULL，不能写 = null