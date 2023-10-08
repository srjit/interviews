-- Given a table of candidates and their skills, 
-- you're tasked with finding the candidates best 
-- suited for an open Data Science job. 
-- You want to find candidates who are proficient in Python, 
-- Tableau, and PostgreSQL.

-- Write a query to list the candidates who possess all 
-- of the required skills for the job. Sort the output by 
-- candidate ID in ascending order.

-- Assumption:
-- There are no duplicates in the candidates table.
-- candidates Table:

-- Column Name	       Type
-- candidate_id	    integer
-- skill	        varchar

-- candidates Example Input
-- candidate_id	skill
-- 123	    Python
-- 123	    Tableau
-- 123  	PostgreSQL
-- 234	    R
-- 234  	PowerBI
-- 234	    SQL Server
-- 345	    Python
-- 345	    Tableau

-- Example Output:
-- candidate_id
-- 123

create table skills(
    candidate_id INT,
    skill VARCHAR(100)
)

INSERT INTO skills (candidate_id, skill) 
VALUES
    (123, 'Python'),
    (123, 'Tableau'),
    (123, 'PostgreSQL'),
    (234, 'R'),
    (234, 'PowerBI'),
    (234, 'SQL Server'),
    (345, 'Python'),
    (345, 'Tableau');

select * from skills;

select A.candidate_id from
(select candidate_id, GROUP_CONCAT(skill)
as skillset
from skills
group by candidate_id
having skillset = 'Python,Tableau,PostgreSQL')
A



select C.candidate_id from
    (select A.candidate_id 
        from(
            (select candidate_id from
                skills where skill = 'Python') A
            inner join
            (select candidate_id from
                skills where skill = 'Tableau') as B
            on A.candidate_id = B.candidate_id)) C
        inner join
            (select candidate_id from
            skills where skill = 'PostgreSQL') D
    on 
    C.candidate_id = D.candidate_id;

