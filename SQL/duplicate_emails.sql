#problem link: https://leetcode.com/problems/duplicate-emails/submissions/

# Write your MySQL query statement below
select email from (
    select email, 
    count(*) as counts
    from 
    person
    group by email
    having counts > 1
) as Email; 