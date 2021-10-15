/*
problem link: https://leetcode.com/problems/rising-temperature/submissions/
problem statement: rwite an SQL query to find all dates' Id with higher temperatures compared to its previous dates (yesterday).
*/

select id from
(
select id,
RecordDate,
Temperature - lag(Temperature) over() as diff,
lag(RecordDate) over() as lastdate
from (
    select *
    from Weather
    order by RecordDate
    ) q
) p
where p.diff> 0 and datediff(p.lastdate,p.RecordDate)=-1;