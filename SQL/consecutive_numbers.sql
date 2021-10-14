/*
problem link: https://leetcode.com/problems/consecutive-numbers/submissions/
problem statement: find all numbers that appear consecutively thrice atleast. 
*/

select distinct(num) as ConsecutiveNums
from
(
select num,
lead(num, 1) over() as numnext,
lead(num,2)  over() as numthird
from logs
) l
where l.num=l.numnext and l.numnext=l.numthird;