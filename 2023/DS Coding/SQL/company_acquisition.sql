



(select A.hacker_id, A.name, B.challange_id, B.score from
    hackers A left join submissions B
        on A.hacker_id = B.hacker_id) 






-- Using CTE

select * from employee limit 5;


using employee_count as (
    select city, count(*) as employee_count 
    from employee 
    group by city
)
select 
