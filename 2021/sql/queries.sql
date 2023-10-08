

CREATE TABLE Occupations (
     NAME VARCHAR(40),
     Occupation VARCHAR(40)
    );

------------

INSERT  INTO Occupations
VALUES
        ('Samantha','Doctor'),
        ('Julia','Actor'),
        ('Maria','Actor'),
        ('Meera','Singer'),
        ('Ashley','Professor'),
        ('Ketty','Professor'),
        ('Christeen','Professor'),
        ('Jane','Actor'),
        ('Jenny','Doctor'),
        ('Priya','Singer');

------------ 

 ROUND(AVG(salary) OVER (
        PARTITION BY department_id
    )) avg_department_salary
FROM
    employees;

------------

select occupation, count(name) as count over (partition by occupation) occ from occupations

------------ 

https://www.mkanalysis.com/tutorial/26

https://github.com/int28h/SQLTasks/blob/master/src/hackerrank-advanced-select.md

------------ 


select case
       when parent = NULL then CONCAT(node, " ROOT")
       when node in (select DISTINCT parent from graph) then concat(node, " INNER")
       else concat(node, " LEAF")
       end
from graph
order by node asc


 select case
       when P IS NULL then CONCAT(N, " Root")
       when N in (select DISTINCT P from BST) then concat(N, " Inner")
       else concat(N, " Leaf")
       end
from BST
order by N asc



select Doctor, Professor, Singer, Actor from
(select occupation,
       row_number() over (partition by occupation) rn
       from occupations)
as source
pivot MAX(Name) FOR occupations IN ("Doctor", "Professor", "Singer", "Actor") as pvt
ORDER BY rn





delete t1 from employee2 t1
inner join employee2 t2
on t1.id < t2.id




CREATE table with duplicates
================


CREATE TABLE contacts (
    id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(255) NOT NULL
);

INSERT INTO contacts (first_name,last_name,email)
VALUES ('Carine ','Schmitt','carine.schmitt@verizon.net'),
       ('Jean','King','jean.king@me.com'),
       ('Peter','Ferguson','peter.ferguson@google.com'),
       ('Janine ','Labrune','janine.labrune@aol.com'),
       ('Jonas ','Bergulfsen','jonas.bergulfsen@mac.com'),
       ('Janine ','Labrune','janine.labrune@aol.com'),
       ('Susan','Nelson','susan.nelson@comcast.net'),
       ('Zbyszek ','Piestrzeniewicz','zbyszek.piestrzeniewicz@att.net'),
       ('Roland','Keitel','roland.keitel@yahoo.com'),
       ('Julie','Murphy','julie.murphy@yahoo.com'),
       ('Kwai','Lee','kwai.lee@google.com'),
       ('Jean','King','jean.king@me.com'),
       ('Susan','Nelson','susan.nelson@comcast.net'),
       ('Roland','Keitel','roland.keitel@yahoo.com');
       id INT PRIMARY KEY AUTO_INCREMENT,
       first_name VARCHAR(50) NOT NULL,
       last_name VARCHAR(50) NOT NULL,
       email VARCHAR(255) NOT NULL
     )


