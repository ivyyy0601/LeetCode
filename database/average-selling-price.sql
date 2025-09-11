# Write your MySQL query statement below
select Prices.product_id, ifnull(ROUND(sum(price*units)/sum(units),2)) as average_price
from Prices left join UnitsSold
on Prices.product_id= UnitsSold.product_id and purchase_date between start_date and end_date
group by Prices.product_id 
#最后会变成这样子1          | null          |
#IFNULL(..., 0) 遇到 NULL 的时候转成 0。