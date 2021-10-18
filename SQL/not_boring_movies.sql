/* 
link: https://leetcode.com/problems/not-boring-movies/submissions/

*/

select id,
movie,
description,
rating
from Cinema
where id%2= 1 and 
description!='boring'
order by rating desc;