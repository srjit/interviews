

-- common table expression
-- analytic function

-- https://www.youtube.com/watch?v=snMpzxf1Wf0

select * from USERS;

with CTE as (
    select cast(created_date as Date) as CREATED_AT,
    count(id) as usercount,
    from users
)
select created_at, usercount, sum(usercount) over (partition by year(created_at), month(created_at))
as cum_count from cte;