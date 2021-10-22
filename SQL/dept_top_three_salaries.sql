/*
link: https://leetcode.com/problems/department-top-three-salaries/submissions/
*/

with ranked_salaries as (
select name,
salary,
dense_rank() over (partition by departmentId order by salary desc) as rrank,
departmentId
from
Employee
),
filtered_ranked_salaries as (
select name,
salary,
departmentId
from ranked_salaries
where rrank<= 3
)
select a.name as Employee,
a.salary as Salary,
b.name as Department
from filtered_ranked_salaries a
LEFT JOIN Department b
ON a.departmentId=b.id;