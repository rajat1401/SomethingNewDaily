/*
link: https://leetcode.com/problems/exchange-seats/submissions/
*/

select 
case 
    when id%2=1 then case when lead(id) over() is null then id else lead(id) over() end
    else lag(id) over()
    end 
as id,
student
from seat
order by id;