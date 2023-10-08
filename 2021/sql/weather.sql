

select A.id from (
select id, temperature - lag(temperature) over (order by recorddate)  as diff from weather order by recorddate) A
where A.diff > 0
