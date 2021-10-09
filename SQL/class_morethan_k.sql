/*
problem link: https://leetcode.com/problems/classes-more-than-5-students/
problem statement: classes with more than 5 students
*/

# Write your MySQL query statement below
select a.class as class
from
(
    select class, count(distinct(student)) as ccount
    from courses
    group by class
) a
where ccount>= 5;