/*
link: https://leetcode.com/problems/combine-two-tables/submissions/
*/

select a.firstName,
a.lastName,
b.city,
b.state
from
Person a
LEFT JOIN
Address b
on a.personid=b.personid;