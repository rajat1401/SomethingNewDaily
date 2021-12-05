/*
https://leetcode.com/problems/count-student-number-in-departments/
*/

with grouped_by_dept as (
select count(student_id) as countt,
dept_id
from Student
group by dept_id
),
joined_by_dept as (
    select a.*,
    d.dept_name
    from grouped_by_dept a
    RIGHT JOIN Department d
    ON a.dept_id=d.dept_id
)
select dept_name,
case when countt!= 0 then countt else 0 end as student_number
from
joined_by_dept
order by countt desc,dept_name;