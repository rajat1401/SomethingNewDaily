/*
link: https://leetcode.com/problems/trips-and-users/submissions/
statement: complex
*/


with filtered_trips as (
    select client_id,
    driver_id,
    `status` as sstatus,
    request_at
    from trips
    where request_at between '2013-10-01' and '2013-10-03'
),
unbanned_users as (
    select users_id
    from users
    where role='client' and banned='No'
),
unbanned_drivers as (
    select users_id
    from users
    where role='driver' and banned='No'
),
joined_trips_users as (
    select a.client_id,
    a.driver_id,
    a.sstatus,
    a.request_at
    from filtered_trips a
    INNER JOIN unbanned_drivers b
    ON a.driver_id=b.users_id
    INNER JOIN unbanned_users c
    ON a.client_id=c.users_id
),
cancelled_trips_users as (
    select request_at,
    count(*) as ccount,
    sum(case when sstatus!='completed' then 1 else 0 end) as tripcancelled
    from joined_trips_users
    group by request_at
)
select request_at as `Day`,
round(tripcancelled/ccount, 2) as `Cancellation Rate`
from cancelled_trips_users;