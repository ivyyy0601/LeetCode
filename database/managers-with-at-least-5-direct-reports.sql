-- # Write your MySQL query statement below
-- select m.name
-- from Employee e
-- join  Employee m
-- on e.managerId = m.id
-- having count(m.id) >=5

##还是有点问题！！！，一般有count的时候就会有group by
#你这句没有 GROUP BY 的聚合是在统计“所有经理的总下属数”。比如 A 有 3 个、B 有 3 个 → 总数 6≥5，你的查询会通过，

SELECT m.name
FROM Employee e
JOIN Employee m ON e.managerId = m.id   -- m是经理，e是下属
group by m.id
having count(m.id) >=5