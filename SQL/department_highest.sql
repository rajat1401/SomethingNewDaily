/* problem link: https://leetcode.com/problems/department-highest-salary/submissions/
problem statement: department wise highest salaries
*/

with ranked_employees as (
select name,
salary,
departmentid,
rank() over(partition by departmentid order by salary desc) rrank
from Employee 
),
filtered_ranked_employees as (
select name,
    salary,
    departmentid
    from ranked_employees
    where rrank= 1
)
select a.name as Employee,
a.salary as Salary,
b.name as Department
from filtered_ranked_employees a 
LEFT JOIN 
Department b
ON 
a.departmentid=b.id;
