# Write your MySQL query statement below
select query_name,
ROUND(avg(rating/position),2) as quality,
ROUND(100.0 * avg(CASE WHEN rating<3 THEN 1 ELSE 0 END),2) as poor_query_percentage
#ROUND(100.0 * AVG(rating < 3), 2)
#    /count(distinct result),2) as poor_query_percentage
#result 可能重复（题目也说表里可能有重复行），用 COUNT(DISTINCT result) 会把重复行合并，分母被缩小，比例就会算错。
from Queries
group by query_name