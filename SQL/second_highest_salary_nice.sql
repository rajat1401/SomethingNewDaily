/*
link: https://leetcode.com/problems/second-highest-salary/submissions/
statement: quite evident
*/

with ordered_salaries as (
select salary,
dense_rank() over(order by salary desc) as rrank
from Employee
) 
select max(case when rrank=2 then salary else null end) as SecondHighestSalary
from ordered_salaries limit 1; 
    