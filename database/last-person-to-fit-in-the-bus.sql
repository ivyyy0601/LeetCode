# Write your MySQL query statement below

#完全不会
-- #用自连接把“前缀和（累计体重）”算出来，再挑出累计 ≤1000 的最后一个人。
-- SELECT q1.turn as q1 , q2.turn as q2
-- FROM Queue q1
-- JOIN Queue q2 ON q1.turn >= q2.turn
-- order by q1.turn
-- #例如 q1.turn = 3 时，连接到 q2.turn ∈ {1,2,3} 的三行。
#用自连接把“前缀和（累计体重）”算出来，再挑出累计 ≤1000 的最后一个人。
SELECT q1.person_name 
FROM Queue q1
JOIN Queue q2 ON q1.turn >= q2.turn
group by q1.turn 
having sum(q2.weight)<=1000
limit 1
#例如 q1.turn = 3 时，连接到 q2.turn ∈ {1,2,3} 的三行。