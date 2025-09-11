# Write your MySQL query statement below
select 
round(count(*)/(SELECT COUNT(DISTINCT player_id)  FROM Activity),2) as fraction
from Activity
where (player_id, event_date) not in 
(select player_id, min(event_date)
from Activity
where games_played != 0
group by player_id)
and games_played !=0
group by player_id

#COUNT() 里面不能直接塞一个 SELECT 子查询。