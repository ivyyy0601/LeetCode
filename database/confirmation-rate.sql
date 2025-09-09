# Write your MySQL query statement below
#如果题目要求“所有用户（包括没请求过的）的确认率”，必须 JOIN，因为 Confirmations 里可能没有这类用户的记录。

select Signups.user_id ,
        #ROUND(avg(count(CASE WHEN action='confirmed' THEN 1 ELSE 0 END)), 2) as confirmation_rate
        #AVG(...) 会在分组后，对这些 1/0 求平均值    本质上就是 总 confirmed 次数 ÷ 总请求次数
        ROUND(AVG(  #SUM(CASE WHEN action='confirmed' THEN 1 ELSE 0 END) / COUNT(*) same
           CASE
               WHEN Confirmations.action = 'confirmed' THEN 1.00     
               ELSE 0.00
           END
       ), 2) AS confirmation_rate
from Signups left join Confirmations
on Signups.user_id = Confirmations.user_id
group by Signups.user_id
