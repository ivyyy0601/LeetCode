# Write your MySQL query statement below
select product_id,  year as first_year,quantity,price
from Sales
where (product_id,year) in (
    select product_id, min(year)
    from Sales
    group by product_id
    )

-- ❌ WHERE year = MIN(year) 不行，因为在 WHERE 阶段还没算出 MIN(year)。
-- ✅ (product_id, year) IN (子查询) 可以，因为子查询已经先算出了每个产品的最小年份。