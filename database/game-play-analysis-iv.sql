# Write your MySQL query statement below
#没有读懂题目“有多少玩家首日玩过”。Write a solution to report the fraction of players that logged in again on the day after the day they first logged in,第二天还玩
select 
round(count(DISTINCT player_id)/(SELECT COUNT(DISTINCT player_id)  FROM Activity),2) as fraction
#不可以(count(*)。 如果某个玩家在“第一天”有多条记录（少见但可能出现），就会被算多次
from Activity
where (player_id,DATE_SUB(event_date, INTERVAL 1 DAY))  in(
    select player_id, min(event_date)
    from Activity
    #where games_played != 0 login就行
    group by player_id
)
#and games_played != 0。  login就行
#DATE_SUB(event_date, INTERVAL 1 DAY)  
#COUNT() 里面不能直接塞一个 SELECT 子查询。