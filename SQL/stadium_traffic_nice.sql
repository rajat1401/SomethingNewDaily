/*
link: https://leetcode.com/problems/human-traffic-of-stadium/submissions/
*/

with filtered_stadium as (
    select id,
    visit_date,
    people
    from stadium
    where people>= 100
),
leag_lag_filtered as (
    select id,
    visit_date,
    people,
    case when lead(id,1) over() is null then 0 else lead(id,1) over() -id end as two,
    case when lead(id,2) over() is null then 0 else lead(id,2) over() -id end as three,
    case when lag(id,1) over() is null then 0 else id-lag(id) over() end as minustwo,
    case when lag(id,2) over() is null then 0 else id-lag(id,2) over() end as minusthree
    from filtered_stadium
)
select id,
visit_date,
people
from leag_lag_filtered
where (two=1 and three=2) or 
(two=1 and minustwo=1) or 
(minustwo=1 and minusthree=2);