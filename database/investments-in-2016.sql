# Write your MySQL query statement below
select round(sum(tiv_2016),2) as tiv_2016
from Insurance i
where i.tiv_2015 in(
    select tiv_2015 
    from Insurance
    group by tiv_2015
    having count(tiv_2015) != 1
) and CONCAT(i.lat, ',', i.lon) in(
    SELECT CONCAT(lat, ',', lon) AS location 
    from Insurance
    group by location
    having  count(location) = 1
)